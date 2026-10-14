"""Chargement, expansion et validation du modèle de données ALM (répertoire model/).

Le modèle YAML est la source unique de vérité. Ce module :
  * charge les fichiers YAML ;
  * expanse les fieldSets (mixins) et les groupes de types ;
  * contrôle la cohérence référentielle (validate()).

Aucune dépendance hors bibliothèque standard + PyYAML.
"""
from __future__ import annotations

import pathlib
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
    test_run_statuses: list[dict[str, Any]]
    test_record_results: list[dict[str, Any]]
    roles: dict[str, Any]
    document_types: dict[str, Any]
    tailoring: dict[str, Any]
    topology: dict[str, Any]
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

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

    def all_workflows(self) -> dict[str, Any]:
        out = dict(self.workflows)
        out.update(self.document_workflows)
        return out


def _load(name: str) -> dict[str, Any]:
    with open(MODEL_DIR / name, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


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
        test_run_statuses=wf.get("testRunStatuses", []),
        test_record_results=wf.get("testRecordResults", []),
        roles=roles,
        document_types=docs,
        tailoring=tailoring,
        topology=topology,
    )


# ============================================================================
#  VALIDATION
# ============================================================================
def validate(m: Model) -> Model:
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
            if not o.get("fr") or not o.get("en"):
                err.append(f"enum {eid}.{o.get('id')}: libellé fr/en manquant")

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
        wf = t.get("workflow")
        if wf not in m.workflows:
            err.append(f"type {tid}: workflow inconnu {wf}")
        elif tid not in m.workflows[wf].get("appliesTo", []):
            err.append(f"type {tid}: absent de appliesTo du workflow {wf}")

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
    for key in m.suspect_fields:
        if key != "default" and key not in m.type_groups and key not in type_ids:
            err.append(f"suspectTriggerFields: clé inconnue {key}")

    # -------------------------------------------------- règles de traçabilité
    link_set = set(role_ids)
    for tr in m.traceability_rules:
        applies = tr.get("appliesTo")
        for x in m.expand_types(applies):
            if x not in type_ids and x != "document":
                err.append(f"{tr['id']}: type inconnu {x}")
        chk = tr.get("check", {})
        for k in ("outgoing", "incoming", "outgoing2"):
            if k in chk and chk[k] not in link_set:
                err.append(f"{tr['id']}: rôle de lien inconnu {chk[k]}")
        for k in ("incomingAny", "outgoingAny"):
            for x in chk.get(k, []) or []:
                if x not in link_set:
                    err.append(f"{tr['id']}: rôle de lien inconnu {x}")
        if "excludeFromCoverage" in chk and chk["excludeFromCoverage"] not in link_set:
            err.append(f"{tr['id']}: rôle de lien inconnu {chk['excludeFromCoverage']}")

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
        for tr in wf["transitions"]:
            for st in tr["from"] + [tr["to"]]:
                if st not in states:
                    err.append(f"workflow {wid}.{tr['id']}: état inconnu {st}")
            for role in tr.get("roles", []):
                if role not in roles:
                    err.append(f"workflow {wid}.{tr['id']}: rôle inconnu {role}")
            for c in tr.get("conditions", []) or []:
                for k in c:
                    if k not in m.conditions_catalog:
                        err.append(f"workflow {wid}.{tr['id']}: condition inconnue {k}")
            for fn in tr.get("functions", []) or []:
                for k in fn:
                    if k not in m.functions_catalog:
                        err.append(f"workflow {wid}.{tr['id']}: fonction inconnue {k}")
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
    del doc_field_ids

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
    bus = {o["id"] for o in m.enumerations["businessUnit"]["options"]}
    for pt, d in defaults.items():
        if pt not in project_types:
            err.append(f"tailoring: typologie inconnue {pt}")
        if d["template"] not in templates:
            err.append(f"tailoring {pt}: gabarit inconnu {d['template']}")
        for b in d.get("bu", []):
            if b not in bus:
                err.append(f"tailoring {pt}: BU inconnue {b}")
    return m


def _check_field(m: Model, where: str, f: dict[str, Any], err: list[str]) -> None:
    fid = f.get("id")
    if not fid:
        err.append(f"{where}: champ sans id")
        return
    if fid in NATIVE_FIELDS:
        err.append(f"{where}: le champ '{fid}' redéfinit un champ natif Polarion")
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
    for w in model.warnings:
        print("WARN ", w)
    for e in model.errors:
        print("ERROR", e)
    print(f"{len(model.errors)} erreur(s), {len(model.warnings)} avertissement(s)")
