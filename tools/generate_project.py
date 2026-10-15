"""Génère le kit de configuration d'un projet à partir de sa fiche de provisioning
(model/pilots/<id>.yaml) : surcharges projet autorisées par la politique
d'extension (model/extension_policy.yaml) et dossier de provisioning.

Le cœur (configuration globale) reste celui de generated/polarion/<lang>/ ;
ce script ne produit QUE les fichiers qu'un projet a le droit de surcharger :
  - sous-ensemble des types de Work Items (tranche activée) ;
  - sous-ensemble des types de documents ;
  - valeurs des énumérations de portée projet ;
  - champs personnalisés des types touchés par un champ masqué par un pack.
Sortie : generated/projects/<id>/<lang>/.polarion/... + provisioning-record.md

Usage :
    python3 tools/generate_project.py            # tous les pilotes, FR et EN
    python3 tools/generate_project.py --pilot P-NUWARD-L1 --lang fr
"""
from __future__ import annotations

import argparse
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import generate_polarion as gp  # noqa: E402
import model_checks  # noqa: E402
from almmodel import ROOT, Model, load_model, validate  # noqa: E402

OUT = ROOT / "generated" / "projects"


def _xml_fields(fields: list[dict], lang: str) -> str:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', gp.HEADER.rstrip(), "<fields>"]
    lines += [gp.field_xml(f, lang) for f in fields]
    lines.append("</fields>")
    return "\n".join(lines) + "\n"


def project_files(m: Model, pilot: dict, lang: str, base: pathlib.Path) -> list[str]:
    """Écrit les surcharges projet ; renvoie la liste des chemins relatifs écrits."""
    written: list[str] = []
    scope = pilot["pilotScope"]
    derived = pilot["derived"]
    active = [t["id"] for t in m.types if t["id"] in scope["activeTypes"]]
    # 1. types de Work Items (sous-ensemble du cœur) + type natif 'heading'
    opts = [{"id": t["id"], "fr": t["fr"], "en": t["en"], "color": t.get("color"),
             "desc": " ".join(str(t.get("desc", "")).split())} for t in m.types if t["id"] in active]
    opts += [{"id": t["id"], "fr": t["fr"], "en": t["en"], "desc": t.get("note", "")} for t in m.native_types]
    rel = "tracker/fields/workitem-type-enum.xml"
    gp.write(base / rel, gp.enum_xml(opts, lang))
    written.append(rel)
    # 2. types de documents (sous-ensemble)
    docs = [d for d in m.document_types["documentTypes"] if d["id"] in scope["activeDocuments"]]
    dopts = [{"id": d["id"], "fr": d["fr"], "en": d["en"],
              "desc": f"Workflow : {d['workflow']} ; types autorisés : {', '.join(d['allowedTypes'])}"} for d in docs]
    rel = "documents/fields/document-type-enum.xml"
    gp.write(base / rel, gp.enum_xml(dopts, lang))
    written.append(rel)
    # 3. énumérations de portée projet
    ans = pilot["answers"]
    keep = {
        "operationalUnit": {"tbd", ans.get("responsibleUnit"), *(ans.get("performingUnits") or [])},
        "businessLine": {ans.get("businessLine"), "other"},
    }
    local_values = pilot.get("projectEnumValues") or {}
    for eid in derived.get("projectEnums", []):
        options = m.enumerations[eid]["options"]
        if eid in keep:
            subset = [o for o in options if o["id"] in keep[eid]]
        else:
            subset = [o for o in options if o.get("default")]
        subset += local_values.get(eid, [])
        rel = f"tracker/fields/{eid}-enum.xml"
        gp.write(base / rel, gp.enum_xml(subset, lang))
        written.append(rel)
    # 4. champs masqués par les packs réglementaires
    hidden = set(derived.get("hiddenFields", []))
    for t in m.types:
        if t["id"] not in active:
            continue
        fields = m.fields_of(t)
        if not hidden & {f["id"] for f in fields}:
            continue
        rel = f"tracker/fields/{t['id']}-custom-fields.xml"
        gp.write(base / rel, _xml_fields([f for f in fields if f["id"] not in hidden], lang))
        written.append(rel)
    return written


def _fmt(v) -> str:
    if isinstance(v, list):
        return ", ".join(f"`{x}`" for x in v) or "—"
    if isinstance(v, dict):
        return ", ".join(f"{k}={x}" for k, x in v.items())
    return f"`{v}`" if v not in (None, "") else "—"


def record_md(m: Model, pilot: dict, files: list[str]) -> str:
    d, ans, scope = pilot["derived"], pilot["answers"], pilot["pilotScope"]
    conf = pilot.get("answerConfidence") or {}
    q_by_param = {q["param"]: q for q in m.setup["questionnaire"]}
    deferred = [t for t in m.type_ids if t not in scope["activeTypes"]]
    out = [f"# Dossier de provisioning — `{pilot['id']}`\n\n",
           "> Document **généré** par `tools/generate_project.py` depuis "
           f"`model/pilots/{pilot['id']}.yaml` — ne pas éditer à la main.\n\n",
           f"**{pilot['fr']}**\n\n{' '.join(str(pilot.get('context', '')).split())}\n\n",
           "## 1. Réponses au questionnaire\n\n| # | Paramètre | Question | Réponse | Confiance |\n|---|---|---|---|---|\n"]
    for param, val in ans.items():
        q = q_by_param.get(param, {})
        out.append(f"| {q.get('id', '')} | `{param}` | {q.get('fr', '')} | {_fmt(val)} | {conf.get(param, '')} |\n")
    if conf.get("note"):
        out.append(f"\n*Note :* {conf['note']}\n")
    inc = next((i["id"] for i in m.extension_policy.get("deploymentIncrements", [])
                if pilot["id"] in (i.get("fromPilots") or [])), "—")
    out.append("\n## 2. Paramètres dérivés (règles D01–D13)\n\n| Paramètre | Valeur |\n|---|---|\n")
    for k, label in (("template", "Gabarit"), ("archetype", "Archétype"), ("projectClass", "Classe de tailoring"),
                     ("score", "Score de cotation"), ("instance", "Instance"), ("packs", "Packs réglementaires"),
                     ("extProject", "Projet sas à créer"), ("enableTypes", "Types activés par règle"),
                     ("enableDocuments", "Documents activés par règle"), ("qualifiedSignatory", "Signatures habilitées"),
                     ("connectors", "Connecteurs"), ("projectEnums", "Énumérations projet"),
                     ("hiddenFields", "Champs masqués (packs)")):
        out.append(f"| {label} | {_fmt(d.get(k))} |\n")
    out.append(f"| Incrément de déploiement du cœur | `{inc}` |\n")
    out.append(f"\n## 3. Tranche activée (sous-ensemble du modèle 150 %)\n\n*{scope['slice']}*\n\n")
    out.append(f"- **Types activés ({len(scope['activeTypes'])} / {len(m.type_ids)})** : {_fmt(scope['activeTypes'])}\n")
    out.append(f"- **Types différés ({len(deferred)})** : {_fmt(deferred)}\n")
    out.append(f"- **Documents activés ({len(scope['activeDocuments'])})** : {_fmt(scope['activeDocuments'])}\n")
    out.append(f"- **Hors périmètre du pilote** : {scope.get('deferred', '—')}\n")
    out.append("\n## 4. Fichiers de configuration projet générés\n\n"
               "À déposer dans le dossier `.polarion/` du projet, **après** déploiement du cœur "
               "(`generated/polarion/<lang>/.polarion/`) en configuration globale. Seuls les fichiers "
               "autorisés par `model/extension_policy.yaml` (overridableProjectFiles) sont produits.\n\n")
    out += [f"- `{f}`\n" for f in files]
    out.append("\n## 5. Bibliothèques à brancher\n\n" + "".join(f"- {x}\n" for x in d.get("libraries", [])))
    roles = model_checks.roles_needed(m, scope["activeTypes"], scope["activeDocuments"])
    real = [r for r in roles if not r.startswith("workitem.") and r not in ("anyProjectMember", "documentOwner")]
    out.append(f"\n## 6. Rôles projet à pourvoir ({len(real)})\n\n"
               "Rôles intervenant dans au moins une transition des workflows activés "
               "(voir annexe A6 pour les droits et licences) :\n\n" + _fmt(real) + "\n")
    out.append("\n## 7. Critères de succès du pilote\n\n| # | Critère | Cible |\n|---|---|---|\n")
    for sc in scope.get("successCriteria", []):
        out.append(f"| {sc['id']} | {sc['fr']} | {sc['target']} |\n")
    out.append("\n## 8. Liste de contrôle de création (doc. 23 § 5)\n\n"
               "- [ ] Réponses de confiance H confirmées en atelier (doc. 24, atelier C4)\n"
               "- [ ] Cœur déployé et spike de conformité clos (doc. 23, étape S1)\n"
               "- [ ] Scripts « socle » en service et testés (doc. 23, étape S3)\n"
               "- [ ] Projet créé depuis le gabarit, surcharges projet ci-dessus déposées\n"
               "- [ ] Projet sas créé et comptes client nominatifs ouverts (si `extProject`)\n"
               "- [ ] Bibliothèques branchées, profil ReqIF client testé sur fichier de référence\n"
               "- [ ] Groupes d'annuaire des rôles alimentés, licences attribuées\n"
               "- [ ] Tableaux de bord du rôle opérationnels sur données de test\n"
               "- [ ] Cas OQ du pilote exécutés, revue go / no-go signée\n")
    return "".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pilot", default=None, help="Identifiant du pilote (défaut : tous)")
    ap.add_argument("--lang", choices=["fr", "en"], default=None, help="Langue (défaut : fr et en)")
    args = ap.parse_args(argv)
    model = validate(load_model())
    if model.errors:
        for e in model.errors:
            print("ERROR", e, file=sys.stderr)
        return 1
    langs = [args.lang] if args.lang else ["fr", "en"]
    for pilot in model.pilots:
        if args.pilot and pilot["id"] != args.pilot:
            continue
        root = OUT / pilot["id"]
        if root.exists():
            shutil.rmtree(root)
        files: list[str] = []
        for lang in langs:
            files = project_files(model, pilot, lang, root / lang / ".polarion")
        (root / "provisioning-record.md").write_text(record_md(model, pilot, files), encoding="utf-8")
        print(f"[{pilot['id']}] {len(files)} fichiers de surcharge projet × {len(langs)} langue(s) "
              f"+ dossier de provisioning → {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
