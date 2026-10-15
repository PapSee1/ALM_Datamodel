# Partie 1.1 — Organisation et périmètres : BU, BL, UO, sites, filiales et écosystème

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **faible** (§ 7 et § 9 décrivent ce que l'organisation impose au modèle, transposable à tout outil) · Historique : [CHANGELOG](../../CHANGELOG.md) · Carte du dépôt : [guide de lecture](../GUIDE_DE_LECTURE.md).*
>
> **En bref.** Ce document décrit qui fait quoi chez Framatome : les Business Units (BU, grandes divisions par métier), les Business Lines (BL, lignes d'activité à l'intérieur d'une BU) et les unités opérationnelles (UO : sites, usines, centres d'ingénierie). Il sert aux ateliers de validation de l'organisation (doc. 24) et alimente trois listes de valeurs du modèle : `businessUnit`, `businessLine`, `operationalUnit`. À lire après la synthèse (doc. 00) ; aucune connaissance de Polarion n'est nécessaire.
>
> **Statut** : cartographie établie à partir de sources ouvertes (OSINT), recherche complétée le 15 octobre 2026 (≈ 80 requêtes ; aucune donnée interne). Chaque fait porte un niveau de confiance :
> **[C]** confirmé (source officielle ou au moins deux sources concordantes) · **[P]** probable (une seule source, souvent une offre d'emploi) · **[P\*]** à revérifier · **[H]** hypothèse de modélisation · **[NT]** non trouvé en source ouverte · **[X]** contredit par les sources. Une double cote (C/P) signifie qu'une ligne mêle des faits de niveaux différents.
> Les sources sont listées en [Annexe C § 1](../annexes/C_Sources_OSINT.md) (références S-n). Les pages n'ont été lues qu'à travers les extraits d'un moteur de recherche : chaque élément est à revérifier sur la page avant d'être figé dans l'outil (atelier B2, doc. 24).
>
> **Vocabulaire.** *Business Unit* (BU) : division opérationnelle de premier niveau. *Business Line* (BL) : ligne d'activité à l'intérieur d'une BU. *Unité opérationnelle* (UO) : entité de réalisation (site industriel, centre d'ingénierie, centre technique, filiale) rattachée à une BL. Framatome ne publie pas son organigramme : les codes cités (IBE, IBM-F, IBC…) viennent d'offres d'emploi.

## 1. Identité de l'entreprise (éléments structurants pour l'ALM)

| Élément | Constat OSINT | Conf. | Conséquence pour le déploiement Polarion |
|---|---|---|---|
| Actionnariat | EDF 80,5 %, Mitsubishi Heavy Industries 19,5 %. Assystem a cédé ses 5 % à EDF en janvier 2024. | C | Le premier client (EDF) est aussi l'actionnaire majoritaire : flux de données massifs avec EDF et Edvance → échanges ReqIF industrialisés et projets sas (ADR-12, ADR-28). |
| Siège | Courbevoie (Paris-La Défense) | C | Hébergement primaire en France (souveraineté, contrôle export). |
| Taille | CA 2025 : 5 399 M€, prises de commandes 5 924 M€, EBITDA 665 M€ ; plus de 22 000 salariés, plus de 70 sites, plus de 20 pays (chiffres variables selon les pages). | C/P | Plusieurs milliers d'utilisateurs potentiels ; licences mixtes ; grappe de serveurs (doc. 15). |
| Gouvernance | Conseil de surveillance et Comité exécutif de dix membres au 1er octobre 2025 : directeur général nommé en juin 2025, directrice générale déléguée / finances (octobre 2025), quatre dirigeants de BU, une direction « Engineering & Design Authority », les fonctions Digital & IT, RH, Supply Chain (S-1 à S-4). | C | Sponsor exécutif à positionner au Comex ; la Design Authority d'entreprise existe déjà comme fonction : la Design Authority *du modèle ALM* (doc. 17) doit s'y articuler. |

## 2. Business Units publiées

L'organisation publiée fait apparaître **quatre BU opérationnelles**, une direction technique transverse comptée publiquement comme cinquième BU, et des marques hors électronucléaire (S-1, S-8, S-10).

| BU (`businessUnit`) | Libellé public et périmètre | Effectifs / sites (publics) | Conf. | Typologies de projets portées (`projectType`) |
|---|---|---|---|---|
| **Base installée** (`ib`) | « Installed Base Business Unit » : ingénierie et services pour les centrales en exploitation, projets de construction neuve (montage) et installations en démantèlement ; remplacements de gros composants (Amérique du Nord, Afrique du Sud, RGV Flamanville 2 démarré en 2025) ; inspection en service. | ≈ 4 000 (offres FR) à 4 600 personnes, 15 pays ; Lyon, Chalon-sur-Saône, Sully, Maubeuge, Rungis, Beaumont-Hague ; États-Unis, Allemagne, Canada, Royaume-Uni, Slovaquie (S-10 à S-13). | C | `steamGeneratorReplacement`, `periodicSafetyReview`, `plantModification`, `fortuit`, `specialTooling`, `inspectionService`, `icRefurbishment` (avec I&C), `powerUprate`, `sparePartsEquivalence`, `hotWorkshopRepair`, `decommissioning`, `labTesting` |
| **Combustible** (`fuel`) | « Fuel Business Unit » : conception, fabrication et vente de combustible pour centrales et réacteurs de recherche ; filière zirconium ; services. L'« excellence opérationnelle » figure dans le titre du dirigeant, pas dans le nom de la BU. | Romans-sur-Isère, Jarrie, Ugine, Rugles, Montreuil-Juigné, Paimboeuf, Lyon ; Lingen, Karlstein, Erlangen ; Richland, Lynchburg (S-14, S-15). | C | `fuelDesign`, `fuelReload`, `fuelSiteServices`, `researchReactorFuel`, `facilityLicensing`, `processQualification`, `componentManufacturing` (composants d'assemblages) |
| **Contrôle-commande** (`ics`) | « Instrumentation and Control Business Unit » : plateformes de sûreté (TELEPERM XS, ex-Rolls-Royce Spinline / Rodline / Hardline, ex-Schneider Tricon / SPEC 200), instrumentation, projets et rénovations ; **BL Cybersécurité** (Allentis, Cyberwatch, FoxGuard) citée dans les résultats 2025. | ≈ 2 400 à 2 800 personnes, 20 sites, 10 pays ; Erlangen, Karlstein, Grenoble / Montbonnot, Lynchburg, Prague, Pékin, Shenzhen (S-10, S-16, S-17, S-25, S-80). | C | `icPlatform`, `icApplication`, `icRefurbishment`, `cybersecurityCompliance`, `simulator` |
| **Projets & fabrication de composants** (`pcm`) | « Projects and Components Manufacturing » : conception et fabrication des composants lourds et mobiles ; pilotage et exécution des projets de réacteurs neufs (EPR2 en EPCC, HPC, SZC) et des remplacements de composants ; **BL Robinetterie** (Vanatome, Segault, Valserve, Sebim) depuis 2024-2026. Issue de la fusion « Large Projects » + « Component Manufacturing » (2020). | ≈ 1 900 personnes en ingénierie de projets ; Saint-Marcel, Le Creusot, Jeumont, Montbard ; La Défense (S-6, S-10, S-18 à S-21). | C | `newBuildLarge`, `newBuildSmr` (projet), `componentDesign`, `componentManufacturing`, `configureToOrder` |
| **Direction technique & ingénierie** (`dti`) | « Direction Technique et Ingénierie (DTI) » : développement, conception et licensing des chaudières nucléaires et des équipements associés ; études pour les exploitants. Portée au Comex par la direction « Engineering & Design Authority » ; comptée publiquement comme BU. Divisions attestées : Ingénierie Mécanique (DTIM), Sûreté et Procédés, Centre Technique. | La Défense, Lyon, Saint-Marcel, Le Creusot / Chalon, Erlangen, Karlstein (S-7, S-9, S-22, S-92 à S-95). | C (existence) / P (rattachement E&DA ↔ DTI) | `newBuildSmr` (études), `rdProgram`, `calculationCode`, appui à toutes les typologies pour la sûreté et les composants |
| Fonctions transverses (`corp`) | Choix de modélisation : porte les bibliothèques `LIB-*` et les fonctions support (Sûreté, Qualité, DSI). | — | H | `library` |
| Marques hors électronucléaire | **Framatome Defense** (marque lancée le 19/10/2020 ; « division » ; ligne de propulsion militaire à Jeumont avec le CEA, 2025), **Framatome Healthcare** (08/07/2021 : Lu-177, At-211 avec IBA, Isogen), **Framatome Space** (19/10/2023). | Le Creusot, Jeumont, Erlangen, Romans (S-23, S-24, S-27, S-28). | C | `defenseProgram` (instance DEF, principe seul), `isotopeProduction` ; `healthcare`, `defense`, `space` |

**Réorganisations attestées 2019-2026 [C]** : BU « Large Projects » et « Component Manufacturing » distinctes en 2019 (S-19), fusionnées en PCM dès les résultats 2020 (S-18) ; marques Defense (2020), Healthcare (2021), Space (2023) ; rachat du C-C civil de Rolls-Royce (2021, > 550 personnes, S-25) ; Framatome ARC (ex-EFINOR) intégrée à IB (2022, S-26) ; BL Robinetterie (Vanatome 2024, Segault, Valserve, Sebim) et BL Cybersécurité (résultats 2025) ; nouvelle gouvernance au 1er octobre 2025 (S-3, S-4). **Conséquence :** l'organisation change tous les 12 à 18 mois ; elle ne doit jamais être codée dans les identifiants de projets ni de types (§ 7).

## 3. Business Lines et unités opérationnelles

Aucune liste officielle des BL et UO n'est publique. Les offres d'emploi Framatome portent un marquage « BU : code entité » (ex. « IB - IBS-F », « IB - IBCO-F », « PCM - HC », « FL - FLDOC », « IC_SPIC - ICT ») qui révèle une convention : préfixe BU, code d'entité, suffixe **-F** pour la France (S-29 à S-33). Le tableau ci-dessous reprend tout ce qui a été trouvé ; le niveau « UO » au sens interne (≈ 40 unités annoncées en atelier) n'est publié nulle part : le terme n'apparaît publiquement que pour les unités de production de Jarrie et dans une offre d'excellence opérationnelle I&C (S-97).

### 3.1 BU Base installée

| Code / entité | Libellé exact relevé | Périmètre | Lieux | Conf. | Id modèle |
|---|---|---|---|---|---|
| **IBE** | « IBE (Engineering Services, 1500 salariés en France et Allemagne) » | Ingénierie au service du parc français et de l'export, de la construction neuve, du démantèlement et des réacteurs avancés (ITER, RJH) ; bureaux Lyon, Paris, Marseille ; antennes Cadarache, Marcoule, Creys-Malville, Royaume-Uni | Lyon, Paris, Marseille | C (≥ 3 offres, S-34, S-35) | BL `ibEngineering` |
| IBEO | « département IBEO “Performance et Support Projets” » | Planification, support des sections d'ingénierie | Lyon | P (S-36) | — (sous-département) |
| IBE_MAD EDVANCE | marquage d'offres | Salariés IBE mis à disposition d'Edvance | Lyon | P (S-29) | UO `edvance` |
| **IBM-F** | « Business Line Grands Projets (IBM-F) » ; « entité IBM-F en charge des Remplacements de Composants (générateurs de vapeur ou tronçons du circuit Primaire) » | RGV, remplacement de tronçons du circuit primaire ; PMO ; finance projet | Chalon-sur-Saône | C (S-37, S-38) | BL `ibMajorProjects` |
| **IBC** (IBCO-F) | « La Business Line IBC intervient … sur tous les projets de construction du nouveau nucléaire (EPR première génération, EPR2, EPR1200, SMR...) » | Préfabrication et montage des tuyauteries et équipements, études de montage, outillages ; chantiers HPC, EPR2 | Lyon, Chalon ; chantiers | C (S-30, S-39, S-40) | BL `ibConstruction` |
| **IBS-F** | « Business Line Maintenance » (≈ 350 personnes) ; « Unité Support Technique (IBS-F) » ; IBSE-F (bureau d'études outillages et machines spéciales) ; IBSED-F = CEDEM (centre de développement pour la maintenance, robotique) | Maintenance et support technique, conception de machines et outillages d'intervention | Lyon, Chalon | C (S-41 à S-45) ; libellé variable selon les offres 2023-2026 | BL `ibMaintenance` ; UO `cedem` |
| **IBT** (IBT-F) | « Direction Travaux » ; IBTM-F (moyens et matériels), IBTMOM-F (maintenance des outillages, 30 personnes), IBTOP-F (préparation et suivi des chantiers) | Préparation et réalisation des opérations de maintenance ; équipes sédentaires et mobiles | Chalon | C (S-46, S-47) | BL `ibSiteWorks` |
| IB-F | « Base Installée France (IB-F) » | Entité France de la BU | Lyon, Chalon | C (S-47, S-48) | — |
| Intercontrôle | « filiale à 100 % … rattachée à la BU Base installée » | CND automatisé, inspection en service (cuve, GV) | Rungis, Chalon, Sully, Cadarache | C (S-49, S-50) | BL `ibInspection` ; UO `rungis` |
| CETIC | « centre commun Framatome / EDF où sont créées et qualifiées les techniques et méthodes d'intervention » | Essais et qualification d'interventions sur maquettes | Chalon | C (S-51) | UO `cetic` |
| Framatome ARC | ex-EFINOR Énergie / Défense (mai 2022), soudage et fabrication | — | Beaumont-Hague | C (S-26, S-52) | UO `beaumontHague` |
| Sully-sur-Loire | « l'un des quatre ateliers nucléaires de la Base installée » ; piscine blindée ; CEDOS (décontamination d'outillages) | Entreposage et maintenance d'outillages, Intercontrôle | Sully | C (S-100) | UO `sully` |
| Maubeuge | ex-SOMANU : inspections, réparations, entreposage temporaire d'équipements contaminés (moteurs, hydrauliques, joints de pompes primaires) ; INB → ICPE par décision du 25 mai 2018 | Atelier chaud | Maubeuge | C (S-101) | UO `maubeuge` |
| Framatome Inc. (IB) | Business Lines publiées sur le site carrières US : « Steam Generator Services », « Pump and Motor Field Services », « Outage Services », « Nuclear Parts Center », « Component Replacement & Repair » (IBR), « Global Sales » (IBGS-A), « Advanced Reactor » (IBA-R) | Services base installée Amérique du Nord | Lynchburg | P (S-54 à S-56) | BL `ibInternational` ; UO `lynchburg` |
| Framatome Canada Ltd | Pickering, Kincardine, Montréal ; maintenance, remplacement de composants lourds, inspections, RGV Bruce (JV avec Aecon) | CANDU | Ontario, Québec | C (S-58, S-59, S-112) | BL `ibInternational` ; UO `pickering`, `kincardine`, `montreal` |
| Framatome Ltd (UK) | « more than 350 employees across four locations » | Avonmouth (Bristol), Cranfield, HPC, Sizewell B | Royaume-Uni | C (S-60) | UO `avonmouth`, `cranfield`, `hinkleyPointC`, `sizewell` |
| Reaktortest s.r.o. | CND ; 100 % Framatome depuis juillet 2025 | — | Slovaquie | C (S-61) | UO `reaktortest` |

Non trouvés en source ouverte [NT] : codes IBI, IBO, IBD, IBP (France), « IBM-I » ou entité IBM internationale, BL « Pièces de rechange » ou « Démantèlement » en France.

### 3.2 BU Combustible

| Entité | Libellé exact relevé | Périmètre | Lieu | Conf. | Id modèle |
|---|---|---|---|---|---|
| **FCEE** | « The department FCEE (Fuel Contracts Europe Export) of the business unit Fuel performs contracts and associated customer projects » | Contrats combustible Europe et export | Erlangen | C (S-62) | BL `fuelContracts` |
| Contracts and Services | « Contracts and Services Business Line in the Fuel Business Unit » | Contrats et services | Lynchburg | P (S-63) | BL `fuelContracts` |
| Fuel Design | « Fuel Design team » (analyses de sûreté, méthodes) ; « Fuel Design & Fuel Contracts » | Conception combustible | Lynchburg, Richland | C (US) / NT (libellé France) (S-64) | BL `fuelDesign` |
| Fuel Manufacturing | « Fuel Manufacturing Business Line » ; licence LEU+ à Richland (mai 2026) | Fabrication d'assemblages | Richland ; Romans ; Lingen | C (S-65, S-66, S-74, S-76) | BL `fuelManufacturing` |
| Physique du cœur | « département Physique du Cœur » ; « groupe céramiques, accidents et modélisation » | Études de cœur, modélisation | Lyon | P (S-73) | BL `fuelCore` |
| Fuel Field Services | « Projektmanager Fuel Field Services » | Services combustible sur site | Erlangen | P (S-68) | BL `fuelFieldServices` |
| **DOC** | « Direction des Opérations Composants … métallurgie du zirconium … produits plats, barres et tubes » ; cinq ou six usines selon les offres | Filière zirconium (éponge → composants) | Jarrie, Ugine, Rugles, Montreuil-Juigné, Paimboeuf, (Montbard) | C (S-33, S-69, S-70) | BL `fuelComponentsOperations` |
| CERCA | « Framatome CERCA » ; nouvel atelier Romans inauguré en 2025 (combustible de réacteurs de recherche, cibles médicales) ; ligne pilote TRISO annoncée | Réacteurs de recherche, cibles | Romans | C (S-71, S-72) | BL `fuelCerca` |
| ANF GmbH | Advanced Nuclear Fuels, filiale de Framatome GmbH, ≈ 450 personnes ; Lingen (siège, assemblages ; autorisation VVER-1000 délivrée le 22/07/2026 sous conditions strictes), Karlstein (composants d'assemblages) | Fabrication | Lingen, Karlstein | C (S-76 à S-78) | UO `lingen`, `karlstein` |

[NT] : une BL « Fuel Products » n'a pas été trouvée (seule une catégorie d'achats « Fuel Related Products » existe, S-79) ; aucun code « FL-… » public hors FLDOC.

### 3.3 BU Contrôle-commande

| Entité | Libellé exact relevé | Lieu | Conf. | Id modèle |
|---|---|---|---|---|
| **BL Cybersécurité** | « Cybersecurity business line » (résultats 2025) ; filiales Allentis (qualifiée ANSSI), Cyberwatch, FoxGuard ; marque « Framatome Cybersecurity » (2023) | France, États-Unis | C (S-10, S-16, S-17) | BL `icCyber` |
| Grenoble / Meylan / Montbonnot | ex-Rolls-Royce Civil Nuclear I&C ; regroupement des équipages iséroises à Montbonnot (ex-site Schneider acquis en 2024, transferts jusqu'en 2028) ; fabrication de produits d'instrumentation | Isère | C (sites) / P (codes ICT) (S-25, S-32, S-80) | UO `grenobleMontbonnot` |
| ICTNMU, ICE-U, Specialty Product Manufacturing | « ICTNMU Business Line » (instrumentation nucléaire), « ICE-U Projects Engineer Business Line », « Specialty Product Manufacturing Business Line » | Lynchburg | P (S-81) | BL `icInstrumentation`, `icProjects` |
| Erlangen | « la plus grande installation d'essais au monde pour les systèmes de C-C numériques » (I&C Test Bay) | Erlangen | C (S-57) | UO `erlangen` |
| Karlstein | centre d'excellence sûreté et instrumentation du cœur ; I&C Academy | Karlstein | C (S-77) | UO `karlstein` |
| Corys | simulateurs ; Framatome 50 %, EDF 25 %, IFP Training 25 % | Grenoble | P (S-83) | — (partenaire, typologie `simulator`) |

[NT] : le « pilier EPR/SMR » et le « centre de compétences ingénierie transverse » évoqués en v0.1 n'ont pas été retrouvés ; conservés comme hypothèse [H] (BL `icSafetySystems`).

### 3.4 BU PCM

| Entité | Libellé exact relevé | Lieu | Conf. | Id modèle |
|---|---|---|---|---|
| **BL Robinetterie** | « Valves business line » ; « ligne d'activité Robinetterie de la BU PCM » ; Vanatome, Segault (70/30 avec TechnicAtome), Valserve (ex-Velan SAS), Sebim (ex-Trillium Flow Technologies France) ; ≈ 1 000 personnes | Saint-Victoret, Vendin-le-Vieil, autres | C (S-10, S-20, S-21, S-84) | BL `valves` |
| Usines de composants | « four major industrial sites in France » : Le Creusot (forge ; marquage « PCM - HC »), Saint-Marcel (assemblage de composants lourds ; « PCM - HM »), Jeumont (équipements mobiles ; installation de mesure de haute précision), Montbard (tubes GV, ex-Valinox acquis le 01/06/2021, « Framatome Montbard » depuis le 01/12/2022) | Bourgogne, Nord | C (sites) / P (sens des codes) (S-31, S-85, S-86) | BL `pcmHeavyComponents`, `pcmMobileEquipment`, `pcmSgTubes` |
| Grands projets | « PCM business unit, which houses the large projects and programmes » ; EPR2 : « Framatome now manages all Engineering, Procurement, Construction & Commissioning (EPCC) activities » ; planificateur du projet NUWARD SMR rattaché à PCM | La Défense, Chalon, Lyon | P (aucun code public) (S-87 à S-89) | BL `pcmLargeProjects` |
| Jeumont Electric | filiale de Framatome et de Naval Group (≈ 620 personnes, 4 sites) | Jeumont | C (S-90) | UO `jeumontElectric` |

### 3.5 Direction technique et ingénierie

| Entité | Libellé exact relevé | Lieu | Conf. | Id modèle |
|---|---|---|---|---|
| Division **Ingénierie Mécanique** (DTIM, support DTIMS) | « chargée de réaliser les activités de conception et spécification des composants primaires, auxiliaires et spéciaux » ; département Composants Primaires ; Centre de Calculs Bourgogne | La Défense, Lyon, Saint-Marcel | C (S-22, S-92, S-93, S-114) | BL `dtiMechanicalEngineering` |
| Division **Sûreté et Procédés** | cellule réglementaire ESPN / DESP ; conséquences radiologiques du nouveau nucléaire | Lyon, La Défense | P (S-22, S-94) | BL `dtiSafetyProcess` |
| **Centre Technique** | « Technical Center … Le Creusot and St-Marcel (France), and in Erlangen and Karlstein (Germany) » ; départements Matériaux, Tenue à l'Environnement / Chimie, Mécanique des fluides et des structures / Thermique / CFD, Support technique transverse (mécatronique) | Le Creusot, Chalon, Erlangen, Karlstein | C (S-22, S-95) | BL `dtiTechnicalCenter` |
| R&D | responsables nommés dans des publications 2023 | — | P (S-7) | BL `dtiRd` |

### 3.6 Décompte et limites

Entités nommées publiquement avec un code ou un libellé : IB France 12, IB États-Unis 8, Combustible 7, C-C 4, PCM 2 (plus la robinetterie), DTI 3, soit **≈ 36**, dont une quinzaine seulement avec un sigle. Les offres montrent au moins **quatre niveaux** sous la BU (BL → direction → département → section, ex. IBT → IBTM-F → IBTMOM-F). Le modèle retient deux niveaux (`businessLine`, `operationalUnit`) ; le rattachement des niveaux inférieurs est porté par le champ texte `wbsCode` ou par l'annuaire, jamais par une énumération (§ 7).

## 4. Sites industriels et centres techniques

| Pays / site | Activité (source) | BU | Conf. | Id `operationalUnit` |
|---|---|---|---|---|
| Courbevoie / La Défense | siège, DTI, EPR2 (contrats, achats) | corp, DTI, PCM | C (S-98) | `laDefense` |
| Lyon-Gerland | ≈ 1 700 salariés regroupés en 2019-2021 : IB-F, IBE, IBS, physique du cœur, DTI | IB, Fuel, DTI | C (S-99) | `lyonGerland` |
| Chalon-sur-Saône | > 1 300 salariés : base arrière de la BI (Direction Travaux, CEDEM, CEMO), CETIC, centre d'expertise CND, centre technique | IB, DTI | C (S-51) | `chalon`, `cetic`, `cedem` |
| Sully-sur-Loire | atelier BI, piscine blindée, CEDOS, maintenance des outillages d'inspection (créé en 1998) | IB | C (S-100) | `sully` |
| Maubeuge (ex-SOMANU) | maintenance nucléaire, entreposage d'équipements contaminés ; ICPE depuis 2018 | IB | C (S-101) | `maubeuge` |
| Rungis | siège Intercontrôle | IB | C (S-49) | `rungis` |
| Beaumont-Hague | Framatome ARC (soudage) | IB | C (S-52) | `beaumontHague` |
| Marseille, Cadarache, Marcoule, Creys-Malville | bureaux et antennes IBE ; Intercontrôle Cadarache | IB | P (S-34, S-49) | `marseilleCadarache` |
| Saint-Marcel | composants lourds (cuves, GV, pressuriseurs) ; calculs de composants (DTI) | PCM, DTI | C (S-85) | `saintMarcel` |
| Le Creusot | forge, internes, atelier mécanique, centre technique ; défense (porte-avions) ; centre de fabrication additive annoncé | PCM, DTI, Defense | C (S-85, S-91, S-103) | `leCreusot` |
| Montbard | tubes GV (ex-Valinox) ; une offre le rattache à la DOC (Fuel), la page composants à PCM | PCM / Fuel ? | C (site) / conflit (S-69, S-86) | `montbard` |
| Jeumont | pompes primaires, mécanismes de grappes ; ligne propulsion militaire (2025) ; Jeumont Electric | PCM, Defense | C (S-28, S-85) | `jeumont`, `jeumontElectric` |
| Romans-sur-Isère | assemblages REP + CERCA ; de 1 045 à 1 300 personnes selon les sources | Fuel | C (S-71, S-74, S-75) | `romans` |
| Jarrie, Ugine, Rugles, Montreuil-Juigné, Paimboeuf | filière zirconium : éponge (Jarrie), demi-produits (Ugine), tôles et feuillards (Rugles), tubes, barres et fils (Montreuil-Juigné), tubes de gainage (Paimboeuf) | Fuel | C (S-69, S-70) | `jarrie`, `ugine`, `rugles`, `montreuilJuigne`, `paimboeuf` |
| Grenoble / Meylan / Montbonnot | C-C (ex-Rolls-Royce) ; regroupement à Montbonnot | I&C | C (S-80) | `grenobleMontbonnot` |
| Saint-Victoret, Vendin-le-Vieil | Sebim (robinetterie, 330 personnes) | PCM | C (S-20) | `saintVictoret`, `vendinLeVieil` |
| **Allemagne** — Erlangen | siège de Framatome GmbH (≈ 3 000 personnes, 4 sites) : ingénierie, I&C Test Bay, laboratoires (radiochimie, cellules chaudes), FCEE | IB, I&C, Fuel, DTI | C (S-57, S-77) | `erlangen` |
| Karlstein (deux sites) | ANF (composants d'assemblages) ; I&C sûreté et instrumentation du cœur, I&C Academy ; centre technique | Fuel, I&C, DTI | C (S-77) | `karlstein` |
| Lingen | ANF, usine d'assemblages ; autorisation VVER (2026) | Fuel | C (S-78) | `lingen` |
| **États-Unis** — Lynchburg, VA | siège de Framatome Inc. (de 2 260 à 2 700 personnes selon les sources) : Fuel, IB, I&C ; centre de pièces, centre chimie et matériaux, centre de service pompes et moteurs ; extension de 49,4 M$ annoncée | IB, Fuel, I&C | C (S-82, S-104) | `lynchburg` |
| Richland, WA | fabrication de combustible ; licence LEU+ (mai 2026) | Fuel | C (S-66) | `richland` |
| Cranberry Township, PA ; Charlotte, NC ; Benicia, CA | bureaux | — | P (S-105) | `cranberry` |
| **Royaume-Uni** — Avonmouth, Cranfield, HPC, Sizewell B | > 350 personnes, quatre sites | IB, PCM | C (S-60) | `avonmouth`, `cranfield`, `hinkleyPointC`, `sizewell` |
| **Canada** — Pickering, Kincardine, Montréal | services CANDU ; de 160 à 300 personnes selon les sources ; « Lachine » (v0.1) non confirmé : les sources disent Montréal | IB | C (S-58, S-59) | `pickering`, `kincardine`, `montreal` |
| **Slovaquie** — Reaktortest | CND, 100 % Framatome (2025) | IB | C (S-61) | `reaktortest` |
| Belgique, Bulgarie, Chine (JV FDJV, ex-RR I&C à Pékin et Shenzhen), Tchéquie (Prague), Inde (Velan IT Bengaluru, 2025), Hongrie, Japon, Afrique du Sud, Espagne, Suède | présence listée sur le site ; « hub Navi Mumbai » (v0.1) non retrouvé | — | P (S-25, S-106, S-107) | `pragueBeijingShenzhen`, `externalPartner` |

## 5. Filiales, coentreprises et entités partenaires

| Entité | Nature / rôle | BU | Conf. | Impact ALM |
|---|---|---|---|---|
| **Framatome GmbH** (Erlangen) | filiale allemande ; certificat ASME N-stamp (déc. 2024) | multi | C (S-57, S-108) | Instance standard partagée France / Allemagne ; contrôle export allemand (`deAwg`). |
| **Advanced Nuclear Fuels GmbH** (Lingen, Karlstein) | filiale de Framatome GmbH, ≈ 450 personnes | Fuel | C (S-76) | Projets VVER cloisonnés (droits d'accès stricts, aucune interface automatique avec des systèmes tiers). |
| **Framatome Inc.** (Lynchburg) | filiale nord-américaine ; **Framatome U.S. Government Solutions** (2021, DOE / DoD) | multi | C (S-82, S-104, S-109) | NQA-1, 10 CFR 50 app. B, Part 21, Part 810 → instance US (ADR-03) ; pack `usNrc`. |
| **Intercontrôle SA** (Rungis) | filiale à 100 %, CND et inspection en service, dans la BU IB | IB | C (S-49) | Typologie `inspectionService` ; qualification des procédés CND. |
| **Framatome ARC** | ex-EFINOR (2022), soudage et fabrication | IB | C (S-26, S-52) | Fabrication et points d'arrêt. |
| **CERCA** | activité / marque de Romans (réacteurs de recherche, cibles) ; statut juridique actuel non vérifié | Fuel | C (activité) (S-71) | Typologie `researchReactorFuel`. |
| « Cezus » | filiale historique (2001) ; la filière zirconium apparaît aujourd'hui comme « Direction des Opérations Composants » de la BU Fuel ; aucune entité « Cezus » active trouvée | Fuel | P (S-69, S-110) | BL `fuelComponentsOperations`. |
| Somanu ; Valinox Nucléaire | intégrées comme établissements Framatome (Maubeuge ; Montbard depuis 2022) | IB ; PCM | C (S-86, S-101) | UO `maubeuge`, `montbard`. |
| **Vanatome, Segault** (70/30 avec TechnicAtome), **Valserve** (ex-Velan SAS), **Sebim** | BL Robinetterie | PCM | C (S-10, S-20, S-21) | Composants ESPN : FNC, dérogations, fabrication ; typologie `configureToOrder`. |
| **Jeumont Electric** | co-détenue avec Naval Group (≈ 620 personnes) | PCM / Defense | C (S-90) | Interfaces défense → classification, cloisonnement. |
| **FoxGuard** (US), **Cyberwatch** (FR), **Allentis** (FR, octobre 2024, qualifiée ANSSI) | BL Cybersécurité | I&C | C (S-16, S-17) | Données de vulnérabilité sensibles → instance SENS pour la cybersécurité d'installation (règle D04). |
| **Edvance** | créée le 30 mai 2017, EDF 80 % / Framatome 20 % ; ingénierie de l'îlot nucléaire des nouveaux réacteurs ; salariés IBE mis à disposition (« IBE_MAD EDVANCE ») | IB (MAD), PCM, DTI | C (S-29, S-111) | **Frontière ALM critique** : comptes à double appartenance, droits par projet, échanges ReqIF avec l'architecte-ensemblier, propriété des exigences (ADR-12, Q-ORG-02). |
| **Corys** | Framatome 50 %, EDF 25 %, IFP Training 25 % (simulateurs) | I&C | P (S-83) | Typologie `simulator`. |
| **Reaktortest s.r.o.** | 100 % depuis juillet 2025 | IB | C (S-61) | Hors vague 1. |
| **SGT** (avec United E&C), **Steam Generator Replacement Team** (avec Aecon ; contrat Bruce de 700 M$, 2024) | coentreprises RGV en Amérique du Nord | IB | C (S-112) | Projets `steamGeneratorReplacement` en partenariat : projet sas. |
| **Isogen** (avec Kinectrics), **Global Morpho Pharma** (minoritaire), partenariat **IBA** (At-211) | Framatome Healthcare | Healthcare | C (S-24, S-113) | Typologie `isotopeProduction` (hors vague 1). |
| **Manoir France** | participation minoritaire (juillet 2026) | chaîne d'approvisionnement | C (S-28) | Fournisseur de forgés : CFSI, surveillance. |
| « European Hexagonal Fuel » (JV TVEL), « BHR Group », « Framatome Cyber » (entité) | cités en v0.1 | — | NT | Retirés de la cartographie ; seule la licence VVER / Lingen est documentée (S-78). |

## 6. Écosystème externe structurant

| Acteur | Rôle vis-à-vis de Framatome | Conf. | Impact sur le modèle |
|---|---|---|---|
| **EDF** (exploitant, *licensee*) | Client principal du parc (56 + 1 réacteurs) et des nouveaux réacteurs ; programme numérique **SWITCH** (3DEXPERIENCE pour le PLM depuis 2018, AVEVA depuis 2021) | C | `customerVisa`, `customerApprovalRequired`, `regulatoryModificationClass` ; interopérabilité ReqIF / 3DEXPERIENCE (doc. 22) |
| **ASNR** (Autorité de sûreté nucléaire et de radioprotection, créée le 01/01/2025 par fusion ASN + IRSN, loi 2024-450) | Autorité de contrôle ; inspections des fabricants ESPN ; instruction des dossiers | C | `authority = asnr`, `regulatoryCommitment`, lettres de suite |
| Organismes agréés ESPN | Évaluation de conformité N2 / N3 (agrément par décision ASN, ISO/CEI 17020) ; N1 par l'ASNR ou ses mandataires | C / P\* (numéro de décision à revérifier, Q-REG-05) | `witnessParty = notifiedBody`, points d'arrêt |
| Exploitants étrangers | TVO (OL3), NNB GenCo (HPC), SZC, Eskom (Koeberg), ČEZ (Temelín), Vattenfall (Ringhals), KKG (Gösgen), Slovenské elektrárne… | C | `region`, `authority`, langues |
| Autorités étrangères | ONR (UK), NRC (US), STUK (FI), SÚJB (CZ), CNSC (CA), autorités allemandes | C | Packs réglementaires (A10) ; `safetyClaim` pour l'ONR ; `part21Evaluation` pour le NRC |
| Partenaires constructeurs | Arabelle Solutions (îlot conventionnel, groupe EDF), génie civil, Eviden / Schneider (C-C non classé EPR2) | C / P | `interfaceScope = partnerOem` |
| Fournisseurs (dont forgés : Manoir France) | Chaîne d'approvisionnement ESPN | C / P | `supplierContributor`, CFSI, `actionType = surveillance` |

## 7. Environnement d'outillage d'ingénierie (OSINT)

| Constat public | Conf. | Conséquence d'architecture |
|---|---|---|
| Framatome déploie un « **Core Model** » intégrant l'**ingénierie système et le PLM sur 3DEXPERIENCE** (Dassault Systèmes), avec des interfaces MES / ERP ; au Creusot, la traçabilité est affichée « du cahier des charges aux preuves de fabrication » (offres 2026). | C | **Décision structurante (ADR-07).** Polarion porte les exigences, la V&V, la démonstration, les écarts d'ingénierie et la configuration documentaire ; 3DEXPERIENCE porte la définition produit (nomenclature, CAO) et la fabrication ; identifiants pivots (`plmItemId`) et OSLC / REST. Le PLM reste un paramètre de création de projet (Q17), Teamcenter n'étant pas attesté. |
| **Capella / Arcadia** utilisé sur les grands projets ; outil maison d'échanges Capella–Excel (Capella Day 2019) ; article INCOSE IS2018. | C | Capella maître de l'architecture (ADR-08) ; synchronisation vers Polarion (doc. 22). |
| C-C : outils **SPACE** (diagrammes fonctionnels TELEPERM XS, génération de code) et **SIVAT** (validation par simulation). | C | Traçabilité exigences logicielles → diagrammes par identifiant (`modelElementId`) ; preuves SIVAT en `evidenceReference`. |
| Aucune mention publique de DOORS, Polarion, Cameo ou Teamcenter chez Framatome. | NT | Inventaire interne de l'existant (Q-ARCH-01). Hypothèse « greenfield » confirmée par la demande. |

## 8. Matrice BU × typologies (synthèse)

La matrice complète « typologie → classe, archétype, gabarit, BU » est générée depuis `model/tailoring.yaml` dans l'[annexe A7](../generated/A7_tailoring.md) (32 lignes). Elle fait foi. Lecture rapide des BU pilotes [H] :

| BU | Typologies où la BU est pilote (`projectTypeDefaults[*].bu[0]`) |
|---|---|
| IB | RGV, réexamen périodique, modification, fortuit, outillage, inspection, rénovation C-C (avec I&C), augmentation de puissance, pièces de rechange, atelier chaud, démantèlement, laboratoire |
| Fuel | conception combustible, recharges, services combustible, combustible de recherche, licensing d'usine |
| I&C | plateforme, application, cybersécurité d'installation, simulateur |
| PCM | grand réacteur neuf, conception et fabrication de composants, produit configuré à la commande, qualification de procédé (avec Fuel, DTI) |
| DTI | SMR (études), R&D, code de calcul |
| corp / healthcare / defense | bibliothèques ; isotopes médicaux ; programme défense |

## 9. Ce que l'organisation impose au modèle Polarion

1. **Propriété par BU, réutilisation transverse.** Chaque projet appartient à une BU (paramètre de projet + groupe de projets). Les bibliothèques (réglementaire, terminologie, agressions, cas V&V) sont transverses, sous la responsabilité de la Design Authority ALM.
2. **Multi-entités juridiques.** France, Allemagne, États-Unis, Royaume-Uni, Canada ont des obligations différentes : contrôle export, assurance qualité (ISO 19443 / NQA-1), signalement des défauts (Part 21). D'où `region`, `exportControl`, `qaProgramLevel`, les packs réglementaires et la décision ADR-03 sur les instances (STD, SENS, US, DEF).
3. **Coentreprises et mise à disposition.** Des comptes ont une double appartenance (Framatome / Edvance), et il existe des projets partagés avec EDF ou avec des partenaires de RGV. Les droits sont accordés par projet via des groupes d'annuaire, jamais globalement ; les échanges passent par des projets sas `EXT-*` ou par ReqIF (ADR-28).
4. **Réorganisations fréquentes** (§ 2). L'organisation ne doit **jamais** être codée dans les identifiants de projets, de types ou de champs. Elle vit dans trois énumérations révisables sans migration : `businessUnit` (globale), `businessLine` et `operationalUnit` (portée projet, restreintes à la création du projet, règle D12). Les niveaux inférieurs (départements, sections) ne sont pas modélisés.
5. **Organisation matricielle BU × UO** (ADR-24). Une BU pilote, des UO réalisent : lots de travaux (`workPackage`), attributs `responsibleUnit` / `performingUnit`, tableau de bord par UO ; pas de projet par UO (doc. 21).
6. **Activités sensibles** (défense, sécurité nucléaire, cybersécurité d'installation, VVER sous licence tierce) : cloisonnées par instance ou par projet, classification obligatoire (`informationClassification`), règles de provisioning D03 à D06bis.
7. **Héritage du Creusot** (irrégularités découvertes en 2016 : environ 430 « dossiers barrés », revue d'environ 6 000 dossiers, reprise de la production en 2018 sous conditions ; dispositif CFSI de l'ASN puis de l'ASNR). Exigence forte d'**intégrité des données** : piste d'audit, signatures, baselines figées, absence de suppression, champ `cfsiSuspected` (doc. 15).

## 10. Questions ouvertes pour les ateliers internes

Elles sont consignées au [doc. 05 § 6.1](../partie2/05_Plan_de_recherche_OSINT.md) (Q-ORG-01 à Q-ORG-12) : liste officielle des codes IB-F et de leur signification, périmètre d'IBC (IB ou PCM), lignes de reporting IBE ↔ Edvance ↔ DTI, structure interne de PCM et de la BU Fuel en France, rattachement de Montbard, codes I&C, définition interne du niveau UO (≈ 40 annoncées), découpage des entités allemandes et américaines, statut des entités Defense / Healthcare / Space, filiales à statut incertain, effectifs.
