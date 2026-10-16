# Annexe B — Glossaire et acronymes

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **mixte** (§ 4 spécifique) · Historique : [CHANGELOG](../../CHANGELOG.md) · Carte du dépôt : [guide de lecture](../GUIDE_DE_LECTURE.md).*

**Comment lire ce glossaire.** Les entrées sont classées par thème (cinq sections ci-dessous), puis par ordre alphabétique dans chaque thème ; chaque ligne développe le sigle et dit à quoi il sert dans ce dépôt.
Les identifiants du modèle (types, champs, options, rôles, gabarits, fichiers) sont écrits en `code` et existent tels quels dans `model/` ; « [à vérifier sur la version cible] » signale une capacité Polarion dépendante de la version (annexe D).
Pour les concepts du modèle, voir le [doc. 08](../partie3/08_Modele_de_donnees.md) ; pour les listes de valeurs complètes, l'[annexe A2](../generated/A2_enumerations.md).

## 1. Nucléaire, sûreté et réglementation

| Terme / sigle | Définition | Équivalent ou forme anglaise |
|---|---|---|
| 10 CFR | Titre 10 du *Code of Federal Regulations* : réglementation nucléaire américaine (NRC). Voir 10 CFR 50 App. B, Part 21, 50.59, Part 810 ; pack `usNrc`, instance US. | 10 CFR |
| 10 CFR 50 App. B | Critères américains d'assurance qualité des centrales, avec ASME NQA-1 ; projets US : option `nqa1AppB` de `qaProgramLevel`. | 10 CFR 50 Appendix B |
| 10 CFR 50.59 | Règle américaine d'évaluation des modifications réalisables sans autorisation préalable de la NRC ; criblage renseigné avant CCB (règle TR-19, pack US). | 10 CFR 50.59 |
| 10 CFR Part 21 | Règle américaine d'obligation de signalement des défauts à la NRC ; champ `part21Evaluation`. | 10 CFR Part 21 |
| 10 CFR Part 810 / Part 110 | Réglementation américaine de contrôle export : assistance technique nucléaire (810) / équipements et matières (110) ; options `us810` / `us110` de `exportControl`. | 10 CFR Part 810 / Part 110 |
| AFCEN | Association française pour les règles de conception, de construction et de surveillance en exploitation des matériels des chaudières électronucléaires ; publie les codes RCC-x et les PTAN. | AFCEN |
| Affaire du Creusot | Irrégularités découvertes en 2016 dans des dossiers de fabrication de l'usine du Creusot (« dossiers barrés »), à l'origine des exigences d'intégrité des enregistrements (ALCOA+, doc. 15 § 5). | Le Creusot forge records |
| AIEA (SSR / SSG / GSR / GS-G / TECDOC / NSS) | Agence internationale de l'énergie atomique : exigences de sûreté (SSR, GSR), guides (SSG, GS-G), rapports techniques (TECDOC), série sécurité (NSS). Pack `intlIaea`. | IAEA |
| AIP | Activité importante pour la protection des intérêts (arrêté INB, art. 1.3) ; champ `aip` sur analyses, livrables et LiveDocs ; contrôle technique obligatoire (art. 2.5.3). | Activity important for protection |
| ALARA | « Aussi bas que raisonnablement possible » : principe d'optimisation des doses en radioprotection (discipline `rpr`, analyse `doseAlara`). | As Low As Reasonably Achievable |
| AN/GV, AN/RRA | Arrêt normal sur générateurs de vapeur (arrêt à chaud) / sur circuit de refroidissement à l'arrêt ; options `angv` / `anrra` de `plantState`. | Hot shutdown on SGs / shutdown on RHR |
| API, APR | Arrêt pour intervention / arrêt pour rechargement ; options `api` / `apr` de `plantState`. | Maintenance / refuelling shutdown |
| ARIS | Base de données de l'AIEA sur les réacteurs avancés, source OSINT pour les SMR (doc. 05 § 5). | Advanced Reactors Information System |
| Arrêté ESPN | Arrêté du 30 décembre 2015 (modifié en 2018) sur les équipements sous pression nucléaires : niveaux N1 à N3, catégories 0 à IV, exigences essentielles de sécurité. | Nuclear pressure equipment order |
| Arrêté INB | Arrêté du 7 février 2012 fixant les règles générales relatives aux installations nucléaires de base ; texte le plus structurant pour le modèle (EIP, AIP, écarts, contrôle technique). | INB Order (7 February 2012) |
| Arrêté INB art. 2.5.3 | Article imposant le contrôle technique de chaque AIP par une personne différente de celle qui l'a réalisée ; condition `approverNotAuthor` (socle NN-02). | INB Order art. 2.5.3 |
| ASME III / XI (BPVC) | Code américain des chaudières et équipements sous pression : section III conception, section XI inspection en service. | ASME Boiler & Pressure Vessel Code |
| ASN / ASNR | Autorité de sûreté nucléaire, devenue ASNR (Autorité de sûreté nucléaire et de radioprotection) le 1er janvier 2025 par fusion avec l'IRSN (loi n° 2024-450) ; option `asnr` de `authority`, pack `frAsnr`. | French nuclear safety and radiation protection authority |
| ASR, VP, VD | Arrêt pour simple rechargement / visite partielle / visite décennale ; options `asr`, `vp`, `vd` de `outageType`. Voir VD. | Refuelling outage / partial inspection outage / ten-yearly outage |
| ATF | Combustible à tolérance accrue aux accidents (ex. PROtect de Framatome) ; typologie `fuelDesign`. | Accident Tolerant Fuel |
| C-C | Contrôle-commande (discipline `icc`, BU `ics`). | Instrumentation & Control (I&C) |
| CAE / GSN | Notations d'argumentaire de sûreté : revendication – argument – preuve (TAG de l'ONR) / *Goal Structuring Notation* ; type `safetyClaim`, lien `supportedBy`. | Claims-Arguments-Evidence / Goal Structuring Notation |
| Catégorie A / B / C (fonctions de C-C) | Catégories des fonctions de contrôle-commande selon IEC 61226 ; la catégorie A exige une V&V indépendante (IEC 60880) ; options `iecCatA` / `iecCatB` / `iecCatC` de `functionCategory`. | IEC 61226 categories A / B / C |
| CFSI | Articles contrefaits, frauduleux ou suspects (ISO 19443, dispositif ASNR depuis 2018) ; champ `cfsiSuspected` obligatoire sur les FNC, cause racine `cfsi`. | Counterfeit, Fraudulent and Suspect Items |
| CGD | Dédicace d'articles commerciaux : qualification d'un composant du commerce pour un usage de sûreté (guides EPRI, 10 CFR 21) ; caractéristiques critiques vérifiées (TR-20). | Commercial Grade Dedication |
| Classe 1E | Classe électrique de sûreté américaine (IEEE) ; option `c1e` de `electricalClass`. | Class 1E |
| Classes de SSC (M / EE / E / K / SC) | Classes attribuées aux structures, systèmes et composants : mécanique (`mechanicalClass`), électrique et C-C (`electricalClass`), qualification (`qualificationClass`), sismique (`seismicCategory`), sûreté (`safetyClass`). | SSC classes |
| CND | Contrôles non destructifs (discipline `cnd`, habilitation `nde`). | NDE / NDT |
| CNSC | Commission canadienne de sûreté nucléaire (CCSN) ; option `cnsc` de `authority`, pack `caCnsc` (CNSC / CSA). | Canadian Nuclear Safety Commission |
| Code de l'environnement (Livre V, Titre IX) | Cadre législatif français des INB : intérêts protégés (L.593-1, `protectedInterest`), modifications substantielles / notables (L.593-14 / 15), réexamen décennal (L.593-18 / 19). | French Environmental Code |
| DAC | Demande d'autorisation de création d'une INB. | Construction licence application |
| DEC-A / DEC-B (RRC-A / RRC-B) | Conditions de dimensionnement étendu sans / avec fusion du cœur (EPR). | Design Extension Conditions |
| Décision RDS | Décision ASN 2015-DC-0532 relative au rapport de sûreté des INB (modifiée par 2026-DC-041) ; rattachée à `safetyCase`. À ne pas confondre avec le dossier de réexamen (rapport de conclusions, L.593-19 ; gabarit `TPL-IB-PSR`). | Safety report decision (« RDS ») |
| Décisions ASN / ASNR | Décisions réglementaires homologuées (ex. 2017-DC-0616 modifications notables ; 2021-DC-0706 et 2025-DC-016 réexamens) ; référence saisie en texte libre dans `authorityReference` (format variable). | ASN / ASNR decisions |
| Défense en profondeur | Niveaux successifs et indépendants de protection (SSR-2/1). | Defence in depth |
| Diffusion Restreinte (DR) | Mention de protection française des informations sensibles ; option `restricted` de `informationClassification`, hébergée sur l'instance SENS. | Restricted distribution |
| Dossiers barrés | Dossiers de fabrication portant des anomalies non déclarées (affaire du Creusot, 2016). | — |
| EES | Exigences essentielles de sécurité de l'annexe I de l'arrêté ESPN ; portées par des `regulatoryRequirement` dans `LIB-REG` et une matrice de conformité. | Essential safety requirements |
| EIP | Élément important pour la protection des intérêts (arrêté INB, art. 1.3) ; champ `eip`, jamais « À déterminer » à l'approbation (socle NN-01) ; liste des EIP = document `classificationList`. | Item important for protection |
| EIPS | EIP au titre de la sûreté (classement EPR2). | Safety-important item |
| EPR / EPR2 | Réacteurs à eau pressurisée de 3e génération : EPR (Flamanville 3, Olkiluoto 3, Taishan, HPC, SZC) et EPR2, nouveau réacteur d'EDF (programme de six tranches) ; options `eprFa3`, `epr2`… de `plantSeries`. | EPR / EPR2 |
| EPRI | Institut de recherche de l'industrie électrique américaine (guides de dédicace CGD). | Electric Power Research Institute |
| EPS | Études probabilistes de sûreté (discipline `eps`, analyse `psa`). | PSA (Probabilistic Safety Assessment) |
| ESP / ESPN | Équipement sous pression / équipement sous pression nucléaire (niveaux N1 à N3, catégories 0 à IV) ; champs `espnLevel`, `espnCategory`. | Pressure equipment / nuclear pressure equipment |
| ESPN N1 / N2 / N3 | Niveaux des ESPN par sensibilité décroissante : N1 (circuits primaire et secondaire principaux, évaluation par l'ASNR), N2 et N3 (organismes agréés) ; options `n1` / `n2` / `n3`. | Nuclear pressure equipment levels |
| ESS / ESR / ESE / EST | Événement significatif pour la sûreté / la radioprotection / l'environnement / le transport ; énumération `significantEventType` (caractérisation des FNC). | Significant events |
| États du réacteur (RP, AN/GV, AN/RRA, API, APR, RCD) | États standard d'une tranche, de la production au cœur déchargé ; énumération `plantState`. | Plant states |
| Exigence définie | Exigence assignée à un EIP ou à une AIP (arrêté INB, art. 1.3) ; champ `definedRequirement` ; traçabilité jusqu'à la preuve (TR-03, NN-03). | Defined requirement |
| F1A / F1B / F2 | Catégories de fonctions de sûreté de l'EPR (Flamanville 3) ; F1A = niveau le plus élevé ; options `f1a` / `f1b` / `f2` de `functionCategory`. | Safety function categories (EPR) |
| FA3 | Flamanville 3 (EPR) et son schéma de classement (F1A / F1B / F2, M, EE / E, K, SC) ; option `eprFr` de `safetyClassScheme`. | Flamanville 3 |
| Filières (REP, REB / BWR, VVER, CANDU, AGR, SMR, MTR) | Technologies de réacteurs ; énumération `reactorTechnology` (`pwrFramatome`, `bwr`, `vver`, `candu`, `agr`, `smr`, `researchReactor`…). | Reactor technologies |
| FME | Exclusion des corps étrangers (propreté des chantiers et des circuits). | Foreign Material Exclusion |
| FOH | Facteurs organisationnels et humains (discipline `foh`, IHM). | Human Factors Engineering |
| Fortuit | Aléa technique découvert pendant un arrêt de tranche, appelant une réponse rapide sous SLA ; type `technicalIssue`, typologie `fortuit` (classe D), option `forced` de `outageType`. | Emergent outage issue |
| GAIA / PROtect / M5 | Assemblage combustible Framatome / sa déclinaison ATF (gaine M5 revêtue de chrome) / alliage de zirconium de gainage. | — |
| GPR | Groupe permanent d'experts « réacteurs » auprès de l'ASN (expertise IRSN ; rapport EPR 2014 sur les classes EE / E / M). | Standing expert group (reactors) |
| GSG-1 | Guide AIEA de classification des déchets radioactifs ; énumération `wasteClass` (GAP-14). | IAEA GSG-1 |
| GSR Part 2 | Norme AIEA de leadership et de management pour la sûreté (2016) ; fonde l'approche graduée du tailoring (doc. 07). | IAEA GSR Part 2 |
| Guide ASN n° 21 | Guide (2015) sur le traitement des écarts de conformité à une exigence définie d'un EIP ; clôture après vérification d'efficacité (workflow `wfNonConformance`). | ASN Guide 21 |
| Guides ASN / ASNR | Guides non contraignants mais attendus : n° 8 / 8 bis (ESPN), n° 21 (écarts), n° 22 (conception des REP, base du classement EPR2), n° 30 (SMI). | ASN / ASNR guides |
| GV / RGV (SGR) | Générateur de vapeur / remplacement de générateurs de vapeur ; typologie `steamGeneratorReplacement`. | Steam generator / Steam Generator Replacement |
| HPC / SZC | Hinkley Point C / Sizewell C (EPR au Royaume-Uni) ; option `eprUk` de `plantSeries` et de `safetyClassScheme`. | Hinkley Point C / Sizewell C |
| IEC 60880 / 62138 / 60987 / 62566 | Normes du C-C de sûreté : logiciel de catégorie A / de catégories B-C / matériel / circuits HDL (option `hdlDevice`) ; types `softwareRequirement`, `hardwareRequirement`. | IEC I&C standards |
| IEC 61226 | Norme de catégorisation des fonctions (A / B / C) et de classement des systèmes de C-C (1 / 2 / 3) ; `functionCategory`, `icSystemClass`. | IEC 61226 |
| IEC 61513 | Norme cadre des systèmes de contrôle-commande nucléaire (sous-comité IEC SC 45A) ; gabarit `TPL-IC-PROJECT`. | IEC 61513 |
| IEC 62645 / 63096 / 62859 | Normes de cybersécurité du C-C nucléaire (mesures, coordination sûreté-sécurité) ; champ `securityDegree`, analyse `cyberRisk`. | IEC cybersecurity standards |
| INB | Installation nucléaire de base (réacteur, usine du cycle…), régime du Code de l'environnement. | Basic nuclear installation |
| Intervenant extérieur | Sous-traitant ou fournisseur au sens de l'arrêté INB ; surveillance proportionnée aux enjeux, tracée par des actions de surveillance (art. 2.2 ; option `surveillance` de `actionType`). | External contractor |
| IPS | Important pour la sûreté : terminologie historique du parc (IPS / IPS-NC) ; option `frLegacy` de `safetyClassScheme`. | Important to safety |
| IRSN | Institut de radioprotection et de sûreté nucléaire (expertise), fusionné dans l'ASNR le 1er janvier 2025. | IRSN |
| ISI | Inspection en service (RSE-M, ASME XI) ; typologie `inspectionService`. | In-Service Inspection |
| ITNS | Important pour la sûreté nucléaire (ISO 19443) ; champ `itns`. | Important To Nuclear Safety |
| Joint Early Review | Revue réglementaire précoce menée conjointement par plusieurs autorités européennes (NUWARD) [P]. | Joint Early Review |
| k-eff | Facteur de multiplication neutronique effectif (criticité). | k-effective |
| K1 / K2 / K3 / AG | Conditions de qualification des matériels : bâtiment réacteur en accident (K1) / en fonctionnement normal (K2) / hors bâtiment réacteur (K3) ; AG = K1 renforcé accident grave (EPR) ; options `k1`, `k2`, `k3`, `sa` de `qualificationClass`. | Equipment qualification classes |
| KTA | Règles de sûreté nucléaire allemandes (*Kerntechnischer Ausschuss*) ; pack `deKta`, option `deKta` de `safetyClassScheme`. | KTA safety standards |
| LEU+ / HALEU | Uranium faiblement enrichi « plus » (5 à 10 %) / uranium à enrichissement intermédiaire (5 à 20 %) [P] ; enjeux de criticité et de licence d'usine (doc. 02 F bis). | LEU+ / HALEU |
| LTO | Exploitation à long terme (SSG-48) ; champ `ageingMechanism`, analyse `ageingLto`. | Long-Term Operation |
| Marquage CE | Conformité européenne des machines ; règlement (UE) 2023/1230 applicable au 20 janvier 2027 ; outillages (`toolingSpec`, option `machinery` de `hazardType`). | CE marking |
| Modification notable / substantielle | Classement réglementaire d'une modification d'INB (Code de l'environnement L.593-14 / 15, décision 2017-DC-0616) ; énumération `regulatoryModificationClass`, dossier `modificationFile`. | Notable / substantial modification |
| MSI | Mise en service industrielle. | Commercial operation |
| MTR | Réacteur d'essai de matériaux (réacteur de recherche) ; typologie `researchReactorFuel`. | Materials Testing Reactor |
| NHSI | Initiative AIEA d'harmonisation et de standardisation réglementaire des SMR (2022 →) ; bibliothèque multi-juridictions NUWARD. | Nuclear Harmonization and Standardization Initiative |
| NQA-1 | Norme américaine d'assurance qualité nucléaire (ASME) ; option `nqa1AppB` de `qaProgramLevel`. | ASME NQA-1 |
| NRC | Autorité de sûreté américaine (base documentaire ADAMS, rapports FSAR) ; option `nrc` de `authority`, pack `usNrc`, instance US. | Nuclear Regulatory Commission |
| NSSS | Chaudière nucléaire : circuit primaire et ses composants (cuve, générateurs de vapeur, pompes, pressuriseur). | Nuclear Steam Supply System |
| NUWARD | Projet de petit réacteur modulaire (SMR) porté par EDF, Framatome partenaire ; premier pilote Polarion (fiche `P-NUWARD-L1`, ligne de produits `PL-NUWARD`). | NUWARD SMR |
| ONR (SAPs / TAG) | Autorité de sûreté britannique ; ses principes d'évaluation de sûreté (SAPs) et guides techniques (TAG, dont le *safety case* par revendication – argument – preuve) ; option `onr`, pack `ukOnr`. | Office for Nuclear Regulation |
| OPECST | Office parlementaire d'évaluation des choix scientifiques et technologiques (source OSINT). | OPECST |
| Organismes agréés | Organismes d'inspection tiers chargés de l'évaluation de conformité des ESPN N2 / N3 (décision 2020-DC-0688) ; option `notifiedBody` de `witnessParty`. | Notified bodies |
| Paliers CP0 / CPY / P4 / P'4 / N4 | Familles de centrales REP du parc français (900, 1300 et 1450 MWe) ; énumération `plantSeries`. | French PWR series |
| PAR | Recombineur autocatalytique passif d'hydrogène (produit catalogue, typologie `configureToOrder`). | Passive Autocatalytic Recombiner |
| PCC-1 à 4 / DBC-1 à 4 / DEC | Conditions de fonctionnement de dimensionnement, catégories 1 à 4 (terminologie EPR / internationale) ; DEC = conditions de dimensionnement étendu (voir DEC-A / DEC-B). | Plant / Design Basis Conditions, Design Extension Conditions |
| PPST / ZRR | Protection du potentiel scientifique et technique de la nation / zones à régime restrictif (Code de la défense) ; option `frPpst` de `exportControl` → instance SENS (règle D06bis). | French PPST scheme / restricted zones |
| PTAN | Publications techniques de l'AFCEN (ex. PTAN-05002-2025, guide du RCC-E au format « Requirement Engineering »). | AFCEN technical publications |
| RCC-E | Code AFCEN des matériels électriques et de contrôle-commande ; édition 2025 au format « Requirement Engineering » (exigences identifiées une à une), importable comme `regulatoryRequirement` sous licence (ADR-14). | AFCEN electrical & I&C code |
| RCC-M / -E / -C / -CW / -F, RSE-M, RCC-MRx, ETC-C / ETC-F | Codes AFCEN : mécanique / électricité et C-C / combustible / génie civil / incendie ; surveillance en exploitation ; réacteurs de recherche ; déclinaisons EPR du génie civil et de l'incendie. Éditions en vigueur : doc. 04 § 3. | AFCEN codes |
| RCD | Réacteur cœur déchargé ; option `rcd` de `plantState`. | Core fully offloaded |
| RE (format) | *Requirement Engineering* : format du RCC-E 2025 où chaque exigence est structurée et identifiée (guide PTAN-05002-2025). À ne pas confondre avec RE = responsable des exigences (§ 2). | Requirement Engineering format |
| Réexamen périodique | Réexamen de sûreté tous les dix ans (L.593-18), conclu par un rapport de conclusions (L.593-19) ; typologie `periodicSafetyReview`, gabarit `TPL-IB-PSR`, prescriptions suivies par `regulatoryCommitment`. | Periodic safety review |
| REP | Réacteur à eau pressurisée ; options `pwrFramatome` / `pwrOther` de `reactorTechnology`. | PWR |
| Revendication (claim) | Affirmation de sûreté à démontrer, racine d'un argumentaire ; type `safetyClaim`, étayée par des analyses ou des cas (`supportedBy`, TR-13). | Claim |
| RP | Selon le contexte : réacteur en production (option `rp` de `plantState`) ou radioprotection (discipline `rpr`, sigle du doc. 02). | Power operation / radiation protection |
| RSE-M | Code AFCEN de surveillance en exploitation des matériels mécaniques (critères de nocivité : fortuits, réexamen). | RSE-M code |
| S1 / S2 / S3 | Classes de sûreté des SSC (EPR2, guide ASN n° 22) ; options `sc1` / `sc2` / `sc3` de `safetyClass`. À ne pas confondre avec SC1 / SC2 (sismique) ni SC-xx (§ 5). | Safety classes |
| SC1 / SC2 | Classes sismiques de l'EPR : SC1 fonctionne pendant et après le séisme ; options `seis1` / `seis2` de `seismicCategory`. À ne pas confondre avec `sc1`..`sc3` (classes de sûreté) ni SC-xx (critères de succès). | Seismic classes |
| SMR | Petit réacteur modulaire (NUWARD) ; typologie `newBuildSmr`, option `smr`. | Small Modular Reactor |
| SSC | Structures, systèmes et composants, objets du classement de sûreté ; type `physicalComponent`, jeu d'attributs `sscClassification`. | Structures, Systems and Components |
| SSG-30 | Guide de sûreté AIEA (2014) sur le classement des SSC ; option `iaeaSsg30` de `safetyClassScheme`. | IAEA SSG-30 |
| SSR-2/1 | Exigences AIEA de conception des centrales : fonctions fondamentales de sûreté (`fundamentalSafetyFunction`), défense en profondeur. | IAEA SSR-2/1 |
| SÚJB | Autorité de sûreté tchèque ; option `sujb` de `authority`. | SÚJB |
| VD / VD4 | Visite décennale : arrêt réalisant les épreuves (circuit primaire, enceinte) et les modifications du réexamen ; VD4 = quatrième visite décennale (900 / 1300 MWe). Option `vd`. | Ten-yearly outage |
| VVER | Réacteur à eau pressurisée de conception russe (ANF Lingen autorisé pour le VVER-1000 en 2026) ; option `vver`. | VVER |
| WENRA | Association des autorités de sûreté d'Europe de l'Ouest (objectifs de sûreté des nouveaux réacteurs, niveaux de référence). | WENRA |
| YVL / STUK | Guides YVL de l'autorité de sûreté finlandaise STUK ; option `stuk` de `authority`. | YVL guides / STUK |
| Zone contrôlée | Zone à accès réglementé pour la radioprotection (Code du travail) ; contraint l'accès à l'outil pendant les arrêts (F-12). | Controlled area |

## 2. Ingénierie système, qualité et gestion de projet

| Terme / sigle | Définition | Équivalent ou forme anglaise |
|---|---|---|
| 21 CFR Part 11 / EudraLex annexe 11 | Règles américaine (FDA) et européenne (BPF) sur les systèmes informatisés, enregistrements et signatures électroniques ; pack `medicalGmp` (validation IQ / OQ / PQ). | 21 CFR Part 11 / EU GMP Annex 11 |
| 95e centile | Valeur sous laquelle se situent 95 % des mesures (seuil de temps de réponse de l'indicateur K-OPS-01). | 95th percentile |
| ALCOA+ | Propriétés d'intégrité des enregistrements : attribuable, lisible, contemporain, original, exact, plus complet, cohérent, durable, disponible (doc. 15 § 5). | ALCOA+ |
| AMDEC | Analyse des modes de défaillance, de leurs effets et de leur criticité (IEC 60812) ; type `fmeaItem`, document `fmeaWorksheet`, indice RPN. | FMEA / FMECA |
| Aval / amont | Amont = ce qui vient en premier dans le cycle en V (besoin, exigence supérieure, hypothèse, preuve) ; aval = ce qui en dépend. Un lien part toujours de l'aval vers l'amont (doc. 09 § 1). | Downstream / upstream |
| Backlog | Liste priorisée et visible des évolutions demandées (boucle d'amélioration du référentiel, doc. 17 § 5). | Backlog |
| BPF | Bonnes pratiques de fabrication pharmaceutiques (isotopes médicaux) ; qualifications QI / QO / QP ; pack `medicalGmp`, habilitation `gmp`. | GMP (Good Manufacturing Practice) |
| Burn-up | Courbe cumulée du réalisé face au total planifié (avancement V&V, indicateur K-VV-03). | Burn-up chart |
| CAO | Conception assistée par ordinateur (maquette 3D dans le PLM ; discipline `lay`). | CAD |
| CAPA | Actions correctives et préventives (traitement des écarts ; ADR-13). | Corrective and Preventive Actions |
| CCB | Comité de maîtrise des modifications d'un projet (`ccbChair`, `ccbMember`, état `ccbReview`) ; le « CCB du modèle » statue sur les évolutions du modèle de données (doc. 17 § 2). | Change Control Board |
| CdC | Cahier des charges ; cahier des charges fonctionnel des outillages selon NF EN 16271 (document `toolingSpec`). | Specification |
| CEM | Compatibilité électromagnétique (IEC 62003 ; qualification des matériels, discipline `qmt`). | EMC |
| Classe I / II (modification) | Classes de modification (ISO 10007, EIA-649) : classe I en CCB complet (impacts avant CCB, TR-12), classe II en CCB allégé (transition `approveClassII`) ; énumération `changeClass`. | Change class I / II |
| Concept d'emploi | Description de la manière dont le système sera utilisé (scénarios opérationnels) ; type `operationalScenario`. | Concept of operations (ConOps) |
| Concession | Acceptation en l'état d'un écart après réalisation ; option `concession` de `waiverType` (type `waiver`). | Concession |
| Contrôle technique | Vérification par une personne différente de l'auteur, tracée par les Approvals (condition `approverNotAuthor`) et signée pour les documents (arrêté INB art. 2.5.3, socle NN-02). | Technical check |
| CP / RE / RT / GI | Chef de projet (`projectManager`) / responsable des exigences (`requirementsManager`) / responsable technique (`technicalLead`) / gestionnaire d'interfaces (`interfaceManager`) : publics des indicateurs du doc. 13. | Project manager / requirements manager / technical lead / interface manager |
| Cycle en V | Enchaînement d'une branche descendante (définition) et d'une branche montante (V&V) ; la « profondeur du V » est le nombre de niveaux de décomposition entre le besoin et les éléments vérifiés. | V-model |
| Décision de conception | Work Item `designDecision` traçant une décision, ses options et sa justification (ex. maintien d'une ancienne édition de code). | Design decision |
| Deviation permit | Dérogation accordée avant réalisation (autorisation d'écart) ; option `deviationPermit` de `waiverType`. | Deviation permit |
| DM / ECR / ECO | Demande de modification (`changeRequest`, ECR côté Polarion) / ordre de modification produit exécuté dans le PLM (ECO). | Change Request / Engineering Change Request / Engineering Change Order |
| EARS | Formes de phrases normalisées pour rédiger les exigences ; champ `requirementPattern`, score `requirementQualityScore`. | Easy Approach to Requirements Syntax |
| FAT / SAT | Essais de réception en usine / sur site. | Factory / Site Acceptance Test |
| FBS / PBS / WBS | Arborescences fonctionnelle / produit (articles de configuration) / des travaux (lien avec la planification et l'ERP ; champ `wbsCode`). | Functional / Product / Work Breakdown Structure |
| FNC | Fiche de non-conformité : type `nonConformance`, workflow `wfNonConformance` (caractérisation `characterise` sous échéance, actions, vérification d'efficacité, clôture). | Non-Conformance Report |
| Go / no-go | Décision formelle de lancer ou non une étape (ici le pilote, étape S12 du doc. 23). | Go / no-go |
| H / W / R (points d'inspection) | Point d'arrêt (*Hold* : l'activité ne continue pas sans l'accord du client ou de l'inspecteur), point de convocation (*Witness* : il est prévenu, l'activité peut continuer), revue documentaire (*Review*) ; énumération `inspectionPoint`. | Hold / Witness / Review points |
| HDL / FPGA | Langage de description matérielle / circuit logique programmable (IEC 62566) ; type `hardwareRequirement`, option `hdlDevice`. | Hardware Description Language / FPGA |
| HVAC | Chauffage, ventilation, climatisation (discipline `hva`). | HVAC |
| Hypercare | Support renforcé pendant les premières semaines après un démarrage (6 semaines par vague, doc. 16). | Hypercare |
| IADT | Méthodes de vérification : inspection, analyse, démonstration, test (ISO/IEC/IEEE 29148) ; énumération `verificationMethod`. | IADT |
| ICD | Document de contrôle d'interfaces, généré depuis le registre des interfaces (côtés A et B) par périmètre contractuel ; document `interfaceControlDocument`. | Interface Control Document |
| IHM | Interface homme-machine (facteurs humains, IEC 60964). | HMI |
| INCOSE (HBK, GtWR) | Association internationale d'ingénierie système ; son manuel (*SE Handbook*, éd. 5) et son guide de rédaction des exigences (*Guide to Writing Requirements*), base des règles du doc. 07 § 3.2. | INCOSE / Systems Engineering Handbook / Guide to Writing Requirements |
| Interface | Work Item `interface` avec exactement un côté A et un côté B (`sideA`, `sideB`, règle TR-08), un type (`interfaceType`), une portée et une maturité (gel `frozen`). | Interface |
| IQ / OQ / PQ | Qualification d'installation / opérationnelle (l'outil configuré fait ce qui est spécifié) / de performance (en conditions réelles) : validation de l'outil (doc. 15 § 4). | Installation / Operational / Performance Qualification |
| IS | Ingénierie système : discipline qui conçoit un système complet, du besoin à la validation (ISO/IEC/IEEE 15288 ; discipline `sys`). | Systems Engineering (SE) |
| ISO 10007 / EIA-649 | Normes de gestion de configuration (classes de modification, baselines). | ISO 10007 / SAE EIA-649 |
| ISO 19443 | ISO 9001 appliquée à la chaîne d'approvisionnement nucléaire (2018) : notions ITNS et CFSI ; avec ISO 9001 § 7.5 (informations documentées), référence des procédures qualité (F-09). | ISO 19443 |
| ISO 31000 / IEC 60812 | Management du risque (type `risk`) / analyse des modes de défaillance (AMDEC). | ISO 31000 / IEC 60812 |
| ISO/IEC 17025 | Compétence des laboratoires d'essais (typologie `labTesting`). | ISO/IEC 17025 |
| ISO/IEC/IEEE 15288 | Norme internationale des processus du cycle de vie d'un système, cadre du doc. 07 ; complétée par 29148 (exigences), 42010 (architecture), 15289 (contenu des documents). | ISO/IEC/IEEE 15288 |
| j·h / ETP | Jour-homme (une personne pendant une journée) / équivalent temps plein : unités des estimations d'effort du doc. 23 § 2. | Person-day / FTE |
| KPI | Indicateur clé de performance, ici toujours calculé depuis les données, jamais saisi (catalogue K-xxx du doc. 13). | Key Performance Indicator |
| Lot de travaux | Contrat interne entre un projet et une UO réalisatrice (ADR-24) ; type `workPackage`, lien `inWorkPackage`, règle TR-18, document `workPackageHandover`. | Work package |
| Matrice N² | Matrice N × N des disciplines dont chaque case hors diagonale est une interface (doc. 03 § 2) ; rapport LiveReport côté A / côté B. | N² chart |
| MBSE | Ingénierie système fondée sur les modèles : l'architecture est un modèle (Capella / Arcadia, Cameo / SysML), pas un document ; Capella maître (ADR-08). | Model-Based Systems Engineering |
| NF EN 16271 | Norme d'expression fonctionnelle du besoin (cahier des charges fonctionnel des outillages). | EN 16271 |
| OTP / commande interne | Organigramme des tâches du projet (structure de découpage, équivalent du WBS) / ordre de travail de l'ERP qui porte le budget d'un lot ; champ `internalOrderReference`. | WBS / internal order |
| P × I | Criticité d'un risque = probabilité × impact. | Probability × impact |
| Pareto | Classement des causes par fréquence décroissante (indicateur K-NC-05). | Pareto chart |
| Plan de management de l'interface | Document contractuel fixant avec un client ou un fournisseur ce qui est échangé, par qui et quand (gabarit ReqIF négocié). | Interface management plan |
| PMO | Bureau de pilotage du programme (discipline `pmo`). | Program Management Office |
| Porte (gate) | Jalon de décision assorti de critères de sortie explicites, prononcé par le comité de pilotage (G0 à G3, doc. 16) ; option `gate` de `reviewType`. | Gate |
| PQP / PMIS / PGC / PDL | Plan qualité projet / plan de management de l'ingénierie système / plan de gestion de configuration / plan de développement logiciel ; document `managementPlan`. | QAP / SEMP / CMP / SDP |
| PV | Procès-verbal (d'essais, de remise de lot). | Test report / handover report |
| RACI | Matrice des responsabilités : réalise / approuve / consulté / informé (doc. 07 § 5). | Responsible, Accountable, Consulted, Informed |
| Revues (SRR / PDR / CDR / MRR / TRR / FQR) | Revues des exigences système / de conception préliminaire / de conception détaillée (critique) / d'aptitude à la fabrication / d'aptitude aux essais / de qualification ; énumération `reviewType`, type `review`. | System Requirements / Preliminary Design / Critical Design / Manufacturing Readiness / Test Readiness / Formal Qualification Review |
| REX | Retour d'expérience ; fiche `lessonLearned`, lien `capitalizes` (GAP-11). | Operating experience / lessons learned |
| RFLP | Méthode d'architecture en quatre vues : exigences, fonctionnel, logique, physique (ISO/IEC/IEEE 42010) ; types `function`, `logicalComponent`, `physicalComponent`. | Requirements-Functional-Logical-Physical |
| RPN | Indice de criticité d'une ligne d'AMDEC. | Risk Priority Number |
| Run | Exploitation courante après déploiement (phase 5 du doc. 16). | Operations / run |
| SDM | Dossier de conception système ; document `systemDesignManual`. | System Design Manual |
| SDRL | Liste des documents dus par un fournisseur ou une usine ; champs `sdrlReference`, `submittalPurpose` (GAP-15). | Supplier Document Requirements List |
| SECM / EIA-731 ; INCOSE MBCM | Modèle de maturité en ingénierie système / matrice de capacités fondées sur les modèles de l'INCOSE (mesure de maturité, F-24). | SE Capability Model / Model-Based Capabilities Matrix |
| SLA | Délai de réponse engagé ; échéance calculée au triage selon l'urgence par le script `fra-sla.js` (champ `responseDueDate`). | Service Level Agreement |
| SMI / SMQ | Système de management intégré (arrêté INB art. 2.4) / système de management de la qualité (ISO 9001). | Integrated / quality management system |
| STB / ST / STE / SRS | Spécification technique de besoin (`stakeholderSpec`) / technique système (`systemSpec`) / d'équipement ou d'approvisionnement (`equipmentSpec`) / d'exigences logicielles (`softwareRequirementsSpec`). | Stakeholder / System / Equipment / Software requirements specification |
| SysML (v1 / v2) | Langage de modélisation système de l'OMG (Cameo / CATIA Magic) ; la v2 (2025) ajoute une API normalisée (interopérabilité MBSE, doc. 14). | SysML |
| SysML deriveReqt / refine / satisfy / verify | Relations normalisées entre exigences et conception ; correspondance avec les rôles de liens `flowsDownFrom`, `refines`, `satisfies`, `verifies`. | SysML relationships |
| Tailoring | Adaptation graduée des moyens d'ingénierie aux enjeux du projet (GSR Part 2, ISO 15288), sans toucher au socle non négociable ; classes A à D (§ 5), `tailoring.yaml`. | Tailoring |
| TBD / TBC | À déterminer / à confirmer : valeurs de maturité d'une exigence (`maturity`) ; `tbd` est aussi la valeur par défaut des champs de sûreté (`yesNoTbd`, principe P4). | To Be Determined / To Be Confirmed |
| TRL | Niveau de maturité technologique (programmes R&D, typologie `rdProgram`). | Technology Readiness Level |
| URS | Exigences utilisateur de l'outil, base de sa validation (doc. 15 § 4) ; tracées vers le modèle et le socle NN-01..08. | User Requirements Specification |
| V&V | Vérification (le produit est conforme à sa spécification) et validation (il répond au besoin) ; liens `verifies` / `validates`, type `verificationCase`. | Verification & Validation |
| V&V indépendante | Vérification et validation par une organisation distincte (logiciel de catégorie A, IEC 60880) ; champs `independentVerifier`, `independenceLevel`. | Independent V&V |

## 3. Organisation et écosystème Framatome

| Terme / sigle | Définition | Équivalent ou forme anglaise |
|---|---|---|
| Architecte-ensemblier | EDF / Edvance : maître d'œuvre d'ensemble, responsable de la conception de l'îlot nucléaire ; échanges ReqIF aller-retour et projet sas (ADR-12). | Lead architect-engineer |
| Base installée (IB) | Activités pour les centrales en exploitation : BU `ib` ; typologies RGV, réexamen, modifications, fortuits, outillages, inspection, démantèlement… ; archétype `TPL-02-IB`, groupe de projets `IB`. | Installed Base |
| BI | Dans les libellés d'énumération, le doc. 00 et le doc. 13 (publics des indicateurs), « BI » = BU Base installée (chef de projet d'arrêt, cellule fortuits). Au doc. 13 § 7 et à la fiche I-10, « BI » = informatique décisionnelle (§ 4). | Installed Base BU / Business Intelligence |
| BL | Business Line : ligne d'activité à l'intérieur d'une BU (ex. `ibEngineering`, `valves`, `icCyber`) ; énumération `businessLine` (28 valeurs, portée projet). Rappel : BL = `businessLine`, UO = `operationalUnit`. | Business Line |
| BU | Business Unit : division de premier niveau de l'entreprise ; énumération `businessUnit` (`ib`, `fuel`, `ics`, `pcm`, `dti`, `corp`, `healthcare`, `defense`, `space`). L'organisation n'est jamais codée dans les identifiants (P8). | Business Unit |
| BU Framatome (IB, Fuel, ICS, PCM, DTI) | Base installée (`ib`) / Combustible (`fuel`) / Contrôle-commande (`ics`) / Projets et fabrication de composants (`pcm`) / Direction technique et ingénierie (`dti`, comptée publiquement comme BU) ; doc. 01 § 2. | Framatome business units |
| Champion | Utilisateur relais formé en premier (un par projet de classe A / B, un par équipe), appui de niveau 1 pour son équipe (doc. 17). | Champion / key user |
| Comex | Comité exécutif de l'entreprise ; porte le sponsor du programme. | Executive committee |
| Comité de pilotage | Instance qui arbitre périmètre, budget, vagues et risques du programme et prononce les portes G0 à G3 (doc. 16, doc. 17 § 1). | Steering committee |
| Corys | Société de simulateurs (Framatome 50 %, EDF 25 %, IFP Training 25 %) [P] ; typologie `simulator`. | Corys |
| CSE / Betriebsrat (BetrVG § 87) | Comité social et économique (France) / comité d'entreprise (Allemagne, codécision au titre de la loi BetrVG § 87) : à consulter avant un déploiement qui trace l'activité des salariés (F-01). | Works council |
| Design Authority ALM (DA ALM) | Autorité de conception : propriétaire du modèle de données et de la configuration, anime le CCB du modèle (doc. 17) ; rôle global `designAuthority`. Distincte de la direction « Engineering & Design Authority » de l'entreprise et de `libraryDesignAuthority` (rôle projet d'une bibliothèque ou d'un produit générique). | Design Authority |
| DPO | Délégué à la protection des données (RGPD). | Data Protection Officer |
| DSI | Direction des systèmes d'information : exploite la plateforme (administration, environnements, sauvegardes, montées de version). | IT department |
| EDF | Exploitant du parc nucléaire français et groupe auquel Framatome est rattachée (segment Framatome de l'URD d'EDF) ; client et architecte-ensemblier des nouveaux réacteurs avec Edvance. | EDF |
| Edvance | Filiale d'ingénierie EDF (80 %) / Framatome (20 %) chargée de la conception d'ensemble de l'îlot nucléaire ; UO `edvance`. | Edvance |
| Filiales et entités | Intercontrôle (CND), Framatome ARC, Framatome Inc., Canada, Ltd (UK), Reaktortest, ANF GmbH, CERCA, Jeumont Electric, Allentis / Cyberwatch / FoxGuard (cyber), Vanatome / Segault / Valserve / Sebim (robinetterie) ; doc. 01 § 3, énumérations `businessLine` / `operationalUnit`. | Subsidiaries and entities |
| Framatome Defense / Healthcare / Space | Marques hors électronucléaire (2020 / 2021 / 2023) ; BU `defense`, `healthcare`, `space` ; typologies `defenseProgram` (instance DEF, principe seul) et `isotopeProduction`. | — |
| FSD | Fonctionnaire de sécurité et de défense (dispositif PPST). | Security and defence officer |
| ICONE / ICAPP / NPIC&HMIT / INCOSE IS | Conférences internationales de génie nucléaire, de contrôle-commande et d'ingénierie système (sources OSINT, doc. 05 § 5). | Conferences |
| Intégrateur | Prestataire qui configure et développe pour le compte de Framatome, dans son dépôt et sous sa CI, sans perte de maîtrise (doc. 24 § 5). | Integrator |
| N0 … N3 (support) | Échelons de support, du libre-service (N0) à l'éditeur (N3) (doc. 17 § 4). À ne pas confondre avec les niveaux ESPN N1 à N3. | Support tiers |
| RSSI | Responsable de la sécurité des systèmes d'information (homologation, SOC, F-06). | CISO |
| SE Referent | Référent ingénierie système d'une BU ou d'un projet : anime les pratiques, répond au questionnaire de provisioning, construit les gabarits ; membre du CCB du modèle. | SE Referent |
| SFEN / RGN | Société française d'énergie nucléaire / Revue générale nucléaire (sources OSINT). | SFEN |
| SPACE / SIVAT | Outils d'ingénierie (spécification) et de validation (simulation) de la plateforme TELEPERM XS ; fiche d'intégration I-07. | SPACE / SIVAT |
| Sponsor | Dirigeant du Comex qui porte le programme ALM devant le comité de pilotage (doc. 17 § 1). | Executive sponsor |
| SWITCH (3DX SWITCH) | Programme d'outillage numérique d'ingénierie d'EDF, fondé sur 3DEXPERIENCE ; interopérabilité attendue avec l'exploitant (F-11). | SWITCH |
| TXS | TELEPERM XS : plateforme de contrôle-commande de sûreté de Framatome (outils SPACE / SIVAT) ; autres plateformes attestées : Spinline / Rodline / Hardline (ex-Rolls-Royce), Tricon / SPEC 200 (ex-Schneider). Typologie `icPlatform`. | TELEPERM XS |
| UO | Unité opérationnelle : entité de réalisation (site, usine, centre d'ingénierie, filiale) ; énumération `operationalUnit` (43 valeurs, amorce OSINT à remplacer en atelier, Q-ORG-01). Rappel : UO = `operationalUnit`, BL = `businessLine`. | Operational unit |
| URD | Document d'enregistrement universel : rapport annuel réglementé d'EDF (segment Framatome), source OSINT. | Universal Registration Document |

## 4. Polarion, outils et SI

| Terme / sigle | Définition | Équivalent ou forme anglaise |
|---|---|---|
| 3DX / 3DEXPERIENCE (Core Model) | Plateforme PLM de Dassault Systèmes, PLM de référence attesté chez Framatome (« Core Model » pour l'ingénierie système et le PLM) ; frontière avec Polarion fixée par l'ADR-07 ; connecteur `CX-PLM-3DX`. | 3DEXPERIENCE |
| AIPD | Analyse d'impact relative à la protection des données (RGPD art. 35) sur journaux, signatures et habilitations (F-02). | DPIA |
| ALM | Gestion du cycle de vie des applications : ici le référentiel d'ingénierie (exigences, essais, documents) et la licence Polarion complète ; Polarion est l'outil ALM de Siemens. | Application Lifecycle Management |
| ANSSI | Agence nationale de la sécurité des systèmes d'information (doctrine, qualifications). | French national cybersecurity agency |
| API REST / REST | Interface web programmable de Polarion (jetons d'accès, connecteurs, extraction BI) ; désactivée par défaut, activée en PROD pour les intégrations [à vérifier sur la version cible : noms des propriétés]. | REST API |
| Approvals | Mécanisme natif Polarion d'approbation nominative d'un Work Item ou d'un document par des approbateurs désignés, sans signature électronique ; trace du contrôle technique (`approverNotAuthor`). | Approvals |
| Bac à sable | Instance Polarion d'essai sans donnée réelle, où bouchons et expérimentations sont admis (projet `SANDBOX`, incubation, ateliers C2 / C3). | Sandbox |
| Baseline | Révision figée de tout un projet Polarion, servant de référence de configuration ; convention `baselineNaming`, fonction `createBaseline` à l'approbation d'un document ou à la clôture d'une DM. | Baseline |
| Bastion | Poste d'administration isolé et tracé (comptes à privilèges nominatifs). | Bastion host |
| BI (informatique décisionnelle) | Entrepôt de données et outils d'analyse de l'entreprise, alimentés par extraction nocturne via l'API REST (doc. 13 § 7, fiche I-10). Voir aussi « BI » au § 3 (base installée). | Business Intelligence |
| Bibliothèque (LIB-*) | Projet référentiel partagé en lecture seule : `LIB-REG` (réglementaire), `LIB-TERM` (glossaire), `LIB-TEMPLATES` (gabarits), `LIB-HAZARD` (agressions), `LIB-VV` (cas génériques), `LIB-PROCESS` (processus, REX, hypothèses OSINT), `LIB-CYBER` ; groupe `CORP`. | Library project |
| Bouchon | Version provisoire d'un script qui ne fait que journaliser son appel ; admis en bac à sable seulement ; un bouchon « toujours vrai » est interdit hors bac à sable. | Stub |
| Branche (de document) | Copie d'un document qui garde la mémoire de son origine (lien `branched_from`) et peut être fusionnée avec elle ; patron de réutilisation par défaut des bibliothèques (ADR-06) [à vérifier sur la version cible : fusion annoncée 2404+]. | Document branch |
| Cameo / CATIA Magic | Outil de modélisation SysML (Dassault Systèmes), utilisé si un client ou un partenaire l'impose ; connecteur `CX-MBSE-CAMEO` (OSLC RM ou ReqIF) [P]. | Cameo / CATIA Magic |
| Capella / Arcadia | Atelier libre de modélisation d'architecture système et sa méthode (couches opérationnelle, fonctionnelle, logique, physique) ; maître de l'architecture (ADR-08), connecteur `CX-MBSE-CAPELLA`. | Capella / Arcadia |
| Cascade document → éléments | Soumission et approbation des Work Items pilotés par un LiveDoc, déclenchées par les transitions du document (fonction `InvokeAction`, condition `cascadedItemsApproved` : tous les éléments pilotés approuvés) ; ADR-30. | Document cascade |
| CMIS | Standard d'accès aux systèmes de gestion documentaire (connecteur GED `CX-EDMS`). | Content Management Interoperability Services |
| Collection | Ensemble de documents Polarion pris chacun à une révision donnée, possiblement de plusieurs projets ; convention `collectionNaming` (affaires de la base installée) [hiérarchie de collections à vérifier sur la version cible : 2410+]. | Collection |
| Condition bloquante | Condition de workflow qui refuse une transition tant qu'elle n'est pas remplie (ex. `approverNotAuthor`, `noSuspectLinks`, `qualifiedSignatory`, `noForbiddenClassification`). | Blocking condition |
| Connecteurs (CX-*) | Fiches de connecteurs de `import_export.yaml` : `CX-PLM-TC`, `CX-PLM-3DX`, `CX-MBSE-CAPELLA`, `CX-MBSE-CAMEO`, `CX-SIMULINK`, `CX-CALC`, `CX-TEST-BENCH`, `CX-EDMS`, `CX-ERP`, `CX-DIRECTORY`, `CX-JIRA`, `CX-DOORS-MIG` ; dérivés au provisioning (D13 / D14). | Connectors |
| Copilot (Polarion) | Module d'IA générative de Polarion fondé sur un grand modèle de langage (LLM) ; désactivé par défaut, ouverture encadrée avec LLM sur site uniquement (ADR-17) [P]. | Polarion Copilot |
| Custom Sets | Permissions Polarion fondées sur une requête : ensemble d'éléments défini par requête auquel on attache des droits ; admis seulement si un projet sas est disproportionné [à vérifier sur la version cible]. | Custom permission sets |
| DEV / RECETTE / PRÉPROD / PROD | Environnements de développement (intégrateur), de recette (validation, tests d'acceptation), de pré-production (miroir de données anonymisées) et de production ; plus le PRA. | Dev / test / staging / production |
| Document dérivé | Copie d'un document source réutilisée avec des champs limités, mise à jour « depuis la source » (lien `derived_from`) ; spécification générique imposée sans adaptation locale. | Derived document |
| DOORS | Outil de gestion d'exigences d'IBM à migrer (connecteur `CX-DOORS-MIG` ou ReqIF) ; identifiants d'origine conservés dans `externalId`. | IBM DOORS |
| eIDAS | Règlement européen (UE) 910/2014 et eIDAS 2 (2024/1183) sur l'identification électronique et les services de confiance : valeur probante des signatures électroniques simples (ADR-11, F-05). | eIDAS |
| Empreinte | Condensat numérique identifiant sans ambiguïté un fichier ou un jeu de données (connecteur de calcul `CX-CALC`). | Hash |
| ERES | Réponse de conformité de Siemens « enregistrements et signatures électroniques » (21 CFR Part 11 / Annexe 11). | Electronic Records, Electronic Signatures |
| ERP | Progiciel de gestion intégré : commandes internes, WBS / OTP, planification ; connecteur `CX-ERP` (fiche I-06). | Enterprise Resource Planning |
| Excel (aller-retour) | Export d'une requête ou d'un document vers un gabarit Excel `XL-*` (`XL-SUPPLIER`, `XL-FIELD-CAPTURE`…), édition hors ligne, ré-import par identifiant ; jamais de transition ni de signature par Excel (doc. 22 § 4). | Excel round-trip |
| Feature model | Arbre des options et contraintes d'un produit configurable, base du module Polarion Variants. | Feature model |
| Form layout | Disposition des champs d'un type dans le formulaire de saisie Polarion (étape S4 : formulaires des types activés). | Form layout |
| Fusion à trois sources (3-way) | Fusion comparant source, branche et ancêtre commun, champ par champ (branchement de documents maître → branche et branche → maître) [à vérifier sur la version cible]. | Three-way merge |
| Gabarit de LiveDoc | Document modèle rangé dans `LIB-TEMPLATES` et copié à l'initialisation de chaque projet : page de garde, cartouche de signatures, historique des révisions, plan type (doc. 12 § 3). | LiveDoc template |
| GED | Gestion électronique des documents : archive de référence des livrables approuvés (PDF/A signé + manifeste de signatures, socle NN-07) ; connecteur `CX-EDMS`, fonction `exportToEdms`. | EDMS |
| Grappe (cluster) | Groupe de serveurs se partageant la charge d'une instance Polarion, coordonné par ZooKeeper (au moins deux nœuds en production, doc. 15 § 1). | Cluster |
| Greenfield | Déploiement sur une instance vierge, sans reprise d'existant autre qu'un import ciblé des référentiels actifs (ADR-23). | Greenfield |
| Groupes de projets | 12 groupes de `project_topology.yaml` : `CORP`, `PL`, `PCM`, `MFG`, `DTI`, `IB`, `FUEL`, `ICS`, `HC`, `SECURE` (instance SENS), `DEFENSE` (instance DEF), `EXT`. | Project groups |
| habilitationBased / roleBased | Politique de signature d'un projet (paramètre `signaturePolicy`, Q13, ADR-27) : rôle seul (défaut) ou rôle + habilitation nominative vérifiée par la condition `qualifiedSignatory` (groupes `HAB-<domaine>-<niveau>`, règle D11). | Signature policy |
| Homologation | Décision formelle d'autorisation de mise en service d'un système au regard de la sécurité (instance SENS). | Security accreditation |
| Hook (de sauvegarde) | Interception d'un événement (ex. enregistrement) par un script ou une extension ; en phase 2 de la suspicion, ne marque suspect que si un champ de `suspectTriggerFields` a changé (ADR-20) [à vérifier sur la version cible]. | Save hook |
| Hub & spoke | Architecture en étoile : une configuration globale unique (*hub*, générée depuis ce dépôt) héritée par tous les projets (*spokes*) (ADR-01, ADR-02). | Hub and spoke |
| Indice | Version diffusée d'un document : brouillons A0, A1… puis diffusions A, B, C… (champ `revisionIndex`, script `fra-revision-index.js`) ; chaque diffusion = baseline + PDF en GED. | Revision index |
| Instance (STD / SENS / US / DEF) | Installation Polarion complète et séparée (serveurs, base, utilisateurs). Quatre instances (ADR-03) : STD (standard, France + Allemagne), SENS (sensible : sécurité nucléaire, Diffusion Restreinte, réseau isolé homologué), US (réglementations américaines), DEF (défense : principe seul, hors périmètre). | Polarion instance |
| InvokeAction / invokeOnDocItems | Fonction native de workflow documentaire Polarion / sa déclaration dans `workflows.yaml` : applique une transition aux Work Items d'un document (cascade) [à vérifier sur la version cible : PF-07]. | InvokeAction |
| Jeton d'API | Clé d'accès d'un programme à l'API REST, stockée dans un gestionnaire de secrets ; jeton de service en lecture seule pour l'extraction BI. | API token |
| Jira | Outil de suivi de tickets des équipes logicielles (Atlassian) ; connecteur `CX-JIRA` (fiche I-08). | Jira |
| Kerberos / SAML / OIDC | Authentification intégrée au domaine Windows / protocoles de fédération d'identité pour l'authentification unique (fiche I-09) [selon la version cible, Q-TOOL-01]. | Kerberos / SAML / OpenID Connect |
| LDAP | Annuaire d'entreprise utilisé pour l'identité, les groupes de rôles et d'habilitation (`HAB-<domaine>-<niveau>`) et la signature électronique ; connecteur `CX-DIRECTORY`. | LDAP directory |
| Licences Polarion (ALM / REQUIREMENTS / QA / PRO / REVIEWER / VARIANTS) | Types de licences (`licenceTypes` de `roles.yaml`) : complète / exigences et LiveDocs / tests et qualité / contribution limitée / lecture, commentaire et approbation (signature de documents à confirmer) / module Variants ; mixte nommées et concurrentes, REVIEWER pour vérificateurs, approbateurs et clients (ADR-18). | Polarion licence types |
| LiveDoc | Document vivant de Polarion composé de texte et de Work Items ; porte les signatures R / V / A et pilote en cascade l'approbation des éléments qu'il contient (ADR-30) ; 22 types dans `document_types.yaml`. | LiveDoc |
| LiveReport | Page de rapport Polarion construite à partir de requêtes (tableaux, indicateurs) ; tableaux de bord par rôle et de portefeuille (doc. 13). | LiveReport |
| LLM | Grand modèle de langage (IA générative) ; voir Copilot (ADR-17). | Large Language Model |
| Lucene | Moteur et langage de recherche indexée de Polarion ; requêtes de la forme « type:… », « status:… », « suspect:true », suffixe « .KEY: » pour les énumérations ; opérateurs en majuscules [à vérifier sur la version cible : PF-08]. | Lucene query |
| luceneMaxClauseCount | Propriété de configuration Polarion fixant le nombre maximal de termes d'une requête de l'index Lucene (20 000 recommandé, doc. 15 § 1). | — |
| Mendix | Plateforme d'applications *low-code* de Siemens ; jugée non nécessaire au démarrage (doc. 18). | Mendix |
| MES / QMS | Système d'exécution de la fabrication (atelier) / système de management de la qualité d'atelier ; les écarts de fabrication y sont traités, avec lien vers Polarion (ADR-13, fiche I-04). | Manufacturing Execution System / Quality Management System |
| MFA | Authentification à plusieurs facteurs, exigée pour l'accès et pour la ré-authentification à la signature. | Multi-Factor Authentication |
| N-1 (politique) | Au plus une version de retard sur la dernière version publiée par l'éditeur ; au moins une montée de version par an (ADR-21). | N-1 version policy |
| Nextedy | Éditeur tiers d'extensions Polarion (documentation consultée en OSINT, doc. 05 § 5). | Nextedy |
| NIS2 / CRA | Directive (UE) 2022/2555 sur la sécurité des réseaux et des systèmes d'information (transposition française à vérifier) / règlement (UE) 2024/2847 sur la cyber-résilience des produits numériques. | NIS2 Directive / Cyber Resilience Act |
| Numérotation AAMM | Convention de version de Siemens Polarion : année-mois (2606 = juin 2026 [P]) ; 2404, 2410, 2506 jalonnent des fonctions dépendant de la version. | YYMM versioning |
| OAIS (ISO 14721) | Modèle de référence des archives numériques (pérennité des données sur plus de 60 ans, F-15). | Open Archival Information System |
| OSLC / OSLC RM | Standard d'interopérabilité par liens entre outils du cycle de vie / son profil de gestion des exigences ; connecteurs PLM 3DEXPERIENCE et Cameo. | Open Services for Lifecycle Collaboration / Requirements Management |
| `__other` | Jeton des règles de liens Polarion autorisant une cible de lien dans tout autre projet (liens inter-projets, `link_roles.yaml`) [à vérifier sur la version cible : PF-01]. | `__other` |
| Parsing | Analyse automatique d'un document Word pour en extraire des éléments structurés (exigences) ; règles du doc. 22 § 3. | Parsing |
| PDF/A | Format PDF d'archivage à long terme (ISO 19005) ; PDF signé versé en GED. | PDF/A |
| PLM | Gestion du cycle de vie du produit (articles, nomenclatures, CAO, fabrication) : Teamcenter (Siemens) ou 3DEXPERIENCE (Dassault Systèmes) ; paramètre de création de projet (Q17, règle D14). | Product Lifecycle Management |
| Polarion | Outil ALM de Siemens retenu par le plan directeur ; configuration générée depuis `model/` ; version cible 2606 [P], hébergement sur site. | Polarion ALM |
| PostgreSQL / SQL | Base de données relationnelle intégrée à Polarion, exposée en lecture pour les requêtes SQL (couverture, orphelins) et l'historique. | PostgreSQL / SQL |
| PRA / PCA | Plan de reprise / de continuité d'activité ; exercice annuel (doc. 15 § 6). | Disaster recovery / business continuity plan |
| primaryType / cascadeTypes / approvalGate | Déclarations d'un type de document (`document_types.yaml`) : type principal du LiveDoc (`primaryType`) / types soumis et approuvés en cascade (`cascadeTypes`) / statuts admis des autres types contenus à l'approbation (`approvalGate`). | Document type cascade keys |
| Profil ReqIF (RIF-*) | Table de correspondance entre attributs d'un fichier ReqIF et champs du modèle, pour un partenaire et un sens d'échange : `RIF-CUSTOMER-IN`, `RIF-CUSTOMER-COMPLIANCE-OUT`, `RIF-SUPPLIER-OUT`, `RIF-SUPPLIER-RETURN`, `RIF-LIBRARY-REG`. | ReqIF mapping profile |
| Projet (Polarion) | Unité de cloisonnement et de droits ; contient des Spaces, des LiveDocs et des Work Items ; préfixes `P-` (réalisation), `PL-`, `LIB-`, `EXT-` (`conventions.projectId`). | Project |
| Projet conteneur | Projet regroupant des affaires courtes et nombreuses (fortuits, modifications, pièces de rechange, outillages, recharges) : un projet par client ou parc, un Space par affaire (ADR-02) ; archétype `TPL-03-EXPRESS`. | Container project |
| Proxy (élément) | Fiche Polarion qui représente un objet maître d'un autre système (document archivé en GED, article du PLM) ; la source de vérité reste ailleurs. | Proxy item |
| Pseudo-rôle | Rôle du modèle qui n'est pas un rôle Polarion à attribuer : `anyProjectMember`, `documentOwner` (script `fra-document-owner.js`), `workitem.assignee`, `workitem.author` [à vérifier : PF-11]. | Pseudo-role |
| R / V / A | Rédigé / vérifié / approuvé : triptyque de signatures d'un LiveDoc (`docAuthor`, `docVerifier`, `docApprover` ; workflows `wfDocumentFull`, `wfDocumentLight`, `wfDocumentLibrary`). | Authored / Verified / Approved |
| reassess / onChangedReimport | Transition de réévaluation d'une exigence d'entrée dont le texte a changé au ré-import d'une révision client (`accepted` → `underAnalysis`) ; attribut `onChangedReimport` du profil `RIF-CUSTOMER-IN`. | Reassess on re-import |
| Référence vivante / figée | Élément d'un autre projet affiché sans copie, suivi automatiquement (*live*) ou à une révision fixée (*frozen*) ; patrons de réutilisation ADR-06. | Live / frozen reference |
| ReqIF | Format standard OMG d'échange d'exigences (`.reqif`, `.reqifz` compressé ; versions 1.1 / 1.2) ; `ReqIF.ForeignID` = identifiant chez le partenaire, stocké dans `externalId` [à vérifier sur la version cible]. | Requirements Interchange Format |
| Reverse proxy / TLS | Serveur frontal qui termine le chiffrement et répartit la charge / protocole de chiffrement des échanges (TLS 1.2+). | Reverse proxy / Transport Layer Security |
| RGPD | Règlement général sur la protection des données : registre des traitements, analyse d'impact (AIPD), minimisation des données personnelles dans l'ALM (F-02). | GDPR |
| RPO / RTO | Perte de données maximale admise / durée maximale d'interruption (ex. 24 h / 48 h pour STD, plus strict pendant les arrêts). | Recovery Point / Time Objective |
| SaaS / AWS | Logiciel hébergé par l'éditeur (Polarion X, hébergé sur AWS [P]) ; écarté pour les données d'ingénierie nucléaire sauf qualification SecNumCloud (ADR-03). | Software as a Service / Amazon Web Services |
| SBB / DB InfraGO | Chemins de fer suisses / gestionnaire d'infrastructure ferroviaire allemand : auteurs de dépôts open source Polarion (export PDF, synchronisation Capella) cités en annexe C. | SBB / DB InfraGO |
| Script de workflow (ScriptCondition / ScriptFunction) | Programme JavaScript exécuté par Polarion à une transition : condition (autorise ou bloque) ou fonction (agit après la transition) ; 17 scripts `fra-*.js` (doc. 10 § 4) [à vérifier : PF-06]. | Workflow script |
| Script planifié | Script exécuté périodiquement côté serveur (pré-calcul nocturne des indicateurs, statut de vérification) [à vérifier sur la version cible : annoncé 2506+]. | Scheduled job |
| SDK | Kit de développement logiciel de l'éditeur (API Java des widgets Velocity). | Software Development Kit |
| SecNumCloud | Qualification ANSSI des services d'informatique en nuage de confiance (condition d'un éventuel SaaS, ADR-03). | SecNumCloud |
| setByImport | Champ posé par l'import et non saisi à la main (`sourceDocument`, `sourceDocumentRevision`) ; dispense de l'obligation à la création (principe P10). | Set by import |
| Signature électronique / signification | Signature Polarion (ré-authentification, horodatage) matérialisant une décision engageante ; porte une signification : rédigé, vérifié, approuvé, avis sûreté, visa qualité, décision CCB… ; signature simple au sens eIDAS (ADR-11). | Electronic signature / signature meaning |
| Simulink | Outil MathWorks de modélisation et de simulation de systèmes dynamiques ; connecteur `CX-SIMULINK`. | Simulink |
| SOC | Centre de supervision de la sécurité, destinataire des journaux de la plateforme. | Security Operations Center |
| Space | Dossier de rangement des documents et pages d'un projet Polarion ; organise mais ne protège pas : ce n'est pas une frontière de sécurité (PR-09, ADR-28). | Space |
| SSI | Sécurité des systèmes d'information. | Information systems security |
| SSO | Authentification unique (Kerberos ou SAML / OIDC), couplée à la MFA. | Single Sign-On |
| Surcharge projet | Fichier de configuration propre à un projet qui remplace, pour ce projet, l'élément global correspondant ; liste fermée `overridableProjectFiles` de `extension_policy.yaml` [à vérifier : PF-12]. | Project override |
| Suspect (lien) | Lien marqué « à revoir » quand son élément amont a changé depuis la dernière validation ; drapeau du lien stocké côté aval, requête « suspect:true » ; condition `noSuspectLinks` (TR-14), indicateur K-CHG-04. | Suspect link |
| SVN | Subversion : gestionnaire de versions sous-jacent à Polarion, dépôt de référence des données et de la configuration (historique immuable). | Subversion |
| Swagger | Documentation interactive de l'API REST (désactivée en PROD). | Swagger / OpenAPI UI |
| Teamcenter | PLM de Siemens (client web Active Workspace) ; connecteur natif `CX-PLM-TC`. | Teamcenter |
| Test Run / Test Record | Campagne d'exécution de cas de vérification, objet natif de Polarion (pas un Work Item) / résultat saisi pour un cas au sein de la campagne (`testResult`) ; toutes les méthodes V&V (ADR-19). | Test Run / Test Record |
| Tracker | Base des Work Items d'un projet Polarion, partagée par tous ses Spaces (la recherche ignore le rangement en Space). | Tracker |
| UUID | Identifiant unique universel (ex. identifiant d'un élément de modèle Capella, champ `modelElementId`). | Universally Unique Identifier |
| Variants (module) / pvSCL | Module payant de Polarion pour les produits configurables : modèle de caractéristiques, spécification maître, conditions de variante en pvSCL (ex. « Cogeneration AND NOT InlandSite ») ; évalué en phase 3 (ADR-05). | Polarion Variants / pvSCL |
| Velocity | Langage de gabarit des widgets et pages de rapport Polarion (texte + appels à l'API Java). | Apache Velocity |
| VSO / VSO-SR / VAO / VAOB / REF | Visas client : vu sans observation / sous réserve / avec observations / avec observations bloquantes / refusé (énumération `customerVisa`, codes à confirmer par client) ; VAOB ou REF → nouvel indice. | Customer review codes |
| Work Item | Élément de travail typé de Polarion (exigence, fonction, cas de vérification, écart, décision, lot de travaux…) ; 36 types dans `work_item_types.yaml`. | Work Item |
| Workflow | Cycle de vie : états (avec catégorie et état de soumission) et transitions d'un type d'élément ou de document ; 24 workflows de Work Items et 3 de LiveDocs (`workflows.yaml`). | Workflow |
| xUnit | Format XML standard de résultats de tests automatisés, importé dans les Test Runs (`CX-TEST-BENCH`). | xUnit |

## 5. Conventions du dépôt

| Terme / sigle | Définition | Équivalent ou forme anglaise |
|---|---|---|
| [à vérifier] | Mention signalant une capacité Polarion dépendante de la version cible, à confirmer au spike S1 (annexe D). | To be verified on the target version |
| ADR-xx | *Architecture Decision Record* : décision d'architecture tracée avec contexte, options et conséquences ; 30 décisions au doc. 06 (ADR-01..30). | Architecture Decision Record |
| Annexe D / PF-xx | Constructions XML Polarion plausibles mais non confirmées sur la version cible (PF-01..PF-14), à lever au spike S1 ; si une construction est infirmée, c'est le générateur que l'on corrige, jamais les fichiers générés. | Polarion constructs to confirm |
| Annexes A1–A11 | Catalogues générés par `tools/generate_docs.py` depuis `model/` (types, énumérations, liens, workflows, documents, rôles, tailoring, méta-modèle, couverture, provisioning, import-export) ; jamais édités à la main. | Generated annexes |
| C / P (annexes A10 / A11) | Codes de confiance de `project_setup.yaml` et `import_export.yaml`, alignés sur l'échelle du plan : C = fonctionnalité publique documentée par l'éditeur, P = à confirmer en maquette sur la version cible. | Confidence codes of the generated annexes |
| [C] / [P] / [P*] / [H] / [NT] / [X] | Niveaux de confiance des faits OSINT (doc. 05 § 3, doc. 01) : C confirmé (source officielle ou ≥ 2 sources) ; P probable (une source) ; P* non revérifié lors de la campagne d'octobre 2026 ; H hypothèse de modélisation ; NT non trouvé en source ouverte ; X contredit par les sources. Les énumérations portent `confidence: C`, `P` ou `H`. | Confidence levels |
| CI | Intégration continue : contrôles automatiques (validateur, tests, générateurs) rejoués à chaque modification du dépôt (`.github/workflows/validate.yml`) ; refuse tout fichier généré non à jour. | Continuous Integration |
| Classes A–D (tailoring) | Classes de projet issues de la grille à 7 critères cotés de 0 à 3 (`scoringGrid`, seuils `thresholds`) : A programme majeur … D express ; un enjeu de sûreté maximal impose au moins la classe B ; profils `classProfiles`, règle D02. | Tailoring classes |
| Commit | Enregistrement d'une modification dans un dépôt de code (Git, SVN). | Commit |
| Cône d'impact | Ensemble des éléments atteints de proche en proche depuis les éléments modifiés (rapport d'analyse d'impact à N niveaux, doc. 09 § 5.4). | Impact cone |
| Configuration « as code » | Modèle en fichiers texte versionnés (`model/*.yaml`), vérifiés (`tools/almmodel.py`) et transformés en configuration Polarion par des générateurs ; on ne modifie jamais un fichier généré à la main (ADR-04). | Configuration as code |
| Convention aval → amont | Un lien part toujours de l'élément dérivé (aval) vers sa source (amont), pour rester compatible avec la suspicion native de Polarion (doc. 09 § 1). | Downstream → upstream link convention |
| Cœur gouverné / modèle 150 % | Stratégie ADR-29 : modèle conçu à 150 % (sur-ensemble des 32 typologies), cœur gouverné à 100 % par le CCB, exposé par incréments, extensions locales délimitées, promotion trimestrielle. À ne pas confondre avec la ligne de produits 150 % des conceptions (doc. 11 § 6). | Governed core / 150 % model |
| D01–D14, D06bis | 15 règles de dérivation de `project_setup.yaml` qui déduisent gabarit, classe, instance, packs, projet sas, lots, signatures, énumérations et connecteurs des réponses Q01–Q19 ; évaluées dans l'ordre, la première qui fixe un paramètre l'emporte. | Derivation rules |
| Demande de fusion (pull request) | Proposition de modification du dépôt relue avant d'être intégrée dans la branche principale ; la CI la rejoue (guide § 7). | Merge request / pull request |
| Déprécié | Identifiant conservé mais signalé comme à ne plus utiliser ; un identifiant n'est jamais renommé ni supprimé (clé `deprecated`). | Deprecated |
| Dogfooding | Appliquer le modèle à sa propre construction : les hypothèses OSINT du plan sont gérées comme des `assumption` de nature `osintHypothesis` dans `LIB-PROCESS`. | Dogfooding |
| Double cote (C/P, P/H) | Ligne d'un tableau qui mêle des faits de niveaux de confiance différents ; « à sourcer » signale un fait sans source en annexe C. | Mixed confidence rating |
| En-tête uniforme | Ligne sous chaque titre : version du plan (v0.5, CHANGELOG), dépendance à l'outil Polarion (faible / moyenne / forte / mixte, guide § 5), historique, carte du dépôt. | Uniform header |
| Énumération | Liste de valeurs fermée (identifiant + libellé FR / EN) ; 112 énumérations dans `enumerations.yaml`, certaines de portée projet (`scope: project`). | Enumeration |
| Extension locale `x_` | Champ informatif local à un projet, préfixé `x_` (5 par type, 15 par projet), jamais dans une condition, une règle TR, un rapport de portefeuille ni un échange ReqIF ; déclaré dans `localFields`, revu chaque trimestre (ADR-29). | Local extension field |
| F-xx | Facteurs de succès du déploiement non couverts par la v0.1 (F-01..F-26, doc. 20) ; à ne pas confondre avec PF-xx (annexe D). | Success factors |
| fieldSet | Jeu d'attributs réutilisable (`fieldSets` : `common`, `requirementCore`, `supplierFlowdown`, `requirementSafety`, `sscClassification`, `functionSafety`, `documentReference`), expansé par le générateur dans chaque type qui l'inclut (principe P3). | Field set |
| Foyer unique | Règle de rédaction du dépôt : chaque sujet n'est développé qu'à un seul endroit, les autres documents y renvoient (ex. doc. 17 § 2 gouvernance du modèle, doc. 21 § 4 projets sas). | Single home section |
| Gabarit de projet (master / archétype / spécialisation) | Projet modèle instancié par le guichet de provisioning, en trois niveaux : `TPL-00-MASTER` (socle non instanciable) → 6 archétypes (`TPL-01-PRODUCT` … `TPL-06-LIBRARY`) → 21 spécialisations ne portant que leurs écarts (`extends`) ; 28 gabarits au total. | Project template |
| GAP-x | Écarts GAP-1..GAP-15 identifiés par l'analyse critique (doc. 18) et traités dans le modèle. | Gaps |
| Générateurs | `tools/generate_polarion.py` (configuration XML FR / EN + manifeste), `tools/generate_project.py` (kit d'un projet pilote), `tools/generate_docs.py` (annexes A1–A11). | Generators |
| H | Dans l'échelle de confiance du plan, « H » = hypothèse de modélisation (atelier interne obligatoire). Ailleurs : point d'arrêt (H / W / R, § 2) ou groupe de projets `HC` (santé). | Hypothesis (confidence level) |
| I-xx | Fiches d'intégration I-01..I-11 du doc. 14 (client ReqIF, Capella, PLM, MES, GED, ERP, outils de C-C, dépôts de code, annuaire, BI, fournisseurs). | Integration sheets |
| Identifiant (règle) | Types, champs, valeurs et rôles sont en anglais, en `camelCase`, jamais renommés ni supprimés une fois publiés : on déprécie ou on migre (guide § 6, ADR-15). | Identifier rule |
| INC-1 … INC-4 | Incréments de déploiement du cœur (`deploymentIncrements` de `extension_policy.yaml`) : NUWARD / base installée (fortuit, outillage) / C-C et logiciel / bibliothèques transverses. | Deployment increments |
| Incubation | Prototypage en bac à sable d'un besoin de type, de rôle de lien ou de workflow, décrit par un scénario de couverture ; décision du CCB du modèle sous 20 jours ouvrés avant entrée dans le cœur. | Incubation |
| K-xxx | Indicateurs du doc. 13 par famille : K-REQ, K-VV, K-SAF, K-CHG, K-NC, K-FOR, K-ITF, K-DLV, K-RSK ; K-ADO (adoption) et K-OPS (exploitation) pour la plateforme. | KPI identifiers |
| localFields / projectEnumValues | Clés d'une fiche de pilote (`model/pilots/*.yaml`) déclarant les champs locaux `x_` et les valeurs locales des énumérations de portée projet (`plantUnit`, `operationalUnit`, `businessLine`). | Local fields / project enumeration values |
| Manifeste (SIGNATURES_ET_SCRIPTS.md) | Fichier généré par `tools/generate_polarion.py` listant les scripts attendus, les points de signature et les constructions à confirmer. | Generated manifest |
| Obligation portée par la transition | Un champ n'est obligatoire dès la création que s'il a une valeur par défaut ou est posé par un import ; sinon l'obligation est portée par le workflow, pour ne jamais bloquer un import ReqIF / Word ni une synchronisation (principe P10, GAP-2). | Transition-borne obligation |
| Ontologie | Ensemble des types et de leurs relations (doc. 08 § 2). | Ontology |
| OSINT | Renseignement de sources ouvertes (sites officiels, communiqués, offres d'emploi, notes de version) : seules sources de ce plan, sans donnée interne ; à valider en atelier. | Open-source intelligence |
| osintHypothesis | Valeur de `assumptionType` identifiant une hypothèse OSINT du registre de cadrage (dogfooding, `LIB-PROCESS`). | OSINT hypothesis |
| P0 / P1 (priorité des scripts) | Indispensable au démarrage du pilote / nécessaire après le démarrage, avec solution manuelle tracée entre-temps (doc. 23 § 3). | Priority 0 / 1 |
| Pack réglementaire | Ensemble de champs, règles et bibliothèques activés par cadre réglementaire (`regulatory_packs.yaml` : `frAsnr`, `usNrc`, `deKta`, `ukOnr`, `caCnsc`, `intlIaea`, `medicalGmp`, `defense`) ; règle D08, ADR-25. | Regulatory pack |
| Pilote (P-NUWARD-L1) | Fiche de provisioning du pilote NUWARD (`P-NUWARD-L1.yaml`, dossier `model/pilots/`) : réponses, tranche activée, champs locaux, critères de succès ; kit généré dans `generated/projects/`. | Pilot sheet |
| PR-xx | Règles de permission transverses PR-01..PR-11 (`roles.yaml`) ; PR-01 = interdiction de suppression, PR-09 = le Space n'est pas une frontière de sécurité, PR-11 = comptes externes nominatifs à expiration. | Permission rules |
| Principes P1–P10 | Principes de modélisation du doc. 08 § 1 : P1 un type = un cycle de vie ; P2 pas de doublon de champ natif ; P3 jeux d'attributs ; P4 pas de défaut affirmatif en sûreté ; P5 champs calculés ; P6 même définition partout ; P7 multi-valeurs réservées aux énumérations ; P8 organisation jamais codée ; P9 libellés FR / EN ; P10 obligation portée par la transition. | Model principles |
| Projet sas EXT-* | Projet Polarion distinct (`EXT-<partenaire>-<affaire>`, gabarit `TPL-EXT`, règle D09) réservé à la collaboration avec un client, fournisseur ou partenaire, alimenté par copie contrôlée ; jamais de lien direct vers un projet interne (ADR-28, PR-09). Les rôles `customerReviewer` / `supplierContributor` n'existent qu'en sas. | Exchange (airlock) project |
| Promotion | Entrée dans le cœur d'une extension locale qui sert au moins deux projets ou BU, ou qu'exige un client ou une autorité ; champ du cœur créé, valeurs recopiées par script, champ `x_` déprécié puis retiré. | Promotion |
| Provisioning | Création reproductible d'un projet à partir d'un gabarit, d'un questionnaire (Q01–Q19) et de règles de dérivation (D01–D14) ; guichet unique, rôle `provisioningOfficer` (doc. 21 § 2). | Provisioning |
| PyYAML | Bibliothèque Python qui lit les fichiers YAML du modèle (`requirements.txt`). | PyYAML |
| Q-xxx | Questions ouvertes à confirmer en atelier (ex. Q-ORG-01, Q-TOOL-01, Q-REG-02 ; registre du doc. 05 § 6). | Open questions |
| Q01–Q19 | Questions du questionnaire de provisioning (`project_setup.yaml`) : typologie, BU / BL / UO, cadres réglementaires et filières, paliers et classement, classification et export, langue, signature, échanges, MBSE / PLM, cotation. | Provisioning questionnaire |
| R-ORG / R-REG / R-BU | Lots du plan de recherche OSINT (doc. 05) : organisation, réglementation (revérification des [P*]), chaque BU. | Research work packages |
| R1–R20 | Lignes de la matrice « exigence réglementaire → impact Polarion » du doc. 04 § 9. | Regulatory impact matrix |
| refines / flowsDownFrom | Rôle de lien « précise » (SysML refine) / « découle de », utilisé pour la déclinaison des exigences (SysML deriveReqt). | refines / flowsDownFrom |
| Rôle de lien | Nature d'un lien entre deux éléments ; 26 rôles dans `link_roles.yaml` (`flowsDownFrom`, `refines`, `satisfies`, `realizes`, `verifies`, `validates`, `mitigates`, `impacts`, `relates_to`…), avec règles type × type et politique de suspicion. | Link role |
| S-n | Références de sources de la campagne OSINT du 15 octobre 2026 (annexe C § 1 bis), citées par le doc. 01 et les énumérations d'organisation. | Source references |
| S0–S13 | Étapes du guide pas à pas du doc. 23, de l'instance vide (S0 prérequis) au pilote en production (S13). | Build steps |
| SC-xx | Critères de succès du pilote NUWARD SC-01..SC-06 (`successCriteria` de la fiche `P-NUWARD-L1`). À ne pas confondre avec `sc1`..`sc3` (classes de sûreté) ni SC1 / SC2 (sismique). | Pilot success criteria |
| Scénario de couverture | Preuve, par typologie, que le modèle couvre ses besoins (types, documents, traces, attributs, valeurs) ; `coverage_scenarios.yaml`, vérifié en CI (annexe A9). | Coverage scenario |
| Socle non négociable (NN-01..NN-08) | Exigences réglementaires minimales dues dans toutes les classes de tailoring (`nonNegotiableCore`) : EIP identifiés, contrôle technique, traçabilité, écarts, modifications, classification et export, archivage GED, hypothèses de sûreté. | Non-negotiable core |
| Spike | Expérimentation courte et bornée qui lève un doute technique avant d'engager la construction. | Spike |
| Spike S1 | Étape S1 du doc. 23 : spike de conformité de la configuration générée sur l'instance cible (2 à 3 semaines, avec un expert Siemens) ; lève les PF-xx de l'annexe D. | Conformance spike |
| submitState / requiredAt | État de soumission déclaré par chaque workflow / étape à laquelle un champ devient obligatoire ; les champs « requis à la soumission » sont exigés sur les transitions menant à cet état (principe P10 ; l'ancienne appellation « P7 » citée au doc. 08 § 1 ne figure plus dans le YAML). | Submit state / required at |
| Test par mutation | Test qui dégrade volontairement le modèle pour vérifier que le validateur détecte la dégradation (doc. 19 § 2.3) ; 46 tests de non-régression. | Mutation test |
| TR-xx | Règles de complétude de la traçabilité TR-01..TR-20 (`link_roles.yaml`) ; TR-03 (exigence définie vérifiée par un cas approuvé) est bloquante (NN-03). | Traceability rules |
| Typologie de projet | L'un des 32 types de projets reconnus (énumération `projectType`, doc. 02), chacun avec un profil de tailoring par défaut et un scénario de couverture. | Project typology |
| Validateur | `tools/almmodel.py` (avec `tools/model_checks.py`) : charge le modèle et vérifie références, workflows, profils, couverture, provisioning ; 0 erreur attendu. | Validator |
| XC-xx | Contrôles d'échange XC-01..XC-04 : filtrage export par classification, journalisation dans le sas, aucun fichier externe direct dans un projet interne, correspondances rejouées à chaque montée de version (doc. 22 § 1). | Exchange controls |
| YAML | Format texte structuré des fichiers du modèle (`model/*.yaml`), lu en YAML 1.2 (typage strict, GAP-4). | YAML |
| Zones d'extension (EXT-FIELD … EXT-SPACE) | Catégories d'extensions locales admises par `extension_policy.yaml` (`EXT-FIELD`, `EXT-ENUM`, valeurs projet, gabarit, page, requête, `EXT-SPACE`) ; à ne pas confondre avec les projets sas `EXT-*`. | Local extension zones |
