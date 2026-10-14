"""Génère les annexes documentaires (Markdown) depuis model/.

Sortie : docs/generated/*.md — catalogues exhaustifs toujours synchronisés
avec la configuration générée (une seule source de vérité).

Usage : python3 tools/generate_docs.py
"""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from almmodel import ROOT, Model, load_model, validate  # noqa: E402

OUT = ROOT / "docs" / "generated"
BANNER = ("> Document **généré** par `tools/generate_docs.py` depuis `model/*.yaml` — "
          "ne pas éditer à la main.\n\n")

FAMILY_FR = {
    "requirements": "Exigences", "architecture": "Architecture (RFLP)",
    "safety": "Sûreté, risques et analyses", "vv": "Vérification & validation",
    "change": "Modifications, écarts, fortuits", "project": "Projet, livrables, revues",
    "library": "Bibliothèque",
}


def esc(s) -> str:
    return " ".join(str(s or "").split()).replace("|", "\\|")


def ftype(f: dict) -> str:
    t = f["type"]
    if t.startswith("enum:"):
        t = f"enum [`{t[5:]}`](A2_enumerations.md#{t[5:].lower()})"
    if f.get("multi"):
        t += " (multi)"
    return t


def anchor(s: str) -> str:
    return s.lower()


# --------------------------------------------------------------------- A1
def gen_types(m: Model) -> str:
    out = ["# Annexe A1 — Catalogue des types de Work Items et de leurs attributs\n\n", BANNER]
    out.append("## Synthèse\n\n| Famille | Type (id) | Libellé | Workflow | Nb attributs |\n|---|---|---|---|---|\n")
    for t in m.types:
        out.append(f"| {FAMILY_FR[t['family']]} | `{t['id']}` | {t['fr']} | `{t['workflow']}` | {len(m.fields_of(t))} |\n")
    out.append(f"\n**Total : {len(m.types)} types personnalisés** (+ type natif `heading`).\n\n")
    out.append("## Jeux d'attributs réutilisables (fieldSets)\n\n")
    for fs_id, fs in m.field_sets.items():
        out.append(f"### `{fs_id}` — {esc(fs.get('desc'))}\n\n| Attribut (id) | Libellé | Type | Obligatoire | Règle |\n|---|---|---|---|---|\n")
        for f in fs["fields"]:
            req = "oui" if f.get("required") else (f"à l'état `{f['requiredAt']}`" if f.get("requiredAt") else "")
            out.append(f"| `{f['id']}` | {f['fr']} | {ftype(f)} | {req} | {esc(f.get('desc'))} |\n")
        out.append("\n")
    current = None
    for t in m.types:
        if t["family"] != current:
            current = t["family"]
            out.append(f"## Famille : {FAMILY_FR[current]}\n\n")
        out.append(f"### `{t['id']}` — {t['fr']} / {t['en']}\n\n{esc(t.get('desc'))}\n\n")
        out.append(f"- Workflow : [`{t['workflow']}`](A4_workflows.md#{anchor(t['workflow'])})\n")
        out.append(f"- Jeux d'attributs hérités : {', '.join('`'+x+'`' for x in t.get('fieldSets', [])) or '—'}\n\n")
        out.append("| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |\n|---|---|---|---|---|---|\n")
        for f in m.fields_of(t):
            req = "oui" if f.get("required") else (f"`{f['requiredAt']}`" if f.get("requiredAt") else "")
            if f.get("computed"):
                req = "calculé"
            out.append(f"| `{f['id']}` | {f['fr']} | {ftype(f)} | {req} | {f['origin']} | {esc(f.get('desc'))} |\n")
        out.append("\n")
    return "".join(out)


# --------------------------------------------------------------------- A2
def gen_enums(m: Model) -> str:
    out = ["# Annexe A2 — Énumérations\n\n", BANNER,
           "Confiance : **C** confirmé par source publique, **P** probable, **H** hypothèse à valider (cf. Partie 2).\n\n"]
    usage: dict[str, list[str]] = {}
    for t in m.types:
        for f in m.fields_of(t):
            if f["type"].startswith("enum:"):
                usage.setdefault(f["type"][5:], []).append(f"{t['id']}.{f['id']}")
    for eid, e in m.enumerations.items():
        conf = e.get("confidence", "")
        scope = " — *surchargée au niveau projet*" if e.get("scope") == "project" else ""
        out.append(f"## {eid}\n\n**{e['fr']}** / {e['en']}{scope}" + (f" — confiance **{conf}**" if conf else "") + "\n\n")
        if e.get("desc"):
            out.append(f"{esc(e['desc'])}\n\n")
        used = usage.get(eid, [])
        if used:
            out.append(f"Utilisée par : {', '.join('`'+u+'`' for u in sorted(set(used))[:12])}"
                       + (" …" if len(set(used)) > 12 else "") + "\n\n")
        out.append("| id | Libellé FR | Libellé EN | Défaut |\n|---|---|---|---|\n")
        for o in e["options"]:
            out.append(f"| `{o['id']}` | {esc(o['fr'])} | {esc(o['en'])} | {'✔' if o.get('default') else ''} |\n")
        out.append("\n")
    return "".join(out)


# --------------------------------------------------------------------- A3
def gen_links(m: Model) -> str:
    out = ["# Annexe A3 — Rôles de liens, règles et matrice de traçabilité\n\n", BANNER]
    out.append("Convention : le lien est créé depuis l'artefact **aval** (source) vers l'artefact **amont** (cible). "
               "Une modification de la cible rend le lien suspect côté source.\n\n")
    out.append("## Rôles de liens\n\n| id | Libellé (sens direct) | Libellé (sens inverse) | Suspicion | Sémantique |\n|---|---|---|---|---|\n")
    for r in m.link_roles:
        out.append(f"| `{r['id']}` | {r['fr']} / *{r['en']}* | {r['frOpposite']} / *{r['enOpposite']}* | "
                   f"{'oui' if r.get('suspect') else 'non'} | {esc(r.get('semantics'))} |\n")
    out.append("\n## Règles d'autorisation (source → cibles)\n\n")
    for r in m.link_roles:
        out.append(f"### `{r['id']}`\n\n")
        rules = r.get("rules", [])
        if not rules:
            out.append("Non restreint.\n\n")
            continue
        for rule in rules:
            frm = rule.get("from")
            to = rule.get("to")
            frm_s = frm if isinstance(frm, str) else ", ".join(frm)
            to_s = to if isinstance(to, str) else ", ".join(to)
            out.append(f"- **{frm_s}** → {('même type' if to == 'same' else to_s)}\n")
        out.append("\n")
    # matrice type × type
    ids = [t["id"] for t in m.types]
    cell: dict[tuple[str, str], list[str]] = {}
    for r in m.link_roles:
        if r["id"] in ("relatesTo", "parent", "branched_from", "derived_from"):
            continue
        for rule in r.get("rules", []):
            frm = m.expand_types(rule.get("from"))
            to = m.expand_types(rule.get("to"))
            for f in frm:
                targets = [f] if to == ["same"] else to
                for t in targets:
                    if f in ids and t in ids:
                        cell.setdefault((f, t), []).append(r["id"])
    out.append("## Matrice de traçabilité (ligne = source aval, colonne = cible amont)\n\n")
    out.append("Hors `parent`, `relatesTo` et rôles système de réutilisation. Abréviations des rôles :\n\n")
    abbr = {r["id"]: "".join(c for c in r["id"] if c.isupper() or c == r["id"][0]).lower()[:4]
            for r in m.link_roles}
    abbr.update({"flowsDownFrom": "FD", "refines": "RF", "satisfies": "SAT", "realizes": "REA",
                 "allocatedTo": "AL", "verifies": "VER", "validates": "VAL", "mitigates": "MIT",
                 "causes": "CAU", "supportedBy": "SUP", "assumes": "ASM", "impacts": "IMP",
                 "resolves": "RES", "sideA": "A", "sideB": "B", "documents": "DOC",
                 "dependsOn": "DEP", "supersedes": "SUPS", "raisedIn": "RAI", "duplicates": "DUP"})
    out.append(", ".join(f"`{v}` = {k}" for k, v in abbr.items()
                         if k not in ("relatesTo", "parent", "branched_from", "derived_from")) + "\n\n")
    short = {t["id"]: t["id"] for t in m.types}
    out.append("| source \\ cible | " + " | ".join(f"`{short[i]}`" for i in ids) + " |\n")
    out.append("|---|" + "---|" * len(ids) + "\n")
    for f in ids:
        row = [" ".join(abbr[x] for x in cell.get((f, t), [])) for t in ids]
        out.append(f"| `{f}` | " + " | ".join(row) + " |\n")
    out.append("\n## Politique de déclenchement de la suspicion\n\n")
    for k, v in m.suspect_fields.items():
        out.append(f"- **{k}** : {', '.join('`'+x+'`' for x in v)}\n")
    out.append("\n## Règles de complétude de la traçabilité\n\n| id | Règle | S'applique à | Sévérité |\n|---|---|---|---|\n")
    for tr in m.traceability_rules:
        ap = tr["appliesTo"] if isinstance(tr["appliesTo"], str) else ", ".join(tr["appliesTo"])
        out.append(f"| {tr['id']} | {esc(tr['fr'])} | {ap} | {tr['severity']} |\n")
    return "".join(out)


# --------------------------------------------------------------------- A4
def gen_workflows(m: Model) -> str:
    out = ["# Annexe A4 — Workflows des Work Items et des LiveDocs\n\n", BANNER]
    out.append("## Catalogue des conditions\n\n| Condition | Implémentation | Correspondance Polarion | Description |\n|---|---|---|---|\n")
    for k, v in m.conditions_catalog.items():
        out.append(f"| `{k}` | {v['impl']} | {esc(v.get('polarion'))} | {esc(v['fr'])} |\n")
    out.append("\n## Catalogue des fonctions\n\n| Fonction | Implémentation | Correspondance Polarion | Description |\n|---|---|---|---|\n")
    for k, v in m.functions_catalog.items():
        out.append(f"| `{k}` | {v['impl']} | {esc(v.get('polarion'))} | {esc(v['fr'])} |\n")
    out.append("\n## Significations de signature\n\n")
    for k, v in m.signature_meanings.items():
        out.append(f"- `{k}` : {v['fr']} / *{v['en']}*\n")
    out.append("\n")
    for wid, wf in m.all_workflows().items():
        kind = "LiveDoc" if wid in m.document_workflows else "Work Item"
        out.append(f"## {wid}\n\n**{wf['fr']}** ({kind})")
        if wf.get("appliesTo"):
            out.append(" — s'applique à : " + ", ".join(f"`{x}`" for x in wf["appliesTo"]))
        out.append("\n\n```mermaid\nstateDiagram-v2\n")
        out.append(f"    [*] --> {wf['initial']}\n")
        for s in wf["states"]:
            out.append(f"    {s['id']} : {s['fr']}\n")
        for tr in wf["transitions"]:
            sig = " ✍" if tr.get("signature", {}).get("required") else ""
            for frm in tr["from"]:
                out.append(f"    {frm} --> {tr['to']} : {tr['id']}{sig}\n")
        for s in wf["states"]:
            if s.get("category") in ("done", "cancelled") and not any(
                    s["id"] in t["from"] for t in wf["transitions"]):
                out.append(f"    {s['id']} --> [*]\n")
        out.append("```\n\n")
        out.append("| Transition | De → vers | Rôles | Champs requis | Conditions | Fonctions | Signature |\n|---|---|---|---|---|---|---|\n")
        for tr in wf["transitions"]:
            conds = "; ".join(f"{k}" + (f"({_short(v)})" if v is not True else "")
                              for c in tr.get("conditions", []) or [] for k, v in c.items())
            fns = "; ".join(f"{k}" for f in tr.get("functions", []) or [] for k in f)
            sig = tr.get("signature") or {}
            sig_s = ""
            if sig.get("required"):
                sig_s = m.signature_meanings[sig["meaning"]]["fr"]
                if sig.get("onlyIf"):
                    sig_s += f" (si {sig['onlyIf']})"
            out.append(f"| `{tr['id']}` {tr['fr']} | {', '.join(tr['from'])} → {tr['to']} | "
                       f"{', '.join(tr.get('roles', []))} | {', '.join(tr.get('requiredFields', []) or [])} | "
                       f"{esc(conds)} | {esc(fns)} | {esc(sig_s)} |\n")
        out.append("\n")
    out.append("## Statuts des Test Runs et résultats d'enregistrement\n\n")
    for s in m.test_run_statuses:
        out.append(f"- Test Run `{s['id']}` : {s['fr']}\n")
    for s in m.test_record_results:
        out.append(f"- Résultat `{s['id']}` : {s['fr']}\n")
    return "".join(out)


def _short(v) -> str:
    if isinstance(v, dict):
        return ", ".join(f"{k}={_short(x)}" for k, x in v.items())
    if isinstance(v, list):
        return "/".join(_short(x) for x in v)
    return str(v)


# --------------------------------------------------------------------- A5
def gen_documents(m: Model) -> str:
    dt = m.document_types
    out = ["# Annexe A5 — Types de LiveDocs et gabarits\n\n", BANNER]
    out.append("## Attributs de document\n\n| id | Libellé | Type | Obligatoire |\n|---|---|---|---|\n")
    for f in dt["documentCustomFields"]:
        out.append(f"| `{f['id']}` | {f['fr']} | {ftype(f)} | {'oui' if f.get('required') else ''} |\n")
    out.append("\n")
    for d in dt["documentTypes"]:
        out.append(f"## `{d['id']}` — {d['fr']}\n\n*{d['en']}* — workflow [`{d['workflow']}`](A4_workflows.md#{anchor(d['workflow'])})\n\n")
        out.append("Types de Work Items autorisés : " + ", ".join(f"`{x}`" for x in d["allowedTypes"]) + "\n\n")
        out.append("Plan type :\n\n" + "".join(f"- {x}\n" for x in d.get("outline", [])) + "\n")
    return "".join(out)


# --------------------------------------------------------------------- A6
def gen_roles(m: Model) -> str:
    r = m.roles
    out = ["# Annexe A6 — Rôles, licences et permissions\n\n", BANNER]
    out.append("## Types de licences\n\n")
    for k, v in r["licenceTypes"].items():
        out.append(f"- **{k}** : {v['fr']}\n")
    out.append("\n## Rôles globaux\n\n| id | Rôle | Note |\n|---|---|---|\n")
    for g in r["globalRoles"]:
        out.append(f"| `{g['id']}` | {g['fr']} | {esc(g.get('note'))} |\n")
    fams = ["REQ", "ARC", "SAF", "VV", "CHG", "PRJ", "DOC", "LIB"]
    out.append("\n## Rôles projet — matrice des droits\n\nR lire · C créer · E modifier · T transitions · A approuver · S signer · L lier · X administrer\n\n")
    out.append("| Rôle | Licence | " + " | ".join(fams) + " | Note |\n|---|---|" + "---|" * len(fams) + "---|\n")
    for p in r["projectRoles"]:
        rights = p.get("rights", {})
        out.append(f"| `{p['id']}` {p['fr']} | {p.get('licence', '')} | "
                   + " | ".join(str(rights.get(f, "")) for f in fams) + f" | {esc(p.get('note'))} |\n")
    out.append("\n## Règles de permission\n\n")
    for pr in r["permissionRules"]:
        out.append(f"- **{pr['id']}** — {pr['fr']}\n")
    return "".join(out)


# --------------------------------------------------------------------- A7
def gen_tailoring(m: Model) -> str:
    t = m.tailoring
    out = ["# Annexe A7 — Tailoring (approche graduée)\n\n", BANNER]
    g = t["scoringGrid"]
    out.append(f"## Grille de cotation\n\n{g['desc']}\n\n| Critère | 0 | 1 | 2 | 3 |\n|---|---|---|---|---|\n")
    for c in g["criteria"]:
        s = c["scale"]
        out.append(f"| **{c['fr']}** | {s[0]} | {s[1]} | {s[2]} | {s[3]} |\n")
    out.append("\nSeuils : " + " ; ".join(f"**{k}** {v}" for k, v in g["thresholds"].items()) + "\n\n")
    out.append("## Socle non négociable\n\n")
    for i in t["nonNegotiableCore"]["items"]:
        out.append(f"- **{i['id']}** — {i['fr']}\n")
    out.append("\n## Profils par classe\n\n| Aspect | " + " | ".join(t["classProfiles"].keys()) + " |\n|---|" + "---|" * len(t["classProfiles"]) + "\n")
    aspects = ["fr", "documentWorkflow", "reviews", "mbse", "icd", "variants", "safetyCase", "ccb", "vvIndependence", "kpiReview"]
    for a in aspects:
        row = []
        for prof in t["classProfiles"].values():
            v = prof.get(a, "")
            row.append(", ".join(v) if isinstance(v, list) else esc(v))
        out.append(f"| {a} | " + " | ".join(row) + " |\n")
    out.append("\n### Types de Work Items actifs par classe\n\n| Type | " + " | ".join(t["classProfiles"].keys()) + " |\n|---|" + "---|" * len(t["classProfiles"]) + "\n")
    for ty in m.types:
        row = []
        for prof in t["classProfiles"].values():
            w = prof["workItemTypes"]
            row.append("●" if w == "all" or ty["id"] in w else "")
        out.append(f"| `{ty['id']}` | " + " | ".join(row) + " |\n")
    out.append("\n## Typologie de projet → classe et gabarit par défaut\n\n| Typologie | Classe | Gabarit | BU |\n|---|---|---|---|\n")
    pt = {o["id"]: o["fr"] for o in m.enumerations["projectType"]["options"]}
    for k, v in t["projectTypeDefaults"].items():
        out.append(f"| {pt[k]} (`{k}`) | {v['defaultClass']} | `{v['template']}` | {', '.join(v['bu'])} |\n")
    return "".join(out)


# --------------------------------------------------------------------- A8
def gen_metamodel(m: Model) -> str:
    out = ["# Annexe A8 — Méta-modèle (vue graphique)\n\n", BANNER]
    out.append("Vue simplifiée des principaux rôles de liens entre types (source → cible amont).\n\n```mermaid\nflowchart BT\n")
    groups = {}
    for t in m.types:
        groups.setdefault(t["family"], []).append(t)
    for fam, ts in groups.items():
        out.append(f"  subgraph {fam}[\"{FAMILY_FR[fam]}\"]\n")
        for t in ts:
            out.append(f"    {t['id']}[\"{t['fr']}\"]\n")
        out.append("  end\n")
    edges = set()
    keep = {"flowsDownFrom", "satisfies", "realizes", "verifies", "validates", "mitigates",
            "supportedBy", "assumes", "sideA", "refines"}
    for r in m.link_roles:
        if r["id"] not in keep:
            continue
        for rule in r.get("rules", []):
            frm = m.expand_types(rule.get("from"))
            to = m.expand_types(rule.get("to"))
            if to == ["same"] or len(frm) > 6:
                continue
            for f in frm:
                for t in to:
                    if f != t and f in m.type_ids and t in m.type_ids:
                        edges.add((f, t, r["id"]))
    for f, t, rid in sorted(edges):
        out.append(f"  {f} -->|{rid}| {t}\n")
    out.append("```\n")
    return "".join(out)


def main() -> int:
    model = validate(load_model())
    if model.errors:
        for e in model.errors:
            print("ERROR", e, file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    files = {
        "A1_types_et_attributs.md": gen_types(model),
        "A2_enumerations.md": gen_enums(model),
        "A3_liens_et_tracabilite.md": gen_links(model),
        "A4_workflows.md": gen_workflows(model),
        "A5_documents.md": gen_documents(model),
        "A6_roles_permissions.md": gen_roles(model),
        "A7_tailoring.md": gen_tailoring(model),
        "A8_metamodele.md": gen_metamodel(model),
    }
    for name, content in files.items():
        (OUT / name).write_text(content, encoding="utf-8")
    print(f"{len(files)} annexes générées → {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
