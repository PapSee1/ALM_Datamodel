# Guide de lecture et carte du dépôt

> **Commencez ici.** Ce dépôt contient à la fois un *plan directeur* (des documents à lire) et un *modèle de données « as code »* (des fichiers que des outils vérifient et transforment en configuration Polarion). Cette page explique ce que contient chaque fichier, dans quel ordre le lire, lequel sert aux ateliers et lequel sert à configurer l'outil.
>
> Public visé par tout le dépôt : un ingénieur avec une formation d'ingénieur mais **nouveau dans le nucléaire et dans Polarion**. Les sigles sont expliqués à leur première apparition dans chaque document, et regroupés dans le [glossaire](annexes/B_Glossaire.md).

## 1. Ce que contient le dépôt, en une image

```
                 LIRE                                  FAIRE
   ┌──────────────────────────┐          ┌────────────────────────────────┐
   │ docs/  (le plan)         │          │ model/*.yaml  (la source)      │
   │  Partie 1 contexte       │  décrit  │   types, attributs, liens,     │
   │  Partie 2 recherche, ADR │ ───────▶ │   workflows, documents, règles │
   │  Partie 3 conception     │          └──────────────┬─────────────────┘
   │  Partie 4 mise en œuvre  │                         │ tools/almmodel.py (vérifie)
   │  Annexes A (générées),   │ ◀────────┐              ▼
   │          B glossaire,    │  produit │ tools/generate_*.py (transforme)
   │          C sources       │          │              │
   └──────────────────────────┘          │              ▼
                                         │ generated/polarion/{fr,en}/  configuration Polarion (cœur)
                                         └ generated/projects/<pilote>/ configuration d'un projet + dossier
```

Règle de base : **on ne modifie jamais un fichier généré à la main**. On modifie le modèle (`model/`), on vérifie (`tools/almmodel.py`), on régénère. La CI (intégration continue, `.github/workflows/validate.yml`) refuse toute incohérence.

## 2. Par où commencer

| Vous avez… | Lisez |
|---|---|
| **1 heure** | [00 Synthèse](00_Synthese_et_note_de_cadrage.md) § 0 et § 1, puis cette page |
| **une demi-journée** | + [01 Organisation](partie1/01_Organisation_BU_BL_UO.md), [02 Typologie des projets](partie1/02_Typologie_projets_cycles_de_vie.md) § 0 et G, [07 Méthodologie et tailoring](partie3/07_Methodologie_IS_et_tailoring.md), [08 Modèle de données](partie3/08_Modele_de_donnees.md) |
| **avant d'animer les ateliers** | + [24 Parcours d'onboarding](partie4/24_Parcours_onboarding_ateliers.md) (il contient l'ordre de lecture **par atelier**), [25 Stratégie de modèle](partie4/25_Strategie_coeur_50_vs_150.md), [18 Analyse critique](partie4/18_Analyse_critique.md) |
| **avant de configurer Polarion** | + [23 Kit de déploiement](partie4/23_Kit_deploiement_guide_pas_a_pas.md), [10 Workflows](partie3/10_Workflows_signatures_roles.md), [README](../README.md) (commandes), annexes A1–A6 |
| **dans cinq ans, pour transposer vers un autre outil** | § 5 de cette page (ce qui dépend de Polarion et ce qui n'en dépend pas), puis le modèle `model/` |

Un ordre de lecture **par profil** (responsable IS, SE Referent, ingénieur configuration, Sûreté, Qualité, DSI, chef de projet) figure au [doc. 24 § 2](partie4/24_Parcours_onboarding_ateliers.md).

## 3. Les documents (`docs/`)

Légende « Usage » : 🎓 ateliers d'onboarding · 🔧 configuration de l'outil · 📋 pilotage du programme · 📚 référence.

### Entrée

| Document | Contenu | Usage | À lire après |
|---|---|---|---|
| [GUIDE_DE_LECTURE](GUIDE_DE_LECTURE.md) (cette page) | Carte du dépôt, ordres de lecture, dépendances | 🎓 📚 | — |
| [00 Synthèse et note de cadrage](00_Synthese_et_note_de_cadrage.md) | Nouveautés par version, recommandations structurantes, correspondance avec la demande, hypothèses | 🎓 📋 | — |

### Partie 1 — Comprendre le contexte (ce que Framatome fait, et sous quelles règles)

| Document | Contenu | Usage | À lire après |
|---|---|---|---|
| [01 Organisation BU / BL / UO](partie1/01_Organisation_BU_BL_UO.md) | Business Units, Business Lines, unités opérationnelles, filiales, écosystème ; ce que cela impose au modèle | 🎓 📚 | 00 |
| [02 Typologie des projets](partie1/02_Typologie_projets_cycles_de_vie.md) | Les 32 types de projets (grand réacteur, SMR, RGV, réexamen, fortuit, outillage, combustible, C-C, composants…) et leurs cycles de vie | 🎓 📚 | 01 |
| [03 Disciplines et interfaces](partie1/03_Disciplines_et_interfaces.md) | Les disciplines d'ingénierie et la gestion des interfaces (ICD) | 🎓 📚 | 02 |
| [04 Référentiels normatifs et réglementaires](partie1/04_Referentiels_normatifs_reglementaires.md) | Arrêté INB, ESPN, codes AFCEN, IEC, AIEA, NRC… et leur effet sur le modèle | 🎓 📚 | 02 |

### Partie 2 — Ce qui reste à vérifier et les décisions d'architecture

| Document | Contenu | Usage | À lire après |
|---|---|---|---|
| [05 Plan de recherche OSINT](partie2/05_Plan_de_recherche_OSINT.md) | Registre des hypothèses à confirmer en atelier (questions Q-xxx) et sources à consulter | 📋 🎓 | 01–04 |
| [06 Décisions d'architecture (ADR)](partie2/06_Decisions_architecture_ADR.md) | 30 décisions (topologie, instances, PLM / MBSE, classement, signatures, licences, stratégie de modèle, cascade document → éléments…), chacune avec options, recommandation, conséquences | 🎓 🔧 📋 | 07–11 |

### Partie 3 — La conception (le modèle et son emploi)

| Document | Contenu | Usage | À lire après |
|---|---|---|---|
| [07 Méthodologie IS et tailoring](partie3/07_Methodologie_IS_et_tailoring.md) | Cycle en V, RFLP, approche graduée (classes A–D), socle non négociable NN-01..08 | 🎓 | 02 |
| [08 Modèle de données](partie3/08_Modele_de_donnees.md) | Principes P1–P9 (dont P7 : état de soumission et champs requis), familles de types, attributs, concepts nucléaires (EIP, AIP, exigence définie, classements) | 🎓 🔧 | 07 |
| [09 Traçabilité et suspicion](partie3/09_Tracabilite_et_suspicion.md) | Rôles de liens, sens des liens, règles de complétude TR-01..20, liens suspects, analyse d'impact | 🎓 🔧 | 08 |
| [10 Workflows, signatures, rôles](partie3/10_Workflows_signatures_roles.md) | Cycles de vie des éléments et des documents, contrôle technique, signatures électroniques (portées par le LiveDoc pour les exigences), cascade document → éléments, les 17 scripts nécessaires | 🎓 🔧 | 09 |
| [11 Topologie, réutilisation, variantes](partie3/11_Topologie_reutilisation_variantes.md) | Instances, projets, bibliothèques, lignes de produits, gabarits, variantes, baselines | 🔧 🎓 | 06, 08 |
| [12 LiveDocs et gabarits](partie3/12_LiveDocs_gabarits.md) | Les documents vivants (STB, ST, dossier de sûreté, procédures…) et leurs plans types | 🔧 | 10 |
| [13 Tableaux de bord, LiveReports, KPI](partie3/13_Dashboards_LiveReports_KPI.md) | Catalogue des indicateurs (K-xxx), tableaux de bord par rôle, contrôle qualité des exigences | 🔧 📋 | 09 |
| [14 Intégrations et échanges](partie3/14_Integrations_et_echanges.md) | Fiches d'intégration I-01..I-11 (client, Capella, PLM, MES, GED, ERP, C-C, code, annuaire, calcul, bancs) | 🔧 | 11 |
| [15 Infrastructure, sécurité, validation](partie3/15_Infrastructure_securite_validation.md) | Environnements, sauvegardes, sécurité, validation de l'outil (IQ / OQ / PQ), intégrité des données | 🔧 📋 | 06 |
| [16 Feuille de route](partie3/16_Feuille_de_route_deploiement.md) | Phases, jalons, formation, risques, coûts du programme | 📋 | 15 |
| [17 Gouvernance et conduite du changement](partie3/17_Gouvernance_conduite_changement.md) | Design Authority, CCB du modèle, processus d'évolution, support, champions | 📋 🎓 | 16 |

### Partie 4 — Revue, mise en œuvre et onboarding (ajouts v0.3 / v0.4, regroupés en v0.5)

| Document | Contenu | Usage | À lire après |
|---|---|---|---|
| [18 Analyse critique](partie4/18_Analyse_critique.md) | Forces et écarts du plan, verdict sur chaque proposition d'une seconde analyse, matrice des normes | 🎓 📋 | 00 |
| [19 Robustesse du modèle](partie4/19_Robustesse_du_modele.md) | Comment on prouve que le modèle couvre tous les projets ; défauts trouvés et corrigés ; limites | 🎓 🔧 | 08, 09 |
| [20 Facteurs de succès non couverts](partie4/20_Facteurs_de_succes_non_couverts.md) | 26 facteurs sociaux, juridiques, de sécurité, d'exploitation et humains (CSE, RGPD, validation, arrêts…) | 📋 | 16 |
| [21 Organisation matricielle, provisioning, habilitations](partie4/21_Organisation_matricielle_provisioning_habilitations.md) | Lots de travaux BU × UO, création des projets par questionnaire, gabarits master / archétypes, signatures habilitées, projets sas | 🎓 🔧 | 11 |
| [22 Import / export, parsing, connecteurs](partie4/22_Import_export_parsing_connecteurs.md) | Profils ReqIF, règles d'analyse Word, aller-retour Excel, connecteurs PLM / MBSE / calcul | 🔧 | 14 |
| [23 Kit de déploiement et guide pas à pas](partie4/23_Kit_deploiement_guide_pas_a_pas.md) | Ce qui est prêt, ce qui reste à construire, effort, étapes S0–S13 jusqu'au pilote NUWARD | 🔧 📋 | 10, 21 |
| [24 Parcours d'onboarding](partie4/24_Parcours_onboarding_ateliers.md) | 12 ateliers pour l'équipe cœur, lecture par profil, compétences visées, appui éditeur / intégrateur | 🎓 📋 | 00 |
| [25 Stratégie de modèle 50 % / 150 %](partie4/25_Strategie_coeur_50_vs_150.md) | Cœur gouverné, exposition par incréments, extensions locales, promotion (ADR-29) | 🎓 🔧 | 17 |

### Annexes

| Annexe | Contenu | Générée ? |
|---|---|---|
| [A1 Types et attributs](generated/A1_types_et_attributs.md) | Catalogue des 36 types et de leurs attributs | oui |
| [A2 Énumérations](generated/A2_enumerations.md) | Les 112 listes de valeurs | oui |
| [A3 Liens et traçabilité](generated/A3_liens_et_tracabilite.md) | Les 26 rôles de liens, règles, suspicion, règles TR | oui |
| [A4 Workflows](generated/A4_workflows.md) | Tous les cycles de vie, transition par transition | oui |
| [A5 Documents](generated/A5_documents.md) | Les 22 types de LiveDocs et leurs plans types | oui |
| [A6 Rôles et permissions](generated/A6_roles_permissions.md) | Rôles, licences, droits, règles de permission | oui |
| [A7 Tailoring](generated/A7_tailoring.md) | Grille de cotation, profils par classe, typologie → gabarit, héritage des gabarits | oui |
| [A8 Méta-modèle](generated/A8_metamodele.md) | Vue graphique des types et de leurs liens | oui |
| [A9 Couverture des typologies](generated/A9_couverture_typologies.md) | Preuve que chaque type de projet est couvert | oui |
| [A10 Provisioning et packs](generated/A10_provisioning_et_packs.md) | Questionnaire de création, règles de dérivation, packs réglementaires | oui |
| [A11 Import / export](generated/A11_import_export.md) | Profils ReqIF, règles Word, gabarits Excel, connecteurs | oui |
| [B Glossaire](annexes/B_Glossaire.md) | Tous les sigles et termes, en français, avec l'anglais | non |
| [C Sources OSINT](annexes/C_Sources_OSINT.md) | Les sources publiques utilisées et leur fiabilité (registre des sources, campagne d'octobre 2026) | non |
| [D Constructions Polarion à confirmer](annexes/D_Formats_Polarion_a_verifier.md) | Les 14 constructions XML (PF-01..PF-14) que le spike S1 doit confirmer sur la version cible, avec le repli si elles sont infirmées | non |

Les annexes générées sont **toujours à jour** avec le modèle (la CI le vérifie) : en cas de doute entre un document rédigé et une annexe générée, l'annexe a raison.

## 4. Le modèle (`model/`) et les outils (`tools/`)

### Les fichiers du modèle

| Fichier | Contient | Lu principalement par | Dépend de |
|---|---|---|---|
| `enumerations.yaml` | Les listes de valeurs (classements de sûreté, disciplines, paliers, UO, typologies…). Certaines sont de **portée projet** (`scope: project`), c'est-à-dire adaptées dans chaque projet. | tous | — |
| `work_item_types.yaml` | Les 36 types d'éléments (exigence, fonction, composant, cas de vérification, écart…), leurs familles, leurs attributs (avec `requiredAt` : à quelle étape un champ devient obligatoire) et les jeux d'attributs partagés (`fieldSets`) | 08, A1 | enumerations |
| `link_roles.yaml` | Les 26 rôles de liens, qui peut être lié à quoi, la politique de suspicion, les règles de complétude TR-xx | 09, A3 | work_item_types |
| `workflows.yaml` | Les cycles de vie (états avec catégorie, état de soumission `submitState`, transitions, rôles, champs requis, conditions, signatures) des éléments et des documents ; le catalogue des conditions / fonctions et leur réalisation Polarion | 10, A4 | work_item_types, roles |
| `roles.yaml` | Rôles projet et globaux, licences, droits, règles de permission PR-xx | 10, A6 | — |
| `document_types.yaml` | Les 22 types de documents, leurs attributs, les types d'éléments admis, les plans types, et la cascade document → éléments (`primaryType`, `cascadeTypes`, `approvalGate`) | 12, A5 | work_item_types, workflows |
| `tailoring.yaml` | Grille de cotation et seuils de classe (`thresholds`, lus par le provisioning), socle non négociable, profils des classes A–D, profil par défaut de chaque typologie | 07, A7 | work_item_types, document_types, project_topology |
| `project_topology.yaml` | Instances, groupes de projets, bibliothèques, lignes de produits, gabarits (master → archétypes → spécialisations), conventions de nommage | 11, 21 | — |
| `coverage_scenarios.yaml` | Pour chaque typologie : ce dont elle a besoin (types, documents, traces, attributs, valeurs). C'est la **preuve de couverture** vérifiée par la CI | 19, A9 | tout ce qui précède |
| `project_setup.yaml` | Questionnaire de création de projet, règles de dérivation, processus de provisioning | 21, A10 | enumerations, topology, tailoring |
| `regulatory_packs.yaml` | Ce qu'active chaque cadre réglementaire (France, US, Allemagne, UK, Canada, AIEA, BPF, défense) | 21, A10 | work_item_types, link_roles |
| `import_export.yaml` | Profils ReqIF, règles d'analyse Word, gabarits Excel, connecteurs | 22, A11 | work_item_types |
| `extension_policy.yaml` | Ce qui relève du cœur, ce qu'un projet peut ajouter localement, les incréments de déploiement | 25 | tout |
| `pilots/P-NUWARD-L1.yaml` | Fiche de provisioning du pilote NUWARD : réponses, tranche activée, champs locaux `x_` et valeurs d'énumération projet, critères de succès | 23 | project_setup, extension_policy |

### Les outils

| Outil | Rôle | Commande |
|---|---|---|
| `tools/almmodel.py` | Charge le modèle et **vérifie sa cohérence** (références, workflows, profils, couverture…). 0 erreur attendu. | `python3 tools/almmodel.py` (`-v` pour le détail) |
| `tools/model_checks.py` | Contrôles complémentaires : provisioning, packs, échanges, pilotes, extensions. Dérive aussi les paramètres d'un projet à partir de ses réponses. | appelé par `almmodel.py` |
| `tools/generate_polarion.py` | Produit la **configuration Polarion du cœur** (249 fichiers XML par langue) et le manifeste `SIGNATURES_ET_SCRIPTS.md` (scripts attendus, points de signature, constructions à confirmer) | `python3 tools/generate_polarion.py --lang fr` |
| `tools/generate_project.py` | Produit le **kit d'un projet pilote** : surcharges projet autorisées + dossier de provisioning | `python3 tools/generate_project.py` |
| `tools/generate_docs.py` | Produit les annexes A1–A11 | `python3 tools/generate_docs.py` |
| `tests/test_model.py` | 46 tests de non-régression : chaque contrôle est protégé par un test qui casse volontairement le modèle ; les générateurs sont testés sur leur sortie | `python3 -m unittest discover -s tests` |
| `.github/workflows/validate.yml` | La CI : validation, tests, régénération, et refus si un fichier généré n'est pas à jour | automatique à chaque poussée |

### Les sorties générées

| Dossier | Contenu | Où ça va |
|---|---|---|
| `generated/polarion/fr/.polarion/`, `generated/polarion/en/.polarion/` | Configuration **globale** Polarion : types, champs, énumérations, statuts, rôles de liens, workflows, types de documents, statuts et résultats de Test Runs | Dépôt de configuration de l'instance (doc. 23 § 4) |
| `generated/polarion/{fr,en}/SIGNATURES_ET_SCRIPTS.md` | Manifeste : scripts appelés (et où), points de signature électronique, constructions à confirmer au spike S1 | Équipe de configuration, spike S1 |
| `generated/projects/P-NUWARD-L1/{fr,en}/.polarion/` | Surcharges **projet** du pilote (sous-ensemble de types et de documents, énumérations projet, champs masqués par les packs, champs locaux `x_`) | Dossier `.polarion` du projet |
| `generated/projects/P-NUWARD-L1/provisioning-record.md` | Dossier de provisioning lisible : réponses, paramètres dérivés, rôles à pourvoir, liste de contrôle | Revue de création du projet |
| `docs/generated/` | Annexes A1–A11 | Lecture |

## 5. Ce qui dépend de Polarion et ce qui n'en dépend pas (horizon cinq ans)

Pour transposer ce travail vers une nouvelle version de Polarion ou vers un autre outil, il faut savoir ce qui est **conceptuel** (réutilisable tel quel) et ce qui est **spécifique à l'outil**.

| Couche | Fichiers / documents | Dépendance à Polarion |
|---|---|---|
| **Concepts métier** : typologies, disciplines, réglementation, approche graduée, socle non négociable, facteurs de succès | Partie 1, doc. 07, 18, 19, 20, `tailoring.yaml`, `coverage_scenarios.yaml`, `regulatory_packs.yaml` (hors `showFields`) | **Aucune.** Réutilisable avec tout outil. |
| **Modèle logique** : types, attributs, rôles de liens, cycles de vie, documents, règles | `work_item_types.yaml`, `link_roles.yaml`, `workflows.yaml` (états, transitions, conditions en vocabulaire neutre), `document_types.yaml`, `roles.yaml`, doc. 08, 09, 10, 12 | **Faible.** Le vocabulaire est neutre ; seules les clés `polarion:` du catalogue de conditions / fonctions et quelques notes (« natif », « rôle système ») sont propres à l'outil. |
| **Organisation de l'outil** : instances, projets, gabarits, extensions, provisioning | `project_topology.yaml`, `extension_policy.yaml`, `project_setup.yaml`, doc. 11, 21, 25 | **Moyenne.** Les notions de projet, Space, gabarit, surcharge sont celles de Polarion ; les décisions (cœur gouverné, archétypes, sas) se transposent. |
| **Réalisation** : configuration XML, scripts, formulaires, tableaux de bord, connecteurs | `tools/generate_polarion.py`, `tools/generate_project.py`, `generated/`, `import_export.yaml` (mécanismes), doc. 13 § 5–6, 14, 22, 23 | **Forte.** À refaire pour un autre outil ; à vérifier à chaque montée de version de Polarion (doc. 23 § 4). |

Chaque document porte, sous son titre, son niveau de dépendance à l'outil (**faible**, **moyenne**, **forte**) et, pour un document mixte, les sections concernées. Les mentions de version de Polarion (par ex. « 2404+ ») signalent une fonctionnalité qui dépend de la version : elles sont à revérifier lors d'une transposition, comme les constructions XML de l'[annexe D](annexes/D_Formats_Polarion_a_verifier.md).

Pour transposer vers un autre outil : garder les couches 1 et 2 telles quelles (le modèle YAML est la spécification), réécrire les générateurs (`tools/generate_*.py`) vers le format du nouvel outil, puis refaire les scripts, tableaux de bord et connecteurs. Les tests de la couche « modèle » restent valables.

## 6. Conventions à connaître

- **Niveaux de confiance** sur les faits issus de sources ouvertes : **[C]** confirmé par une source publique fiable · **[P]** probable · **[P\*]** à revérifier · **[H]** hypothèse de travail. Les énumérations portent aussi `confidence: H` ou `P` quand leurs valeurs sont des amorces à remplacer en atelier.
- **Identifiants** (types, champs, valeurs, rôles) : en anglais, en `camelCase`, **jamais renommés** une fois publiés (on déprécie, on ne renomme pas). Les libellés sont en français et en anglais.
- **Numérotation des règles** : NN-xx socle non négociable · P1–P9 principes du modèle · TR-xx traçabilité · PR-xx permissions · ADR-xx décisions · F-xx facteurs de succès (doc. 20) · PF-xx constructions Polarion à confirmer (annexe D) · GAP-x écarts · Q-xxx questions ouvertes · K-xxx indicateurs · I-xx fiches d'intégration · S0–S13 étapes de construction · Q01–Q19 questions et D01–D14 (+ D06bis) règles de provisioning · INC-x incréments · SC-xx critères de succès du pilote · XC-xx contrôles d'échange.
- **Versions** du plan : voir [CHANGELOG](../CHANGELOG.md). Chaque document indique sous son titre la version du plan à laquelle il a été relu en entier.
- **Sigles** : expliqués à leur première occurrence dans chaque document (les documents se lisent indépendamment) et réunis dans le [glossaire](annexes/B_Glossaire.md).
- **Langue** : documents en français ; identifiants techniques en anglais ; la configuration est générée dans les deux langues.

## 7. Comment faire évoluer le dépôt

1. Modifier le modèle (`model/`) ou un document rédigé — jamais un fichier généré.
2. Lancer `python3 tools/almmodel.py` (0 erreur) puis les tests.
3. Régénérer : `generate_polarion.py --lang fr` et `--lang en`, `generate_docs.py`, `generate_project.py`.
4. Soumettre une demande de fusion ; la CI rejoue tout.
5. Décision du CCB du modèle pour toute évolution du cœur (doc. 17 § 2, doc. 25 § 5).
