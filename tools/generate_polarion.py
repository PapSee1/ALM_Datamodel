"""Génère la configuration Polarion (fichiers XML du dépôt SVN) depuis model/.

Formats alignés sur des configurations Polarion réelles publiées (modèles de
projet open source, aide Polarion) – cf. docs/partie3/15 §"Configuration as
code". Sortie : generated/polarion/<lang>/.polarion/...

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
from almmodel import ROOT, Model, load_model, validate  # noqa: E402

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

STATE_COLORS = {
    "open": "#9E9E9E",
    "inProgress": "#1E88E5",
    "done": "#43A047",
    "cancelled": "#757575",
}

HEADER = (
    "<!-- GÉNÉRÉ par tools/generate_polarion.py depuis model/*.yaml – ne pas éditer à la main.\n"
    "     Modifier le modèle, valider (tools/almmodel.py), régénérer, puis déployer via\n"
    "     la procédure de configuration (Design Authority ALM). -->\n"
)


def label(obj: dict, lang: str) -> str:
    return obj.get(lang) or obj.get("fr") or obj.get("en") or obj.get("id", "")


def attr(name: str, value) -> str:
    return f" {name}={quoteattr(str(value))}"


def write(path: pathlib.Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# ----------------------------------------------------------------- énumérations
def enum_xml(options: list[dict], lang: str, extra=None) -> str:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', HEADER.rstrip(), "<enumeration>"]
    for i, o in enumerate(options, start=1):
        a = attr("id", o["id"]) + attr("name", label(o, lang))
        desc = o.get("desc")
        if desc:
            a += attr("description", desc)
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


def gen_type_enum(m: Model, lang: str, base: pathlib.Path) -> None:
    opts = []
    for t in m.types:
        opts.append({"id": t["id"], "fr": t["fr"], "en": t["en"], "color": t.get("color"),
                     "desc": " ".join(str(t.get("desc", "")).split())})
    for t in m.native_types:
        opts.append({"id": t["id"], "fr": t["fr"], "en": t["en"], "desc": t.get("note", "")})
    write(base / "tracker" / "fields" / "workitem-type-enum.xml", enum_xml(opts, lang))


# -------------------------------------------------------------- rôles de liens
def gen_link_roles(m: Model, lang: str, base: pathlib.Path) -> None:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', HEADER.rstrip(), "<enumeration>"]
    for i, r in enumerate(m.link_roles, start=1):
        name = r["fr"] if lang == "fr" else r["en"]
        opp = r["frOpposite"] if lang == "fr" else r["enOpposite"]
        rid = "relates_to" if r["id"] == "relatesTo" else r["id"]
        a = attr("id", rid) + attr("name", name) + attr("oppositeName", opp)
        a += attr("description", " ".join(str(r.get("semantics", "")).split()))
        if r.get("parent"):
            a += attr("parent", "true")
        if rid == "relates_to":
            a += attr("default", "true")
        a += attr("sortOrder", i)
        rules = _expand_rules(m, r)
        if not rules:
            lines.append(f"  <option{a}/>")
            continue
        lines.append(f"  <option{a}>")
        for frm, to in rules:
            if to == "__same__":
                lines.append(f"    <rule{attr('from', frm)}{attr('to', frm)}/>")
            else:
                lines.append(f"    <rule{attr('from', frm)}{attr('to', to)}/>")
        lines.append("  </option>")
    lines.append("</enumeration>")
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
    desc = f.get("desc")
    if f.get("computed"):
        desc = (desc + " " if desc else "") + "[Calculé – alimenté par script, ne pas saisir]"
    if desc:
        a += attr("description", " ".join(desc.split()))
    if f.get("required"):
        a += attr("required", "true")
    if f.get("multi"):
        a += attr("multi", "true")
    return f"  <field{a}/>"


def gen_custom_fields(m: Model, lang: str, base: pathlib.Path) -> int:
    n = 0
    for t in m.types:
        fields = m.fields_of(t)
        lines = ['<?xml version="1.0" encoding="UTF-8"?>', HEADER.rstrip(), "<fields>"]
        lines += [field_xml(f, lang) for f in fields]
        lines.append("</fields>")
        write(base / "tracker" / "fields" / f"{t['id']}-custom-fields.xml", "\n".join(lines) + "\n")
        n += len(fields)
    return n


# ------------------------------------------------------------------- workflows
def _param(name: str, value) -> str:
    if isinstance(value, (list, tuple)):
        value = ",".join(str(v) for v in value)
    return f"<param{attr('name', name)}{attr('value', value)}/>"


def _script_condition(script: str, **params) -> str:
    ps = [_param("engine", "js"), _param("script", script)]
    ps += [_param(k, v) for k, v in params.items() if v not in (None, "", [])]
    return f'<condition name="ScriptCondition">{"".join(ps)}</condition>'


_MODEL: Model | None = None  # positionné par main() (listes d'états calculées depuis le modèle)


def _condition_xml(key: str, val, is_doc: bool) -> list[str]:
    if key == "approverNotAuthor":
        return [_script_condition("fra-independence.js")]
    if key == "noSuspectLinks":
        if is_doc:
            return ['<condition name="ContainsNoMatchingWorkItems">' + _param("query", "suspect:true") + "</condition>"]
        roles = val if isinstance(val, list) else (val.get("scope") if isinstance(val, dict) else "")
        return [_script_condition("fra-no-suspect.js", roles=roles)]
    if key == "noForbiddenClassification":
        if is_doc:
            q = "informationClassification.KEY:(sensitiveSecurity restricted)"
            return ['<condition name="ContainsNoMatchingWorkItems">' + _param("query", q) + "</condition>"]
        return [_script_condition("fra-classification.js")]
    if key == "noDocItemsInStatus":
        wanted = list(val.get("statuses", []))
        cats = set(val.get("categories", []))
        if cats:
            wanted += sorted({s["id"] for wf in _MODEL.workflows.values() for s in wf["states"]
                              if s.get("category") in cats})
        wanted += [x for x in val.get("plus", []) if x not in wanted]
        excl = " ".join(val.get("excludeTypes", []))
        q = f"status:({' '.join(wanted)})" + (f" AND NOT type:({excl})" if excl else "")
        return ['<condition name="ContainsNoMatchingWorkItems">' + _param("query", q) + "</condition>"]
    if key == "allDocItemsInStatus":
        wanted = val.get("statuses")
        if wanted is None:
            cats = set(val.get("categories", []))
            wanted = sorted({s["id"] for wf in _MODEL.workflows.values() for s in wf["states"]
                             if s.get("category") in cats})
        statuses = " ".join(wanted)
        excl = " ".join(val.get("excludeTypes", []))
        # clause positive obligatoire : une requête Lucene purement négative ne renvoie rien
        q = f"HAS_VALUE:type AND NOT status:({statuses})" + (f" AND NOT type:({excl})" if excl else "")
        return ['<condition name="ContainsNoMatchingWorkItems">' + _param("query", q) + "</condition>"]
    if key == "allApprovalsDone":
        return ['<condition name="ApprovalState">' + _param("commonApprovalState", "approved") + "</condition>"]
    if key == "linkedItemsStatus":
        p = [_param("back.link.roles" if val.get("direction") == "incoming" else "link.roles", val["role"]),
             _param("valid.states", val.get("statuses", []))]
        return ['<condition name="LinkedWorkItemsStatus">' + "".join(p) + "</condition>"]
    if key == "hasLink":
        simple = (val.get("min", 1) == 1 and "exactly" not in val and not val.get("linkedStatus")
                  and not any(k.startswith("only") or k.startswith("unless") for k in val)
                  and isinstance(val.get("role"), str))
        if simple:
            p = [_param("link.role", val["role"]),
                 _param("backlink", "true" if val.get("direction") == "incoming" else "false")]
            if val.get("fromType"):
                p.append(_param("target.work.item.type", val["fromType"]))
            return ['<condition name="LinkedWorkItem">' + "".join(p) + "</condition>"]
        return [_script_condition("fra-link-cardinality.js", rule=_flat(val))]
    if key == "fieldValue":
        return [_script_condition("fra-field-rule.js", rule=_flat(val))]
    if key == "safetyApprovalIf":
        return [_script_condition("fra-safety-approval.js", rule=val)]
    if key == "qualifiedSignatory":
        # inopérante si le paramètre projet signaturePolicy = roleBased (décision de provisioning)
        return [_script_condition("fra-habilitation.js", rule=_flat(val), projectParameter="signaturePolicy")]
    return [f"<!-- condition non mappée : {key} -->"]


def _flat(d) -> str:
    if isinstance(d, dict):
        return "; ".join(f"{k}={_flat(v)}" for k, v in d.items())
    if isinstance(d, list):
        return "[" + ",".join(_flat(x) for x in d) + "]"
    if isinstance(d, bool):
        return "true" if d else "false"
    return str(d)


def _function_xml(key: str, val) -> str:
    if key == "setFieldValue":
        value = val.get("value", val.get("valueIfEmpty"))
        return ('<function name="ChangeField">' + _param("field.name", val["field"])
                + _param("field.value", value) + "</function>")
    if key == "clearField":
        return '<function name="ClearField">' + _param("field.name", val) + "</function>"
    if key == "createLinkedItem":
        return ('<function name="CreateLinkedWorkItem">' + _param("type", val["type"])
                + _param("link.role", "relates_to" if val["role"] == "relatesTo" else val["role"])
                + "</function>")
    if key == "invokeOnDocItems":
        return ('<function name="InvokeAction">' + _param("statusId", val["statusId"])
                + _param("actionId", val["actionId"]) + _param("query", val["query"]) + "</function>")
    if key == "addApprovals":
        return '<function name="AddDefaultApprovals">' + _param("approvals.roles", val) + "</function>"
    script = {
        "setDueDateFromNow": "fra-sla.js",
        "notifyRoles": "fra-notify.js",
        "recomputeVerificationStatus": "fra-verification-status.js",
        "createBaseline": "fra-baseline.js",
        "incrementRevisionIndex": "fra-revision-index.js",
        "exportToEdms": "fra-export-edms.js",
        "lockFields": "fra-lock-fields.js",
        "requestSafetyApproval": "fra-request-safety-approval.js",
    }.get(key, f"fra-{key}.js")
    args = "" if val is True else _param("args", _flat(val))
    return ('<function name="ScriptFunction">' + _param("engine", "js") + _param("script", script)
            + args + "</function>")


def workflow_xml(wf: dict, lang: str, available_fields: set[str] | None, is_doc: bool) -> str:
    proto = "Module" if is_doc else "WorkItem"
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', HEADER.rstrip(),
             f'<workflow initial-status="{wf["initial"]}" prototype="{proto}">', "  <transitions>"]
    for tr in wf["transitions"]:
        for frm in tr["from"]:
            lines.append(f'    <transition{attr("action", tr["id"])}{attr("from", frm)}{attr("to", tr["to"])}/>')
    lines += ["  </transitions>", "  <actions>"]
    for tr in wf["transitions"]:
        name = tr.get(lang) or tr.get("fr")
        lines.append(f'    <action{attr("id", tr["id"])}{attr("name", name)}>')
        req = [f for f in tr.get("requiredFields", []) or []
               if available_fields is None or f in available_fields]
        if req:
            lines.append("      <required>" + "".join(f"<field{attr('name', f)}/>" for f in req) + "</required>")
        conds = []
        if tr.get("roles"):
            conds.append('<condition name="RoleCondition">' + _param("roles", tr["roles"]) + "</condition>")
        for c in tr.get("conditions", []) or []:
            for k, v in c.items():
                conds.extend(_condition_xml(k, v, is_doc))
        if conds:
            lines.append("      <conditions>")
            lines += [f"        {c}" for c in conds]
            lines.append("      </conditions>")
        fns = [_function_xml(k, v) for fn in tr.get("functions", []) or [] for k, v in fn.items()]
        if fns:
            lines.append("      <functions>")
            lines += [f"        {f}" for f in fns]
            lines.append("      </functions>")
        sig = tr.get("signature")
        if sig and sig.get("required"):
            meaning = sig.get("meaning")
            note = f"<!-- signature : {meaning}"
            if sig.get("onlyIf"):
                note += f" ; intention conditionnelle ({sig['onlyIf']}) appliquée de façon conservatrice : signature systématique"
            note += " -->"
            lines.append(f"      {note}")
            if is_doc:
                lines.append('      <signatures><signature-policy name="all"/></signatures>')
            else:
                lines.append("      <signatures/>")
        lines.append("    </action>")
    lines += ["  </actions>", "</workflow>"]
    return "\n".join(lines) + "\n"


def gen_workflows(m: Model, lang: str, base: pathlib.Path) -> None:
    for t in m.types:
        wf = m.workflows[t["id"] if t["id"] in m.workflows else t["workflow"]]
        fields = m.field_ids_of(t["id"]) | {
            "title", "description", "assignee", "severity", "priority", "dueDate", "resolution"}
        write(base / "tracker" / "workflow" / f"{t['id']}-workflow.xml",
              workflow_xml(wf, lang, fields, is_doc=False))
        opts = [dict(s, color=STATE_COLORS.get(s.get("category")),
                     desc=f"Catégorie : {s.get('category')}") for s in wf["states"]]
        for o in opts:
            if o["id"] == wf["initial"]:
                o["default"] = True
        write(base / "tracker" / "fields" / f"{t['id']}-status-enum.xml", enum_xml(opts, lang))


# ------------------------------------------------------------------ documents
def gen_documents(m: Model, lang: str, base: pathlib.Path) -> None:
    dt = m.document_types
    opts = [{"id": d["id"], "fr": d["fr"], "en": d["en"],
             "desc": f"Workflow : {d['workflow']} ; types autorisés : {', '.join(d['allowedTypes'])}"}
            for d in dt["documentTypes"]]
    write(base / "documents" / "fields" / "document-type-enum.xml", enum_xml(opts, lang))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', HEADER.rstrip(), "<fields>"]
    lines += [field_xml(f, lang) for f in dt["documentCustomFields"]]
    lines.append("</fields>")
    write(base / "documents" / "fields" / "custom-fields.xml", "\n".join(lines) + "\n")
    states: dict[str, dict] = {}
    for wf in m.document_workflows.values():
        for s in wf["states"]:
            states.setdefault(s["id"], dict(s, color=STATE_COLORS.get(s.get("category"))))
    write(base / "documents" / "fields" / "document-status-enum.xml", enum_xml(list(states.values()), lang))
    for d in dt["documentTypes"]:
        wf = m.document_workflows[d["workflow"]]
        write(base / "documents" / "workflow" / f"{d['id']}-workflow.xml",
              workflow_xml(wf, lang, None, is_doc=True))


def gen_testing(m: Model, lang: str, base: pathlib.Path) -> None:
    write(base / "testing" / "configuration" / "testrun-status-enum.xml",
          enum_xml(m.test_run_statuses, lang))


# ------------------------------------------------------------------------ main
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
    global _MODEL
    _MODEL = model
    out = args.out or ROOT / "generated" / "polarion" / args.lang
    base = out / ".polarion"
    if base.exists():
        shutil.rmtree(base)
    gen_type_enum(model, args.lang, base)
    gen_link_roles(model, args.lang, base)
    n_enum = gen_enumerations(model, args.lang, base)
    n_fields = gen_custom_fields(model, args.lang, base)
    gen_workflows(model, args.lang, base)
    gen_documents(model, args.lang, base)
    gen_testing(model, args.lang, base)
    n_files = sum(1 for _ in base.rglob("*.xml"))
    print(f"[{args.lang}] {len(model.types)} types, {len(model.link_roles)} rôles de liens, "
          f"{n_enum} énumérations, {n_fields} champs, {n_files} fichiers XML → {base}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
