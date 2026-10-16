# Plan directeur Polarion — Ingénierie système Framatome : synthèse et note de cadrage

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **moyenne** (§ 1, recommandations 9 à 12, et § 3 spécifiques à Polarion ; le reste est indépendant de l'outil) · Historique : [CHANGELOG](../CHANGELOG.md) · Carte du dépôt : [guide de lecture](GUIDE_DE_LECTURE.md).*

> **En bref**
> - **À quoi sert ce document.** C'est la porte d'entrée du plan directeur. Il résume en quinze recommandations comment déployer **Polarion** (l'outil **ALM** de Siemens — *Application Lifecycle Management*, gestion du cycle de vie des exigences, des essais et des documents d'ingénierie) pour l'ingénierie système (**IS**) de Framatome, et il indique dans quel document chaque sujet est détaillé (§ 2).
> - **Qui le lit.** Tout nouvel arrivant dans l'équipe ALM, les membres de la **Design Authority** (l'instance qui arbitre l'architecture et les évolutions du modèle) et les participants aux ateliers de validation.
> - **À lire avant.** Rien. Lire ensuite le [guide de lecture](GUIDE_DE_LECTURE.md) (carte du dépôt) et le [glossaire](annexes/B_Glossaire.md).
> - **Ce qu'il faut savoir.** Le plan est établi **exclusivement à partir de sources ouvertes** (**OSINT**, *open source intelligence* ; annexe C) et de connaissances publiques des référentiels, sans aucune donnée interne. Il est destiné à être **confronté aux ateliers internes** (document 05) avant toute mise en production.

> Apports successifs : v0.3, revue critique, confrontation à une seconde analyse, robustesse du modèle démontrée sur 32 typologies ; v0.4, kit de déploiement, kit pilote NUWARD, parcours d'onboarding, stratégie de modèle ; v0.5, revue de cohérence, organisation vérifiée en sources ouvertes, lisibilité (voir § 0). Toute affirmation porte un niveau de confiance : **[C]** confirmé · **[P]** probable · **[P\*]** à revérifier · **[H]** hypothèse de modélisation · **[NT]** non trouvé · une double cote (C/P) mêle des faits de niveaux différents.

## 0. Nouveautés des versions 0.3, 0.4 et 0.5

| Sujet | Apport | Document |
|---|---|---|
| Analyse critique | Forces, 15 écarts classés 🔴 / 🟡 / 🟢 et corrigés, verdict sur chaque proposition de la seconde analyse (retenue, adaptée, rejetée, à vérifier) | [18](partie4/18_Analyse_critique.md) |
| Robustesse | Critères R1–R9, rejeu de la v0.1 (198 erreurs → 0), tests par mutation (on altère volontairement le modèle pour vérifier que le validateur le détecte), 4 défauts réels corrigés (dont les identifiants `yes` / `no` générés en `True` / `False`), limites de la preuve statique | [19](partie4/19_Robustesse_du_modele.md) |
| Couverture | 32 typologies (15 nouvelles), 261 traces de référence, 8 scénarios transverses, tous prouvés | [A9](generated/A9_couverture_typologies.md) |
| Facteurs de succès | 26 facteurs absents de la v0.1 : instances représentatives du personnel, RGPD (protection des données personnelles), PPST (protection du potentiel scientifique et technique), validation du système, arrêts de tranche, réversibilité, habilitations, fournisseurs, valeur | [20](partie4/20_Facteurs_de_succes_non_couverts.md) |
| Organisation matricielle et provisioning | Lots de travaux BU × UO (*Business Unit* × unité opérationnelle), assistant de création de projet (19 questions, 15 règles de dérivation D01–D14 + D06bis), gabarit master + 6 archétypes, signatures habilitées au choix du projet, projets sas (projets d'échange cloisonnés `EXT-*`) | [21](partie4/21_Organisation_matricielle_provisioning_habilitations.md), [A10](generated/A10_provisioning_et_packs.md) |
| Import / export | 5 profils ReqIF (format standard d'échange d'exigences), 11 règles d'analyse Word, 4 gabarits Excel, 12 connecteurs (PLM Teamcenter et 3DEXPERIENCE, MBSE Capella et Cameo, calcul, bancs) | [22](partie4/22_Import_export_parsing_connecteurs.md), [A11](generated/A11_import_export.md) |
| Packs réglementaires | 8 packs : France, US (10 CFR 50.59, Part 21), Allemagne, UK (argumentaire CAE — *claims, arguments, evidence* — obligatoire), Canada, AIEA, BPF (bonnes pratiques de fabrication, isotopes médicaux), défense | [A10](generated/A10_provisioning_et_packs.md) |
| **v0.4 — Kit de déploiement** | Inventaire honnête de ce qui est prêt et de ce qui reste à construire (scripts, formulaires, gabarits, tableaux de bord, permissions, validation) ; effort restant chiffré en ordres de grandeur ; guide pas à pas S0–S13 jusqu'au pilote | [23](partie4/23_Kit_deploiement_guide_pas_a_pas.md) |
| **v0.4 — Kit pilote NUWARD** | Fiche de provisioning (création outillée du projet), paramètres dérivés, surcharges projet générées (28 types sur 36, 9 documents), rôles à pourvoir, critères de succès | `model/pilots/P-NUWARD-L1.yaml`, [dossier de provisioning](../generated/projects/P-NUWARD-L1/provisioning-record.md) |
| **v0.4 — Onboarding** | Parcours de 12 ateliers (Comprendre, Décider, Construire), guide de lecture par profil, compétences visées, appui Siemens / intégrateur sans perte de maîtrise | [24](partie4/24_Parcours_onboarding_ateliers.md) |
| **v0.4 — Stratégie 50 % / 150 %** | Arbitrage : modèle conçu à 150 % (sur-ensemble de tous les besoins), cœur gouverné, exposé par incréments, extensions locales `x_`, promotion par le CCB (ADR-29) | [25](partie4/25_Strategie_coeur_50_vs_150.md) |
| **v0.5 — Revue de cohérence, organisation OSINT, lisibilité** | Revue complète du dépôt (modèle, outils, tests, documents) ; docs 18–25 regroupés en partie 4 ; doc. 01 refondu depuis une campagne OSINT (≈ 28 Business Lines et ≈ 43 unités opérationnelles, chacune cotée) ; état de soumission et champs requis à la soumission dans chaque workflow ; cascade document → éléments rendue explicite (ADR-30) ; signatures générées et manifeste `generated/polarion/<lang>/SIGNATURES_ET_SCRIPTS.md` ; annexe D des constructions Polarion à vérifier ; guide de lecture ; glossaire complété ; journal des versions | [Guide de lecture](GUIDE_DE_LECTURE.md), [CHANGELOG](../CHANGELOG.md), [01](partie1/01_Organisation_BU_BL_UO.md), [06](partie2/06_Decisions_architecture_ADR.md), [D](annexes/D_Formats_Polarion_a_verifier.md) |

## 1. Synthèse : les recommandations structurantes

1. **Architecture fédérée « hub & spoke »** (en étoile : un centre partagé, des projets qui s'y rattachent ; ADR-01) :
   - une configuration globale unique, générée depuis ce dépôt (*configuration as code* : la configuration est décrite dans des fichiers versionnés, puis produite par des outils) ;
   - des projets bibliothèques (réglementaire, terminologie, agressions, V&V — vérification et validation —, gabarits) ;
   - des projets lignes de produits (EPR2, UK EPR, NUWARD, parc par palier, GV — générateurs de vapeur —, combustible, plateformes de contrôle-commande (C-C), outillages) ;
   - des projets de réalisation qui réutilisent par branchement de documents avec fusion 3-way (fusion à trois sources : version d'origine, copie du projet, bibliothèque modifiée) ;
   - des projets conteneurs pour les affaires courtes (fortuits — aléas découverts en arrêt de tranche —, modifications, recharges, outillages).
2. **Frontière claire avec le Core Model 3DEXPERIENCE** (la plateforme PLM — *Product Lifecycle Management*, gestion du cycle de vie du produit — de Dassault Systèmes, déployée publiquement chez Framatome pour l'ingénierie système et le PLM ; ADR-07) :
   - Polarion est maître des exigences, de la V&V, de la démonstration de sûreté, des écarts d'ingénierie et de la configuration documentaire ;
   - 3DEXPERIENCE est maître du produit (nomenclature, CAO — conception assistée par ordinateur) et de la fabrication ;
   - Capella (atelier MBSE open source — *Model-Based Systems Engineering*, ingénierie système fondée sur les modèles) est maître de l'architecture (ADR-08).
   - **C'est la décision la plus risquée du programme.**
3. **Un modèle de données nucléaire natif** :
   - 36 types de **Work Items** (l'élément de travail Polarion : une exigence, un cas de vérification, un écart, une décision…), 327 attributs distincts, 112 énumérations (listes de valeurs), 26 rôles de liens (natures de lien entre éléments) ;
   - 24 workflows (cycles de vie à états et transitions) de Work Items et 3 workflows documentaires ; 22 types de **LiveDocs** (documents Polarion composés de Work Items et de texte).
   - Les notions de l'arrêté INB (arrêté du 7 février 2012 fixant les règles générales des installations nucléaires de base) y sont toutes représentées : **EIP** (élément important pour la protection des intérêts), **AIP** (activité importante pour la protection), **exigence définie, contrôle technique indépendant, écart**. Les classements y sont **multi-schémas** (parc, FA3 — Flamanville 3 —, EPR2, UK, AIEA SSG-30, IEC 61226, US), ainsi que le statut ESPN (équipement sous pression nucléaire), les classes K (qualification), SC (sismique), M, EE / E (classes mécaniques, électriques et de C-C), les CFSI (articles contrefaits, frauduleux ou suspects) et le contrôle export.
4. **Un socle non négociable** (NN-01 à NN-08 : les règles dues quelle que soit la taille du projet), appliqué à toutes les classes de projets, y compris aux fortuits express. Il est **outillé par des conditions de workflow bloquantes** (une transition refusée tant que la condition n'est pas remplie) :
   - indépendance auteur ≠ vérificateur ;
   - absence de liens suspects ;
   - classification ;
   - avis Sûreté conditionnel ;
   - signature électronique avec signification.
5. **Approche graduée (tailoring : adaptation du processus aux enjeux) en 4 classes** (A programme majeur → D express) :
   - une grille de cotation à 7 critères détermine la classe ;
   - chaque classe dispose de profils de types, de documents, de revues, de MBSE et de CCB (*Change Control Board*, comité de maîtrise des modifications) ;
   - la classe D est réellement légère (15 types, 2 documents, workflow documentaire express) sans renoncer au socle ;
   - chacune des 32 typologies de projet est **prouvée** par un scénario de couverture exécuté en CI (intégration continue : vérifications automatiques à chaque modification du dépôt ; doc. 19, annexe A9).
6. **Traçabilité aval → amont et suspicion maîtrisée** (un lien devient « suspect » quand l'élément amont change : il doit être revu) :
   - convention de direction des liens compatible avec le comportement natif de Polarion ;
   - 20 règles de complétude de la traçabilité (TR-01 à TR-20) ;
   - suspicion native en phase 1, filtrée par champ en phase 2 ;
   - analyse d'impact transitive (« cône d'impact » : tout ce qui dépend, de proche en proche, d'un élément modifié) pour le CCB.
7. **Documents de référence en GED** (gestion électronique des documents, l'archive d'entreprise) : LiveDocs signés R / V / A (rédigé / vérifié / approuvé), baseline (référence figée) automatique et export PDF/A (format d'archivage pérenne) signé avec manifeste versé en GED (archive de référence, durée de vie des installations supérieure à 60 ans) (ADR-11, ADR-30).
8. **Échanges client par ReqIF aller-retour** (ReqIF : format standard OMG d'échange d'exigences) :
   - le texte du client est verbatim et verrouillé ;
   - une position de conformité est portée par Framatome ;
   - les clients et partenaires accèdent par des projets sas `EXT-*` (jamais par un simple Space du projet interne) avec des licences REVIEWER (lecture, commentaire, approbation) (ADR-12, ADR-28).
9. **Multi-instance sur site** (plusieurs installations Polarion séparées, hébergées chez Framatome ; ADR-03) :
   - instance standard UE (`STD`) ;
   - instance sensible (`SENS`) et instance US (`US`), si l'analyse juridique et de sécurité les confirme ;
   - instance défense (`DEF`) : principe seul d'une instance isolée, aucun contenu modélisé (hors périmètre OSINT) ;
   - aucune donnée sensible ou classifiée sur l'instance standard (contrôle bloquant) ;
   - IA générative désactivée par défaut (ADR-17).
10. **L'outil est validé comme logiciel support d'AIP** (IQ / OQ / PQ — qualification de l'installation, du fonctionnement et des performances — fondés sur les risques). Les tests OQ sont dérivés des conditions bloquantes du modèle. L'intégrité des données suit les principes ALCOA+ (données attribuables, lisibles, contemporaines, originales, exactes, complètes, cohérentes, durables, disponibles ; leçons de l'affaire des dossiers de fabrication du Creusot, annexe C § 8).
11. **Déploiement en cinq phases (0 à 4) sur environ 34 mois** jusqu'à la fin de la vague 3, puis exploitation (phase 5) :
    - phase 0, cadrage (avec 20 à 24 ateliers de validation des hypothèses OSINT) ;
    - phase 1, fondations ;
    - phase 2, **pilotes : NUWARD (lot de conception, classe A) puis un pilote court sur la base installée** (fortuit ou outillage, lancé environ 2 mois après) — v0.4 : ramené des « trois pilotes contrastés » de la v0.1 à NUWARD + pilote court (doc. 23 § 6.1) ;
    - phase 3, industrialisation ;
    - phase 4, vagues : base installée (IB) → Combustible + C-C → PCM (projets et fabrication de composants) + DTI (direction technique et ingénierie).
12. **Gouvernance par une Design Authority ALM** :
    - CCB du modèle (comité qui décide des évolutions du modèle de données) ;
    - identifiants jamais renommés ;
    - CI qui valide et régénère la configuration à chaque évolution ;
    - réseau de champions (utilisateurs relais dans chaque BU) ;
    - support de niveaux 1 à 3.

13. **Organisation matricielle et provisioning outillé** (ADR-24, ADR-26) :
    - les UO (unités opérationnelles : sites, centres d'ingénierie, filiales) réalisent des **lots de travaux** signés à l'accord et à la réception ; un tableau de bord par UO est disponible sans projet par UO ;
    - tout projet naît d'un **questionnaire** (19 questions) et de règles de dérivation (15) : gabarit (master, socle non instanciable → archétype → spécialisation), classe, instance, packs, projet sas.
14. **Packs réglementaires et abstraction de filière** (ADR-25) : un modèle unique, des champs affichés ou masqués par cadre réglementaire, aucun vocabulaire REP (réacteur à eau pressurisée) français figé dans la structure.
15. **Signatures habilitées au choix du projet** (ADR-27) et **cloisonnement par projets sas** (ADR-28) : le Space (dossier qui organise les documents à l'intérieur d'un projet Polarion) n'est pas une frontière de sécurité. La signature électronique des exigences et des éléments d'architecture est **portée par le LiveDoc** qui les contient, dont l'approbation les approuve en cascade (ADR-30).

## 2. Correspondance avec la demande

| Livrable demandé | Document(s) |
|---|---|
| **Partie 1.1** Organisation et périmètres (BU / BL / UO) | [01_Organisation_BU_BL_UO](partie1/01_Organisation_BU_BL_UO.md) |
| **Partie 1.2** Typologie des projets et cycles de vie | [02_Typologie_projets_cycles_de_vie](partie1/02_Typologie_projets_cycles_de_vie.md) |
| **Partie 1.3** Disciplines et interfaces | [03_Disciplines_et_interfaces](partie1/03_Disciplines_et_interfaces.md) |
| **Partie 1.4** Référentiels normatifs et réglementaires | [04_Referentiels_normatifs_reglementaires](partie1/04_Referentiels_normatifs_reglementaires.md) |
| **Partie 2** Plan de recherche et matrice d'acquisition | [05_Plan_de_recherche_OSINT](partie2/05_Plan_de_recherche_OSINT.md) |
| **Partie 2** Questions d'architecture à trancher (ADR-01..30) | [06_Decisions_architecture_ADR](partie2/06_Decisions_architecture_ADR.md) |
| **Partie 3.1** Méthodologie IS (ingénierie système) et tailoring | [07_Methodologie_IS_et_tailoring](partie3/07_Methodologie_IS_et_tailoring.md) |
| **Partie 3.2** Modèle de données : Work Items, attributs | [08_Modele_de_donnees](partie3/08_Modele_de_donnees.md) + Annexes [A1](generated/A1_types_et_attributs.md), [A2](generated/A2_enumerations.md), [A8](generated/A8_metamodele.md) |
| **Partie 3.2** Liens et suspicion | [09_Tracabilite_et_suspicion](partie3/09_Tracabilite_et_suspicion.md) + [A3](generated/A3_liens_et_tracabilite.md) |
| **Partie 3.2** Workflows, signatures, rôles | [10_Workflows_signatures_roles](partie3/10_Workflows_signatures_roles.md) + [A4](generated/A4_workflows.md), [A6](generated/A6_roles_permissions.md) |
| **Partie 3.3** LiveDocs et gabarits | [12_LiveDocs_gabarits](partie3/12_LiveDocs_gabarits.md) + [A5](generated/A5_documents.md) |
| **Partie 3.3** Tableaux de bord et LiveReports | [13_Dashboards_LiveReports_KPI](partie3/13_Dashboards_LiveReports_KPI.md) |
| Compléments (au-delà du texte reçu, tronqué) | [11 Topologie / réutilisation / variantes](partie3/11_Topologie_reutilisation_variantes.md), [14 Intégrations](partie3/14_Integrations_et_echanges.md), [15 Infrastructure / sécurité / validation](partie3/15_Infrastructure_securite_validation.md), [16 Feuille de route](partie3/16_Feuille_de_route_deploiement.md), [17 Gouvernance](partie3/17_Gouvernance_conduite_changement.md), [A7 Tailoring](generated/A7_tailoring.md) |
| **Partie 3 / 4** Import / export et interopérabilité (ReqIF, Word / Excel, parsing, PLM, MBSE, calcul) | [14 Intégrations](partie3/14_Integrations_et_echanges.md) + [22 Import / export, parsing, connecteurs](partie4/22_Import_export_parsing_connecteurs.md) + [A11](generated/A11_import_export.md) |
| **Partie 3 / 4** Feuille de route A-Z (gouvernance, Master Template vs gabarits par typologie, conduite du changement, pilote, industrialisation) | [16 Feuille de route](partie3/16_Feuille_de_route_deploiement.md), [17 Gouvernance](partie3/17_Gouvernance_conduite_changement.md), [21 Provisioning et gabarits](partie4/21_Organisation_matricielle_provisioning_habilitations.md), [20 Facteurs de succès](partie4/20_Facteurs_de_succes_non_couverts.md) |
| **Partie 4** Revue critique et robustesse (demande de suivi) | [18 Analyse critique](partie4/18_Analyse_critique.md), [19 Robustesse](partie4/19_Robustesse_du_modele.md), [A9 Couverture](generated/A9_couverture_typologies.md) |
| **Partie 4** Onboarding de l'équipe, guide de configuration, kit pilote, stratégie de modèle (demande de suivi) | [23 Kit et guide pas à pas](partie4/23_Kit_deploiement_guide_pas_a_pas.md), [24 Parcours d'ateliers](partie4/24_Parcours_onboarding_ateliers.md), [25 Stratégie 50 % / 150 %](partie4/25_Strategie_coeur_50_vs_150.md) |
| Configuration Polarion exécutable | `model/*.yaml` → `generated/polarion/{fr,en}/.polarion/` (249 fichiers XML par langue) |

> **Note.** Le texte de la demande initiale s'interrompait au § 3.3 (« gestion des … »). La fin, retrouvée dans la conversation fournie ensuite, demandait l'import / export avec règles de parsing et connecteurs, puis la feuille de route A-Z avec Master Template et gabarits par typologie. Ces deux points sont traités en v0.3 (docs 21 et 22, annexes A10 et A11). L'écart est analysé au doc. 18 § 3.

## 3. Hypothèses de cadrage

| # | Hypothèse | Conf. |
|---|---|---|
| H1 | Déploiement greenfield : aucune instance Polarion existante chez Framatome ; d'éventuels référentiels d'exigences existants (Word, Excel, outils) sont à inventorier | Demande + NT |
| H2 | 3DEXPERIENCE (Core Model SE / PLM) et Capella sont déployés ou en cours de déploiement et restent en place | C |
| H3 | La GED d'entreprise reste le système d'archivage de référence | H |
| H4 | La version cible de Polarion est 2606 (numérotation AAMM : juin 2026) ou la suivante au lancement | P (mois de sortie à vérifier : annexe D, Q-TOOL-01) |
| H5 | L'hébergement sur site est privilégié pour les données d'ingénierie nucléaire | H |
| H6 | La langue de travail est bilingue FR / EN (+ DE pour Framatome GmbH) | P |

## 4. Mode d'emploi du dépôt

```bash
python3 tools/almmodel.py                     # valide la cohérence du modèle (0 erreur attendu ; -v : informations)
python3 tools/generate_polarion.py --lang fr  # configuration Polarion (libellés FR)
python3 tools/generate_polarion.py --lang en  # configuration Polarion (libellés EN)
python3 tools/generate_docs.py                # annexes A1-A11 (catalogues exhaustifs)
```

Toute évolution du modèle suit le processus du document 17 § 2 (CCB du modèle, demande de fusion — *pull request* —, CI). Les constructions Polarion que la configuration générée suppose sans les avoir vérifiées sur la version cible sont listées en [annexe D](annexes/D_Formats_Polarion_a_verifier.md) (PF-01..PF-14).
