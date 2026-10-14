# ALM Datamodel — Plan directeur Polarion pour l'ingénierie système (nucléaire, Framatome)

Ce dépôt contient le **plan directeur** et le **modèle de données « as code »** d'un déploiement de Siemens Polarion ALM sur une instance vierge (greenfield). Il couvre les activités d'ingénierie système de Framatome : nouveaux réacteurs (EPR2, UK EPR, SMR NUWARD), base installée (RGV, réexamens / VD, modifications, fortuits, outillages, augmentation de puissance, démantèlement, atelier chaud), combustible (dont MTR et licensing d'usine), contrôle-commande, composants, codes de calcul, simulateurs, cybersécurité, santé. Au total, **32 typologies de projets, chacune prouvée par un scénario de couverture exécuté en CI**.

> **Sources ouvertes uniquement (OSINT).** Aucune donnée interne ou confidentielle n'a été utilisée. Chaque fait porte un niveau de confiance : **[C]** confirmé, **[P]** probable, **[P\*]** à revérifier, **[H]** hypothèse. Le contenu doit être validé en ateliers internes avant tout paramétrage en production (voir `docs/partie2/05_Plan_de_recherche_OSINT.md`).

## Point d'entrée

**[docs/00_Synthese_et_note_de_cadrage.md](docs/00_Synthese_et_note_de_cadrage.md)** : les nouveautés de la v0.3, les recommandations structurantes et la correspondance avec la demande. Revue critique : [doc. 18](docs/partie3/18_Analyse_critique.md) ; robustesse : [doc. 19](docs/partie3/19_Robustesse_du_modele.md).

## Structure

```
model/                         Source unique de vérité (YAML)
  enumerations.yaml            111 énumérations (classements de sûreté multi-schémas, ESPN, K, filières, UO…)
  work_item_types.yaml         36 types de Work Items, jeux d'attributs (fieldSets), 325 attributs distincts
  link_roles.yaml              26 rôles de liens, règles from→to, politique de suspicion, règles TR-01..20
  workflows.yaml               24 workflows de Work Items + 3 workflows de LiveDocs, conditions, signatures
  roles.yaml                   rôles, licences, matrice des droits, règles de permission PR-01..11
  document_types.yaml          22 types de LiveDocs, attributs de document, plans types
  tailoring.yaml               grille de cotation, socle non négociable, profils A–D, 32 typologies
  project_topology.yaml        instances, groupes de projets, master → 6 archétypes → spécialisations
  coverage_scenarios.yaml      preuve de couverture par typologie (types, documents, traces, attributs)
  project_setup.yaml           provisioning : questionnaire, règles de dérivation, habilitations
  regulatory_packs.yaml        packs réglementaires (FR, US, DE, UK, CA, AIEA, BPF, défense)
  import_export.yaml           profils ReqIF, règles d'analyse Word, gabarits Excel, connecteurs
tools/
  almmodel.py                  chargement (YAML 1.2) + validation de cohérence et de couverture (CI)
  model_checks.py              contrôles du provisioning, des packs et des échanges
  generate_polarion.py         génération de la configuration Polarion (.polarion/…) FR / EN
  generate_docs.py             génération des annexes A1–A11 (Markdown + Mermaid)
generated/polarion/{fr,en}/    configuration Polarion générée (types, champs, énumérations, liens, workflows, documents)
docs/
  00_Synthese_et_note_de_cadrage.md
  partie1/                     cartographie contextuelle (organisation, projets, disciplines, réglementation)
  partie2/                     plan de recherche OSINT, décisions d'architecture (ADR-01..28)
  partie3/                     méthodologie, modèle, traçabilité, workflows, topologie, LiveDocs,
                               tableaux de bord, intégrations, infrastructure / validation, feuille de route, gouvernance,
                               analyse critique (18), robustesse (19), facteurs de succès (20),
                               organisation matricielle / provisioning / habilitations (21), import-export (22)
  generated/                   annexes générées A1–A11 (ne pas éditer)
  annexes/                     glossaire, sources OSINT
tests/                         tests de non-régression du modèle et des générateurs
```

## Utilisation

Prérequis : Python 3.10+ et PyYAML.

```bash
python3 tools/almmodel.py                     # validation (doit afficher 0 erreur ; -v pour les informations)
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
