"""Contrôles de cohérence des modèles de provisioning, de packs réglementaires
et d'import / export (model/project_setup.yaml, regulatory_packs.yaml,
import_export.yaml).

Appelé par almmodel.validate() ; les fonctions reçoivent le modèle chargé et
ajoutent leurs constats à m.errors / m.warnings.
"""
from __future__ import annotations

from typing import Any

# Pseudo-champs acceptés dans les correspondances d'échange (champs natifs
# Polarion ou structure de document)
_PSEUDO_FIELDS = {"id", "title", "description", "heading", "status"}


def _enum_ids(m, enum_id: str) -> set[str]:
    return {o["id"] for o in m.enumerations.get(enum_id, {}).get("options", [])}


def _all_field_ids(m) -> set[str]:
    ids: set[str] = set()
    for t in m.types:
        ids |= m.field_ids_of(t["id"])
    ids |= {f["id"] for f in m.document_types.get("documentCustomFields", [])}
    return ids


def _field_def(m, type_id: str, field_id: str) -> dict[str, Any] | None:
    for f in m.fields_of(m.type_by_id(type_id)):
        if f["id"] == field_id:
            return f
    return None


# --------------------------------------------------------------------------
def validate_setup(m) -> None:
    s = m.setup
    if not s:
        return
    err = m.errors
    params: dict[str, dict[str, Any]] = {}
    for q in s.get("questionnaire", []):
        where = f"provisioning {q.get('id')}"
        if q.get("param") in params:
            err.append(f"{where}: paramètre dupliqué {q.get('param')}")
        params[q["param"]] = q
        if "enum" in q and q["enum"] not in m.enumerations:
            err.append(f"{where}: énumération inconnue {q['enum']}")
        for o in q.get("options", []) or []:
            if not isinstance(o.get("id"), str) or not o.get("fr") or not o.get("en"):
                err.append(f"{where}: option invalide {o}")
        if not any(k in q for k in ("enum", "options", "scoring", "text")):
            err.append(f"{where}: ni énumération, ni options, ni cotation, ni texte")

    def allowed(param: str) -> set[str] | None:
        q = params.get(param)
        if q is None:
            return None
        if "enum" in q:
            return _enum_ids(m, q["enum"])
        if "options" in q:
            return {o["id"] for o in q["options"]}
        return None

    instances = {i["id"] for i in m.topology.get("instances", [])}
    templates = {t["id"] for t in m.topology.get("projectTemplates", [])}
    type_ids = set(m.type_ids)
    doc_ids = {d["id"] for d in m.document_types.get("documentTypes", [])}
    for r in s.get("derivationRules", []):
        where = f"provisioning {r.get('id')}"
        for param, values in (r.get("when") or {}).items():
            if param not in params:
                err.append(f"{where}: paramètre de condition inconnu {param}")
                continue
            ok = allowed(param)
            if ok is not None and isinstance(values, list):
                for v in values:
                    if v not in ok:
                        err.append(f"{where}: valeur {v} inconnue pour {param}")
        sets = r.get("sets") or {}
        if "instance" in sets and sets["instance"] not in instances:
            err.append(f"{where}: instance inconnue {sets['instance']}")
        if "extProject" in sets and sets["extProject"] not in templates:
            err.append(f"{where}: gabarit inconnu {sets['extProject']}")
        for t in sets.get("enableTypes", []) or []:
            if t not in type_ids:
                err.append(f"{where}: type inconnu {t}")
        for d in sets.get("enableDocuments", []) or []:
            if d not in doc_ids:
                err.append(f"{where}: document inconnu {d}")
        for e in sets.get("projectEnums", []) or []:
            if e not in m.enumerations:
                err.append(f"{where}: énumération inconnue {e}")
    for p in s.get("projectParameters", []):
        if p not in params and p not in ("projectClass", "instance", "template"):
            err.append(f"provisioning: paramètre projet sans question ni dérivation {p}")
    disciplines = _enum_ids(m, "discipline")
    domains = _enum_ids(m, "habilitationDomain")
    for d, h in (s.get("habilitationDefaults") or {}).items():
        if d not in disciplines:
            err.append(f"provisioning: discipline inconnue {d}")
        if h not in domains:
            err.append(f"provisioning: domaine d'habilitation inconnu {h}")


# --------------------------------------------------------------------------
def validate_regulatory_packs(m) -> None:
    rp = m.regulatory_packs
    if not rp:
        return
    err = m.errors
    packs = rp.get("packs", {})
    frameworks = _enum_ids(m, "regulatoryFramework")
    for f in frameworks:
        if f not in packs:
            err.append(f"packs réglementaires : aucun pack pour le cadre {f}")
    fields = _all_field_ids(m)
    authorities = _enum_ids(m, "authority")
    schemes = _enum_ids(m, "safetyClassScheme")
    tr_ids = {t["id"] for t in m.traceability_rules}
    type_ids = set(m.type_ids)
    doc_ids = {d["id"] for d in m.document_types.get("documentTypes", [])}
    for pid, p in packs.items():
        where = f"pack {pid}"
        if pid not in frameworks:
            err.append(f"{where}: cadre réglementaire inconnu")
        for a in p.get("authorities", []):
            if a not in authorities:
                err.append(f"{where}: autorité inconnue {a}")
        if p.get("defaultSafetyClassScheme") not in schemes:
            err.append(f"{where}: schéma de classement inconnu {p.get('defaultSafetyClassScheme')}")
        shown, hidden = set(p.get("showFields", [])), set(p.get("hideFields", []))
        for f in shown | hidden:
            if f not in fields:
                err.append(f"{where}: champ inconnu {f}")
        if shown & hidden:
            err.append(f"{where}: champs à la fois affichés et masqués {sorted(shown & hidden)}")
        for t in p.get("requiredTypes", []) or []:
            if t not in type_ids:
                err.append(f"{where}: type inconnu {t}")
        for d in p.get("requiredDocuments", []) or []:
            if d not in doc_ids:
                err.append(f"{where}: document inconnu {d}")
        for tr in p.get("traceabilityRules", []) or []:
            if tr not in tr_ids:
                err.append(f"{where}: règle de traçabilité inconnue {tr}")
        for k in p.get("keyTexts", []) or []:
            if k.get("confidence") not in ("H", "P"):
                err.append(f"{where}: niveau de confiance invalide pour {k.get('ref')}")
        # un champ masqué ne doit pas être exigé par une transition de workflow
        for wid, wf in m.workflows.items():
            for tr in wf["transitions"]:
                bad = hidden & set(tr.get("requiredFields", []) or [])
                if bad:
                    err.append(f"{where}: champ masqué {sorted(bad)} exigé par {wid}.{tr['id']}")


# --------------------------------------------------------------------------
def _check_field_value(m, where: str, type_id: str, field_id: str, value: Any) -> None:
    f = _field_def(m, type_id, field_id)
    if f is None:
        if field_id not in _PSEUDO_FIELDS:
            m.errors.append(f"{where}: champ {type_id}.{field_id} absent")
        return
    if value is None or not f["type"].startswith("enum:"):
        return
    if isinstance(value, str) and value.startswith("<"):
        return
    if value not in _enum_ids(m, f["type"][5:]):
        m.errors.append(f"{where}: valeur {value} inconnue pour {type_id}.{field_id}")


def validate_import_export(m) -> None:
    ie = m.import_export
    if not ie:
        return
    err = m.errors
    type_ids = set(m.type_ids)
    seen: set[str] = set()
    for p in (ie.get("reqif") or {}).get("profiles", []):
        where = f"ReqIF {p.get('id')}"
        if p["id"] in seen:
            err.append(f"{where}: identifiant dupliqué")
        seen.add(p["id"])
        if p.get("direction") not in ("import", "export"):
            err.append(f"{where}: sens invalide {p.get('direction')}")
        if p.get("type") not in type_ids:
            err.append(f"{where}: type inconnu {p.get('type')}")
            continue
        for mp in p.get("mapping", []):
            _check_field_value(m, where, p["type"], mp["field"], None)
        for f, v in (p.get("constants") or {}).items():
            _check_field_value(m, where, p["type"], f, v)
        for f in p.get("excludeFields", []) or []:
            _check_field_value(m, where, p["type"], f, None)
        if p.get("direction") == "import" and not p.get("updateOnly"):
            # un import créant des éléments doit renseigner les champs obligatoires sans défaut
            have = {mp["field"] for mp in p.get("mapping", [])} | set((p.get("constants") or {}).keys())
            for f in m.fields_of(m.type_by_id(p["type"])):
                if f.get("setByImport") and f["id"] not in have:
                    m.warnings.append(f"{where}: champ setByImport {f['id']} non alimenté par le profil")
    for r in (ie.get("word") or {}).get("rules", []):
        where = f"Word {r.get('id')}"
        ct = r.get("createsType")
        if ct not in type_ids and ct not in ("heading", "none", None):
            err.append(f"{where}: type inconnu {ct}")
        target = ct if ct in type_ids else None
        for f, v in (r.get("setFields") or {}).items():
            if target:
                _check_field_value(m, where, target, f, v)
            elif f not in _all_field_ids(m):
                err.append(f"{where}: champ inconnu {f}")
    for t in (ie.get("excel") or {}).get("templates", []):
        where = f"Excel {t.get('id')}"
        if t.get("type") not in type_ids:
            err.append(f"{where}: type inconnu {t.get('type')}")
            continue
        for f in (t.get("editableFields") or []) + (t.get("lockedFields") or []):
            _check_field_value(m, where, t["type"], f, None)
        computed = {f["id"] for f in m.fields_of(m.type_by_id(t["type"])) if f.get("computed")}
        bad = computed & set(t.get("editableFields") or [])
        if bad:
            err.append(f"{where}: champs calculés éditables {sorted(bad)}")
    for c in ie.get("connectors", []):
        where = f"connecteur {c.get('id')}"
        if c.get("confidence") not in ("H", "P"):
            err.append(f"{where}: niveau de confiance invalide")
        for o in c.get("objects", []) or []:
            if o.get("type") not in type_ids:
                err.append(f"{where}: type inconnu {o.get('type')}")
                continue
            for f in o.get("fields", []):
                _check_field_value(m, where, o["type"], f, None)


# --------------------------------------------------------------------------
#  Provisioning d'un projet : dérivation des paramètres à partir des réponses
# --------------------------------------------------------------------------
_CLASS_ORDER = ["classD", "classC", "classB", "classA"]
_MBSE_CONNECTORS = {"capella": "CX-MBSE-CAPELLA", "catiaMagic": "CX-MBSE-CAMEO"}
_PLM_CONNECTORS = {"teamcenter": "CX-PLM-TC", "threeDx": "CX-PLM-3DX"}


def _class_from_score(m, scores: dict[str, int]) -> tuple[str, int]:
    """Classe de tailoring : seuils de la grille + planchers éliminatoires."""
    total = sum(int(v) for v in scores.values())
    cls = "classA" if total >= 15 else "classB" if total >= 9 else "classC" if total >= 4 else "classD"
    for c in m.tailoring["scoringGrid"]["criteria"]:
        floor = (c.get("floor") or {}).get(scores.get(c["id"]))
        if floor and _CLASS_ORDER.index(floor) > _CLASS_ORDER.index(cls):
            cls = floor
    return cls, total


def _matches(when: dict[str, Any], answers: dict[str, Any]) -> bool:
    for param, values in (when or {}).items():
        ans = answers.get(param)
        if values == "multiple":
            if not (isinstance(ans, list) and len(ans) > 1):
                return False
            continue
        have = set(ans) if isinstance(ans, list) else {ans}
        if not have & set(values):
            return False
    return True


def derive_project(m, answers: dict[str, Any]) -> dict[str, Any]:
    """Applique les règles de dérivation de project_setup.yaml à un jeu de réponses."""
    d: dict[str, Any] = {"enableTypes": [], "enableDocuments": [], "connectors": [],
                         "qualifiedSignatory": "inactive", "extProject": None}
    pt = answers["projectType"]
    d["template"] = m.tailoring["projectTypeDefaults"][pt]["template"]
    d["archetype"] = m.archetype_of(d["template"])
    d["defaultClass"] = m.tailoring["projectTypeDefaults"][pt]["defaultClass"]
    d["projectClass"], d["score"] = _class_from_score(m, answers.get("tailoringScore") or {})
    d["packs"] = list(answers.get("regulatoryFrameworks") or [])
    for r in m.setup.get("derivationRules", []):
        if not _matches(r.get("when"), answers):
            continue
        sets = r.get("sets") or {}
        if "instance" in sets and "instance" not in d:
            d["instance"] = sets["instance"]
        if "extProject" in sets:
            d["extProject"] = sets["extProject"]
        d["enableTypes"] += [t for t in sets.get("enableTypes", []) or [] if t not in d["enableTypes"]]
        d["enableDocuments"] += [x for x in sets.get("enableDocuments", []) or [] if x not in d["enableDocuments"]]
        if sets.get("qualifiedSignatory") == "active":
            d["qualifiedSignatory"] = "active"
        if "projectEnums" in sets:
            d["projectEnums"] = list(sets["projectEnums"])
    for key, table in (("mbseTool", _MBSE_CONNECTORS), ("plmSystem", _PLM_CONNECTORS)):
        if answers.get(key) in table:
            d["connectors"].append(table[answers[key]])
    packs = (m.regulatory_packs or {}).get("packs", {})
    d["requiredTypes"] = sorted({t for p in d["packs"] for t in packs.get(p, {}).get("requiredTypes", []) or []})
    d["requiredDocuments"] = sorted({x for p in d["packs"] for x in packs.get(p, {}).get("requiredDocuments", []) or []})
    d["libraries"] = [lib for p in d["packs"] for lib in packs.get(p, {}).get("libraries", [])]
    d["hiddenFields"] = sorted({f for p in d["packs"] for f in packs.get(p, {}).get("hideFields", [])}
                               - {f for p in d["packs"] for f in packs.get(p, {}).get("showFields", [])})
    return d


def roles_needed(m, types: list[str], documents: list[str]) -> list[str]:
    """Rôles projet intervenant dans les transitions des workflows activés."""
    roles: set[str] = set()
    wfs = {m.type_by_id(t)["workflow"] for t in types}
    for w in wfs:
        for tr in m.workflows[w]["transitions"]:
            roles |= set(tr.get("roles", []))
    doc_by_id = {d["id"]: d for d in m.document_types.get("documentTypes", [])}
    for did in documents:
        for tr in m.document_workflows[doc_by_id[did]["workflow"]]["transitions"]:
            roles |= set(tr.get("roles", []))
    return sorted(roles)


def validate_pilots(m) -> None:
    if not m.pilots:
        return
    err = m.errors
    params = {q["param"]: q for q in m.setup.get("questionnaire", [])}
    type_ids = set(m.type_ids)
    doc_by_id = {d["id"]: d for d in m.document_types.get("documentTypes", [])}
    lib_types = {t["id"] for t in m.types if t["family"] == "library"}
    socle = {"nonConformance", "verificationCase", "deliverable"}
    criteria = {c["id"] for c in m.tailoring["scoringGrid"]["criteria"]}
    ids = [p.get("id") for p in m.pilots]
    if len(ids) != len(set(ids)):
        err.append("pilotes : identifiants dupliqués")
    for p in m.pilots:
        where = f"pilote {p.get('id')}"
        if len(p.get("id", "")) > 20:
            err.append(f"{where}: identifiant de projet > 20 caractères (convention)")
        ans = p.get("answers") or {}
        for param, q in params.items():
            if q.get("required") and param not in ans:
                err.append(f"{where}: réponse obligatoire manquante {param}")
        for param, val in ans.items():
            q = params.get(param)
            if q is None:
                err.append(f"{where}: paramètre inconnu {param}")
                continue
            if q.get("scoring"):
                if set(val) != criteria:
                    err.append(f"{where}: cotation incomplète ou inconnue {sorted(set(val) ^ criteria)}")
                for c, v in val.items():
                    if v not in (0, 1, 2, 3):
                        err.append(f"{where}: cote invalide {c}={v}")
                continue
            if q.get("text"):
                continue
            allowed = _enum_ids(m, q["enum"]) if "enum" in q else {o["id"] for o in q.get("options", [])}
            vals = val if isinstance(val, list) else [val]
            if isinstance(val, list) and not q.get("multi"):
                err.append(f"{where}: {param} n'accepte qu'une valeur")
            for v in vals:
                if v not in allowed:
                    err.append(f"{where}: valeur {v} inconnue pour {param}")
        if ans.get("projectType") not in m.tailoring.get("projectTypeDefaults", {}):
            continue
        d = derive_project(m, ans)
        p["derived"] = d
        if d["projectClass"] != d["defaultClass"] and not ans.get("tailoringJustification"):
            err.append(f"{where}: classe {d['projectClass']} ≠ classe par défaut {d['defaultClass']} sans justification (D02)")
        scope = p.get("pilotScope") or {}
        ptypes, pdocs = m.effective_profile(ans["projectType"])
        ptypes |= set(d["enableTypes"])
        pdocs |= set(d["enableDocuments"])
        active = set(scope.get("activeTypes", []))
        adocs = set(scope.get("activeDocuments", []))
        for t in sorted(active - type_ids):
            err.append(f"{where}: type inconnu {t}")
        for t in sorted((active & type_ids) - ptypes):
            err.append(f"{where}: type activé hors profil effectif {t}")
        for t in sorted(socle - active):
            err.append(f"{where}: type du socle non négociable non activé {t}")
        for t in d["requiredTypes"]:
            if t not in active:
                err.append(f"{where}: type imposé par un pack réglementaire non activé {t}")
        for x in sorted(adocs):
            if x not in doc_by_id:
                err.append(f"{where}: document inconnu {x}")
                continue
            if x not in pdocs:
                err.append(f"{where}: document activé hors profil effectif {x}")
            primary = next((t for t in doc_by_id[x]["allowedTypes"] if t not in lib_types), None)
            if primary and primary not in active:
                err.append(f"{where}: type principal {primary} du document {x} non activé")
        for x in d["requiredDocuments"]:
            if x not in adocs:
                err.append(f"{where}: document imposé par un pack réglementaire non activé {x}")
        for t in d["enableTypes"]:
            if t not in active:
                m.warnings.append(f"{where}: type activé par une règle de provisioning mais hors tranche pilote {t}")
        # une transition d'un workflow activé ne doit pas dépendre d'un type désactivé
        for w in sorted({m.type_by_id(t)["workflow"] for t in active & type_ids}):
            for tr in m.workflows[w]["transitions"]:
                for c in tr.get("conditions", []) or []:
                    for val in c.values():
                        if not isinstance(val, dict):
                            continue
                        for key in ("fromType", "type"):
                            dep = val.get(key)
                            if dep in type_ids and dep not in active:
                                err.append(f"{where}: {w}.{tr['id']} dépend du type non activé {dep}")
        scen = (m.coverage or {}).get("scenarios", {}).get(ans["projectType"], {})
        missing = [t for t in scen.get("types", []) if t not in active]
        if missing:
            m.infos.append(f"{where}: couverture partielle assumée, types du scénario non activés {missing}")


def validate_extension_policy(m) -> None:
    ep = m.extension_policy
    if not ep:
        return
    err = m.errors
    where = "politique d'extension"
    for e in ep.get("projectScopedEnums", []):
        if e not in m.enumerations:
            err.append(f"{where}: énumération inconnue {e}")
        elif m.enumerations[e].get("scope") != "project":
            err.append(f"{where}: {e} n'est pas déclarée de portée projet (scope: project)")
    prefix = ep.get("localFieldPrefix", "x_")
    core_fields = _all_field_ids(m)
    clash = sorted(f for f in core_fields if f.startswith(prefix))
    if clash:
        err.append(f"{where}: champs du cœur utilisant le préfixe local {prefix} {clash}")
    clash_enums = sorted(e for e in m.enumerations if e.startswith(prefix))
    if clash_enums:
        err.append(f"{where}: énumérations du cœur utilisant le préfixe local {prefix} {clash_enums}")
    pilot_ids = {p.get("id") for p in m.pilots}
    planned: dict[str, str] = {}
    for inc in ep.get("deploymentIncrements", []):
        types = list(inc.get("types", []) or [])
        for pid in inc.get("fromPilots", []) or []:
            if pid not in pilot_ids:
                err.append(f"{where}: {inc['id']} – pilote inconnu {pid}")
                continue
            pilot = next(p for p in m.pilots if p.get("id") == pid)
            types += (pilot.get("pilotScope") or {}).get("activeTypes", [])
        for t in types:
            if t not in m.type_ids:
                err.append(f"{where}: {inc['id']} – type inconnu {t}")
            planned.setdefault(t, inc["id"])
    unplanned = [t for t in m.type_ids if t not in planned]
    if ep.get("deploymentIncrements") and unplanned:
        err.append(f"{where}: types sans incrément de déploiement planifié {unplanned}")
