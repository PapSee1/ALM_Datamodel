# Partie 1.4 — Référentiels normatifs et réglementaires : impacts sur le modèle de données et les workflows

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **faible** (référentiels ; seule la colonne « impact » renvoie aux éléments du modèle) · Historique : [CHANGELOG](../../CHANGELOG.md) · Carte du dépôt : [guide de lecture](../GUIDE_DE_LECTURE.md).*

> **En bref**
> - **À quoi sert ce document.** Il recense les textes qui s'imposent à l'ingénierie nucléaire de Framatome (lois, arrêtés, décisions et guides de l'autorité, codes industriels, normes, textes européens et étrangers) et indique, pour chacun, ce qu'il impose au modèle de données et aux workflows Polarion (champ, type, condition de transition, gabarit).
> - **Qui le lit.** Les référents sûreté, qualité et normalisation qui valideront les références en atelier ; les concepteurs du modèle qui doivent justifier chaque champ réglementaire.
> - **À lire avant.** Le [doc. 02](02_Typologie_projets_cycles_de_vie.md) (typologies) ; les sigles sont dans le [glossaire](../annexes/B_Glossaire.md). Le § 9 (matrice exigence → impact) est le résumé opérationnel.

> Confiance : **[C]** confirmé (extrait de source officielle ou ≥ 2 sources) · **[P]** probable · **[P\*]** connaissance non revérifiée lors de la campagne OSINT d'octobre 2026, à revérifier en priorité (Partie 2, lot R-REG) ; « à sourcer » signale un fait sans source en annexe C.
> Les textes protégés par le droit d'auteur (AFCEN — association française des règles de conception et de construction des matériels des chaudières nucléaires —, IEC, ISO, ASME) ne sont **jamais** intégralement chargés dans Polarion sans licence. Le projet bibliothèque `LIB-REG` stocke la référence, la clause et une paraphrase (`copyrightRestricted = true`).

## 1. Hiérarchie des référentiels

```mermaid
flowchart TD
  L["Lois et codes<br/>Code de l'environnement (Livre V, Titre IX)"] --> D["Décrets"]
  D --> A["Arrêtés<br/>INB 7/02/2012 · ESPN 30/12/2015"]
  A --> DEC["Décisions réglementaires ASN/ASNR<br/>(homologuées)"]
  DEC --> G["Guides ASN/ASNR<br/>(non contraignants mais attendus)"]
  A --> C["Codes industriels AFCEN<br/>RCC-M, RCC-E, RCC-C, RCC-CW, RSE-M, RCC-F"]
  C --> N["Normes IEC / ISO / IEEE"]
  I["Normes de sûreté AIEA, WENRA"] -.inspire.-> G
  F["Réglementations étrangères<br/>10 CFR, ONR SAPs, YVL"] -.projets export.-> N
  EU["Législation UE<br/>Machines, double usage, NIS2, CRA, eIDAS"] --> A
  CL["Exigences clients<br/>(spécifications, prescriptions)"] --> P["Projet"]
  N --> P
  G --> P
```

## 2. Socle réglementaire français

Repères : **INB** = installation nucléaire de base (réacteur, usine du cycle…) ; **ESPN** = équipement sous pression nucléaire ; **ASN** = Autorité de sûreté nucléaire, devenue **ASNR** (Autorité de sûreté nucléaire et de radioprotection) le 1er janvier 2025 par fusion avec l'IRSN (expertise) ; **EIP** = élément important pour la protection des intérêts ; **AIP** = activité importante pour la protection ; **SMI** = système de management intégré.

### 2.1 Code de l'environnement [C]

| Article | Objet | Impact Polarion |
|---|---|---|
| L.593-1 | Intérêts protégés : sécurité, santé et salubrité publiques, protection de la nature et de l'environnement | Énumération `protectedInterest` |
| L.593-7 | Démonstration de sûreté de l'installation (support des définitions d'EIP et d'AIP) | `safetyClaim`, `safetyCase` |
| L.593-14 | Modification **substantielle** : nouvelle autorisation | `regulatoryModificationClass = substantial` |
| L.593-15 | Modification **notable** : déclaration ou autorisation de l'ASNR | `regulatoryModificationClass = notableDeclaration` / `notableAuthorization` |
| L.593-18 / L.593-19 | Réexamen périodique tous les 10 ans ; rapport de conclusions (enquête publique au-delà de 35 ans de fonctionnement d'un réacteur) | Gabarit `TPL-IB-PSR`, `regulatoryCommitment` |
| R.593-55 à R.593-58 | Modifications soumises à autorisation | Dossier `modificationFile` |
| R.593-59 et R.593-60 | Modifications soumises à déclaration | idem |

### 2.2 Arrêté du 7 février 2012 fixant les règles générales relatives aux INB (« arrêté INB ») [C]

Modifié notamment en 2013, 2015 (par l'article 14 de l'arrêté ESPN [P\*]) et 2018 [P\*]. Aucune modification 2024-2025 trouvée [P\* — à revérifier, lot R-REG, doc. 05 § 7 item 2]. C'est **le texte le plus structurant pour le modèle de données**.

| Article | Exigence (paraphrase) | Traduction dans le modèle Polarion |
|---|---|---|
| 1.3 | Définitions : **écart** (non-respect d'une exigence définie ou d'une exigence du SMI), **exigence définie** (exigence assignée à un EIP ou à une AIP), **EIP**, **AIP**, intervenant extérieur (sous-traitant, fournisseur) | Champs `eip`, `definedRequirement`, `aip` ; type `nonConformance` (fiche de non-conformité, FNC) |
| 2.2.1 à 2.2.4 | Surveillance des intervenants extérieurs : proportionnée aux enjeux, documentée, réalisée par des personnes compétentes | `actionType = surveillance` ; rôles externes cloisonnés ; preuves |
| 2.3.1 / 2.3.3 | Politique de protection des intérêts et son évaluation | Gouvernance (document 17) |
| 2.4.1 / 2.4.2 | Système de management intégré : les exigences de protection sont systématiquement prises en compte dans toute décision ; organisation et ressources adaptées | Processus IS outillé ; revue de la configuration ALM |
| **2.5.1** | Identification des **EIP** et de leurs **exigences définies**, liste tenue à jour ; qualification des EIP proportionnée | `eip`, `definedRequirement` (jamais « À déterminer » à l'approbation, socle NN-01), document `classificationList`, `qualificationStatus` |
| **2.5.2** | Identification des **AIP** et de leurs exigences définies ; réalisation permettant de satisfaire *a priori* les exigences | `aip` sur `analysis`, `deliverable`, LiveDocs |
| **2.5.3** | **Contrôle technique** de chaque AIP, réalisé par une **personne différente** de celle qui a accompli l'activité | Condition `approverNotAuthor` sur toutes les transitions d'approbation ; signature `verified` sur les workflows qui en portent une, sinon signature portée par le LiveDoc qui contient l'élément (socle non négociable NN-02, ADR-30) |
| **2.5.4** | Vérifications par sondage et évaluation périodique, par des personnes différentes de celles qui ont réalisé **ou contrôlé** l'activité | Rôle `qualityEngineer` ; audits ; rapport d'échantillonnage (document 13) |
| 2.5.5 | Compétences et qualification des personnes réalisant les AIP, les contrôles et les vérifications | Rôles alimentés par l'annuaire selon les habilitations (document 17) |
| **2.5.6** | AIP, contrôles techniques, vérifications et évaluations **documentés et tracés**, pour démontrer *a priori* et vérifier *a posteriori* ; enregistrements à jour, accessibles, lisibles, protégés, archivés pendant une durée justifiée | Historique immuable (Polarion stocke chaque révision dans Subversion, SVN), signatures, baselines (références figées), interdiction de suppression (règle de permission PR-01), export PDF signé en GED — gestion électronique des documents — (NN-07), politique de conservation |
| **2.6.1** | Détection des écarts, y compris chez les intervenants extérieurs | `nonConformance` ouverte par tout contributeur, y compris les fournisseurs |
| **2.6.2** | Examen sans délai : importance pour la protection, qualification éventuelle en événement significatif, mesures conservatoires | Transition `characterise` du workflow `wfNonConformance` : `affectsEip`, `significantEventType`, `containmentAction`, échéance (script `fra-sla.js`) |
| **2.6.3** | Traitement dans des délais adaptés aux enjeux : causes, actions curatives, préventives, correctives, efficacité | `rootCauseCategory`, actions enfants, transition `verify` (efficacité) |
| 2.6.4 / 2.6.5 | Déclaration des événements significatifs et rapport d'analyse (rôle de l'exploitant) | `significantEventType` (information de l'exploitant) |
| 2.7.1 | Revue périodique des écarts non soldés (effet cumulé, récurrence) [P] | Tableau de bord des écarts (âge, cumul par EIP, récurrence) |

### 2.3 Décisions et guides ASN / ASNR

| Référence | Objet | Conf. | Impact |
|---|---|---|---|
| Loi n° 2024-450 du 21/05/2024 | Création de l'**ASNR** (fusion ASN + IRSN) au 1er janvier 2025 | C | Énumération `authority = asnr` |
| Décision 2015-DC-0532 (dite « décision RDS »), modifiée par la décision 2026-DC-041 | Rapport de sûreté des INB (phase de construction précisée en 2026) | C | Gabarit `safetyCase` |
| Décision 2017-DC-0616, modifiée par la décision 2023-DC-0770 | Modifications notables des INB | C | `regulatoryModificationClass`, `modificationFile` |
| Décision 2021-DC-0706 | 4e réexamen des 900 MWe (phase générique) | C | `regulatoryCommitment` (prescriptions) |
| Décision ASNR 2025-DC-016 | 4e réexamen des 1300 MWe (phase générique) | C | idem |
| Décision 2020-DC-0688 | Agrément des organismes ESPN (ISO/CEI 17020) | P (à sourcer, lot R-REG) | `witnessParty = notifiedBody` |
| Guide ASN n° 21 (2015) | Traitement des écarts de conformité à une exigence définie d'un EIP ; clôture après évaluation de l'efficacité | C | Workflow `wfNonConformance` (transition `verify` → état `effectivenessVerified`, puis `close` → `closed`) |
| Guide ASN n° 22 (2017) | Conception des REP ; base du classement EPR2 | C | `safetyClassScheme = epr2` |
| Guide n° 8 / n° 8 bis (mars 2026) | Conformité des ESPN / ESPN N1 des REP (réacteurs à eau pressurisée) | P (à sourcer, lot R-REG) | `espnLevel`, dossier ESPN |
| Guide n° 30 | Politique de protection des intérêts et SMI | P (à sourcer, lot R-REG) | Gouvernance |
| Dispositif CFSI (courrier de 2018, portail de signalement, plan d'action poursuivi en 2026) | Contrefaçons, falsifications, suspicions de fraude (CFSI : articles contrefaits, frauduleux ou suspects) | C | `cfsiSuspected` (obligatoire sur les FNC), `rootCauseCategory = cfsi` |

> Le **format de numérotation** des décisions a changé (« 2021-DC-0706 » puis « 2025-DC-016 »). Le champ `authorityReference` est donc une chaîne libre (aucun contrôle de format).

### 2.4 Équipements sous pression nucléaires : arrêté du 30 décembre 2015 modifié (2018) [C]

| Point | Contenu | Modèle |
|---|---|---|
| Article 3 | Niveaux **N1, N2, N3** par sensibilité décroissante ; catégories **0 à IV** | `espnLevel`, `espnCategory` |
| N1 | Défaillance pouvant conduire à des situations accidentelles non couvertes par le rapport de sûreté ; inclut les circuits primaire et secondaire principaux [P] | `espnLevel = n1` → points d'arrêt, accord autorité pour les FNC |
| N2 | Non N1, défaillance pouvant conduire à un rejet supérieur à 370 GBq | `n2` |
| Évaluation de conformité | N1 : ASNR ou ses mandataires ; N2 et la plupart des N3 : organismes agréés (organismes d'inspection tiers) | `witnessParties`, `authorityNotificationRequired` |
| Annexe I | Exigences essentielles de sécurité (EES) | `regulatoryRequirement` (LIB-REG) + matrice de conformité |

### 2.5 Autres codes français mobilisés par les disciplines [P\*]

| Texte | Objet | Modèle |
|---|---|---|
| Code du travail (radioprotection des travailleurs, zonage) | Discipline RPR du document 03 : dosimétrie prévisionnelle, zonage | `analysis` (`analysisType = radiological` / `doseAlara`), `operationalScenario.doseEstimate` |
| Code de la défense (protection du potentiel scientifique et technique — PPST / ZRR —, secret de la défense nationale) | Discipline SEC du document 03 ; cloisonnement des données | Instance `SENS` (règles de provisioning D05 / D06bis), `exportControl = frPpst` ; instance `DEF` (principe seul) |

## 3. Codes industriels AFCEN : éditions en vigueur [C sauf mention]

Les éditions sont celles lues sur le catalogue AFCEN ou citées par l'ASNR ; lorsque l'annexe C ne pointe pas vers la page de l'édition citée, la ligne est marquée « à vérifier » (annexe C § 5).

| Code | Dernière édition | Remarques pour l'ALM |
|---|---|---|
| RCC-M | **2024** [à vérifier : la source de l'annexe C § 5 est la page de l'édition 2020] (RCC-M 2018 + fiches 2020/2022/2024 comme référentiel ESPN ; addendum EPR2 2025) | Exigences de conception (partie B), matériaux (M), soudage (S), fabrication (F), contrôles (MC) → `equipmentRequirement.designCode`, `verificationCase` (manufacturing) |
| RCC-MRx | **2025** [à vérifier : la source de l'annexe C § 5 est la page de l'édition 2018] | Réacteurs de recherche et de fusion (CERCA, R&D) |
| RCC-E | **2025**, **au format « Requirement Engineering »** (exigences structurées et identifiées une à une ; guide PTAN-05002-2025, analyse d'écarts PTAN-05003-2025 — PTAN : publications techniques de l'AFCEN) | **Opportunité majeure** : exigences structurées et identifiées, importables comme `regulatoryRequirement` si la licence le permet (ADR-14) |
| RCC-CW (et ETC-C pour l'EPR) | **2025** | Génie civil |
| RCC-C | 2022 confirmé ; 2025 probable [P] | Combustible (`designCriterion`) |
| RSE-M | **2024** | Surveillance en service, critères de nocivité (fortuits, réexamen) |
| RCC-F (et ETC-F pour l'EPR) | **2024** | Incendie (`hazardType = intFire`) |

## 4. Normes IEC de contrôle-commande (C-C) nucléaire (sous-comité IEC SC 45A) [C sauf mention]

| Norme | Édition | Objet | Impact modèle |
|---|---|---|---|
| IEC 61513 | **Ed. 3.0, 2026** | Exigences générales des systèmes de C-C (alignée sur SSR-2/1 et SSG-39) | Gabarit `TPL-IC-PROJECT` (étapes du cycle) |
| IEC 61226 | Ed. 4.0, 2020 | Catégorisation des fonctions A/B/C, classes de systèmes 1/2/3 | `functionCategory = iecCatA/B/C`, `icSystemClass` |
| IEC 60880 | Ed. 2.0, 2006 (éd. 3 en cours) | Logiciel de catégorie A | `softwareRequirement`, V&V indépendante |
| IEC 62138 | Ed. 2.0, 2018 | Logiciel de catégories B / C | idem, indépendance graduée |
| IEC 60987 | Ed. 3.0, 2021 [P] | Matériel | `hardwareRequirement` |
| IEC 62566 / 62566-2 | 2012 [P] / 2020 | Circuits HDL (langage de description matérielle, circuits programmables ; catégorie A / B-C) | `hardwareRequirement`, `componentNature = hdlDevice` |
| IEC 62340 | 2007 | Défaillances de cause commune | `analysisType = ccfDiversity` |
| IEC 60709 | 2018 | Séparation | `reqCategory = designConstraint` |
| IEC 62645 / 63096 / 62859 | 2019 / 2020 / 2016+A1:2019 | Cybersécurité ; mesures ; coordination sûreté-sécurité | `securityDegree`, `analysisType = cyberRisk` |
| IEC 60964 / 61772 / 62241 | 2018 / 2009 [P] / 2004 [P\*] | Salle de commande, écrans, alarmes | `reqCategory = humanFactors` |
| IEC/IEEE 60780-323 / 60980-344 | 2016 / 2020 | Qualification (ambiances, séisme) | `verificationCase.qualificationStandard` |
| IEC 62003 / 61500 / 62671 | 2020 / 2018 / 2013 | CEM (compatibilité électromagnétique) ; communications de catégorie A ; appareils numériques à fonctionnalité limitée | idem |

## 5. Normes de sûreté de l'AIEA [C sauf mention]

L'AIEA (Agence internationale de l'énergie atomique) publie des *Safety Requirements* (SSR, GSR), des *Safety Guides* (SSG, GS-G), des rapports techniques (TECDOC) et une série sécurité (NSS).

| Référence | Objet | Usage dans le modèle |
|---|---|---|
| SSR-2/1 Rev.1 (2016, révision DS562 en cours) | Conception des centrales | Fonctions fondamentales de sûreté (`fundamentalSafetyFunction`), défense en profondeur |
| SSR-2/2 Rev.1 [P\*] | Mise en service et exploitation | Essais, modifications |
| GSR Part 2 (2016) | Leadership et management pour la sûreté ; **approche graduée** | Tailoring (document 07) |
| GSR Part 4 Rev.1 [P\*] | Évaluation de sûreté | `analysis` |
| SSG-30 (2014) | Classement de sûreté des SSC (structures, systèmes et composants) | `safetyClassScheme = iaeaSsg30` |
| SSG-39 [P\*] / SSG-51 (2019) / SSG-52 / SSG-56 (2020) | C-C ; facteurs humains ; cœur ; circuit primaire | Catégories d'exigences |
| SSG-71 (2022) | Modifications des centrales | `changeRequest` |
| SSG-25 (2013) | Réexamen périodique de sûreté | `TPL-IB-PSR` |
| SSG-48 (2018) | Vieillissement et exploitation à long terme | `ageingMechanism`, `analysisType = ageingLto` |
| SSG-61 (2021) | Format et contenu du rapport de sûreté | Plan type `safetyCase` |
| NSS 17-T Rev.1 (2021) | Techniques de sécurité informatique | `cybersecurity` |
| TECDOC-1335 (2003), TECDOC-1651 (2010) | Gestion de configuration des centrales | Documents 07 § 3.6 et 11 § 7 |
| GS-G-3.5 (2009 ; DS513 en cours) | Système de management | Gouvernance |
| NHSI (2022 →) | Harmonisation des SMR (petits réacteurs modulaires) | NUWARD (bibliothèque multi-juridictions) |

## 6. Ingénierie système, qualité et gestion de configuration [P\* — lot de revérification R-REG-SE]

| Référence | Édition présumée | Impact |
|---|---|---|
| ISO/IEC/IEEE 15288 | 2023 | Processus du cycle de vie (document 07) |
| ISO/IEC/IEEE 29148 | 2018 | Qualité des exigences, méthodes de vérification IADT (inspection, analyse, démonstration, test ; `verificationMethod`) |
| ISO/IEC/IEEE 42010 | 2022 | Description d'architecture (points de vue RFLP : exigences - fonctionnel - logique - physique) |
| ISO/IEC/IEEE 15289 | 2019 | Contenu des éléments d'information (gabarits) |
| ISO 10007 | 2017 | Gestion de configuration (`changeClass`, baselines) |
| SAE EIA-649C | 2019 | Gestion de configuration (classes I / II) |
| **ISO 19443** | 2018 | ISO 9001 appliquée à la chaîne d'approvisionnement nucléaire : **ITNS** (important pour la sûreté nucléaire), **CFSI** | `itns`, `cfsiSuspected` |
| ISO 9001 | 2015 + Amd 1:2024 (révision 2026 en cours) | SMQ (système de management de la qualité) |
| ASME NQA-1 / 10 CFR 50 App. B | 2022 ou plus récent | Assurance qualité nucléaire américaine ; projets US : `qaProgramLevel = nqa1AppB` |
| 10 CFR Part 21 | — | `part21Evaluation` |
| 10 CFR 50.59 | — | Modifications US (équivalent de `regulatoryModificationClass`) |
| 10 CFR Part 810 / Part 110 | — | `exportControl = us810 / us110` |
| INCOSE SE Handbook éd. 5 (2023) ; Guide to Writing Requirements v4 | — | Règles de rédaction, contrôles qualité des exigences (document 13) |
| SysML v2 (OMG, adopté en 2025) | — | Interopérabilité MBSE (ingénierie système fondée sur les modèles ; document 14) |
| NF EN 16271 | — | Analyse fonctionnelle du besoin (cahier des charges fonctionnel des outillages, document 03 OUT ; `toolingSpec`) |
| IEC 60812 / IEC 61025 | — | AMDEC / arbres de défaillance (document 03 SDF ; `fmeaItem`, `analysisType = reliability`) |
| ISO 21500 | — | Management de projet (document 03 PMO ; `risk`, `review`, `action`) |

## 7. Législation européenne et cadre transverse [P\*]

| Texte | Échéance clé | Impact |
|---|---|---|
| Règlement Machines (UE) 2023/1230 | Application au **20 janvier 2027** (abroge la directive 2006/42/CE) — même niveau [P\*] au doc. 02 § B5 ; Q-IB-07 | Outillages : `toolingSpec`, `hazardType = machinery`, analyse de risques EN ISO 12100 |
| Règlement double usage (UE) 2021/821, annexe I catégorie 0 | Mise à jour annuelle | `exportControl = euDualUse` |
| Directive NIS2 (UE) 2022/2555 (sécurité des réseaux et systèmes d'information) | Transposition française à vérifier (projet de loi « résilience » 2025) | Sécurité de la plateforme ALM (document 15) |
| Cyber Resilience Act (UE) 2024/2847 | Signalement au 11/09/2026 ; application complète au 11/12/2027 | Produits numériques livrés (C-C, outillages logiciels) : exigences de cybersécurité produit |
| eIDAS (UE) 910/2014 et eIDAS 2 (2024/1183) (identification électronique et services de confiance) | En vigueur | Valeur probante des signatures électroniques (ADR-11) |
| RGPD (règlement général sur la protection des données) | En vigueur | Minimisation des données personnelles dans l'ALM (identité des signataires uniquement) |

## 8. Réglementations étrangères (projets export) [P\*]

| Pays | Références | Impact modèle |
|---|---|---|
| Royaume-Uni | ONR (*Office for Nuclear Regulation*) : SAPs (*Safety Assessment Principles*, éd. 2014, rév. 1 de 2020) ; TAG (*Technical Assessment Guide*) NS-TAST-GD-051 (*safety case* : revendication, argument, preuve) ; TAG NS-TAST-GD-094 (catégorisation) | `safetyClaim` (CAE : *claims-arguments-evidence*), `safetyClassScheme = eprUk` |
| États-Unis | 10 CFR (*Code of Federal Regulations*, titre 10) 50 App. B, Part 21, 50.59, Part 810 ; NQA-1 ; ASME BPVC sections III (conception) et XI (inspection en service) ; Regulatory Guides C-C de la NRC | Instance US, `qaProgramLevel`, `part21Evaluation`, `equipmentRequirement.designCode` |
| Finlande | Guides YVL (règles de l'autorité finlandaise STUK) | `authority = stuk`, LIB-REG |
| International | WENRA (association des autorités de sûreté d'Europe de l'Ouest) : objectifs de sûreté des nouveaux réacteurs (2010) ; niveaux de référence (2020) | LIB-REG |

## 9. Matrice de synthèse : exigence réglementaire → impact Polarion

| # | Exigence source | Mécanisme Polarion | Élément du modèle | Contrôle |
|---|---|---|---|---|
| R1 | EIP identifiés, liste à jour (2.5.1) | Champ obligatoire + rapport | `eip`, `classificationList` | TR-07, tableau de bord EIP |
| R2 | Exigences définies (2.5.1) | Champ obligatoire, socle NN-01 | `definedRequirement` | TR-03 |
| R3 | Contrôle technique par une personne différente (2.5.3) | Condition de workflow + signature (portée par l'élément ou par son LiveDoc, ADR-30) | `approverNotAuthor`, signature `verified` / `approved` | Bloquant |
| R4 | Vérification par d'autres que les auteurs ou contrôleurs (2.5.4) | Rôle qualité, échantillonnage | `qualityEngineer` | Rapport d'échantillonnage |
| R5 | Documentation, traçabilité, archivage (2.5.6) | Historique, baselines, GED | PR-01, `createBaseline`, `exportToEdms` | Audit |
| R6 | Détection et examen des écarts (2.6.1-2.6.2) | Workflow FNC, SLA (délai de caractérisation engagé) | `nonConformance` | Âge des FNC |
| R7 | Traitement et efficacité (2.6.3) | Actions enfants, vérification | `action`, état `verified` | Bloquant (clôture) |
| R8 | Revue périodique des écarts (2.7.1) | Tableau de bord | Requêtes FNC | Revue trimestrielle |
| R9 | Surveillance des intervenants extérieurs (2.2.x) | Actions de surveillance, droits fournisseurs | `actionType = surveillance` | Rapport |
| R10 | Modifications notables (L.593-15, 2017-DC-0616) | Champ de classement + dossier | `regulatoryModificationClass` | Requis en CCB |
| R11 | Réexamen périodique (L.593-18) | Gabarit + engagements | `TPL-IB-PSR`, `regulatoryCommitment` | TR-15 |
| R12 | ESPN : niveaux, conformité, EES | Champs + bibliothèque EES + points H/W (points d'arrêt et de notification) | `espnLevel`, `inspectionPoint` | Matrice de conformité |
| R13 | Prescriptions / lettres de suite | Suivi d'engagements | `regulatoryCommitment` | Échéances |
| R14 | CFSI (ISO 19443, dispositif ASNR) | Champ obligatoire FNC | `cfsiSuspected` | Notification qualité |
| R15 | Catégorisation C-C (IEC 61226) | Champs | `functionCategory`, `icSystemClass` | TR-06 |
| R16 | Indépendance de la V&V logicielle catégorie A (IEC 60880) | Rôle et niveau d'indépendance | `independentVerifier`, `independenceLevel` | Rapport |
| R17 | Cybersécurité (IEC 62645) | Degrés, exigences | `securityDegree` | Couverture |
| R18 | Machines (2023/1230) | Analyse de risques, exigences | `hazard` (machinery) | Revue |
| R19 | Contrôle export | Champ obligatoire + ségrégation | `exportControl`, instances | PR-07 |
| R20 | Signatures électroniques (eIDAS, procédure qualité) | Ré-authentification, signification | Signatures | Validation de l'outil (document 15) |

## 10. Veille réglementaire outillée (processus LIB-REG)

1. Toute nouvelle édition d'un texte (ex. RCC-M 2024 → éditions suivantes ; IEC 61513 éd. 3) est créée dans `LIB-REG` comme nouveaux Work Items `regulatoryRequirement`. Ils sont reliés par le lien `supersedes` aux anciens, qui passent à l'état `superseded`.
2. Le document de bibliothèque est publié (transition `publish` du workflow `wfDocumentLibrary`, qui approuve en cascade les exigences qu'il contient, ADR-30). Les projets qui l'ont branché (copie liée, modifiable et fusionnable) voient leurs liens `branched_from` devenir suspects (à revoir).
3. Le `requirementsManager` (rôle projet : responsable des exigences) analyse l'impact : applicabilité contractuelle de la nouvelle édition, dispositions transitoires (`transitionalProvisions`). Il fusionne (fusion 3-way : origine, copie projet, bibliothèque modifiée), ou décide le maintien de l'édition contractuelle avec justification (`designDecision`).
4. Indicateurs :
   - projets sur une édition périmée ;
   - suspects ouverts depuis plus de N jours sur les liens vers LIB-REG.
