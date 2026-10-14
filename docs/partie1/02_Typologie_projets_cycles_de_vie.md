# Partie 1.2 — Typologie des projets et cycles de vie associés

> Confiance : **[C]** confirmé · **[P]** probable · **[H]** hypothèse de modélisation. Les identifiants entre accolades renvoient au modèle (`model/`). Les classes de tailoring A à D sont définies au [document 07](../partie3/07_Methodologie_IS_et_tailoring.md).

## 0. Vue comparative

| Typologie | Classe | Durée typique | Profondeur du V | Régime de configuration | Intensité réglementaire | Taux de réutilisation |
|---|:-:|---|---|---|---|---|
| Grand réacteur neuf (EPR2, UK EPR) | A | 10-15 ans (études → MSI) | 5-6 niveaux : installation → système → sous-système → équipement → composant / logiciel | Baselines par jalon et par tranche ; ligne de produits (6 tranches EPR2) | Maximale (DAC, ESPN N1, C-C classe 1) | Fort sur la conception de référence, faible sur le site |
| SMR NUWARD | A | 8-12 ans | 5 niveaux + modules usine | Produit sur étagère : référence générique + variantes de site | Maximale ; revue multi-autorités (Joint Early Review) | Visé très fort (standardisation) |
| RGV / SGR | B | 2-5 ans (étude → arrêt) | 3-4 niveaux : intervention → système → équipement → outillage | Effectivité par tranche ; configuration « telle que réalisée » | Forte (ESPN N1, requalification) | Fort (série 1300, 900) |
| Réexamen périodique / VD | B | 5-10 ans (générique) + déclinaisons tranche | 2-3 niveaux (exigence réglementaire → étude → preuve) | Référentiel par palier, déclinaison par tranche | Maximale (décisions, prescriptions) | Fort entre tranches d'un palier |
| Modification base installée | C | 6 mois - 3 ans | 2-3 niveaux | Effectivité palier / tranche ; état « avant / après » | Variable (non notable → autorisation) | Moyen |
| Fortuit | D | Heures à semaines | 1-2 niveaux (critère → justification) | Configuration constatée sur la tranche | Variable, souvent ESPN | Faible (mais REX générique fort) |
| Outillage spécial / inspection | C | 6-24 mois | 3 niveaux (besoin → système → module) | Configuration machine (série, version logicielle) | Machine (CE), RP, qualification CND | Moyen (catalogue) |
| Conception combustible / ATF | A | 5-15 ans (qualification) | 4 niveaux (produit → assemblage → crayon / structure → matériau) | Gammes produits + versions de design | Forte, multi-pays (ASNR, NRC...) | Moyen |
| Recharges | C | Par cycle (12-18 mois), récurrent | 2 niveaux (limites de référence → paramètres du cycle) | Tranche × cycle | Forte (respect des hypothèses de sûreté) | Très fort (gabarit + données) |
| Plateforme C-C | A | Continu (versions) | 4 niveaux (plateforme → module → matériel / logiciel / HDL) | Versions de plateforme, qualification générique | Forte (IEC 61513, 60880) | Socle de tous les projets C-C |
| Projet / rénovation C-C | B | 3-8 ans | 5 niveaux IEC 61513 | Versions logicielles, configuration par tranche | Forte (catégorie A, cybersécurité) | Fort (plateforme) |
| Composant (conception / fabrication) | B / C | 2-6 ans | 3 niveaux (spécification d'approvisionnement → équipement → pièce) | Numéro de série, dossier de fin de fabrication | Forte (ESPN, RCC-M) | Moyen à fort |
| R&D | C | 1-5 ans | 2-3 niveaux | Légère | Faible à moyenne | Faible |

---

## A. Nouveau nucléaire

### A1. Grands réacteurs : EPR2 et UK EPR (HPC, SZC)

**Contexte OSINT**
- Programme EPR2 : 6 réacteurs (3 paires : Penly, Gravelines, Bugey), d'environ 1,7 GWe chacun [C].
  - Devis présenté au conseil d'EDF le 18/12/2025 : 72,8 Md€ (euros 2020) [C].
  - Décision finale d'investissement visée fin 2026 ; mise en service de Penly 1 visée en 2038 [C].
  - En janvier 2026, l'ASNR a demandé des évolutions de la conception du génie civil de Penly [C].
  - Décret de travaux préparatoires de Gravelines : 22/08/2026 [C].
- Rôle de Framatome sur l'EPR2 [C] : conception, fabrication, montage et mise en service du circuit primaire (6 cuves, 24 GV, 25 pompes primaires, 6 pressuriseurs, 534 mécanismes de grappes) et 6 systèmes d'instrumentation nucléaire et de C-C de sûreté. Framatome annonce en 2026 une intégration complète de l'îlot nucléaire [P].
- Hinkley Point C : mise en service des tranches 1 et 2 visée en 2030 et 2031, montage du circuit primaire en cours, cuve de la tranche 2 installée en juin 2026 [C].
- Sizewell C : décision finale d'investissement le 22/07/2025 ; contrats Framatome portant sur 2 chaudières, le C-C de sûreté et le combustible [C].
- Classement EPR2 [C] : fonctions de catégories 1, 2 et 3 ; SSC de classes S1, S2 et S3. Chaque EIPS reçoit la classe de la catégorie la plus élevée de ses fonctions. Démarche fondée sur le Guide ASN n° 22.
- Classement FA3 [C] :
  - fonctions F1A (atteinte de l'état contrôlé après PCC-2 à PCC-4), F1B (atteinte de l'état sûr) et F2 ;
  - classes mécaniques M1 à M3, électriques EE1 et EE2, de C-C E1A, E1B et E2 ;
  - classes sismiques SC1 et SC2.
- L'ONR a jugé ce schéma imparfaitement aligné sur la pratique britannique [C] → le schéma HPC/SZC est spécifique (`eprUk`).

**Cycle de vie et jalons**

| Phase (`lifecyclePhase`) | Jalons techniques (`reviewType`) | Jalons réglementaires France | Artefacts Polarion dominants |
|---|---|---|---|
| Conception de base | SRR, PDR, revues de sûreté | Dossier d'options de sûreté, puis rapport préliminaire de sûreté dans la demande d'autorisation de création | `sourceRequirement` (exigences de l'architecte-ensemblier), `stakeholderRequirement`, `function`, `safetyRequirement`, `hazard`, `safetyClaim`, `classificationList` |
| Conception détaillée | CDR par système, gel des interfaces | Instruction de la demande, puis décret d'autorisation de création | `systemRequirement`, `equipmentRequirement`, `interface` (ICD), `analysis`, `designDecision`, `systemDesignManual` |
| Approvisionnement & fabrication | Revue avant fabrication, points H/W | ESPN N1 : évaluation de conformité (ASNR) ; qualification technique | `equipmentSpec`, `verificationCase` (stage `manufacturing`), `nonConformance`, `waiver`, `deliverable` (dossier ESPN) |
| Montage | Revue d'aptitude aux essais | Inspections de chantier | `verificationCase` (`siteInstallation`), `changeRequest` |
| Essais & mise en service | Essais à froid / à chaud, essais de démarrage | Autorisation de mise en service, rapport de sûreté | Test Runs, `anomaly`, `regulatoryCommitment` |

**Profondeur du V et configuration**
- Le V s'étend de l'installation au composant ; pour le C-C, il descend jusqu'au logiciel et au HDL (voir D2).
- **Ligne de produits** :
  - `PL-EPR2` porte la conception de référence ;
  - chaque paire ou tranche est un projet de réalisation qui réutilise la référence par branchement de documents ;
  - les différences de site (données de site, ajustements) sont des variantes tracées (`applicableUnits`, `applicabilityCondition`).
- **Baselines** : par jalon (`<projet>-<jalon>-<date>`) et par tranche ; collections Polarion pour figer un ensemble cohérent de documents à un jalon.
- **Interfaces** : très nombreuses, intra-Framatome (PCM / ICS / Fuel / DTI) et externes (architecte-ensemblier, îlot conventionnel, génie civil). Registre `interface` obligatoire, ICD par périmètre contractuel.

**Spécificités du modèle**
- Coexistence de trois schémas de classement → champ `safetyClassScheme` sur chaque SSC.
- Argumentaire de sûreté structuré (`safetyClaim`), attendu par l'ONR pour HPC/SZC et utile pour la DAC EPR2.
- Volume : centaines de milliers d'artefacts. Projets découpés par périmètre (NSSS, C-C) et par tranche.

### A2. SMR NUWARD

**Contexte OSINT**
- Projet lancé en 2019 (EDF, CEA, Naval Group, TechnicAtome) ; Framatome et Tractebel l'ont rejoint en 2022 ; filiale NUWARD SAS créée en 2023 [C].
- En **juillet 2024**, le design initial (2 × 170 MWe) a été abandonné au profit de « briques technologiques éprouvées » [C].
- **Nouveau design : environ 400 MWe**, avec une option de cogénération d'environ 100 MWt [C].
- Calendrier [P] : conception conceptuelle visée mi-2026, conception de base vers 2028, début de construction vers 2030.
- Revue réglementaire précoce menée conjointement par plusieurs autorités européennes [P].
- Rôle précis de Framatome dans le nouveau design : **non trouvé** → [H] chaudière / composants, C-C et combustible.

**Spécificités d'ingénierie**
- Logique **produit sur étagère** : conception générique, standardisée et certifiable dans plusieurs pays, déclinée par site. Fabrication modulaire en usine et intégration en usine plutôt que sur site.
- Multi-réglementation dès la conception, d'où l'intérêt de l'initiative AIEA NHSI pour l'harmonisation des SMR (lancée en 2022, phase II approuvée en octobre 2024 [C]).
  - Le schéma de classement est probablement inspiré de SSG-30 (`iaeaSsg30`) [H].
  - La bibliothèque réglementaire doit être multi-juridictions (`jurisdiction`).
- Redesign en cours : la gestion des **hypothèses** (`assumption`) et des **décisions** (`designDecision`) doit être rigoureuse, avec un registre des décisions d'architecture et la traçabilité des options abandonnées.
- MBSE Capella attendu comme source maîtresse de l'architecture, avec une forte itération en phase conceptuelle.

**Cycle de vie** : pré-conception → conception conceptuelle → conception de base → conception détaillée générique → instanciation par site. Les revues de conception de base servent de portes de sortie de la phase de changement intensif. Après cette porte, CCB à deux niveaux (produit / site).

**Configuration** :
- `PL-NUWARD` est la spécification maître ; les **variantes** (site, cogénération, options) sont gérées par module de variantes (feature model) ou par conditions d'applicabilité (ADR-05).
- Les différences entre un site et la référence générique sont tracées comme des écarts au produit standard (`waiver` de type `requirementWaiver` + `designDecision`).

---

## B. Base installée

### B1. Remplacement de générateurs de vapeur (RGV / SGR)

**Contexte OSINT**
- Framatome est maître d'œuvre des RGV en France [C].
- 44 GV de remplacement ont été commandés pour le palier 1300 MWe en 2011 [P].
- Exemples : RGV de Flamanville 2 pendant un arrêt achevé fin 2025 [P] ; Cruas 3 avec des GV de nouvelle conception [P] ; avis ASNR 2025-00098 sur la réutilisation de la boulonnerie dans les RGV 1300 [C].
- À l'international : Koeberg (Afrique du Sud, 6 GV) [C] ; remplacements de gros composants en Amérique du Nord [C].

**Spécificités**
- Projet hybride :
  - conception ou adaptation du GV de remplacement (composant ESPN N1, fabrication) ;
  - ingénierie d'intervention : découpe et soudage des tuyauteries primaires, manutention lourde, logistique, radioprotection et ALARA, déchets ;
  - requalification : épreuve, essais ;
  - le tout sur le **chemin critique d'un arrêt de tranche**.
- Interface avec une **installation existante**, dont la configuration réelle (« telle que construite ») doit être relevée : relevés, contrôles préalables, hypothèses (`assumption` de type donnée de site).
- Séquences d'intervention modélisées en `operationalScenario` (`scenarioType = intervention`), avec dose collective prévisionnelle (`doseEstimate`) et AMDEC d'intervention (`fmeaType = intervention`).
- **Effectivité par tranche** : un projet par site ou campagne (`P-SGR-<site>`), réutilisant un référentiel palier (`PL-SG`, `PL-FLEET-FR`).

**Cycle de vie** : faisabilité → études de conception (GV + intervention) → fabrication → qualification des procédés et des outillages sur maquette → revue d'aptitude à l'intervention (`interventionReadiness`) → intervention en arrêt → requalification → retour d'expérience.

### B2. Réexamen périodique, visites décennales (VD) et dossiers associés

**Contexte OSINT**
- Le réexamen périodique a lieu tous les 10 ans (Code de l'environnement, L.593-18). Le rapport de conclusions du réexamen est prévu par l'article L.593-19 ; au-delà de 35 ans de fonctionnement, il est soumis à enquête publique [C].
- 4e réexamen des 900 MWe [C] : décision **2021-DC-0706** du 23/02/2021 pour la phase générique ; la déclinaison réacteur par réacteur s'étale jusqu'en 2031.
- 4e réexamen des 1300 MWe [C] : décision **ASNR 2025-DC-016** du 1er juillet 2025, pour la phase générique des 20 réacteurs.
- La VD est l'arrêt réalisant les épreuves (circuit primaire, enceinte) et les modifications du réexamen [C].

> **Point de terminologie.** Dans la réglementation, la « décision RDS » désigne la décision **2015-DC-0532** relative au **rapport de sûreté** des INB, modifiée en 2026 par la décision 2026-DC-041 [C]. Le dossier de réexamen relève, lui, du **rapport de conclusions du réexamen** (L.593-19). Le modèle les distingue :
> - le rapport de sûreté est rattaché à `safetyCase` ;
> - le réexamen est porté par le gabarit `TPL-IB-PSR` et l'énumération `periodicSafetyReview`.

**Contenu d'ingénierie (rôle de Framatome probable [P/H])**
- **Examen de conformité** : comparaison de l'état réel avec le référentiel, ce qui génère des écarts (`nonConformance`).
- **Réévaluation de sûreté** : nouvelles exigences au regard des objectifs du réexamen ; études de justification (cuve, fatigue, nocivité de défauts, agressions).
- **Vieillissement / aptitude à la poursuite de fonctionnement** : mécanismes (`ageingMechanism`) et programmes d'investigations.
- **Modifications** issues du réexamen (B3).
- Suivi des **prescriptions et demandes** de l'autorité : `regulatoryCommitment` (`requestCategory = prescription`), échéances, preuves (TR-15).

**Configuration** :
- référentiel générique par palier (`P-PSR-<palier>`) ;
- déclinaison par tranche via `applicableUnits` et documents dérivés ;
- traçabilité **prescription → étude → modification → preuve → clôture**.

### B3. Études de modifications (base installée)

**Contexte** : la qualification réglementaire des modifications relève de l'exploitant. Elle est encadrée par les articles L.593-14 (modification substantielle) et L.593-15 (modification notable : déclaration ou autorisation), les articles R.593-55 à R.593-60, et la décision **2017-DC-0616** modifiée par la décision 2023-DC-0770 [C]. Framatome produit les études et les éléments d'appréciation.

**Spécificités** :
- dossier de modification (`modificationFile`) : exigences, solution, analyse d'impact, classement réglementaire proposé (`regulatoryModificationClass`), programme de requalification, documents d'exploitation impactés ;
- **état avant / après** : l'existant est tracé par des éléments `physicalComponent` (palier) et la modification par une `changeRequest` liée par `impacts` ;
- **effectivité** : tranches et dates d'intégration par arrêt (`outageType`).

**Cycle de vie** : faisabilité → avant-projet → études détaillées → dossier de réalisation → intégration dans un arrêt → requalification → mise à jour documentaire → retour d'expérience.

### B4. Fortuits (aléas en arrêt de tranche)

**Nature** : constat inattendu pendant un arrêt (indication en contrôle non destructif, fuite, défaut, corps étranger, dégradation), qui appelle une réponse d'ingénierie rapide :
- justification « en l'état » (mécanique de la rupture, critères RSE-M) ;
- réparation ;
- remplacement ;
- investigations complémentaires ;
- mesure compensatoire.

Le délai est de quelques heures à quelques semaines, souvent sur le **chemin critique de l'arrêt**.

**Exigences contradictoires à concilier** :
- réactivité maximale ;
- conservation du socle non négociable : contrôle technique indépendant des AIP, traçabilité vers les exigences définies, gestion d'écart, archivage.

**Réponse du modèle** :
- type `technicalIssue` avec le workflow express `wfTechnicalIssue`, les SLA calculés selon l'urgence (`setDueDateFromNow`) et la notification Sûreté si `safetyImpact = yes` ;
- un **projet conteneur** par client (`P-FORTUIT-<client>`) avec un Space par affaire ;
- gabarit de **note de justification** (`justificationNote`, workflow documentaire allégé `wfDocumentLight`, deux signatures) ;
- champ `genericImpact` pour remonter les problèmes génériques (palier ou flotte) ; REX obligatoire à la clôture (`lessonsLearnedCaptured`).

### B5. Outillages spéciaux et services d'inspection

**Contexte OSINT** :
- machine d'inspection en service des cuves : robot d'environ 12 t, plus de 350 cuves inspectées, méthodes qualifiées selon le RSE-M et l'ASME [C] ;
- robotique, outillages d'intervention et manutention [P].

**Spécificités** :
- produit **mécatronique** (mécanique, électricité, contrôle-commande, logiciel) ;
- conformité au cadre « machines » : directive 2006/42/CE, **remplacée par le règlement (UE) 2023/1230 applicable au 20 janvier 2027** [P] ;
- contraintes du site : radioprotection, contamination, exclusion des corps étrangers (FME), accessibilité, manutention ;
- qualification sur maquette ;
- pour l'inspection, qualification des procédés de CND.

**Cycle de vie** : expression fonctionnelle du besoin (NF EN 16271, `toolingSpec`) → conception → prototype → qualification sur maquette → réception client → emploi sur site → maintenance et évolutions (versions).

**Modèle** :
- `function` (`functionType = toolFunction`) ;
- `hazard` (`hazardType = machinery`) ;
- `fmeaItem` (`fmeaType = intervention`) ;
- `physicalComponent` (`componentNature = tool`, `isConfigurationItem`) ;
- catalogue `PL-TOOLS` pour la réutilisation.

---

## C. Combustible

### C1. Conception de produits combustibles (dont ATF)

**Contexte OSINT** :
- GAIA avec PROtect E-ATF : gaine M5 revêtue de chrome et pastilles dopées à l'oxyde de chrome. Quatre assemblages précurseurs ont été fabriqués à Richland et irradiés trois cycles à Vogtle 2 ; la solution à long terme est le SiC [C].
- Développement de designs VVER [P].
- Volume historique : plus de 230 000 assemblages [P].

**Spécificités** :
- exigences issues de critères de conception, au sens du RCC-C (édition en vigueur à vérifier) : pression interne, oxydation, critère d'ébullition critique, fusion à cœur, tenue des grilles, etc. (`reqCategory = designCriterion`) ;
- **qualification longue** : essais hors pile, puis assemblages précurseurs, puis irradiation et examens ;
- **licensing multi-pays** : dossiers soumis à plusieurs autorités, par exemple ASNR et NRC → `regulatoryCommitment` par autorité ;
- codes de calcul qualifiés (`codeQualification`).

**Configuration** : gammes de produits (`PL-FUEL`) ; versions de design ; effectivité par client et par réacteur.

### C2. Contrats de recharge (études de cœur)

**Nature** : pour chaque tranche et chaque cycle, conception du plan de chargement. On vérifie que les paramètres de sûreté de la recharge respectent les limites des études de référence, puis on produit le rapport de sûreté de recharge et le programme d'essais physiques de redémarrage. L'activité est récurrente, très normalisée et soumise à une forte pression calendaire.

**Modèle** :
- `designParameter` (`designParameterType = coreParameter` ; valeurs `limitValue`, `calculatedValue` ; marge calculée ; `cycleOrConfiguration`) ;
- `verificationCase` (vérification par paramètre, étape `reloadStartupPhysics` pour les essais) ;
- gabarit `reloadSafetyReport` instancié **par tranche et par cycle** dans un projet conteneur (`P-RELOAD-<client>`).

**Automatisation** :
- import des résultats de calcul ;
- remplissage des valeurs calculées ;
- rapport des marges ;
- détection automatique des dépassements.

---

## D. Contrôle-commande

### D1. Plateformes de C-C qualifiées

**Contexte OSINT** :
- TELEPERM XS (TXS) installé ou en cours d'installation sur 92 réacteurs dans 17 pays [P] ; TXS Compact approuvé par la NRC [C] ;
- plateformes issues d'acquisitions : Spinline, Rodline, Hardline (ex-Rolls-Royce), Tricon nuclear, SPEC 200 (ex-Schneider) [C] ;
- outils SPACE (spécification et génération de code) et SIVAT (simulation) [C].

**Spécificités** :
- produit générique avec **qualification générique** : environnement, séisme, CEM, logiciel système ;
- gestion des **versions** : chaque projet hérite d'une version qualifiée ;
- les anomalies sur la plateforme sont **génériques** et doivent être propagées vers les projets impactés (`genericImpact`, liens `impacts` inter-projets).

### D2. Projets de C-C (application, rénovation)

**Contexte OSINT** :
- rénovation du C-C de sûreté des 20 tranches de 1300 MWe (contrat 2011) [P] ;
- Ringhals 3 et 4, Gösgen, Kursk II, Sizewell C, EPR2 [C].

**Cycle IEC 61513** (édition 3 de 2026 [C]) :
1. exigences globales du C-C ;
2. architecture du C-C (catégorisation IEC 61226 éd. 4 de 2020) ;
3. exigences des systèmes (classes 1, 2, 3) ;
4. spécifications logicielles (IEC 60880 pour la catégorie A, IEC 62138 pour B/C), matérielles (IEC 60987) et HDL (IEC 62566 / 62566-2) ;
5. intégration ;
6. validation du système ;
7. installation ;
8. mise en service.

S'y ajoutent les défaillances de cause commune (IEC 62340), la séparation (IEC 60709) et la cybersécurité (IEC 62645, 63096, 62859).

**Modèle** :
- `function` (`functionCategory = iecCatA/B/C`) ;
- `logicalComponent` (`logicalType = icSystem`, `icSystemClass`) ;
- `softwareRequirement`, `hardwareRequirement` ;
- `verificationCase` (étapes `integration`, `fat`, `sat`) ;
- `anomaly` ;
- **V&V indépendante** (`independenceLevel = independentOrg`, rôle `independentVerifier`) pour la catégorie A ;
- `securityDegree` et exigences `cybersecurity`.

**Traçabilité jusqu'au code** : diagrammes fonctionnels SPACE identifiés (`modelElementId`) ; preuves de simulation (`evidenceReference`) ; liens vers les dépôts de code si applicable.

---

## E. Composants : conception et fabrication (ESPN)

**Contexte OSINT** :
- arrêté ESPN du 30/12/2015 modifié en 2018 : niveaux N1, N2, N3 ; catégories 0 à IV ; évaluation de la conformité par l'ASNR pour le N1, par des organismes agréés pour N2 et N3 ; exigences essentielles de sécurité en annexe I [C] ;
- RCC-M édition 2024 [C] ; guide ASNR n° 8 bis pour les ESPN N1 des REP (mars 2026) [C].

**Spécificités** :
- spécification d'approvisionnement (`equipmentSpec`) : classement, code, matériaux, chimie, fabrication, contrôles, qualification ;
- **points d'arrêt et de notification** (`inspectionPoint`, `witnessParties`) ;
- FNC et dérogations très encadrées : accord du client et de l'autorité ou de l'organisme selon le niveau ;
- dossier ESPN (notice d'instructions, dossier technique) ;
- dossier de fin de fabrication ;
- **intégrité des enregistrements** (héritage du Creusot).

**Frontière avec 3DEXPERIENCE / MES** :
- dans Polarion : exigences, conformité, plan de contrôle (cas de vérification de fabrication), FNC d'ingénierie ;
- dans le MES ou le Core Model : gammes, ordres de fabrication, relevés d'exécution, preuves de fabrication ;
- lien entre les deux par identifiants et preuves (`evidenceReference`) ;
- voir ADR-07.

---

## F. R&D et innovation

Programmes amont : nouveaux matériaux, ATF, méthodes de calcul, numérique, robotique, isotopes. Exigences de maturité (TRL), hypothèses et décisions dominantes ; transition vers un projet produit (classe A/B) avec **reprise des exigences et des décisions** par branchement documentaire. Gabarit `TPL-RD` (classe C par défaut).

## F bis. Typologies ajoutées en v0.3

La revue critique (doc. 18) et la confrontation à une seconde analyse ont porté le nombre de typologies de 17 à 32. Chacune dispose d'un profil de tailoring et d'un scénario de couverture prouvé en CI ([annexe A9](../generated/A9_couverture_typologies.md)).

| Typologie | Spécificité de cycle de vie | Ce qui casserait un modèle « standard » | Réponse du modèle |
|---|---|---|---|
| **Augmentation de puissance** | Réévaluation des marges et des études d'accidents, licensing, déploiement par tranche | Marges multi-paramètres, licence à amender | `designParameter` (marges), `analysis`, `regulatoryCommitment`, `unitDeployment`, 50.59 (pack US) |
| **Pièces de rechange / obsolescence (CGD)** | Équivalence d'un article de remplacement ; dédicace d'un article commercial | Caractéristiques critiques, méthodes CGD 1 à 4, Part 21 | `commercialGradeDedication`, `criticalCharacteristics`, méthodes de vérification CGD, `supersedes` inter-projets, TR-20 |
| **Atelier chaud** | Équipement contaminé suivi par numéro de série ; réparation, requalification, retour site | Exemplaire unique, dose, déchets | `physicalComponent` (`serialNumber`, `expectedWasteClass`), `operationalScenario` (dose), `testEnvironment` = atelier chaud |
| **Démantèlement** | V inversé : état initial (caractérisation) → scénarios de découpe → déchets → état final | Données as-built du parc, catégories de déchets | Branche du référentiel parc, `wasteClass`, scénarios `decommissioning`, `TPL-IB-DECOM` |
| **Services combustible sur site** | Campagnes d'inspection / réparation d'assemblages par arrêt | Criticité, manutention, assemblage suivi individuellement | `fuelAssembly` par numéro de série, `hazardType` = criticité / chute de charge, `unitDeployment` (cycle, arrêt) |
| **Combustible et cibles MTR** | Commande client, série, export | Filière non REP, licences d'export | `reactorTechnology` = réacteur de recherche, `irradiationTarget`, SDRL, `exportControl` |
| **Licensing d'usine / d'emballage** | Démonstration de criticité, transport, LEU+ / HALEU | Codes de calcul validés, limites (k-eff, enrichissement) | `designParameter` (limite, incertitude), `analysisType` = criticité / validation de code, `safetyClaim` |
| **Qualification de procédé / matériau** | Fenêtre de procédé, essais de qualification, dossier | Paramètres de procédé, témoins | `designParameterType` = fenêtre de procédé, `qualificationDossier`, habilitations soudage / CND |
| **Simulateur pleine échelle** | Fidélité, validation, mise à jour selon la tranche de référence | Synchronisation avec les modifications de la tranche | `reqCategory` = fidélité simulateur, `dependsOn` inter-projets, anomalies |
| **Cybersécurité d'installation** | Inventaire des actifs numériques critiques, mesures, évaluation | Données sensibles (instance SENS) | Typologie forcée sur SENS (règle D04), `hazardType` = menace cyber, `securityDegree` |
| **Code de calcul scientifique** | Usages visés, V&V et quantification des incertitudes, versions qualifiées | Propagation d'une anomalie aux études utilisatrices | `anomaly` —impacts→ `analysis` inter-projets ; `qualificationDossier` |
| **Essais de laboratoire / cellule chaude** | Demande, échantillons, incertitudes, rapport (ISO/IEC 17025) | Échantillons, environnements spécifiques | `testEnvironment` = laboratoire / cellule chaude / boucle, `uncertainty` |
| **Produit catalogue configuré à la commande** | Branche de la spécification maître, qualification de type réutilisée | Qualification portée par la ligne de produits | `branched_from`, `verifies` inter-projets, `TPL-CTO` |
| **Isotopes médicaux** | Sûreté nucléaire du réacteur hôte + BPF (QI / QO / QP) | Deux référentiels réglementaires simultanés | Packs `caCnsc` + `medicalGmp`, `vvStage` QI / QO / QP |
| **Programme défense** | Hors périmètre OSINT | Secret | Principe seul : instance DEF, aucun contenu modélisé |

## G. Synthèse des exigences de modèle par typologie

| Besoin | Typologies concernées | Réponse du modèle |
|---|---|---|
| Ligne de produits / variantes | EPR2, NUWARD, plateformes C-C, combustible, outillages | Projets `PL-*`, branchement de documents (fusion 3-way), `applicablePlantSeries`, `applicableUnits`, module Variants (ADR-05) |
| Effectivité par tranche / cycle | RGV, modifications, recharges, réexamen | `applicableUnits`, `effectivity`, `cycleOrConfiguration`, documents dérivés |
| Cycle court sous SLA | Fortuits, problèmes génériques | `technicalIssue` + `wfTechnicalIssue` + `wfDocumentLight` |
| Prescriptions et engagements | Réexamen, nouveau nucléaire, combustible | `regulatoryCommitment` + TR-15 |
| Intégrité des enregistrements de fabrication | Composants, ESPN | Signatures, baselines, interdiction de suppression (PR-01), `cfsiSuspected` |
| Indépendance de la V&V | C-C catégorie A, analyses AIP | `independenceLevel`, `approverNotAuthor`, `independentVerifier` |
| Démonstration de sûreté structurée | Nouveau nucléaire, UK | `safetyClaim` (CAE/GSN), `supportedBy` |
| Hypothèses de site et existant | RGV, modifications, NUWARD | `assumption` + lien `assumes` (suspicion) |
| Statut par tranche / cycle (v0.2) | RGV, modifications, réexamen, recharges, augmentation de puissance | `unitDeployment` (un enregistrement par tranche, son propre workflow) |
| Réalisation par plusieurs UO (v0.3) | Grands projets, composants, démantèlement | `workPackage`, `performingUnit` (doc. 21) |
| Multi-juridiction, autres filières (v0.3) | International, combustible non REP, MTR, isotopes | Packs réglementaires, `reactorTechnology` (ADR-25) |
