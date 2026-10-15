"""Génère la configuration Polarion (fichiers XML du dépôt de configuration)
depuis model/.

Formats alignés sur des configurations Polarion publiées (modèles de projet
open source, aide en ligne). Chaque construction dont le format n'a pas été
confirmé sur la version cible est listée dans docs/annexes/D_Formats_Polarion_a_verifier.md
et doit être validée au spike S1 (docs/partie4/23). Sortie :
generated/polarion/<lang>/.polarion/... + SIGNATURES_ET_SCRIPTS.md (manifeste
de ce que la configuration attend : scripts, signatures, points à vérifier).

Usage :
    python3 tools/generate_polarion.py --lang fr
    python3 tools/generate_polarion.py --lang en --out /chemin/vers/projet
"""
from __future__ import annotations

import argparse
import pathlib
import shutil
import sys
from xml.sax.saxutils import quoteattr

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from almmodel import NATIVE_FIELDS, ROOT, Model, load_model, validate  # noqa: E402

TYPE_MAP = {
    "string": "string",
    "text": "text",
    "richtext": "text/html",
    "integer": "integer",
    "float": "float",
    "currency": "currency",
    "date": "date",
    "datetime": "date-time",
    "duration": "duration",
    "boolean": "boolean",
    "user": "enum:@user",
    "testSteps": "struct:TestSteps",
}

# Champs natifs utilisables dans <required> d'une transition de Work Item
NATIVE_REQUIRABLE = {"title", "description", "assignee", "severity", "priority", "dueDate", "resolution"}

# Correspondance fonction neutre → script de workflow
SCRIPTS = {
    "setDueDateFromNow": "fra-sla.js",
    "notifyRoles": "fra-notify.js",
    "recomputeVerificationStatus": "fra-verification-status.js",
    "createBaseline": "fra-baseline.js",
    "incrementRevisionIndex": "fra-revision-index.js",
    "exportToEdms": "fra-export-edms.js",
    "requestSafetyApproval": "fra-request-safety-approval.js",
}

HEADER = (
    "<!-- GÉNÉRÉ par tools/generate_polarion.py depuis model/*.yaml – ne pas éditer à la main.\n"
    "     Modifier le modèle, valider (tools/almmodel.py), régénérer, puis déployer via\n"
    "     la procédure de configuration (Design Authority ALM). -->\n"
)


def label(obj: dict, lang: str) -> str:
    return obj.get(lang) or obj.get("fr") or obj.get("en") or obj.get("id", "")


def desc_for(obj: dict, lang: str) -> str | None:
    """Description dans la langue demandée : 'descEn' pour l'anglais, sinon rien
    (une description française dans une configuration anglaise serait du bruit)."""
    if lang == "fr":
        return obj.get("desc")
    return obj.get("descEn")


def attr(name: str, value) -> str:
    return f" {name}={quoteattr(str(value))}"


def write(path: pathlib.Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class Manifest:
    """Collecte ce que la configuration générée attend de l'instance."""

    def __init__(self) -> None:
        self.scripts: dict[str, set[str]] = {}
        self.signatures: list[tuple[str, str, str, str]] = []  # (workflow/type, action, meaning, note)
        self.to_verify: set[str] = set()

    def script(self, name: str, where: str) -> None:
        self.scripts.setdefault(name, set()).add(where)

    def markdown(self, lang: str) -> str:
        out = [f"# Manifeste de la configuration générée ({lang})\n\n",
               "> Document **généré** par `tools/generate_polarion.py`. Il liste ce que la configuration "
               "attend de l'instance Polarion : scripts de workflow à développer, points de signature "
               "électronique à activer, constructions à confirmer au spike S1 (docs/partie4/23).\n\n",
               "## Scripts de workflow appelés\n\n| Script | Workflows ou documents concernés (nombre) | Liste |\n|---|---|---|\n"]
        for name in sorted(self.scripts):
            where = sorted(self.scripts[name])
            out.append(f"| `{name}` | {len(where)} | {', '.join(where[:12])}{' …' if len(where) > 12 else ''} |\n")
        out.append("\n## Points de signature électronique\n\n| Workflow / type | Action | Signification | Note |\n|---|---|---|---|\n")
        for w, a, mn, note in self.signatures:
            out.append(f"| {w} | `{a}` | {mn} | {note} |\n")
        out.append("\n## Constructions à confirmer sur la version cible\n\n")
        out += [f"- {x}\n" for x in sorted(self.to_verify)]
        return "".join(out)


# ----------------------------------------------------------------- énumérations
def enum_xml(options: list[dict], lang: str, extra=None) -> str:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', HEADER.rstrip(), "<enumeration>"]
    for i, o in enumerate(options, start=1):
        a = attr("id", o["id"]) + attr("name", label(o, lang))
        desc = desc_for(o, lang)
        if desc:
            a += attr("description", " ".join(str(desc).split()))
        if o.get("color"):
            a += attr("color", o["color"])
        if o.get("default"):
            a += attr("default", "true")
        a += attr("sortOrder", i)
        if extra:
            a += extra(o)
        lines.append(f"  <option{a}/>")
    lines.append("</enumeration>")
    return "\n".join(lines) + "\n"


def gen_enumerations(m: Model, lang: str, base: pathlib.Path) -> int:
    n = 0
    for eid, e in m.enumerations.items():
        write(base / "tracker" / "fields" / f"{eid}-enum.xml", enum_xml(e["options"], lang))
        n += 1
    return n


def type_options(m: Model, lang: str, type_ids: list[str] | None = None) -> list[dict]:
    opts = []
    for t in m.types:
        if type_ids is not None and t["id"] not in type_ids:
            continue
        opts.append({"id": t["id"], "fr": t["fr"], "en": t["en"], "color": t.get("color"),
                     "desc": " ".join(str(t.get("desc", "")).split()), "descEn": t.get("descEn")})
    for t in m.native_types:
        opts.append({"id": t["id"], "fr": t["fr"], "en": t["en"], "desc": t.get("note", "")})
    return opts


def gen_type_enum(m: Model, lang: str, base: pathlib.Path) -> None:
    write(base / "tracker" / "fields" / "workitem-type-enum.xml", enum_xml(type_options(m, lang), lang))


# -------------------------------------------------------------- rôles de liens
def gen_link_roles(m: Model, lang: str, base: pathlib.Path, manifest: Manifest) -> None:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', HEADER.rstrip(), "<enumeration>"]
    for i, r in enumerate(m.link_roles, start=1):
        name = r["fr"] if lang == "fr" else r["en"]
        opp = r["frOpposite"] if lang == "fr" else r["enOpposite"]
        a = attr("id", r["id"]) + attr("name", name) + attr("oppositeName", opp)
        if lang == "fr":
            a += attr("description", " ".join(str(r.get("semantics", "")).split()))
        if r.get("parent"):
            a += attr("parent", "true")
        if r["id"] == "relates_to":
            a += attr("default", "true")
        a += attr("sortOrder", i)
        rules = _expand_rules(m, r)
        if not rules:
            lines.append(f"  <option{a}/>")
            continue
        lines.append(f"  <option{a}>")
        for frm, to in rules:
            lines.append(f"    <rule{attr('from', frm)}{attr('to', frm if to == '__same__' else to)}/>")
        lines.append("  </option>")
    lines.append("</enumeration>")
    manifest.to_verify.add("Règles de liens `<rule from to>` imbriquées dans les options de "
                           "`workitem-link-role-enum.xml`, et jeton `__other` pour l'inter-projets")
    write(base / "tracker" / "fields" / "workitem-link-role-enum.xml", "\n".join(lines) + "\n")


def _expand_rules(m: Model, role: dict) -> list[tuple[str, str]]:
    """Retourne des couples (from, 'to1, to2') ; vide = rôle non restreint."""
    out: list[tuple[str, str]] = []
    for rule in role.get("rules", []):
        frm = m.expand_types(rule.get("from"))
        to = m.expand_types(rule.get("to"))
        if "any" in frm or "any" in to:
            return []
        if to == ["same"]:
            for f in frm:
                out.append((f, "__same__"))
            continue
        targets = list(dict.fromkeys(to))
        if role.get("crossProject"):
            targets.append("__other")
        out.append((", ".join(dict.fromkeys(frm)), ", ".join(targets)))
    return out


# ---------------------------------------------------------- champs personnalisés
def field_xml(f: dict, lang: str) -> str:
    t = f["type"]
    ptype = t if t.startswith("enum:") else TYPE_MAP[t]
    a = attr("id", f["id"]) + attr("name", label(f, lang)) + attr("type", ptype)
    desc = desc_for(f, lang)
    if f.get("computed"):
        tag = "[Calculé – alimenté par script, ne pas saisir]" if lang == "fr" else "[Computed by script – do not edit]"
        desc = (desc + " " if desc else "") + tag
    if desc:
        a += attr("description", " ".join(desc.split()))
    if f.get("required"):
        a += attr("required", "true")
    if f.get("multi"):
        a += attr("multi", "true")
    return f"  <field{a}/>"


def fields_file(fields: list[dict], lang: str) -> str:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', HEADER.rstrip(), "<fields>"]
    lines += [field_xml(f, lang) for f in fields]
    lines.append("</fields>")
    return "\n".join(lines) + "\n"


def gen_custom_fields(m: Model, lang: str, base: pathlib.Path) -> int:
    n = 0
    for t in m.types:
        fields = m.fields_of(t)
        write(base / "tracker" / "fields" / f"{t['id']}-custom-fields.xml", fields_file(fields, lang))
        n += len(fields)
    return n


# ------------------------------------------------------------------- workflows
def _param(name: str, value) -> str:
    if isinstance(value, (list, tuple)):
        value = ",".join(str(v) for v in value)
    return f"<param{attr('name', name)}{attr('value', value)}/>"


def _flat(d) -> str:
    if isinstance(d, dict):
        return "; ".join(f"{k}={_flat(v)}" for k, v in d.items() if k != "note")
    if isinstance(d, list):
        return "[" + ",".join(_flat(x) for x in d) + "]"
    if isinstance(d, bool):
        return "true" if d else "false"
    return str(d)


def _script_condition(script: str, **params) -> str:
    ps = [_param("engine", "js"), _param("script", script)]
    ps += [_param(k, v) for k, v in params.items() if v not in (None, "", [])]
    return f'<condition name="ScriptCondition">{"".join(ps)}</condition>'


class Ctx:
    """Contexte de rendu d'un workflow : type de Work Item ou type de document."""

    def __init__(self, m: Model, manifest: Manifest, type_id: str | None = None, doc: dict | None = None):
        self.m, self.manifest, self.type_id, self.doc = m, manifest, type_id, doc
        self.where = type_id or (doc["id"] if doc else "?")

    @property
    def is_doc(self) -> bool:
        return self.doc is not None

    def script(self, name: str) -> None:
        self.manifest.script(name, self.where)


def _condition_xml(key: str, val, ctx: Ctx) -> list[str]:
    m = ctx.m
    if isinstance(val, dict) and val.get("forTypes") and ctx.type_id not in val["forTypes"]:
        return []
    if key == "approverNotAuthor":
        ctx.script("fra-independence.js")
        return [_script_condition("fra-independence.js")]
    if key == "noSuspectLinks":
        if ctx.is_doc:
            return ['<condition name="ContainsNoMatchingWorkItems">' + _param("query", "suspect:true") + "</condition>"]
        roles = val if isinstance(val, list) else (val.get("scope") if isinstance(val, dict) else "")
        if isinstance(roles, list) and ctx.type_id:
            # ne garder que les rôles suspects dont ce type est une source
            roles = [r for r in roles if any(ctx.type_id in m.expand_types(rule.get("from")) or
                                             "any" in m.expand_types(rule.get("from"))
                                             for rl in m.link_roles if rl["id"] == r and rl.get("suspect")
                                             for rule in rl.get("rules", []))]
            if not roles:
                return []
        ctx.script("fra-no-suspect.js")
        return [_script_condition("fra-no-suspect.js", roles=roles)]
    if key == "noForbiddenClassification":
        if ctx.is_doc:
            q = "informationClassification.KEY:(sensitiveSecurity restricted)"
            return ['<condition name="ContainsNoMatchingWorkItems">' + _param("query", q) + "</condition>"]
        ctx.script("fra-classification.js")
        return [_script_condition("fra-classification.js")]
    if key == "cascadedItemsApproved":
        out = []
        for types, target in _cascade_groups(m, ctx.doc, "approve"):
            q = f"type:({' '.join(types)}) AND NOT status:({target})"
            out.append('<condition name="ContainsNoMatchingWorkItems">' + _param("query", q) + "</condition>")
        for t, statuses in (ctx.doc.get("approvalGate") or {}).items():
            q = f"type:{t} AND NOT status:({' '.join(statuses)})"
            out.append('<condition name="ContainsNoMatchingWorkItems">' + _param("query", q) + "</condition>")
        return out
    if key == "allApprovalsDone":
        return ['<condition name="ApprovalState">' + _param("commonApprovalState", "approved") + "</condition>"]
    if key == "linkedItemsStatus":
        native_keys = {"role", "direction", "statuses", "note"}
        if set(val) <= native_keys:
            p = [_param("back.link.roles" if val.get("direction") == "incoming" else "link.roles", val["role"]),
                 _param("valid.states", val.get("statuses", []))]
            return ['<condition name="LinkedWorkItemsStatus">' + "".join(p) + "</condition>"]
        ctx.script("fra-link-status.js")
        return [_script_condition("fra-link-status.js", rule=_flat(val))]
    if key == "hasLink":
        simple = (val.get("min", 1) == 1 and "exactly" not in val and not val.get("linkedStatus")
                  and not any(k.startswith("only") or k.startswith("unless") for k in val)
                  and isinstance(val.get("role"), str) and not val.get("toType"))
        if simple:
            p = [_param("link.role", val["role"]),
                 _param("backlink", "true" if val.get("direction") == "incoming" else "false")]
            if val.get("fromType"):
                p.append(_param("target.work.item.type", val["fromType"]))
            return ['<condition name="LinkedWorkItem">' + "".join(p) + "</condition>"]
        ctx.script("fra-link-cardinality.js")
        return [_script_condition("fra-link-cardinality.js", rule=_flat(val))]
    if key == "fieldValue":
        if set(val) - {"note", "forTypes"} == {"field", "nonEmpty"} and val.get("nonEmpty") is True:
            return ['<condition name="FieldNonEmpty">' + _param("field.name", val["field"]) + "</condition>"]
        ctx.script("fra-field-rule.js")
        return [_script_condition("fra-field-rule.js", rule=_flat({k: v for k, v in val.items() if k != "forTypes"}))]
    if key == "safetyApprovalIf":
        ctx.script("fra-safety-approval.js")
        return [_script_condition("fra-safety-approval.js", rule=val)]
    if key == "qualifiedSignatory":
        ctx.script("fra-habilitation.js")
        return [_script_condition("fra-habilitation.js", rule=_flat(val), projectParameter="signaturePolicy")]
    raise ValueError(f"condition non mappée : {key}")


def _cascade_groups(m: Model, doc: dict, action_id: str) -> list[tuple[list[str], str]]:
    """Groupes (types, état cible) des types cascadés par un document pour une action donnée."""
    groups: dict[str, list[str]] = {}
    for t in doc.get("cascadeTypes", []) or []:
        wf = m.workflows[m.type_by_id(t)["workflow"]]
        tr = next((x for x in wf["transitions"] if x["id"] == action_id), None)
        if tr is None:
            raise ValueError(f"document {doc['id']}: le type cascadé {t} n'a pas d'action {action_id}")
        groups.setdefault(tr["to"], []).append(t)
    return [(types, target) for target, types in groups.items()]


def _function_xml(key: str, val, ctx: Ctx) -> list[str]:
    if key == "setFieldValue":
        if "valueIfEmpty" in val:
            ctx.script("fra-set-if-empty.js")
            return [('<function name="ScriptFunction">' + _param("engine", "js") + _param("script", "fra-set-if-empty.js")
                     + _param("args", _flat({"field": val["field"], "value": val["valueIfEmpty"]})) + "</function>")]
        return [('<function name="ChangeField">' + _param("field.name", val["field"])
                 + _param("field.value", val["value"]) + "</function>")]
    if key == "createLinkedItem":
        return [('<function name="CreateLinkedWorkItem">' + _param("type", val["type"])
                 + _param("link.role", val["role"]) + "</function>")]
    if key == "invokeOnDocItems":
        out = []
        for types, target in _cascade_groups(ctx.m, ctx.doc, val["actionId"]):
            froms: set[str] = set()
            for t in types:
                wf = ctx.m.workflows[ctx.m.type_by_id(t)["workflow"]]
                tr = next(x for x in wf["transitions"] if x["id"] == val["actionId"])
                froms |= set(tr["from"])
            q = f"type:({' '.join(types)}) AND status:({' '.join(sorted(froms))})"
            out.append('<function name="InvokeAction">' + _param("statusId", target)
                       + _param("actionId", val["actionId"]) + _param("query", q) + "</function>")
        return out
    if key in SCRIPTS:
        script = SCRIPTS[key]
        ctx.script(script)
        args = "" if val is True else _param("args", _flat(val))
        return [('<function name="ScriptFunction">' + _param("engine", "js") + _param("script", script)
                 + args + "</function>")]
    raise ValueError(f"fonction non mappée : {key}")


def required_fields_for(m: Model, wf: dict, tr: dict, type_id: str | None) -> list[str]:
    """Champs requis d'une transition : liste de la transition + champs 'requiredAt'
    du type dont l'état cible est celui de la transition (principe P7)."""
    req = list(tr.get("requiredFields", []) or [])
    if type_id is None:
        return req
    available = m.field_ids_of(type_id)
    for f in m.fields_of(m.type_by_id(type_id)):
        at = f.get("requiredAt")
        if not at:
            continue
        if at == "soumission":
            at = wf.get("submitState")
        if at == tr["to"] and f["id"] not in req:
            req.append(f["id"])
    for f in req:
        if f not in available and f not in NATIVE_REQUIRABLE:
            raise ValueError(f"{wf.get('fr', '?')}.{tr['id']}: champ requis '{f}' indisponible sur {type_id}")
    return req


def role_condition(roles: list[str], ctx: Ctx) -> list[str]:
    pseudo = {r["id"] for r in ctx.m.roles.get("projectRoles", []) if r.get("pseudo")}
    real = [r for r in roles if r not in pseudo or r.startswith("workitem.")]
    out = []
    if "documentOwner" in roles:
        ctx.script("fra-document-owner.js")
        out.append(_script_condition("fra-document-owner.js"))
        ctx.manifest.to_verify.add("Rôle « propriétaire du document » : réalisé par ScriptCondition "
                                   "`fra-document-owner.js` (aucun rôle spécial Polarion connu pour l'auteur d'un document)")
    if real and "anyProjectMember" not in roles:
        out.append('<condition name="RoleCondition">' + _param("roles", real) + "</condition>")
        if any(r.startswith("workitem.") for r in real):
            ctx.manifest.to_verify.add("Rôles spéciaux `workitem.assignee` / `workitem.author` dans RoleCondition")
    return out


def workflow_xml(wf: dict, lang: str, ctx: Ctx) -> str:
    proto = "Module" if ctx.is_doc else "WorkItem"
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', HEADER.rstrip(),
             f'<workflow initial-status="{wf["initial"]}" prototype="{proto}">', "  <transitions>"]
    for tr in wf["transitions"]:
        for frm in tr["from"]:
            lines.append(f'    <transition{attr("action", tr["id"])}{attr("from", frm)}{attr("to", tr["to"])}/>')
    lines += ["  </transitions>", "  <actions>"]
    for tr in wf["transitions"]:
        lines.append(f'    <action{attr("id", tr["id"])}{attr("name", label(tr, lang))}>')
        req = required_fields_for(ctx.m, wf, tr, ctx.type_id)
        if req:
            lines.append("      <required>" + "".join(f"<field{attr('name', f)}/>" for f in req) + "</required>")
        conds = role_condition(tr.get("roles", []) or [], ctx)
        for c in tr.get("conditions", []) or []:
            for k, v in c.items():
                conds.extend(_condition_xml(k, v, ctx))
        if conds:
            lines.append("      <conditions>")
            lines += [f"        {c}" for c in conds]
            lines.append("      </conditions>")
        fns = [x for fn in tr.get("functions", []) or [] for k, v in fn.items() for x in _function_xml(k, v, ctx)]
        if fns:
            lines.append("      <functions>")
            lines += [f"        {f}" for f in fns]
            lines.append("      </functions>")
        sig = tr.get("signature")
        if sig and sig.get("required"):
            meaning = sig.get("meaning")
            note = "signature systématique"
            if sig.get("onlyIf"):
                note = f"intention conditionnelle ({sig['onlyIf']}) rendue systématique (la signature Polarion n'est pas conditionnelle)"
            lines.append(f"      <!-- signature électronique : {meaning} ; {note} -->")
            lines.append('      <signatures><signature-policy name="all"/></signatures>')
            ctx.manifest.signatures.append((ctx.where, tr["id"], meaning, note))
            ctx.manifest.to_verify.add("Bloc `<signatures><signature-policy name=\"all\"/></signatures>` sur une action "
                                       "(documents et Work Items) : format et effet à confirmer")
        lines.append("    </action>")
    lines += ["  </actions>", "</workflow>"]
    return "\n".join(lines) + "\n"


def state_options(m: Model, wf: dict, lang: str) -> list[dict]:
    cats = m.state_categories
    opts = []
    for s in wf["states"]:
        cat = cats.get(s.get("category"), {})
        o = dict(s, color=cat.get("color"))
        o["desc"] = f"Catégorie : {cat.get('fr', s.get('category'))}"
        o["descEn"] = f"Category: {cat.get('en', s.get('category'))}"
        if s["id"] == wf["initial"]:
            o["default"] = True
        opts.append(o)
    return opts


def gen_workflows(m: Model, lang: str, base: pathlib.Path, manifest: Manifest) -> None:
    for t in m.types:
        wf = m.workflows[t["workflow"]]
        write(base / "tracker" / "workflow" / f"{t['id']}-workflow.xml",
              workflow_xml(wf, lang, Ctx(m, manifest, type_id=t["id"])))
        write(base / "tracker" / "fields" / f"{t['id']}-status-enum.xml", enum_xml(state_options(m, wf, lang), lang))


# ------------------------------------------------------------------ documents
def doc_type_options(m: Model, lang: str, doc_ids: list[str] | None = None) -> list[dict]:
    return [{"id": d["id"], "fr": d["fr"], "en": d["en"],
             "desc": f"Workflow : {d['workflow']} ; types autorisés : {', '.join(d['allowedTypes'])}",
             "descEn": f"Workflow: {d['workflow']}; allowed types: {', '.join(d['allowedTypes'])}"}
            for d in m.document_types["documentTypes"] if doc_ids is None or d["id"] in doc_ids]


def gen_documents(m: Model, lang: str, base: pathlib.Path, manifest: Manifest) -> None:
    dt = m.document_types
    write(base / "documents" / "fields" / "document-type-enum.xml", enum_xml(doc_type_options(m, lang), lang))
    write(base / "documents" / "fields" / "custom-fields.xml", fields_file(dt["documentCustomFields"], lang))
    states: dict[str, dict] = {}
    for wf in m.document_workflows.values():
        for o in state_options(m, wf, lang):
            states.setdefault(o["id"], o)
    write(base / "documents" / "fields" / "document-status-enum.xml", enum_xml(list(states.values()), lang))
    for d in dt["documentTypes"]:
        wf = m.document_workflows[d["workflow"]]
        write(base / "documents" / "workflow" / f"{d['id']}-workflow.xml",
              workflow_xml(wf, lang, Ctx(m, manifest, doc=d)))
    manifest.to_verify.add("Fichiers `documents/fields/document-type-enum.xml`, `document-status-enum.xml` et "
                           "`documents/workflow/<type>-workflow.xml` (prototype Module) : emplacement et noms")
    manifest.to_verify.add("`InvokeAction(statusId, actionId, query)` : comportement lorsque l'action n'est pas "
                           "disponible pour un élément de la requête")


# -------------------------------------------------------------------- testing
def gen_testing(m: Model, lang: str, base: pathlib.Path, manifest: Manifest) -> None:
    write(base / "testing" / "configuration" / "testrun-status-enum.xml", enum_xml(m.test_run_statuses, lang))
    write(base / "testing" / "configuration" / "testrecord-result-enum.xml", enum_xml(m.test_record_results, lang))
    manifest.to_verify.add("Configuration Testing : nom du fichier des résultats de Test Record "
                           "(`testrecord-result-enum.xml` supposé), type de cas de test (`verificationCase`, "
                           "`polarionTestCase: true`) et rôle de couverture `verifies` à déclarer dans l'administration Testing")
    manifest.to_verify.add("Types de champs `text`, `date-time`, `struct:TestSteps`, `enum:@user` ; attributs "
                           "`sortOrder` / `description` des options d'énumération")
    manifest.to_verify.add("Paramètres additionnels de ScriptCondition / ScriptFunction (`rule`, `roles`, `args`, "
                           "`projectParameter`) et moteur `js`")


# ------------------------------------------------------------------------ main
def generate(m: Model, lang: str, out: pathlib.Path) -> tuple[int, int, int, Manifest]:
    base = out / ".polarion"
    if base.exists():
        shutil.rmtree(base)
    manifest = Manifest()
    gen_type_enum(m, lang, base)
    gen_link_roles(m, lang, base, manifest)
    n_enum = gen_enumerations(m, lang, base)
    n_fields = gen_custom_fields(m, lang, base)
    gen_workflows(m, lang, base, manifest)
    gen_documents(m, lang, base, manifest)
    gen_testing(m, lang, base, manifest)
    write(out / "SIGNATURES_ET_SCRIPTS.md", manifest.markdown(lang))
    n_files = sum(1 for _ in base.rglob("*.xml"))
    return n_enum, n_fields, n_files, manifest


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--lang", choices=["fr", "en"], default="fr")
    ap.add_argument("--out", type=pathlib.Path, default=None,
                    help="Répertoire racine de sortie (défaut : generated/polarion/<lang>)")
    args = ap.parse_args(argv)
    model = validate(load_model())
    if model.errors:
        for e in model.errors:
            print("ERROR", e, file=sys.stderr)
        return 1
    out = args.out or ROOT / "generated" / "polarion" / args.lang
    n_enum, n_fields, n_files, manifest = generate(model, args.lang, out)
    print(f"[{args.lang}] {len(model.types)} types, {len(model.link_roles)} rôles de liens, "
          f"{n_enum} énumérations, {n_fields} champs, {n_files} fichiers XML, "
          f"{len(manifest.scripts)} scripts attendus → {out / '.polarion'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
