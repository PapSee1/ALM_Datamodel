# ALM Datamodel — Plan directeur Polarion pour l'ingénierie système (nucléaire, Framatome)

Ce dépôt contient le **plan directeur** et le **modèle de données « as code »** d'un déploiement de Siemens Polarion ALM sur une instance vierge (greenfield). Il couvre les activités d'ingénierie système de Framatome : nouveaux réacteurs (EPR2, UK EPR, SMR NUWARD), base installée (RGV, réexamens / VD, modifications, fortuits, outillages), combustible, contrôle-commande et composants.

> **Sources ouvertes uniquement (OSINT).** Aucune donnée interne ou confidentielle n'a été utilisée. Chaque fait porte un niveau de confiance : **[C]** confirmé, **[P]** probable, **[P\*]** à revérifier, **[H]** hypothèse. Le contenu doit être validé en ateliers internes avant tout paramétrage en production (voir `docs/partie2/05_Plan_de_recherche_OSINT.md`).

## Point d'entrée

**[docs/00_Synthese_et_note_de_cadrage.md](docs/00_Synthese_et_note_de_cadrage.md)** : les 12 recommandations structurantes et la correspondance avec la demande.

## Structure

```
model/                         Source unique de vérité (YAML)
  enumerations.yaml            100 énumérations (classements de sûreté multi-schémas, ESPN, K, états…)
  work_item_types.yaml         33 types de Work Items, jeux d'attributs (fieldSets), 284 attributs distincts
  link_roles.yaml              24 rôles de liens, règles from→to, politique de suspicion, règles TR-01..17
  workflows.yaml               21 workflows de Work Items + 3 workflows de LiveDocs, conditions, signatures
  roles.yaml                   rôles, licences, matrice des droits, règles de permission
  document_types.yaml          20 types de LiveDocs, attributs de document, plans types
  tailoring.yaml               grille de cotation, socle non négociable, profils de classes A–D
  project_topology.yaml        instances, groupes de projets, bibliothèques, lignes de produits, gabarits
tools/
  almmodel.py                  chargement + validation de cohérence (CI)
  generate_polarion.py         génération de la configuration Polarion (.polarion/…) FR / EN
  generate_docs.py             génération des annexes A1–A8 (Markdown + Mermaid)
generated/polarion/{fr,en}/    configuration Polarion générée (types, champs, énumérations, liens, workflows, documents)
docs/
  00_Synthese_et_note_de_cadrage.md
  partie1/                     cartographie contextuelle (organisation, projets, disciplines, réglementation)
  partie2/                     plan de recherche OSINT, décisions d'architecture (ADR-01..23)
  partie3/                     méthodologie, modèle, traçabilité, workflows, topologie, LiveDocs,
                               tableaux de bord, intégrations, infrastructure / validation, feuille de route, gouvernance
  generated/                   annexes générées A1–A8 (ne pas éditer)
  annexes/                     glossaire, sources OSINT
tests/                         tests de non-régression du modèle et des générateurs
```

## Utilisation

Prérequis : Python 3.10+ et PyYAML.

```bash
python3 tools/almmodel.py                     # validation (doit afficher 0 erreur)
python3 tools/generate_polarion.py --lang fr  # → generated/polarion/fr/.polarion/
python3 tools/generate_polarion.py --lang en  # → generated/polarion/en/.polarion/
python3 tools/generate_docs.py                # → docs/generated/
python3 -m unittest discover -s tests         # tests
```

La configuration générée suit l'arborescence `.polarion/` d'un dépôt Polarion :
- `tracker/fields/*-enum.xml`, `*-custom-fields.xml`, `*-status-enum.xml` ;
- `tracker/workflow/*-workflow.xml` ;
- `documents/fields`, `documents/workflow` ;
- `testing/configuration`.

Elle se déploie en configuration globale ou dans un gabarit de projet, après recette.

Certaines conditions de workflow reposent sur des scripts (`ScriptCondition` / `ScriptFunction`, JavaScript). Ils sont spécifiés au document `docs/partie3/10_Workflows_signatures_roles.md` § 4 et sont à développer et qualifier lors de la phase de fondations.

## Gouvernance des évolutions

Toute modification passe par le modèle YAML. Le circuit est le suivant :
1. validation (CI) ;
2. régénération ;
3. revue (pull request) ;
4. recette ;
5. déploiement.

Un identifiant (type, attribut, option, rôle de lien) n'est jamais renommé ni supprimé : il est déprécié ou migré. Voir `docs/partie3/17_Gouvernance_conduite_changement.md`.
