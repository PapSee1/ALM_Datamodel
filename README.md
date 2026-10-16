# ALM Datamodel — Plan directeur Polarion pour l'ingénierie système (nucléaire, Framatome)

Ce dépôt contient le **plan directeur** et le **modèle de données « as code »** d'un déploiement de Siemens Polarion ALM sur une instance vierge (greenfield). Il couvre les activités d'ingénierie système de Framatome : nouveaux réacteurs (EPR2, UK EPR, SMR NUWARD), base installée (RGV, réexamens / VD, modifications, fortuits, outillages, augmentation de puissance, démantèlement, atelier chaud), combustible (dont MTR et licensing d'usine), contrôle-commande, composants, codes de calcul, simulateurs, cybersécurité, santé. Au total, **32 typologies de projets, chacune prouvée par un scénario de couverture exécuté en CI**.

> **Sources ouvertes uniquement (OSINT).** Aucune donnée interne ou confidentielle n'a été utilisée. Chaque fait porte un niveau de confiance : **[C]** confirmé, **[P]** probable, **[P\*]** à revérifier, **[H]** hypothèse de modélisation, **[NT]** non trouvé en source ouverte, **[X]** contredit par les sources. Le contenu doit être validé en ateliers internes avant tout paramétrage en production (voir `docs/partie2/05_Plan_de_recherche_OSINT.md`).

## Point d'entrée

**Nouveau dans le dépôt ?** Lisez d'abord **[docs/GUIDE_DE_LECTURE.md](docs/GUIDE_DE_LECTURE.md)** : la carte du dépôt (rôle de chaque document, fichier de modèle, outil et dossier généré), les ordres de lecture par profil, ce qui sert aux ateliers et ce qui sert à construire Polarion, et ce qui dépend ou non de l'outil.

**[docs/00_Synthese_et_note_de_cadrage.md](docs/00_Synthese_et_note_de_cadrage.md)** : la synthèse, les recommandations structurantes, les apports de chaque version et la correspondance avec la demande. L'historique des versions est dans [CHANGELOG.md](CHANGELOG.md) ; le glossaire dans [docs/annexes/B_Glossaire.md](docs/annexes/B_Glossaire.md).

Pour démarrer avec une équipe :
1. [doc. 24 — parcours d'onboarding en 12 ateliers](docs/partie4/24_Parcours_onboarding_ateliers.md) ;
2. [doc. 25 — stratégie de modèle (cœur gouverné, extensions)](docs/partie4/25_Strategie_coeur_50_vs_150.md) ;
3. [doc. 23 — inventaire du kit et guide pas à pas jusqu'au pilote NUWARD](docs/partie4/23_Kit_deploiement_guide_pas_a_pas.md).

Revue critique : [doc. 18](docs/partie4/18_Analyse_critique.md) ; robustesse : [doc. 19](docs/partie4/19_Robustesse_du_modele.md).

## Structure

```
model/                         Source unique de vérité (YAML)
  enumerations.yaml            112 énumérations (classements de sûreté multi-schémas, ESPN, K, filières, UO…)
  work_item_types.yaml         36 types de Work Items, familles, jeux d'attributs (fieldSets), 327 attributs distincts
  link_roles.yaml              26 rôles de liens, règles from→to, politique de suspicion, règles TR-01..20
  workflows.yaml               24 workflows de Work Items + 3 workflows de LiveDocs, états de soumission, conditions, signatures
  roles.yaml                   rôles, licences, matrice des droits, règles de permission PR-01..11
  document_types.yaml          22 types de LiveDocs, attributs de document, plans types, cascade document → éléments
  tailoring.yaml               grille de cotation et seuils de classe, socle non négociable, profils A–D, 32 typologies
  project_topology.yaml        instances, groupes de projets, master → 6 archétypes → spécialisations
  coverage_scenarios.yaml      preuve de couverture par typologie (types, documents, traces, attributs)
  project_setup.yaml           provisioning : questionnaire (19 questions), règles de dérivation (D01–D14), habilitations
  regulatory_packs.yaml        packs réglementaires (FR, US, DE, UK, CA, AIEA, BPF, défense)
  import_export.yaml           profils ReqIF, règles d'analyse Word, gabarits Excel, connecteurs
  extension_policy.yaml        cœur gouverné vs extensions locales, incréments de déploiement (ADR-29)
  pilots/P-NUWARD-L1.yaml      fiche de provisioning du pilote NUWARD (réponses, tranche activée, critères)
tools/
  almmodel.py                  chargement (YAML 1.2) + validation de cohérence et de couverture (CI)
  model_checks.py              contrôles du provisioning, des packs, des échanges, des pilotes et des extensions
  generate_project.py          kit de configuration d'un projet (surcharges autorisées + dossier de provisioning)
  generate_polarion.py         génération de la configuration Polarion (.polarion/…) FR / EN
  generate_docs.py             génération des annexes A1–A11 (Markdown + Mermaid)
generated/polarion/{fr,en}/    configuration Polarion générée (249 fichiers XML par langue) + manifeste SIGNATURES_ET_SCRIPTS.md
generated/projects/<id>/       kit de chaque projet pilote : surcharges projet FR / EN + provisioning-record.md
docs/
  00_Synthese_et_note_de_cadrage.md
  partie1/                     cartographie contextuelle (organisation, projets, disciplines, réglementation)
  partie2/                     plan de recherche OSINT, décisions d'architecture (ADR-01..30)
  partie3/                     méthodologie, modèle, traçabilité, workflows, topologie, LiveDocs,
                               tableaux de bord, intégrations, infrastructure / validation, feuille de route, gouvernance (07–17)
  partie4/                     revue critique (18), robustesse (19), facteurs de succès (20),
                               organisation matricielle / provisioning / habilitations (21), import-export (22),
                               kit de déploiement et guide pas à pas (23), parcours d'onboarding (24),
                               stratégie de modèle 50 % / 150 % (25)
  generated/                   annexes générées A1–A11 (ne pas éditer)
  annexes/                     glossaire (B), sources OSINT (C), constructions Polarion à confirmer (D)
  GUIDE_DE_LECTURE.md          carte du dépôt : rôle de chaque fichier, ordres de lecture, dépendances
tests/                         tests de non-régression du modèle et des générateurs (unittest)
CHANGELOG.md                   historique des versions (v0.1 → v0.5)
requirements.txt               dépendance Python (PyYAML)
```

## Utilisation

Prérequis : Python 3.10+ et PyYAML (`pip install -r requirements.txt`).

```bash
python3 tools/almmodel.py                     # validation (doit afficher 0 erreur ; -v pour les informations)
python3 tools/generate_polarion.py --lang fr  # → generated/polarion/fr/.polarion/
python3 tools/generate_polarion.py --lang en  # → generated/polarion/en/.polarion/
python3 tools/generate_docs.py                # → docs/generated/
python3 tools/generate_project.py             # → generated/projects/<id>/ (kits des pilotes)
python3 -m unittest discover -s tests         # tests
```

La configuration générée suit l'arborescence `.polarion/` d'un dépôt Polarion :
- `tracker/fields/*-enum.xml`, `*-custom-fields.xml`, `*-status-enum.xml` ;
- `tracker/workflow/*-workflow.xml` ;
- `documents/fields`, `documents/workflow` ;
- `testing/configuration`.

Elle se déploie en configuration globale ou dans un gabarit de projet, après recette.

Certaines conditions de workflow reposent sur des scripts (`ScriptCondition` / `ScriptFunction`, JavaScript) : 17 scripts `fra-*.js`. Ils sont spécifiés au document `docs/partie3/10_Workflows_signatures_roles.md` § 4, priorisés au document `docs/partie4/23_Kit_deploiement_guide_pas_a_pas.md` § 3 et listés, avec les points de signature, dans le manifeste généré `generated/polarion/<lang>/SIGNATURES_ET_SCRIPTS.md`. Ils sont à développer et qualifier lors de la phase de fondations.

La configuration n'a pas encore été chargée dans une instance Polarion : les constructions XML à confirmer sur la version cible sont listées dans `docs/annexes/D_Formats_Polarion_a_verifier.md` (spike S1 du doc. 23).

## Gouvernance des évolutions

Toute modification passe par le modèle YAML. Le circuit est le suivant :
1. validation (CI) ;
2. régénération ;
3. revue (pull request) ;
4. recette ;
5. déploiement.

Un identifiant (type, attribut, option, rôle de lien) n'est jamais renommé ni supprimé : il est déprécié ou migré. Voir `docs/partie3/17_Gouvernance_conduite_changement.md`.
