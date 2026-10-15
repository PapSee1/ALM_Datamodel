"""Chargement, expansion et validation du modèle de données ALM (répertoire model/).

Le modèle YAML est la source unique de vérité. Ce module :
  * charge les fichiers YAML ;
  * expanse les fieldSets (mixins) et les groupes de types ;
  * contrôle la cohérence référentielle (validate()).

Aucune dépendance hors bibliothèque standard + PyYAML.
"""
from __future__ import annotations

import pathlib
import re
from dataclasses import dataclass, field
from typing import Any

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODEL_DIR = ROOT / "model"

# Champs natifs Polarion : jamais redéfinis en champs personnalisés, mais
# utilisables dans les champs requis des transitions.
NATIVE_FIELDS = {
    "id", "type", "title", "description", "status", "resolution", "severity",
    "priority", "assignee", "author", "created", "updated", "dueDate",
    "plannedIn", "plannedStart", "plannedEnd", "categories", "hyperlinks",
    "attachments", "comments", "linkedWorkItems", "approvals", "project",
    "outlineNumber", "timeSpent", "remainingEstimate", "initialEstimate",
    "location", "module", "document", "watches", "resolvedOn", "timePoint",
}

FIELD_TYPES = {
    "string", "text", "richtext", "integer", "float", "currency", "date",
    "datetime", "duration", "boolean", "user", "testSteps",
}

SPECIAL_RULE_TARGETS = {"same", "any"}


@dataclass
class Model:
    enumerations: dict[str, Any]
    field_sets: dict[str, Any]
    types: list[dict[str, Any]]
    native_types: list[dict[str, Any]]
    type_groups: dict[str, list[str]]
    link_roles: list[dict[str, Any]]
    suspect_fields: dict[str, list[str]]
    traceability_rules: list[dict[str, Any]]
    workflows: dict[str, Any]
    document_workflows: dict[str, Any]
    conditions_catalog: dict[str, Any]
    functions_catalog: dict[str, Any]
    signature_meanings: dict[str, Any]
    state_categories: dict[str, Any]
    families: dict[str, Any]
    test_run_statuses: list[dict[str, Any]]
    test_record_results: list[dict[str, Any]]
    roles: dict[str, Any]
    document_types: dict[str, Any]
    tailoring: dict[str, Any]
    topology: dict[str, Any]
    coverage: dict[str, Any] = field(default_factory=dict)
    setup: dict[str, Any] = field(default_factory=dict)
    regulatory_packs: dict[str, Any] = field(default_factory=dict)
    import_export: dict[str, Any] = field(default_factory=dict)
    extension_policy: dict[str, Any] = field(default_factory=dict)
    pilots: list[dict[str, Any]] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    infos: list[str] = field(default_factory=list)

    # ------------------------------------------------------------------ helpers
    @property
    def type_ids(self) -> list[str]:
        return [t["id"] for t in self.types]

    def type_by_id(self, type_id: str) -> dict[str, Any]:
        for t in self.types:
            if t["id"] == type_id:
                return t
        raise KeyError(type_id)

    def expand_types(self, ref: Any) -> list[str]:
        """Expanse une référence de types : liste, groupe, 'same', 'any'."""
        if ref is None:
            return []
        if isinstance(ref, str):
            if ref in self.type_groups:
                return list(self.type_groups[ref])
            if ref in SPECIAL_RULE_TARGETS:
                return [ref]
            return [ref]
        out: list[str] = []
        for r in ref:
            out.extend(self.expand_types(r))
        return out

    def fields_of(self, type_def: dict[str, Any]) -> list[dict[str, Any]]:
        """Champs personnalisés d'un type, fieldSets expansés (ordre conservé)."""
        result: list[dict[str, Any]] = []
        seen: dict[str, dict[str, Any]] = {}
        for fs in type_def.get("fieldSets", []) or []:
            for f in self.field_sets[fs]["fields"]:
                if f["id"] not in seen:
                    seen[f["id"]] = f
                    result.append(dict(f, origin=fs))
        for f in type_def.get("fields", []) or []:
            if f["id"] in seen:
                # surcharge locale : remplace la définition héritée
                result = [x for x in result if x["id"] != f["id"]]
            seen[f["id"]] = f
            result.append(dict(f, origin="local"))
        return result

    def field_ids_of(self, type_id: str) -> set[str]:
        return {f["id"] for f in self.fields_of(self.type_by_id(type_id))}

    def role_ids(self) -> set[str]:
        ids = {r["id"] for r in self.roles.get("projectRoles", [])}
        ids |= {r["id"] for r in self.roles.get("globalRoles", [])}
        return ids

    def link_allowed(self, src: str, role_id: str, dst: str, cross_project: bool = False) -> bool:
        """Vrai si les règles du rôle autorisent src → dst (dst d'un autre projet si cross_project)."""
        role = next((r for r in self.link_roles if r["id"] == role_id), None)
        if role is None:
            return False
        rules = role.get("rules", [])
        if not rules:
            return True
        for rule in rules:
            frm = self.expand_types(rule.get("from"))
            to = self.expand_types(rule.get("to"))
            if "any" in frm or "any" in to:
                return True
            if src not in frm:
                continue
            if to == ["same"] and src == dst:
                return True
            if dst in to:
                return True
            if cross_project and role.get("crossProject"):
                return True
        return False

    def effective_profile(self, project_type: str) -> tuple[set[str], set[str]]:
        """Types et documents du profil effectif d'une typologie (classe ∪ compléments)."""
        d = self.tailoring["projectTypeDefaults"][project_type]
        prof = self.tailoring["classProfiles"][d["defaultClass"]]
        types = set(self.type_ids) if prof["workItemTypes"] == "all" else set(prof["workItemTypes"])
        all_docs = {x["id"] for x in self.document_types["documentTypes"]}
        docs = all_docs if prof["documentTypes"] == "all" else set(prof["documentTypes"])
        types |= set(d.get("addTypes", []))
        docs |= set(d.get("addDocuments", []))
        return types, docs

    def template_chain(self, template_id: str) -> list[str]:
        """Chaîne d'héritage d'un gabarit (lui-même → … → master)."""
        by_id = {t["id"]: t for t in self.topology.get("projectTemplates", [])}
        chain, cur = [], template_id
        while cur and cur in by_id and cur not in chain:
            chain.append(cur)
            cur = by_id[cur].get("extends")
        return chain

    def template_level(self, template_id: str) -> str | None:
        for t in self.topology.get("projectTemplates", []):
            if t["id"] == template_id:
                return t.get("level")
        return None

    def archetype_of(self, template_id: str) -> str | None:
        for tid in self.template_chain(template_id):
            if self.template_level(tid) == "archetype":
                return tid
        return None

    def all_workflows(self) -> dict[str, Any]:
        out = dict(self.workflows)
        out.update(self.document_workflows)
        return out


class _Yaml12Loader(yaml.SafeLoader):
    """SafeLoader aux booléens YAML 1.2 (true / false uniquement).

    En YAML 1.1 (comportement par défaut de PyYAML), yes / no / on / off sont des
    booléens : l'option d'énumération 'yes' deviendrait l'identifiant Polarion
    'True' et ne correspondrait plus aux requêtes ni aux conditions ('eip = yes').
    """


_Yaml12Loader.yaml_implicit_resolvers = {
    k: [(tag, rx) for tag, rx in v if tag != "tag:yaml.org,2002:bool"]
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
_Yaml12Loader.add_implicit_resolver(
    "tag:yaml.org,2002:bool", re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$"), list("tTfF"))


def load_yaml(path: pathlib.Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as fh:
        return yaml.load(fh, Loader=_Yaml12Loader) or {}  # noqa: S506 (loader dérivé de SafeLoader)


def _load(name: str) -> dict[str, Any]:
    return load_yaml(MODEL_DIR / name)


def _load_optional(name: str) -> dict[str, Any]:
    return _load(name) if (MODEL_DIR / name).exists() else {}


def load_model() -> Model:
    enums = _load("enumerations.yaml")
    wit = _load("work_item_types.yaml")
    links = _load("link_roles.yaml")
    wf = _load("workflows.yaml")
    roles = _load("roles.yaml")
    docs = _load("document_types.yaml")
    tailoring = _load("tailoring.yaml")
    topology = _load("project_topology.yaml")
    return Model(
        enumerations=enums["enumerations"],
        field_sets=wit.get("fieldSets", {}),
        types=wit["workItemTypes"],
        native_types=wit.get("nativeTypes", []),
        type_groups=links.get("typeGroups", {}),
        link_roles=links["linkRoles"],
        suspect_fields=links.get("suspectTriggerFields", {}),
        traceability_rules=links.get("traceabilityRules", []),
        workflows=wf["workflows"],
        document_workflows=wf.get("documentWorkflows", {}),
        conditions_catalog=wf.get("conditionsCatalog", {}),
        functions_catalog=wf.get("functionsCatalog", {}),
        signature_meanings=wf.get("signatureMeanings", {}),
        state_categories=wf.get("stateCategories", {}),
        families=wit.get("families", {}),
        test_run_statuses=wf.get("testRunStatuses", []),
        test_record_results=wf.get("testRecordResults", []),
        roles=roles,
        document_types=docs,
        tailoring=tailoring,
        topology=topology,
        coverage=_load_optional("coverage_scenarios.yaml"),
        setup=_load_optional("project_setup.yaml"),
        regulatory_packs=_load_optional("regulatory_packs.yaml"),
        import_export=_load_optional("import_export.yaml"),
        extension_policy=_load_optional("extension_policy.yaml"),
        pilots=[load_yaml(p) for p in sorted((MODEL_DIR / "pilots").glob("*.yaml"))],
    )


# ============================================================================
#  VALIDATION
# ============================================================================
def validate(m: Model) -> Model:
    m.errors, m.warnings, m.infos = [], [], []
    err, warn = m.errors, m.warnings
    type_ids = set(m.type_ids)
    native_type_ids = {t["id"] for t in m.native_types}

    # ---------------------------------------------------------- énumérations
    for eid, e in m.enumerations.items():
        ids = [o["id"] for o in e.get("options", [])]
        if not ids:
            err.append(f"enum {eid}: aucune option")
        if len(ids) != len(set(ids)):
            err.append(f"enum {eid}: identifiants d'option dupliqués")
        defaults = [o for o in e.get("options", []) if o.get("default")]
        if len(defaults) > 1:
            err.append(f"enum {eid}: plusieurs options par défaut")
        for o in e.get("options", []):
            if not isinstance(o.get("id"), str):
                err.append(f"enum {eid}: identifiant d'option non textuel {o.get('id')!r} (booléen YAML 1.1 ? citer la valeur)")
            if not o.get("fr") or not o.get("en"):
                err.append(f"enum {eid}.{o.get('id')}: libellé fr/en manquant")

    used_enums: set[str] = set()
    for fs in m.field_sets.values():
        used_enums |= {f["type"][5:] for f in fs.get("fields", []) if f["type"].startswith("enum:")}
    for t in m.types:
        used_enums |= {f["type"][5:] for f in t.get("fields", []) or [] if f["type"].startswith("enum:")}
    used_enums |= {f["type"][5:] for f in m.document_types.get("documentCustomFields", []) if f["type"].startswith("enum:")}
    used_enums |= {q.get("enum") for q in m.setup.get("questionnaire", [])}
    used_enums |= {"projectType", "projectClass", "businessUnit", "businessLine", "operationalUnit", "reviewType",
                   "regulatoryFramework", "safetyClassScheme", "authority", "discipline", "habilitationDomain"}
    for eid in m.enumerations:
        if eid not in used_enums:
            warn.append(f"enum {eid}: référencée par aucun champ ni paramètre")
        for o in m.enumerations[eid].get("options", []):
            oid = o.get("id")
            if isinstance(oid, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_]*$", oid):
                err.append(f"enum {eid}: identifiant d'option non conforme {oid!r}")

    # --------------------------------------------------------------- types
    if len(type_ids) != len(m.type_ids):
        err.append("types: identifiants dupliqués")
    for fs_id, fs in m.field_sets.items():
        for f in fs.get("fields", []):
            _check_field(m, f"fieldSet {fs_id}", f, err)
    global_field_types: dict[str, tuple[str, bool, str]] = {}
    for t in m.types:
        tid = t["id"]
        for fs in t.get("fieldSets", []) or []:
            if fs not in m.field_sets:
                err.append(f"type {tid}: fieldSet inconnu {fs}")
        local_ids = [f["id"] for f in t.get("fields", []) or []]
        if len(local_ids) != len(set(local_ids)):
            err.append(f"type {tid}: champs locaux dupliqués")
        if not re.match(r"^[a-z][A-Za-z0-9]*$", tid):
            err.append(f"type {tid}: identifiant non conforme (camelCase attendu)")
        for f in t.get("fields", []) or []:
            _check_field(m, f"type {tid}", f, err)
        for f in m.fields_of(t):
            sig = (f["type"], bool(f.get("multi")), tid)
            prev = global_field_types.get(f["id"])
            if prev and (prev[0], prev[1]) != (sig[0], sig[1]):
                err.append(
                    f"champ '{f['id']}': définition incohérente entre {prev[2]} "
                    f"({prev[0]}, multi={prev[1]}) et {tid} ({sig[0]}, multi={sig[1]})"
                )
            global_field_types.setdefault(f["id"], sig)
        if m.families and t.get("family") not in m.families:
            err.append(f"type {tid}: famille inconnue {t.get('family')}")
        wf = t.get("workflow")
        if wf not in m.workflows:
            err.append(f"type {tid}: workflow inconnu {wf}")
        elif tid not in m.workflows[wf].get("appliesTo", []):
            err.append(f"type {tid}: absent de appliesTo du workflow {wf}")
        else:
            states = {s["id"] for s in m.workflows[wf]["states"]}
            for f in m.fields_of(t):
                at = f.get("requiredAt")
                if not at:
                    continue
                if at == "soumission":
                    if not m.workflows[wf].get("submitState"):
                        err.append(f"type {tid}: champ {f['id']} requiredAt 'soumission' mais le workflow {wf} n'a pas de submitState")
                elif at not in states:
                    err.append(f"type {tid}: champ {f['id']} requiredAt '{at}' n'est pas un état de {wf}")
    # un même identifiant de champ → un seul couple de libellés (information)
    labels: dict[str, set] = {}
    for t in m.types:
        for f in m.fields_of(t):
            labels.setdefault(f["id"], set()).add((f["fr"], f["en"]))
    for fid, ls in labels.items():
        if len(ls) > 1:
            m.infos.append(f"champ '{fid}': libellés différents selon le type {sorted(ls)}")

    # --------------------------------------------------------- groupes types
    for g, members in m.type_groups.items():
        for x in members:
            if x not in type_ids:
                err.append(f"typeGroup {g}: type inconnu {x}")

    # ------------------------------------------------------------ liens
    role_ids = [r["id"] for r in m.link_roles]
    if len(role_ids) != len(set(role_ids)):
        err.append("linkRoles: identifiants dupliqués")
    for r in m.link_roles:
        for k in ("fr", "frOpposite", "en", "enOpposite"):
            if not r.get(k):
                err.append(f"linkRole {r['id']}: libellé {k} manquant")
        for rule in r.get("rules", []):
            for side in ("from", "to"):
                for x in m.expand_types(rule.get(side)):
                    if x in SPECIAL_RULE_TARGETS:
                        continue
                    if x not in type_ids and x not in native_type_ids:
                        err.append(f"linkRole {r['id']}: type inconnu '{x}' ({side})")
    for key, fields in m.suspect_fields.items():
        if key == "default":
            continue
        if key not in m.type_groups and key not in type_ids:
            err.append(f"suspectTriggerFields: clé inconnue {key}")
            continue
        for x in m.expand_types(key):
            missing = [f for f in fields if f not in m.field_ids_of(x) and f not in NATIVE_FIELDS]
            if missing:
                err.append(f"suspectTriggerFields {key}: champs absents de {x} {missing}")

    # -------------------------------------------------- règles de traçabilité
    link_set = set(role_ids)
    for tr in m.traceability_rules:
        applies = tr.get("appliesTo")
        for x in m.expand_types(applies):
            if x not in type_ids and x != "document":
                err.append(f"{tr['id']}: type inconnu {x}")
        applies_types = [x for x in m.expand_types(applies) if x in type_ids]
        for chk in ([tr["check"]] if "check" in tr else []) + list(tr.get("checks", []) or []):
            for k in ("outgoing", "incoming"):
                if k in chk and chk[k] not in link_set:
                    err.append(f"{tr['id']}: rôle de lien inconnu {chk[k]}")
                elif k in chk:
                    ok = any(m.link_allowed(x, chk[k], y, True) if k == "outgoing" else m.link_allowed(y, chk[k], x, True)
                             for x in applies_types for y in type_ids)
                    if applies_types and not ok:
                        err.append(f"{tr['id']}: aucun type de appliesTo n'est {'source' if k == 'outgoing' else 'cible'} du rôle {chk[k]}")
            for k in ("incomingAny", "outgoingAny"):
                for x in chk.get(k, []) or []:
                    if x not in link_set:
                        err.append(f"{tr['id']}: rôle de lien inconnu {x}")
            if "excludeFromCoverage" in chk and chk["excludeFromCoverage"] not in link_set:
                err.append(f"{tr['id']}: rôle de lien inconnu {chk['excludeFromCoverage']}")
            for k in ("field", "fieldNonEmpty", "unlessFieldNonEmpty"):
                if k in chk:
                    missing = [x for x in applies_types if chk[k] not in m.field_ids_of(x) and chk[k] not in NATIVE_FIELDS]
                    if missing:
                        err.append(f"{tr['id']}: champ {chk[k]} absent de {missing}")
        when = tr.get("when") or {}
        if "field" in when:
            missing = [x for x in applies_types if when["field"] not in m.field_ids_of(x)]
            if missing:
                err.append(f"{tr['id']}: champ de condition {when['field']} absent de {missing}")
        for st in when.get("status", []) or []:
            if applies_types and not any(st in {s["id"] for s in m.workflows[m.type_by_id(x)["workflow"]]["states"]} for x in applies_types):
                err.append(f"{tr['id']}: état {st} inconnu des workflows de appliesTo")

    # ------------------------------------------------------------ workflows
    roles = m.role_ids()
    for wid, wf in m.all_workflows().items():
        is_doc = wid in m.document_workflows
        states = [s["id"] for s in wf["states"]]
        if len(states) != len(set(states)):
            err.append(f"workflow {wid}: états dupliqués")
        if wf["initial"] not in states:
            err.append(f"workflow {wid}: état initial inconnu {wf['initial']}")
        tids = [t["id"] for t in wf["transitions"]]
        if len(tids) != len(set(tids)):
            err.append(f"workflow {wid}: transitions dupliquées")
        applies = wf.get("appliesTo", [])
        for x in applies:
            if x not in type_ids:
                err.append(f"workflow {wid}: type inconnu {x}")
        if not is_doc and wf.get("submitState") not in states:
            err.append(f"workflow {wid}: submitState inconnu ou absent {wf.get('submitState')}")
        tr_ids = set(tids)
        suspect_roles = {r["id"] for r in m.link_roles if r.get("suspect")}
        reachable = {wf["initial"]}
        changed = True
        while changed:
            changed = False
            for tr in wf["transitions"]:
                if set(tr["from"]) & reachable and tr["to"] not in reachable:
                    reachable.add(tr["to"])
                    changed = True
        for s in wf["states"]:
            if s["id"] not in reachable:
                err.append(f"workflow {wid}: état {s['id']} inatteignable")
            outgoing = [t for t in wf["transitions"] if s["id"] in t["from"]]
            if not outgoing and s.get("category") not in ("done", "cancelled"):
                warn.append(f"workflow {wid}: état non terminal sans sortie {s['id']}")
            if outgoing and s.get("category") == "cancelled":
                warn.append(f"workflow {wid}: état de catégorie 'cancelled' avec transition sortante {s['id']}")
            if m.state_categories and s.get("category") not in m.state_categories:
                err.append(f"workflow {wid}: catégorie inconnue {s.get('category')} pour {s['id']}")
            if not s.get("en"):
                err.append(f"workflow {wid}: état {s['id']} sans libellé en")
        for tr in wf["transitions"]:
            for st in tr["from"] + [tr["to"]]:
                if st not in states:
                    err.append(f"workflow {wid}.{tr['id']}: état inconnu {st}")
            if not tr.get("en"):
                err.append(f"workflow {wid}.{tr['id']}: transition sans libellé en")
            for role in tr.get("roles", []):
                if role not in roles:
                    err.append(f"workflow {wid}.{tr['id']}: rôle inconnu {role}")
            for c in tr.get("conditions", []) or []:
                for k, v in c.items():
                    if k not in m.conditions_catalog:
                        err.append(f"workflow {wid}.{tr['id']}: condition inconnue {k}")
                    if k == "noSuspectLinks" and isinstance(v, list):
                        for r in v:
                            if r not in suspect_roles:
                                err.append(f"workflow {wid}.{tr['id']}: noSuspectLinks cite un rôle non suspect {r}")
                            elif not any(m.link_allowed(x, r, y, True) for x in applies for y in type_ids):
                                err.append(f"workflow {wid}.{tr['id']}: aucun type de appliesTo n'est source du rôle {r}")
                    if isinstance(v, dict):
                        for ft in v.get("forTypes", []) or []:
                            if ft not in applies:
                                err.append(f"workflow {wid}.{tr['id']}: forTypes cite {ft} hors appliesTo")
                        fld = v.get("field")
                        targets = v.get("forTypes") or applies
                        if k in ("fieldValue",) and fld and not is_doc:
                            missing = [x for x in targets if fld not in m.field_ids_of(x) and fld not in NATIVE_FIELDS]
                            if missing:
                                err.append(f"workflow {wid}.{tr['id']}: champ {fld} absent de {missing}")
                        for key in ("unlessFieldNonEmpty",):
                            if v.get(key) and not is_doc:
                                missing = [x for x in targets if v[key] not in m.field_ids_of(x)]
                                if missing:
                                    err.append(f"workflow {wid}.{tr['id']}: champ {v[key]} absent de {missing}")
                        for key in ("nonEmptyAny",):
                            for fld2 in v.get(key, []) or []:
                                missing = [x for x in targets if fld2 not in m.field_ids_of(x)]
                                if missing:
                                    err.append(f"workflow {wid}.{tr['id']}: champ {fld2} absent de {missing}")
                        if k == "linkedItemsStatus":
                            if v.get("type") and v["type"] not in type_ids:
                                err.append(f"workflow {wid}.{tr['id']}: type lié inconnu {v['type']}")
                            if v.get("type"):
                                st_ok = {s["id"] for s in m.workflows[m.type_by_id(v["type"])["workflow"]]["states"]}
                                bad = [x for x in v.get("statuses", []) if x not in st_ok]
                                if bad:
                                    err.append(f"workflow {wid}.{tr['id']}: statuts {bad} inconnus pour {v['type']}")
                qs = c.get("qualifiedSignatory")
                if isinstance(qs, dict):
                    fld = qs.get("field")
                    if is_doc:
                        if fld not in {f["id"] for f in m.document_types.get("documentCustomFields", [])}:
                            err.append(f"workflow {wid}.{tr['id']}: champ d'habilitation '{fld}' absent des champs de document")
                    else:
                        missing = [x for x in applies if fld not in m.field_ids_of(x)]
                        if missing:
                            err.append(f"workflow {wid}.{tr['id']}: champ d'habilitation '{fld}' absent de {missing}")
            for fn in tr.get("functions", []) or []:
                for k, v in fn.items():
                    if k not in m.functions_catalog:
                        err.append(f"workflow {wid}.{tr['id']}: fonction inconnue {k}")
                    if k == "setFieldValue" and not is_doc:
                        fld = v.get("field")
                        missing = [x for x in applies if fld not in m.field_ids_of(x)]
                        if missing:
                            err.append(f"workflow {wid}.{tr['id']}: champ {fld} absent de {missing}")
                        val = v.get("value", v.get("valueIfEmpty"))
                        for x in applies:
                            fdef = next((f for f in m.fields_of(m.type_by_id(x)) if f["id"] == fld), None)
                            if fdef and fdef["type"].startswith("enum:"):
                                opts = {o["id"] for o in m.enumerations[fdef["type"][5:]]["options"]}
                                if val not in opts:
                                    err.append(f"workflow {wid}.{tr['id']}: valeur {val} inconnue pour {fld}")
                    if k == "createLinkedItem":
                        if v.get("type") not in type_ids:
                            err.append(f"workflow {wid}.{tr['id']}: type inconnu {v.get('type')}")
                        if v.get("role") not in link_set:
                            err.append(f"workflow {wid}.{tr['id']}: rôle inconnu {v.get('role')}")
                    if k == "invokeOnDocItems" and v.get("actionId") not in ("submit", "approve"):
                        err.append(f"workflow {wid}.{tr['id']}: invokeOnDocItems n'admet que submit / approve")
            sig = tr.get("signature")
            if sig and sig.get("required") and sig.get("meaning") not in m.signature_meanings:
                err.append(f"workflow {wid}.{tr['id']}: signification de signature inconnue")
            if not is_doc:
                for rf in tr.get("requiredFields", []) or []:
                    if rf in NATIVE_FIELDS:
                        continue
                    missing = [x for x in applies if rf not in m.field_ids_of(x)]
                    if missing:
                        err.append(f"workflow {wid}.{tr['id']}: champ requis '{rf}' absent de {missing}")

    # -------------------------------------------------------------- documents
    doc_field_ids = {f["id"] for f in m.document_types.get("documentCustomFields", [])}
    for f in m.document_types.get("documentCustomFields", []):
        _check_field(m, "documentCustomFields", f, err)
    for d in m.document_types.get("documentTypes", []):
        if d["workflow"] not in m.document_workflows:
            err.append(f"documentType {d['id']}: workflow inconnu {d['workflow']}")
        for x in d.get("allowedTypes", []):
            if x not in type_ids:
                err.append(f"documentType {d['id']}: type inconnu {x}")
        if d.get("primaryType") not in d.get("allowedTypes", []):
            err.append(f"documentType {d['id']}: primaryType absent ou hors allowedTypes")
        for x in d.get("cascadeTypes", []) or []:
            if x not in d.get("allowedTypes", []):
                err.append(f"documentType {d['id']}: type cascadé {x} hors allowedTypes")
                continue
            trs = {t["id"] for t in m.workflows[m.type_by_id(x)["workflow"]]["transitions"]}
            if not {"submit", "approve"} <= trs:
                err.append(f"documentType {d['id']}: le type cascadé {x} n'a pas d'actions submit et approve")
        for x, statuses in (d.get("approvalGate") or {}).items():
            if x not in d.get("allowedTypes", []):
                err.append(f"documentType {d['id']}: approvalGate cite {x} hors allowedTypes")
                continue
            st = {s["id"] for s in m.workflows[m.type_by_id(x)["workflow"]]["states"]}
            bad = [y for y in statuses if y not in st]
            if bad:
                err.append(f"documentType {d['id']}: statuts {bad} inconnus pour {x}")
        for x in d.get("allowedTypes", []):
            if x in (d.get("cascadeTypes") or []) or x in (d.get("approvalGate") or {}):
                continue
            if m.type_by_id(x)["family"] == "library":
                continue
            m.infos.append(f"documentType {d['id']}: le type {x} n'est ni cascadé ni sous approvalGate (non contrôlé à l'approbation)")
    # une condition cascadedItemsApproved / invokeOnDocItems doit être calculable pour chaque document
    for wid, wf in m.document_workflows.items():
        for tr in wf["transitions"]:
            for fn in tr.get("functions", []) or []:
                for k, v in fn.items():
                    if k == "invokeOnDocItems":
                        for d in m.document_types.get("documentTypes", []):
                            if d["workflow"] != wid:
                                continue
                            for x in d.get("cascadeTypes", []) or []:
                                trs = {t["id"] for t in m.workflows[m.type_by_id(x)["workflow"]]["transitions"]}
                                if v.get("actionId") not in trs:
                                    err.append(f"documentType {d['id']}: cascade {v.get('actionId')} impossible pour {x}")
    del doc_field_ids

    # ------------------------------------------------------------------ rôles
    g_ids = [r["id"] for r in m.roles.get("globalRoles", [])]
    p_ids = [r["id"] for r in m.roles.get("projectRoles", [])]
    for dup in sorted(set(g_ids) & set(p_ids)):
        err.append(f"roles: identifiant {dup} défini à la fois en rôle global et en rôle projet")
    if len(p_ids) != len(set(p_ids)) or len(g_ids) != len(set(g_ids)):
        err.append("roles: identifiants dupliqués")
    for r in m.roles.get("projectRoles", []):
        if r.get("pseudo") and r["id"] not in ("anyProjectMember", "documentOwner", "workitem.assignee", "workitem.author"):
            err.append(f"roles: pseudo-rôle {r['id']} sans mappage dans le générateur")

    # -------------------------------------------------------------- tailoring
    doc_type_ids = {d["id"] for d in m.document_types.get("documentTypes", [])}
    for cid, prof in m.tailoring.get("classProfiles", {}).items():
        wits = prof.get("workItemTypes")
        if wits != "all":
            for x in wits:
                if x not in type_ids:
                    err.append(f"tailoring {cid}: type inconnu {x}")
        dts = prof.get("documentTypes")
        if dts != "all":
            for x in dts:
                if x not in doc_type_ids:
                    err.append(f"tailoring {cid}: type de document inconnu {x}")
        if prof.get("documentWorkflow") not in m.document_workflows:
            err.append(f"tailoring {cid}: workflow documentaire inconnu")
        review_opts = {o["id"] for o in m.enumerations["reviewType"]["options"]}
        for r in prof.get("reviews", []):
            if r not in review_opts:
                err.append(f"tailoring {cid}: type de revue inconnu {r}")
        if prof.get("reviews") and wits != "all" and "review" not in wits:
            err.append(f"tailoring {cid}: des revues sont imposées mais le type 'review' est absent du profil")
        if wits != "all" and "reviewFinding" in wits and "review" not in wits:
            err.append(f"tailoring {cid}: reviewFinding sans review (lien raisedIn impossible)")
    thresholds = m.tailoring.get("scoringGrid", {}).get("thresholds", {})
    for cid, th in thresholds.items():
        if cid not in m.tailoring.get("classProfiles", {}) or not isinstance(th, dict) or "min" not in th:
            err.append(f"tailoring: seuil invalide pour {cid} (attendu {{min: n, fr: ...}})")
        # le socle doit rester applicable : FNC, vérification, livrable
        if wits != "all":
            for core in ("nonConformance", "verificationCase", "deliverable"):
                if core not in wits:
                    err.append(f"tailoring {cid}: type du socle non négociable absent ({core})")
    project_types = {o["id"] for o in m.enumerations["projectType"]["options"]}
    defaults = m.tailoring.get("projectTypeDefaults", {})
    for pt in project_types:
        if pt not in defaults:
            err.append(f"tailoring: typologie de projet sans profil par défaut {pt}")
    templates = {t["id"] for t in m.topology.get("projectTemplates", [])}
    _validate_topology(m)
    bus = {o["id"] for o in m.enumerations["businessUnit"]["options"]}
    for pt, d in defaults.items():
        if pt not in project_types:
            err.append(f"tailoring: typologie inconnue {pt}")
        if d["template"] not in templates:
            err.append(f"tailoring {pt}: gabarit inconnu {d['template']}")
        elif m.template_level(d["template"]) == "master":
            err.append(f"tailoring {pt}: le gabarit master n'est pas instanciable")
        for b in d.get("bu", []):
            if b not in bus:
                err.append(f"tailoring {pt}: BU inconnue {b}")
        for x in d.get("addTypes", []):
            if x not in type_ids:
                err.append(f"tailoring {pt}: type ajouté inconnu {x}")
        for x in d.get("addDocuments", []):
            if x not in doc_type_ids:
                err.append(f"tailoring {pt}: document ajouté inconnu {x}")

    # ---------------- cohérence documents ↔ profil effectif (par typologie)
    doc_by_id = {x["id"]: x for x in m.document_types.get("documentTypes", [])}
    for pt in defaults:
        if pt not in project_types:
            continue
        ptypes, pdocs = m.effective_profile(pt)
        lib_types = {t["id"] for t in m.types if t["family"] == "library"}
        for did in sorted(pdocs):
            allowed = [x for x in doc_by_id[did]["allowedTypes"] if x not in lib_types]
            if allowed and allowed[0] not in ptypes:
                err.append(f"profil {pt}: le type principal '{allowed[0]}' du document {did} est absent du profil")
            hidden = [x for x in allowed[1:] if x not in ptypes]
            if hidden:
                m.infos.append(f"profil {pt}: document {did} – types optionnels masqués par le profil {hidden}")

    # ---------------- états : un même identifiant = une même catégorie
    cats: dict[str, set] = {}
    for wid, wf in m.all_workflows().items():
        for st in wf["states"]:
            cats.setdefault(st["id"], set()).add(st.get("category"))
    for sid, cs in cats.items():
        if len(cs) > 1:
            err.append(f"état '{sid}' : catégories divergentes selon les workflows {sorted(cs)}")

    # ---------------- politique des champs obligatoires (P6)
    for t in m.types:
        if t.get("creationMode", "any") not in ("any", "manual"):
            err.append(f"type {t['id']}: creationMode invalide")
        for f in m.fields_of(t):
            if not f.get("required"):
                continue
            ty = f["type"]
            has_default = ty.startswith("enum:") and ty[5:] in m.enumerations and any(
                o.get("default") for o in m.enumerations[ty[5:]]["options"])
            if not (has_default or f.get("setByImport") or t.get("creationMode") == "manual"):
                err.append(f"type {t['id']}: champ '{f['id']}' obligatoire à la création sans défaut "
                           f"(bloquerait imports / synchronisations) – utiliser requiredAt")

    # ---------------- contrôle technique : indépendance obligatoire
    for wid, wf in m.all_workflows().items():
        for tr in wf["transitions"]:
            keys = {k for c in tr.get("conditions", []) or [] for k in c}
            if tr.get("technicalCheck") and "approverNotAuthor" not in keys:
                err.append(f"workflow {wid}.{tr['id']}: technicalCheck sans condition approverNotAuthor")
            sig = tr.get("signature") or {}
            if sig.get("required") and sig.get("meaning") == "verified" and not tr.get("technicalCheck"):
                err.append(f"workflow {wid}.{tr['id']}: signature 'vérifié' sans technicalCheck")

    # ---------------- scénarios de couverture
    _validate_coverage(m, project_types, doc_type_ids)

    # ---------------- provisioning, packs réglementaires, import / export
    import model_checks  # noqa: PLC0415 (module voisin, évite un import circulaire)
    model_checks.validate_setup(m)
    model_checks.validate_regulatory_packs(m)
    model_checks.validate_import_export(m)
    model_checks.validate_pilots(m)
    model_checks.validate_extension_policy(m)
    return m


def _validate_topology(m: Model) -> None:
    err = m.errors
    tpls = m.topology.get("projectTemplates", [])
    by_id = {t["id"]: t for t in tpls}
    if len(by_id) != len(tpls):
        err.append("topologie : identifiants de gabarits dupliqués")
    masters = [t["id"] for t in tpls if t.get("level") == "master"]
    if len(masters) != 1:
        err.append(f"topologie : un et un seul gabarit master attendu ({masters})")
    for t in tpls:
        lvl = t.get("level")
        if lvl not in ("master", "archetype", "specialization"):
            err.append(f"gabarit {t['id']}: niveau invalide {lvl}")
        if lvl != "master":
            if t.get("extends") not in by_id:
                err.append(f"gabarit {t['id']}: extends inconnu {t.get('extends')}")
                continue
            chain = m.template_chain(t["id"])
            if by_id.get(chain[-1], {}).get("level") != "master":
                err.append(f"gabarit {t['id']}: chaîne d'héritage sans master (cycle ?) {chain}")
        if lvl == "archetype" and by_id.get(t.get("extends"), {}).get("level") != "master":
            err.append(f"gabarit {t['id']}: un archétype hérite directement du master")
    instances = {i["id"] for i in m.topology.get("instances", [])}
    for g in m.topology.get("projectGroups", []):
        if g.get("instance") and g["instance"] not in instances:
            err.append(f"groupe {g['id']}: instance inconnue {g['instance']}")
        for p in g.get("projects", []):
            if p.get("template") and p["template"] not in by_id:
                err.append(f"projet {p['id']}: gabarit inconnu {p['template']}")


def _validate_coverage(m: Model, project_types: set, doc_type_ids: set) -> None:
    err = m.errors
    cov = m.coverage or {}
    scen = cov.get("scenarios", {})
    for pt in project_types:
        if pt not in scen:
            err.append(f"couverture : aucun scénario pour la typologie {pt}")
    type_ids = set(m.type_ids)
    for pt, sc in scen.items():
        if pt not in project_types:
            err.append(f"couverture : typologie inconnue {pt}")
            continue
        ptypes, pdocs = m.effective_profile(pt)
        for x in sc.get("types", []):
            if x not in type_ids:
                err.append(f"couverture {pt}: type inconnu {x}")
            elif x not in ptypes:
                err.append(f"couverture {pt}: type requis {x} absent du profil effectif")
        for x in sc.get("documents", []):
            if x not in doc_type_ids:
                err.append(f"couverture {pt}: document inconnu {x}")
            elif x not in pdocs:
                err.append(f"couverture {pt}: document requis {x} absent du profil effectif")
        _check_traces(m, f"couverture {pt}", sc.get("traces", []), ptypes)
        for tid, fields in (sc.get("fields") or {}).items():
            if tid not in type_ids:
                err.append(f"couverture {pt}: type inconnu {tid}")
                continue
            have = m.field_ids_of(tid)
            for f in fields:
                if f not in have:
                    err.append(f"couverture {pt}: attribut {tid}.{f} absent")
        for eid, opts in (sc.get("enumOptions") or {}).items():
            if eid not in m.enumerations:
                err.append(f"couverture {pt}: énumération inconnue {eid}")
                continue
            have = {o["id"] for o in m.enumerations[eid]["options"]}
            for o in opts:
                if o not in have:
                    err.append(f"couverture {pt}: valeur {eid}.{o} absente")
    for i, sc in enumerate(cov.get("transverse", []) or []):
        _check_traces(m, f"couverture transverse #{i + 1}", sc.get("traces", []), None)


def _check_traces(m: Model, where: str, traces: list, ptypes: set | None) -> None:
    type_ids = set(m.type_ids) | {t["id"] for t in m.native_types}
    for tr in traces:
        src, role, dst = tr[0], tr[1], tr[2]
        xp = len(tr) > 3 and tr[3] == "xp"
        if src not in type_ids or dst not in type_ids:
            m.errors.append(f"{where}: type inconnu dans la trace {tr}")
            continue
        if not any(r["id"] == role for r in m.link_roles):
            m.errors.append(f"{where}: rôle inconnu dans la trace {tr}")
            continue
        if not m.link_allowed(src, role, dst, cross_project=xp):
            m.errors.append(f"{where}: trace non autorisée par les règles de liens {tr}")
        role_def = next(r for r in m.link_roles if r["id"] == role)
        if xp and not (role_def.get("crossProject") or role_def.get("system")):
            m.errors.append(f"{where}: trace inter-projets sur un rôle non déclaré crossProject {tr}")
        if ptypes is not None:
            if src not in ptypes:
                m.errors.append(f"{where}: type source {src} hors profil (trace {tr})")
            if not xp and dst not in ptypes:
                m.errors.append(f"{where}: type cible {dst} hors profil (trace {tr}) – marquer 'xp' si inter-projets")


def _check_field(m: Model, where: str, f: dict[str, Any], err: list[str]) -> None:
    fid = f.get("id")
    if not fid:
        err.append(f"{where}: champ sans id")
        return
    if fid in NATIVE_FIELDS:
        err.append(f"{where}: le champ '{fid}' redéfinit un champ natif Polarion")
    if not re.match(r"^[a-z][A-Za-z0-9_]*$", fid):
        err.append(f"{where}: identifiant de champ non conforme {fid!r}")
    t = f.get("type", "")
    if t.startswith("enum:"):
        if t[5:] not in m.enumerations:
            err.append(f"{where}.{fid}: énumération inconnue {t[5:]}")
    elif t not in FIELD_TYPES:
        err.append(f"{where}.{fid}: type inconnu {t}")
    if f.get("multi") and not t.startswith("enum:"):
        err.append(f"{where}.{fid}: multi n'est permis que pour les énumérations (Polarion)")
    if not f.get("fr") or not f.get("en"):
        err.append(f"{where}.{fid}: libellé fr/en manquant")


if __name__ == "__main__":  # pragma: no cover
    model = validate(load_model())
    import sys
    if "-v" in sys.argv:
        for i in model.infos:
            print("INFO ", i)
    for w in model.warnings:
        print("WARN ", w)
    for e in model.errors:
        print("ERROR", e)
    print(f"{len(model.errors)} erreur(s), {len(model.warnings)} avertissement(s), "
          f"{len(model.infos)} information(s) (-v pour le détail)")
    sys.exit(1 if model.errors else 0)
