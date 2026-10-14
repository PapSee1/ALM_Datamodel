# Plan directeur Polarion — Ingénierie système Framatome : synthèse et note de cadrage

> Version 0.3 (OSINT), octobre 2026 : revue critique, confrontation à une seconde analyse, robustesse du modèle démontrée sur 32 typologies (voir § 0). Établi **exclusivement à partir de sources ouvertes** (Annexe C) et de connaissances publiques des référentiels. Toute affirmation porte un niveau de confiance ([C] confirmé · [P] probable · [P\*] à revérifier · [H] hypothèse). Ce plan est destiné à être **confronté aux ateliers internes** (document 05) avant toute mise en production.

## 0. Nouveautés de la version 0.3

| Sujet | Apport | Document |
|---|---|---|
| Analyse critique | Forces, 15 écarts classés 🔴 / 🟡 / 🟢 et corrigés, verdict sur chaque proposition de la seconde analyse (retenue, adaptée, rejetée, à vérifier) | [18](partie3/18_Analyse_critique.md) |
| Robustesse | Critères R1–R9, rejeu de la v0.1 (198 erreurs → 0), tests par mutation, 4 défauts réels corrigés (dont les identifiants `yes` / `no` générés en `True` / `False`), limites de la preuve statique | [19](partie3/19_Robustesse_du_modele.md) |
| Couverture | 32 typologies (15 nouvelles), 261 traces de référence, 8 scénarios transverses, tous prouvés | [A9](generated/A9_couverture_typologies.md) |
| Facteurs de succès | 26 facteurs absents de la v0.1 : instances représentatives du personnel, RGPD, PPST, validation du système, arrêts de tranche, réversibilité, habilitations, fournisseurs, valeur | [20](partie3/20_Facteurs_de_succes_non_couverts.md) |
| Organisation matricielle et provisioning | Lots de travaux BU × UO, assistant de création (19 questions, 13 règles), master + 6 archétypes, signatures habilitées au choix du projet, projets sas | [21](partie3/21_Organisation_matricielle_provisioning_habilitations.md), [A10](generated/A10_provisioning_et_packs.md) |
| Import / export | 5 profils ReqIF, 11 règles d'analyse Word, 4 gabarits Excel, 12 connecteurs (Teamcenter et 3DEXPERIENCE, Capella et Cameo, calcul, bancs) | [22](partie3/22_Import_export_parsing_connecteurs.md), [A11](generated/A11_import_export.md) |
| Packs réglementaires | France, US (50.59, Part 21), Allemagne, UK (CAE obligatoire), Canada, AIEA, BPF, défense | [A10](generated/A10_provisioning_et_packs.md) |

## 1. Synthèse : les recommandations structurantes

1. **Architecture fédérée « hub & spoke »** (ADR-01) :
   - une configuration globale unique, générée depuis ce dépôt (*configuration as code*) ;
   - des projets bibliothèques (réglementaire, terminologie, agressions, V&V, gabarits) ;
   - des projets lignes de produits (EPR2, UK EPR, NUWARD, parc par palier, GV, combustible, plateformes C-C, outillages) ;
   - des projets de réalisation qui réutilisent par branchement de documents avec fusion 3-way ;
   - des projets conteneurs pour les affaires courtes (fortuits, modifications, recharges, outillages).
2. **Frontière claire avec le Core Model 3DEXPERIENCE** (SE / PLM), déployé publiquement chez Framatome (ADR-07) :
   - Polarion est maître des exigences, de la V&V, de la démonstration de sûreté, des écarts d'ingénierie et de la configuration documentaire ;
   - 3DEXPERIENCE est maître du produit (nomenclature, CAO) et de la fabrication ;
   - Capella est maître de l'architecture (ADR-08).
   - **C'est la décision la plus risquée du programme.**
3. **Un modèle de données nucléaire natif** :
   - 36 types de Work Items, 325 attributs distincts, 111 énumérations, 26 rôles de liens ;
   - 24 workflows de Work Items et 3 workflows documentaires ; 22 types de LiveDocs.
   - Les notions de l'arrêté INB y sont toutes représentées : **EIP, AIP, exigence définie, contrôle technique indépendant, écart**. Les classements y sont **multi-schémas** (parc, FA3, EPR2, UK, SSG-30, IEC 61226, US), ainsi que le statut ESPN, les classes K, SC, M, EE / E, les CFSI et le contrôle export.
4. **Un socle non négociable** (NN-01 à NN-08), appliqué à toutes les classes de projets, y compris aux fortuits express. Il est **outillé par des conditions de workflow bloquantes** :
   - indépendance auteur ≠ vérificateur ;
   - absence de liens suspects ;
   - classification ;
   - avis Sûreté conditionnel ;
   - signature électronique avec signification.
5. **Approche graduée (tailoring) en 4 classes** (A programme majeur → D express) :
   - une grille de cotation à 7 critères détermine la classe ;
   - chaque classe dispose de profils de types, de documents, de revues, de MBSE et de CCB ;
   - la classe D est réellement légère (14 types, 2 documents, workflow documentaire express) sans renoncer au socle ;
   - chacune des 32 typologies de projet est **prouvée** par un scénario de couverture exécuté en CI (doc. 19, annexe A9).
6. **Traçabilité aval → amont et suspicion maîtrisée** :
   - convention de direction compatible avec le comportement natif de Polarion ;
   - 20 règles de complétude (TR-01 à TR-20) ;
   - suspicion native en phase 1, filtrée par champ en phase 2 ;
   - analyse d'impact transitive (« cône d'impact ») pour le CCB.
7. **Documents de référence en GED** : LiveDocs signés R / V / A, baseline automatique et export PDF/A signé avec manifeste versé en GED (archive de référence, durée de vie des installations supérieure à 60 ans) (ADR-11).
8. **Échanges client par ReqIF aller-retour** :
   - le texte du client est verbatim et verrouillé ;
   - une position de conformité est portée par Framatome ;
   - des espaces de collaboration utilisent des licences REVIEWER (ADR-12).
9. **Multi-instance sur site** (ADR-03) :
   - instance standard UE ;
   - instance sensible et instance US, si l'analyse juridique et de sécurité les confirme ;
   - aucune donnée sensible ou classifiée sur l'instance standard (contrôle bloquant) ;
   - IA générative désactivée par défaut (ADR-17).
10. **L'outil est validé comme logiciel support d'AIP** (IQ / OQ / PQ fondés sur les risques). Les tests OQ sont dérivés des conditions bloquantes du modèle. L'intégrité des données suit les principes ALCOA+ (leçons du Creusot).
11. **Déploiement en 5 phases sur environ 34 mois** jusqu'à la fin de la vague 3 :
    - cadrage (avec 20 à 24 ateliers de validation des hypothèses OSINT) ;
    - fondations ;
    - **trois pilotes contrastés** (outillage, fortuits, C-C ou NUWARD) ;
    - industrialisation ;
    - vagues BI → Combustible + C-C → PCM + DTI.
12. **Gouvernance par une Design Authority ALM** :
    - CCB du modèle ;
    - identifiants jamais renommés ;
    - CI qui valide et régénère la configuration à chaque évolution ;
    - réseau de champions ;
    - support de niveaux 1 à 3.

13. **Organisation matricielle et provisioning outillé** (ADR-24, ADR-26) :
    - les UO réalisent des **lots de travaux** signés à l'accord et à la réception ; un tableau de bord par UO est disponible sans projet par UO ;
    - tout projet naît d'un **questionnaire** et de règles de dérivation : gabarit (master → archétype → spécialisation), classe, instance, packs, projet sas.
14. **Packs réglementaires et abstraction de filière** (ADR-25) : un modèle unique, des champs affichés ou masqués par cadre réglementaire, aucun vocabulaire REP français figé dans la structure.
15. **Signatures habilitées au choix du projet** (ADR-27) et **cloisonnement par projets sas** (ADR-28) : le Space n'est pas une frontière de sécurité.

## 2. Correspondance avec la demande

| Livrable demandé | Document(s) |
|---|---|
| **Partie 1.1** Organisation et périmètres (BU / BL / UO) | [01_Organisation_BU_BL_UO](partie1/01_Organisation_BU_BL_UO.md) |
| **Partie 1.2** Typologie des projets et cycles de vie | [02_Typologie_projets_cycles_de_vie](partie1/02_Typologie_projets_cycles_de_vie.md) |
| **Partie 1.3** Disciplines et interfaces | [03_Disciplines_et_interfaces](partie1/03_Disciplines_et_interfaces.md) |
| **Partie 1.4** Référentiels normatifs et réglementaires | [04_Referentiels_normatifs_reglementaires](partie1/04_Referentiels_normatifs_reglementaires.md) |
| **Partie 2** Plan de recherche et matrice d'acquisition | [05_Plan_de_recherche_OSINT](partie2/05_Plan_de_recherche_OSINT.md) |
| **Partie 2** Questions d'architecture à trancher | [06_Decisions_architecture_ADR](partie2/06_Decisions_architecture_ADR.md) |
| **Partie 3.1** Méthodologie IS et tailoring | [07_Methodologie_IS_et_tailoring](partie3/07_Methodologie_IS_et_tailoring.md) |
| **Partie 3.2** Modèle de données : Work Items, attributs | [08_Modele_de_donnees](partie3/08_Modele_de_donnees.md) + Annexes [A1](generated/A1_types_et_attributs.md), [A2](generated/A2_enumerations.md), [A8](generated/A8_metamodele.md) |
| **Partie 3.2** Liens et suspicion | [09_Tracabilite_et_suspicion](partie3/09_Tracabilite_et_suspicion.md) + [A3](generated/A3_liens_et_tracabilite.md) |
| **Partie 3.2** Workflows, signatures, rôles | [10_Workflows_signatures_roles](partie3/10_Workflows_signatures_roles.md) + [A4](generated/A4_workflows.md), [A6](generated/A6_roles_permissions.md) |
| **Partie 3.3** LiveDocs et gabarits | [12_LiveDocs_gabarits](partie3/12_LiveDocs_gabarits.md) + [A5](generated/A5_documents.md) |
| **Partie 3.3** Tableaux de bord et LiveReports | [13_Dashboards_LiveReports_KPI](partie3/13_Dashboards_LiveReports_KPI.md) |
| Compléments (au-delà du texte reçu, tronqué) | [11 Topologie / réutilisation / variantes](partie3/11_Topologie_reutilisation_variantes.md), [14 Intégrations](partie3/14_Integrations_et_echanges.md), [15 Infrastructure / sécurité / validation](partie3/15_Infrastructure_securite_validation.md), [16 Feuille de route](partie3/16_Feuille_de_route_deploiement.md), [17 Gouvernance](partie3/17_Gouvernance_conduite_changement.md), [A7 Tailoring](generated/A7_tailoring.md) |
| **Partie 3** Import / export et interopérabilité (ReqIF, Word / Excel, parsing, PLM, MBSE, calcul) | [14 Intégrations](partie3/14_Integrations_et_echanges.md) + [22 Import / export, parsing, connecteurs](partie3/22_Import_export_parsing_connecteurs.md) + [A11](generated/A11_import_export.md) |
| **Partie 3** Feuille de route A-Z (gouvernance, Master Template vs gabarits par typologie, conduite du changement, pilote, industrialisation) | [16 Feuille de route](partie3/16_Feuille_de_route_deploiement.md), [17 Gouvernance](partie3/17_Gouvernance_conduite_changement.md), [21 Provisioning et gabarits](partie3/21_Organisation_matricielle_provisioning_habilitations.md), [20 Facteurs de succès](partie3/20_Facteurs_de_succes_non_couverts.md) |
| Revue critique et robustesse (demande de suivi) | [18 Analyse critique](partie3/18_Analyse_critique.md), [19 Robustesse](partie3/19_Robustesse_du_modele.md), [A9 Couverture](generated/A9_couverture_typologies.md) |
| Configuration Polarion exécutable | `model/*.yaml` → `generated/polarion/{fr,en}/.polarion/` (247 fichiers XML par langue) |

> **Note.** Le texte de la demande initiale s'interrompait au § 3.3 (« gestion des … »). La fin, retrouvée dans la conversation fournie ensuite, demandait l'import / export avec règles de parsing et connecteurs, puis la feuille de route A-Z avec Master Template et gabarits par typologie. Ces deux points sont traités en v0.3 (docs 21 et 22, annexes A10 et A11). L'écart est analysé au doc. 18 § 3.

## 3. Hypothèses de cadrage

| # | Hypothèse | Conf. |
|---|---|---|
| H1 | Déploiement greenfield : aucune instance Polarion existante chez Framatome ; d'éventuels référentiels d'exigences existants (Word, Excel, outils) sont à inventorier | Demande + NT |
| H2 | 3DEXPERIENCE (Core Model SE / PLM) et Capella sont déployés ou en cours de déploiement et restent en place | C |
| H3 | La GED d'entreprise reste le système d'archivage de référence | H |
| H4 | La version cible de Polarion est 2606 (ou la suivante au lancement) | C (versions) |
| H5 | L'hébergement sur site est privilégié pour les données d'ingénierie nucléaire | H |
| H6 | La langue de travail est bilingue FR / EN (+ DE pour Framatome GmbH) | P |

## 4. Mode d'emploi du dépôt

```bash
python3 tools/almmodel.py                     # valide la cohérence du modèle (0 erreur attendu)
python3 tools/generate_polarion.py --lang fr  # configuration Polarion (libellés FR)
python3 tools/generate_polarion.py --lang en  # configuration Polarion (libellés EN)
python3 tools/generate_docs.py                # annexes A1-A11 (catalogues exhaustifs)
```

Toute évolution du modèle suit le processus du document 17 § 2 (CCB du modèle, demande de fusion, CI).
