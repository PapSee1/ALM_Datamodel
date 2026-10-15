# Annexe A2 — Énumérations

> Document **généré** par `tools/generate_docs.py` depuis `model/*.yaml` — ne pas éditer à la main.

Confiance : **C** confirmé par source publique, **P** probable, **H** hypothèse à valider (cf. Partie 2).

## businessUnit

**Business Unit** / Business Unit — confiance **C**

BU propriétaire de l'artefact / du projet, selon l'organisation publiée (page Governance de framatome.com et résultats financiers 2025, consultés en octobre 2026 ; annexe C § 1). Les BU opérationnelles sont IB, Fuel, I&C et PCM ; la Direction technique et ingénierie (DTI) est portée au Comex par la direction « Engineering & Design Authority » et comptée publiquement comme une cinquième BU. Healthcare, Defense et Space sont des marques / divisions. À re-valider à chaque réorganisation.

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `ib` | Base installée (Installed Base, IB) | Installed Base (IB) |  |
| `fuel` | Combustible (BU Fuel) | Fuel |  |
| `ics` | Contrôle-commande (I&C, dont BL Cybersécurité) | Instrumentation & Control (incl. Cybersecurity BL) |  |
| `pcm` | Projets & fabrication de composants (PCM) | Projects & Components Manufacturing (PCM) |  |
| `dti` | Direction technique & ingénierie (DTI / E&DA) | Technical & Engineering Directorate (DTI / E&DA) |  |
| `corp` | Fonctions transverses (Sûreté, Qualité, DSI...) | Corporate functions (Safety, Quality, IT...) |  |
| `healthcare` | Framatome Healthcare (hors vague 1) | Framatome Healthcare (out of wave 1) |  |
| `defense` | Framatome Defense (instance dédiée si requis) | Framatome Defense (dedicated instance if required) |  |
| `space` | Framatome Space (hors vague 1) | Framatome Space (out of wave 1) |  |

## businessLine

**Business Line** / Business Line — *surchargée au niveau projet* — confiance **P**

Niveau immédiatement inférieur à la BU (les unités opérationnelles, sites et départements sont dans operationalUnit). Aucune liste officielle n'est publique : les codes entre parenthèses (IBE, IBM-F, IBC, IBS-F, IBT, FCEE, DOC, DTIM...) proviennent d'offres d'emploi Framatome 2022-2026 (annexe C § 1, sources S-29 à S-95) ; [C] ≥ 2 sources concordantes, [P] une seule source, [H] hypothèse. Liste à confirmer en atelier (Q-ORG-01) et surchargée dans chaque projet.

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `ibEngineering` | BI – Ingénierie (IBE, Engineering Services) | IB – Engineering services (IBE) |  |
| `ibMajorProjects` | BI – Grands projets, remplacement de composants (IBM-F) | IB – Major projects, component replacement (IBM-F) |  |
| `ibConstruction` | BI – Construction nouveau nucléaire (IBC) | IB – New-build construction (IBC) |  |
| `ibMaintenance` | BI – Maintenance / support technique (IBS-F, CEDEM) | IB – Maintenance / technical support (IBS-F, CEDEM) |  |
| `ibSiteWorks` | BI – Direction Travaux (IBT) | IB – Site works directorate (IBT) |  |
| `ibInspection` | BI – Inspection / CND (Intercontrôle) | IB – Inspection / NDE (Intercontrôle) |  |
| `ibInternational` | BI – Entités internationales (Framatome Inc., GmbH, Canada, UK, Reaktortest) | IB – International entities |  |
| `fuelContracts` | Comb. – Contrats et services combustible (FCEE, Contracts & Services) | Fuel – Fuel contracts & services (FCEE) |  |
| `fuelDesign` | Comb. – Conception combustible et méthodes | Fuel – Fuel design & methods |  |
| `fuelCore` | Comb. – Physique du cœur / recharges | Fuel – Core physics / reloads |  |
| `fuelManufacturing` | Comb. – Fabrication d'assemblages (Romans, Lingen, Richland) | Fuel – Fuel assembly manufacturing |  |
| `fuelComponentsOperations` | Comb. – Direction des Opérations Composants (DOC, filière zirconium) | Fuel – Components Operations Directorate (DOC, zirconium) |  |
| `fuelCerca` | Comb. – CERCA (réacteurs de recherche, cibles médicales) | Fuel – CERCA (research reactors, medical targets) |  |
| `fuelFieldServices` | Comb. – Services combustible sur site | Fuel – Fuel field services |  |
| `icSafetySystems` | C-C – Systèmes de sûreté et plateformes qualifiées | I&C – Safety systems & qualified platforms |  |
| `icInstrumentation` | C-C – Instrumentation nucléaire et produits | I&C – Nuclear instrumentation & products |  |
| `icProjects` | C-C – Projets et services | I&C – Projects & services |  |
| `icCyber` | C-C – Cybersécurité | I&C – Cybersecurity |  |
| `pcmLargeProjects` | PCM – Grands projets et programmes (EPR2, HPC, SZC, NUWARD) | PCM – Large projects & programmes |  |
| `pcmHeavyComponents` | PCM – Composants lourds (Le Creusot, Saint-Marcel) | PCM – Heavy components (Le Creusot, Saint-Marcel) |  |
| `pcmMobileEquipment` | PCM – Équipements mobiles, pompes et mécanismes (Jeumont) | PCM – Mobile equipment, pumps & mechanisms (Jeumont) |  |
| `pcmSgTubes` | PCM – Tubes de générateurs de vapeur (Montbard, ex-Valinox) | PCM – Steam generator tubes (Montbard) |  |
| `valves` | PCM – BL Robinetterie (Vanatome, Segault, Valserve, Sebim) | PCM – Valves BL |  |
| `dtiMechanicalEngineering` | DTI – Division Ingénierie Mécanique (DTIM) | DTI – Mechanical Engineering division (DTIM) |  |
| `dtiSafetyProcess` | DTI – Division Sûreté et Procédés | DTI – Safety & Process division |  |
| `dtiTechnicalCenter` | DTI – Centre technique (Le Creusot, Chalon, Erlangen, Karlstein) | DTI – Technical centre |  |
| `dtiRd` | DTI – R&D | DTI – R&D |  |
| `other` | Autre (à préciser) | Other (specify) |  |

## projectType

**Typologie de projet** / Project type

Pilote le tailoring (model/tailoring.yaml) et le gabarit de projet Polarion.

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `newBuildLarge` | Nouveau nucléaire – grand réacteur (EPR, EPR2) | New build – large reactor (EPR, EPR2) |  |
| `newBuildSmr` | Nouveau nucléaire – SMR (NUWARD) | New build – SMR (NUWARD) |  |
| `steamGeneratorReplacement` | Remplacement de gros composants (RGV/SGR, MCR CANDU, couvercles...) | Large component replacement (SGR, CANDU MCR, heads...) |  |
| `periodicSafetyReview` | Réexamen périodique / VD / rapport de conclusions du réexamen | Periodic safety review / ten-year outage |  |
| `plantModification` | Étude de modification base installée | Installed-base plant modification |  |
| `fortuit` | Fortuit / aléa en arrêt de tranche (cycle court) | Unplanned event / emergent outage issue |  |
| `specialTooling` | Outillage spécial (mécatronique, robotique, manutention) | Special tooling (mechatronics, robotics, handling) |  |
| `inspectionService` | Prestation d'inspection / CND / ISI | Inspection / NDE / ISI service |  |
| `fuelDesign` | Conception combustible (nouvel assemblage, ATF) | Fuel design (new assembly, ATF) |  |
| `fuelReload` | Contrat de recharge (études de cœur) | Reload contract (core design) |  |
| `icPlatform` | Plateforme C-C (produit générique) | I&C platform (generic product) |  |
| `icApplication` | Application / projet C-C | I&C application project |  |
| `icRefurbishment` | Rénovation C-C base installée | I&C refurbishment |  |
| `componentDesign` | Conception de composant (GV, pressuriseur, RCP, MCG...) | Component design (SG, PZR, RCP, CRDM...) |  |
| `componentManufacturing` | Fabrication de composant (ESPN) | Component manufacturing (ESPN) |  |
| `rdProgram` | Programme R&D / innovation | R&D / innovation programme |  |
| `library` | Projet bibliothèque / référentiel | Library / reference project |  |
| `powerUprate` | Augmentation de puissance d'une tranche existante | Power uprate |  |
| `sparePartsEquivalence` | Pièces de rechange, obsolescence, qualification d'équivalents (CGD) | Spare parts, obsolescence, equivalence qualification |  |
| `hotWorkshopRepair` | Réparation en atelier chaud (équipements contaminés) | Hot workshop repair (contaminated equipment) |  |
| `decommissioning` | Démantèlement / découpe (cycle en V inversé) | Decommissioning / segmentation |  |
| `fuelSiteServices` | Services combustible sur site (inspection, réparation d'assemblages) | Fuel site services (inspection, repair) |  |
| `researchReactorFuel` | Combustible et cibles de réacteurs de recherche (MTR) | Research reactor fuel & targets (MTR) |  |
| `facilityLicensing` | Licensing usine / transport (criticité, LEU+/HALEU, emballages) | Fuel facility / transport licensing (criticality, LEU+/HALEU, casks) |  |
| `processQualification` | Qualification de procédé / matériau (alliage Zr, fabrication additive, soudage) | Process / material qualification (Zr alloy, AM, welding) |  |
| `simulator` | Simulateur pleine échelle / plateforme de validation | Full-scope simulator / validation platform |  |
| `cybersecurityCompliance` | Mise en conformité cybersécurité d'une installation | Plant cybersecurity compliance |  |
| `calculationCode` | Développement et qualification d'un code de calcul scientifique | Scientific calculation code development & qualification |  |
| `labTesting` | Essais de laboratoire / cellules chaudes (ISO/IEC 17025) | Laboratory / hot-cell testing (ISO/IEC 17025) |  |
| `configureToOrder` | Produit catalogue configuré à la commande (FCCS, PAR, instrumentation...) | Configure-to-order catalogue product |  |
| `isotopeProduction` | Système de production d'isotopes médicaux (sûreté + BPF/GMP) | Medical isotope production system (nuclear + GMP) |  |
| `defenseProgram` | Programme défense / propulsion (instance dédiée isolée) | Defence / propulsion programme (dedicated isolated instance) |  |

## projectClass

**Classe de projet (tailoring)** / Project class (tailoring)

Résultat de la grille de tailoring (docs/partie3/07). Le socle non négociable s'applique à toutes les classes.

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `classA` | A – Programme majeur (cycle en V complet, MBSE) | A – Major programme (full V, MBSE) |  |
| `classB` | B – Projet significatif (V complet allégé) | B – Significant project (lean full V) |  |
| `classC` | C – Projet courant / récurrent (réutilisation) | C – Routine / recurring project (reuse) |  |
| `classD` | D – Express (fortuit, petite adaptation) | D – Express (emergent, small adaptation) |  |

## lifecyclePhase

**Phase du cycle de vie** / Life-cycle phase

Utilisée par : `action.lifecyclePhase`, `analysis.lifecyclePhase`, `anomaly.lifecyclePhase`, `assumption.lifecyclePhase`, `changeRequest.lifecyclePhase`, `deliverable.lifecyclePhase`, `designDecision.lifecyclePhase`, `designParameter.lifecyclePhase`, `equipmentRequirement.lifecyclePhase`, `fmeaItem.lifecyclePhase`, `function.lifecyclePhase`, `hardwareRequirement.lifecyclePhase` …

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `preConceptual` | Pré-conception / faisabilité | Pre-conceptual / feasibility |  |
| `conceptual` | Conception préliminaire (APS / Conceptual) | Conceptual design |  |
| `basic` | Conception de base (APD / Basic design) | Basic design |  |
| `detailed` | Conception détaillée (études d'exécution) | Detailed design |  |
| `manufacturing` | Approvisionnement & fabrication | Procurement & manufacturing |  |
| `construction` | Construction / montage / intervention site | Construction / erection / site works |  |
| `commissioning` | Essais & mise en service | Testing & commissioning |  |
| `operation` | Exploitation / support à l'exploitation | Operation / operation support |  |
| `lto` | Réexamen / poursuite de fonctionnement (LTO) | Periodic review / long-term operation |  |
| `decommissioning` | Mise à l'arrêt définitif / démantèlement | Decommissioning |  |

## plantSeries

**Palier / modèle de réacteur** / Plant series / reactor model — confiance **P**

Applicabilité produit. Les paliers français sont publics (900 CP0/CPY, 1300 P4/P'4, 1450 N4, EPR). Valeurs étrangères à étendre.

Utilisée par : `action.applicablePlantSeries`, `analysis.applicablePlantSeries`, `anomaly.applicablePlantSeries`, `assumption.applicablePlantSeries`, `changeRequest.applicablePlantSeries`, `deliverable.applicablePlantSeries`, `designDecision.applicablePlantSeries`, `designParameter.applicablePlantSeries`, `equipmentRequirement.applicablePlantSeries`, `fmeaItem.applicablePlantSeries`, `function.applicablePlantSeries`, `hardwareRequirement.applicablePlantSeries` …

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `cp0` | 900 MWe – CP0 | 900 MWe – CP0 |  |
| `cpy` | 900 MWe – CPY (CP1/CP2) | 900 MWe – CPY (CP1/CP2) |  |
| `p4` | 1300 MWe – P4 | 1300 MWe – P4 |  |
| `p4prime` | 1300 MWe – P'4 | 1300 MWe – P'4 |  |
| `n4` | 1450 MWe – N4 | 1450 MWe – N4 |  |
| `eprFa3` | EPR – Flamanville 3 | EPR – Flamanville 3 |  |
| `eprOl3` | EPR – Olkiluoto 3 | EPR – Olkiluoto 3 |  |
| `eprTaishan` | EPR – Taishan 1/2 | EPR – Taishan 1/2 |  |
| `eprUk` | UK EPR (HPC, SZC) | UK EPR (HPC, SZC) |  |
| `epr2` | EPR2 | EPR2 |  |
| `nuward` | SMR NUWARD | NUWARD SMR |  |
| `pwrForeign` | REP étranger (autre conception) | Foreign PWR (other design) |  |
| `bwr` | REB (BWR) | BWR |  |
| `vver` | VVER | VVER |  |
| `researchReactor` | Réacteur de recherche | Research reactor |  |
| `generic` | Générique (tous paliers) | Generic (all series) |  |

## plantUnit

**Tranche (unité)** / Unit — *surchargée au niveau projet*

Gabarit : chaque projet surcharge la liste avec ses tranches (code site + numéro). Valeurs exemples uniquement.

Utilisée par : `action.applicableUnits`, `analysis.applicableUnits`, `anomaly.applicableUnits`, `assumption.applicableUnits`, `changeRequest.applicableUnits`, `deliverable.applicableUnits`, `designDecision.applicableUnits`, `designParameter.applicableUnits`, `equipmentRequirement.applicableUnits`, `fmeaItem.applicableUnits`, `function.applicableUnits`, `hardwareRequirement.applicableUnits` …

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `tbd` | À définir | To be defined | ✔ |

## frenchSite

**Site nucléaire (France)** / Nuclear site (France) — confiance **C**

CNPE en exploitation (source publique ASN(R)/EDF). Étendre pour l'international.

Utilisée par : `technicalIssue.site`, `unitDeployment.deploymentSite`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `belleville` | Belleville | Belleville |  |
| `blayais` | Blayais | Blayais |  |
| `bugey` | Bugey | Bugey |  |
| `cattenom` | Cattenom | Cattenom |  |
| `chinon` | Chinon | Chinon |  |
| `chooz` | Chooz | Chooz |  |
| `civaux` | Civaux | Civaux |  |
| `cruas` | Cruas | Cruas |  |
| `dampierre` | Dampierre | Dampierre |  |
| `flamanville` | Flamanville | Flamanville |  |
| `golfech` | Golfech | Golfech |  |
| `gravelines` | Gravelines | Gravelines |  |
| `nogent` | Nogent-sur-Seine | Nogent-sur-Seine |  |
| `paluel` | Paluel | Paluel |  |
| `penly` | Penly | Penly |  |
| `stAlban` | Saint-Alban | Saint-Alban |  |
| `stLaurent` | Saint-Laurent-des-Eaux | Saint-Laurent-des-Eaux |  |
| `tricastin` | Tricastin | Tricastin |  |
| `foreign` | Site étranger (préciser) | Foreign site (specify) |  |

## region

**Entité / juridiction** / Entity / jurisdiction

Juridiction applicable (réglementation, contrôle export, résidence des données).

Utilisée par : `regulatoryRequirement.jurisdiction`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `fr` | France | France |  |
| `de` | Allemagne | Germany |  |
| `us` | États-Unis | United States |  |
| `uk` | Royaume-Uni | United Kingdom |  |
| `fi` | Finlande | Finland |  |
| `cn` | Chine | China |  |
| `cz` | République tchèque | Czech Republic |  |
| `eu` | Union européenne (générique) | European Union (generic) |  |
| `intl` | International (AIEA) | International (IAEA) |  |
| `ca` | Canada | Canada |  |
| `in` | Inde | India |  |
| `za` | Afrique du Sud | South Africa |  |
| `se` | Suède | Sweden |  |
| `ch` | Suisse | Switzerland |  |
| `sk` | Slovaquie | Slovakia |  |
| `other` | Autre | Other |  |

## discipline

**Discipline** / Discipline

Discipline pilote de l'artefact. Codes 3 lettres utilisables dans les identifiants externes.

Utilisée par : `action.contributingDisciplines`, `action.discipline`, `analysis.contributingDisciplines`, `analysis.discipline`, `anomaly.contributingDisciplines`, `anomaly.discipline`, `assumption.contributingDisciplines`, `assumption.discipline`, `changeRequest.contributingDisciplines`, `changeRequest.discipline`, `changeRequest.impactedDisciplines`, `deliverable.contributingDisciplines` …

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `sys` | SYS – Ingénierie système & architecture | SYS – Systems engineering & architecture |  |
| `sur` | SUR – Sûreté nucléaire (déterministe) | SUR – Nuclear safety (deterministic) |  |
| `eps` | EPS – Études probabilistes de sûreté | PSA – Probabilistic safety assessment |  |
| `agr` | AGR – Agressions internes & externes | HAZ – Internal & external hazards |  |
| `neu` | NEU – Neutronique / physique du cœur | NEU – Neutronics / core physics |  |
| `thy` | THY – Thermohydraulique | THY – Thermal-hydraulics |  |
| `cmb` | CMB – Conception & mécanique combustible | FUE – Fuel design & mechanics |  |
| `mec` | MEC – Mécanique, calculs (cuve, GV, tuyauteries, supports) | MEC – Mechanical design & stress analysis |  |
| `mat` | MAT – Matériaux, métallurgie, chimie | MAT – Materials, metallurgy, chemistry |  |
| `pro` | PRO – Procédés / systèmes fluides | PRO – Process / fluid systems |  |
| `hva` | HVA – Ventilation / HVAC | HVA – HVAC |  |
| `ele` | ELE – Électricité (distribution, alimentations) | ELE – Electrical (distribution, power supply) |  |
| `icc` | ICC – Contrôle-commande (système, matériel, logiciel) | ICC – I&C (system, hardware, software) |  |
| `cyb` | CYB – Cybersécurité | CYB – Cybersecurity |  |
| `gcv` | GCV – Génie civil & structures | CIV – Civil works & structures |  |
| `sis` | SIS – Sismique & dynamique | SEI – Seismic & dynamics |  |
| `rpr` | RPR – Radioprotection (ALARA, protections biologiques) | RPR – Radiation protection (ALARA, shielding) |  |
| `foh` | FOH – Facteurs organisationnels & humains (IHM) | HFE – Human factors engineering (HMI) |  |
| `env` | ENV – Environnement, rejets, déchets | ENV – Environment, discharges, waste |  |
| `fab` | FAB – Fabrication, soudage, procédés spéciaux | MFG – Manufacturing, welding, special processes |  |
| `cnd` | CND – Contrôles non destructifs / inspection | NDE – Non-destructive examination / inspection |  |
| `qmt` | QMT – Qualification des matériels (K1-K3, séisme, CEM) | EQ – Equipment qualification (harsh env., seismic, EMC) |  |
| `ess` | ESS – Essais & mise en service | TST – Testing & commissioning |  |
| `sdf` | SDF – Sûreté de fonctionnement (FMDS/RAMS) | RAM – Dependability (RAMS) |  |
| `mnt` | MNT – Maintenance, SLI, exploitabilité | MNT – Maintenance, ILS, operability |  |
| `out` | OUT – Outillages, mécatronique, robotique, manutention | TOO – Tooling, mechatronics, robotics, handling |  |
| `lay` | LAY – Implantation / CAO 3D | LAY – Layout / 3D CAD |  |
| `sec` | SEC – Sécurité nucléaire (malveillance) – instance dédiée | SEC – Nuclear security – dedicated instance |  |
| `cfg` | CFG – Gestion de configuration | CFG – Configuration management |  |
| `qal` | QAL – Qualité / surveillance | QAL – Quality assurance / oversight |  |
| `pmo` | PMO – Management de projet | PMO – Project management |  |
| `ach` | ACH – Achats / chaîne d'approvisionnement | SCM – Procurement / supply chain |  |
| `lic` | LIC – Licensing / relations autorités | LIC – Licensing / regulator interface |  |

## stakeholder

**Partie prenante** / Stakeholder

Utilisée par : `sourceRequirement.sourceIssuer`, `stakeholderRequirement.stakeholder`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `customerUtility` | Client exploitant / électricien | Customer utility / licensee |  |
| `architectEngineer` | Architecte-ensemblier | Architect-engineer |  |
| `operator` | Conduite / exploitation | Plant operations |  |
| `maintenance` | Maintenance | Maintenance |  |
| `regulator` | Autorité de sûreté / organisme agréé | Safety regulator / notified body |  |
| `fuelManager` | Gestionnaire combustible | Fuel manager |  |
| `manufacturing` | Fabrication interne | Internal manufacturing |  |
| `supplier` | Fournisseur / sous-traitant | Supplier / subcontractor |  |
| `publicEnv` | Public / environnement | Public / environment |  |
| `decommissioner` | Démantèlement / déchets | Decommissioning / waste |  |
| `internalRd` | R&D / marketing produit | R&D / product marketing |  |

## language

**Langue** / Language

Utilisée par : `deliverable.language`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `fr` | Français | French | ✔ |
| `en` | Anglais | English |  |
| `de` | Allemand | German |  |
| `zh` | Chinois | Chinese |  |
| `other` | Autre | Other |  |

## reqCategory

**Catégorie d'exigence** / Requirement category

Catégorie principale (une seule). Les catégories secondaires passent par le champ 'Catégories' natif Polarion si besoin.

Utilisée par : `equipmentRequirement.reqCategory`, `hardwareRequirement.reqCategory`, `safetyRequirement.reqCategory`, `softwareRequirement.reqCategory`, `stakeholderRequirement.reqCategory`, `systemRequirement.reqCategory`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `functional` | Fonctionnelle | Functional |  |
| `performance` | Performance | Performance |  |
| `interface` | Interface | Interface |  |
| `safety` | Sûreté nucléaire | Nuclear safety |  |
| `radiationProtection` | Radioprotection | Radiation protection |  |
| `cybersecurity` | Cybersécurité | Cybersecurity |  |
| `humanFactors` | Facteurs humains / IHM | Human factors / HMI |  |
| `environmentalConditions` | Conditions d'environnement (ambiance, irradiation) | Environmental conditions |  |
| `seismic` | Sismique | Seismic |  |
| `hazardProtection` | Protection contre les agressions | Hazard protection |  |
| `regulatory` | Réglementaire / normative | Regulatory / code |  |
| `quality` | Qualité / assurance qualité | Quality assurance |  |
| `reliability` | Sûreté de fonctionnement (fiabilité, disponibilité) | Reliability / availability |  |
| `maintainability` | Maintenabilité | Maintainability |  |
| `operability` | Exploitabilité / conduite | Operability |  |
| `inspectability` | Inspectabilité (ISI / CND) | Inspectability (ISI / NDE) |  |
| `manufacturability` | Fabricabilité | Manufacturability |  |
| `constructability` | Constructibilité / montage / intervention | Constructability / installation |  |
| `testability` | Testabilité / essais périodiques | Testability / periodic testing |  |
| `materials` | Matériaux & chimie | Materials & chemistry |  |
| `ageing` | Vieillissement / durée de vie | Ageing / design life |  |
| `environment` | Environnement (rejets, déchets) | Environment (discharges, waste) |  |
| `decommissioning` | Démantèlement | Decommissioning |  |
| `logistics` | Logistique / transport / manutention | Logistics / transport / handling |  |
| `documentation` | Documentation / livrables | Documentation / deliverables |  |
| `designConstraint` | Contrainte de conception | Design constraint |  |
| `designCriterion` | Critère de conception (combustible, mécanique) | Design criterion |  |
| `criticalitySafety` | Sûreté-criticité | Criticality safety |  |
| `transportPackage` | Transport / emballage de matières | Transport package |  |
| `pharmaceuticalGmp` | Qualité pharmaceutique (BPF / GMP) | Pharmaceutical quality (GMP) |  |
| `simulatorFidelity` | Fidélité de simulation | Simulator fidelity |  |

## reqLevel

**Niveau d'exigence** / Requirement level

Utilisée par : `equipmentRequirement.reqLevel`, `systemRequirement.reqLevel`, `verificationCase.vvLevel`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `plant` | Installation / tranche | Plant / unit |  |
| `system` | Système (élémentaire) | System |  |
| `subsystem` | Sous-système | Subsystem |  |
| `equipment` | Équipement / matériel | Equipment |  |
| `component` | Composant / pièce | Component / part |  |
| `software` | Logiciel | Software |  |
| `hardware` | Matériel électronique / HDL | Hardware / HDL |  |

## bindingLevel

**Force de l'exigence** / Binding level

Doit (prescriptif) / devrait (recommandation) / peut (information). Conforme au style INCOSE GtWR et aux verbes normatifs IEC/ISO.

Utilisée par : `equipmentRequirement.bindingLevel`, `hardwareRequirement.bindingLevel`, `regulatoryRequirement.bindingLevel`, `safetyRequirement.bindingLevel`, `softwareRequirement.bindingLevel`, `sourceRequirement.bindingLevel`, `stakeholderRequirement.bindingLevel`, `systemRequirement.bindingLevel`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `mandatory` | Prescriptive (doit / shall) | Mandatory (shall) | ✔ |
| `recommendation` | Recommandation (devrait / should) | Recommendation (should) |  |
| `permission` | Permission (peut / may) | Permission (may) |  |
| `information` | Information / contexte | Information / context |  |

## maturity

**Maturité** / Maturity

Utilisée par : `equipmentRequirement.maturity`, `hardwareRequirement.maturity`, `interface.maturity`, `safetyRequirement.maturity`, `softwareRequirement.maturity`, `stakeholderRequirement.maturity`, `systemRequirement.maturity`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `tbd` | À définir (TBD) | To be defined (TBD) |  |
| `tbc` | À confirmer (TBC) | To be confirmed (TBC) |  |
| `preliminary` | Préliminaire | Preliminary | ✔ |
| `consolidated` | Consolidée | Consolidated |  |
| `frozen` | Figée (gelée) | Frozen |  |

## complianceStatus

**Statut de conformité** / Compliance status

Position de conformité à une exigence d'entrée (matrice de conformité client / réglementaire).

Utilisée par : `equipmentRequirement.supplierComplianceStatus`, `hardwareRequirement.supplierComplianceStatus`, `regulatoryRequirement.complianceStatus`, `softwareRequirement.supplierComplianceStatus`, `sourceRequirement.complianceStatus`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `toBeAssessed` | À évaluer | To be assessed | ✔ |
| `compliant` | Conforme | Compliant |  |
| `compliantWithComment` | Conforme avec commentaire | Compliant with comment |  |
| `partiallyCompliant` | Partiellement conforme | Partially compliant |  |
| `nonCompliant` | Non conforme | Non-compliant |  |
| `deviationRequested` | Dérogation demandée | Deviation requested |  |
| `clarificationRequested` | Clarification demandée au client | Clarification requested |  |
| `notApplicable` | Non applicable (justifié) | Not applicable (justified) |  |

## requirementSourceType

**Nature de la source** / Source type

Utilisée par : `sourceRequirement.requirementSourceType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `contract` | Contrat / CCTP / spécification client | Contract / customer specification |  |
| `customerStandard` | Référentiel / prescription client | Customer standard |  |
| `utilityRequirements` | Exigences d'électriciens (EUR, URD) | Utility requirements (EUR, URD) |  |
| `licensingCommitment` | Engagement de licensing | Licensing commitment |  |
| `internalStandard` | Standard / règle interne | Internal standard |  |
| `operatingExperience` | Retour d'expérience (REX) | Operating experience |  |
| `productStrategy` | Stratégie produit / marché | Product / market strategy |  |
| `stakeholderWorkshop` | Atelier parties prenantes | Stakeholder workshop |  |
| `supplierData` | Donnée fournisseur | Supplier data |  |

## regulatoryDocType

**Type de texte réglementaire / normatif** / Regulatory / normative document type

Utilisée par : `regulatoryRequirement.regulatoryDocType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `law` | Loi / code (Code de l'environnement...) | Law / code |  |
| `decree` | Décret | Decree |  |
| `ministerialOrder` | Arrêté (INB, ESPN...) | Ministerial order |  |
| `regulatorDecision` | Décision réglementaire de l'autorité | Regulator decision |  |
| `regulatorGuide` | Guide de l'autorité | Regulator guide |  |
| `regulatorPosition` | Position / courrier de l'autorité | Regulator position letter |  |
| `iaeaStandard` | Norme de sûreté AIEA | IAEA safety standard |  |
| `designCode` | Code de conception (AFCEN RCC-x, ASME) | Design code (AFCEN RCC-x, ASME) |  |
| `intlStandard` | Norme internationale (IEC, ISO, IEEE) | International standard (IEC, ISO, IEEE) |  |
| `euLegislation` | Législation UE (règlement, directive) | EU legislation |  |
| `foreignRegulation` | Réglementation étrangère (10 CFR, SAP ONR, YVL...) | Foreign regulation |  |
| `utilityDoc` | Document d'exigences d'électriciens | Utility requirement document |  |
| `industryGuide` | Guide industriel / bonne pratique | Industry guide / good practice |  |

## verificationMethod

**Méthode de vérification** / Verification method

Méthodes IADT (ISO/IEC/IEEE 29148) complétées des pratiques nucléaires (revue, similitude, essai de qualification, certificat).

Utilisée par : `equipmentRequirement.verificationMethods`, `hardwareRequirement.verificationMethods`, `interface.verificationMethods`, `safetyRequirement.verificationMethods`, `softwareRequirement.verificationMethods`, `stakeholderRequirement.verificationMethods`, `systemRequirement.verificationMethods`, `verificationCase.verificationMethod`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `inspection` | Inspection / contrôle | Inspection |  |
| `analysis` | Analyse / calcul / simulation | Analysis / calculation / simulation |  |
| `demonstration` | Démonstration | Demonstration |  |
| `test` | Essai | Test |  |
| `review` | Revue (conception, documentaire) | Review (design, document) |  |
| `similarity` | Similitude / justification par REX | Similarity |  |
| `qualificationTest` | Essai de qualification | Qualification test |  |
| `certificate` | Certificat / attestation fournisseur | Certificate of conformity |  |
| `commercialGradeSurvey` | Évaluation du fournisseur commercial (CGD méthode 2) | Commercial grade survey (CGD method 2) |  |
| `sourceVerification` | Vérification à la source (CGD méthode 3) | Source verification (CGD method 3) |  |
| `performanceHistory` | Historique de performance de l'article / du fournisseur (CGD méthode 4) | Acceptable item / supplier performance record (CGD method 4) |  |

## vvType

**Nature V&V** / V&V type

Utilisée par : `verificationCase.vvType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `verification` | Vérification (le produit est-il bien fait ?) | Verification | ✔ |
| `validation` | Validation (est-ce le bon produit ?) | Validation |  |

## vvStage

**Étape V&V** / V&V stage

Utilisée par : `anomaly.detectedIn`, `equipmentRequirement.vvStagesPlanned`, `hardwareRequirement.vvStagesPlanned`, `safetyRequirement.vvStagesPlanned`, `softwareRequirement.vvStagesPlanned`, `stakeholderRequirement.vvStagesPlanned`, `systemRequirement.vvStagesPlanned`, `verificationCase.vvStage`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `designReview` | Revue de conception | Design review |  |
| `designAnalysis` | Études / analyses de conception | Design analysis |  |
| `mockup` | Prototype / maquette | Prototype / mock-up |  |
| `qualification` | Qualification | Qualification |  |
| `manufacturing` | Contrôles de fabrication | Manufacturing inspection |  |
| `fat` | Essais usine (FAT) | Factory acceptance test (FAT) |  |
| `integration` | Intégration (plateforme / banc) | Integration (platform / bench) |  |
| `siteInstallation` | Montage / installation site | Site installation |  |
| `sat` | Essais sur site (SAT) | Site acceptance test (SAT) |  |
| `preoperational` | Essais de pré-exploitation (à froid / à chaud) | Pre-operational tests (cold / hot) |  |
| `startup` | Essais de démarrage | Start-up tests |  |
| `periodic` | Essais périodiques (exploitation) | Periodic tests (operation) |  |
| `requalification` | Requalification post-intervention | Post-maintenance requalification |  |
| `inService` | Inspection en service (ISI) | In-service inspection |  |
| `reloadStartupPhysics` | Essais physiques de redémarrage (recharge) | Reload start-up physics tests |  |
| `installationQualification` | Qualification d'installation (QI / IQ – BPF) | Installation qualification (IQ – GMP) |  |
| `operationalQualification` | Qualification opérationnelle (QO / OQ – BPF) | Operational qualification (OQ – GMP) |  |
| `performanceQualification` | Qualification de performance (QP / PQ – BPF) | Performance qualification (PQ – GMP) |  |

## vvStatus

**Statut V&V** / V&V status

Sur une exigence : calculé (script) à partir des cas de vérification liés et des derniers enregistrements de Test Run.

Utilisée par : `equipmentRequirement.verificationStatus`, `hardwareRequirement.verificationStatus`, `regulatoryRequirement.verificationStatus`, `safetyRequirement.verificationStatus`, `softwareRequirement.verificationStatus`, `sourceRequirement.verificationStatus`, `stakeholderRequirement.verificationStatus`, `systemRequirement.verificationStatus`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `notPlanned` | Non planifiée | Not planned | ✔ |
| `planned` | Planifiée | Planned |  |
| `inProgress` | En cours | In progress |  |
| `passed` | Satisfaisante | Passed |  |
| `passedWithReserves` | Satisfaisante avec réserves | Passed with reserves |  |
| `failed` | Non satisfaisante | Failed |  |
| `waived` | Couverte par dérogation | Waived |  |
| `notApplicable` | Non applicable | Not applicable |  |

## testEnvironment

**Environnement de vérification** / Verification environment

Utilisée par : `verificationCase.testEnvironment`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `desk` | Bureau d'études (analyse, revue) | Desk (analysis, review) |  |
| `simulator` | Simulateur / jumeau numérique | Simulator / digital twin |  |
| `testBench` | Banc d'essais / plateforme | Test bench / platform |  |
| `mockup` | Maquette (échelle 1 ou réduite) | Mock-up |  |
| `laboratory` | Laboratoire / boucle d'essais | Laboratory / test loop |  |
| `factory` | Usine | Factory |  |
| `site` | Site (hors tranche en service) | Site (construction) |  |
| `plant` | Tranche en exploitation | Operating plant |  |
| `reactor` | Irradiation en réacteur (LTA / essais) | In-reactor irradiation (LTA / tests) |  |
| `hotCell` | Cellule chaude / laboratoire actif | Hot cell / active laboratory |  |
| `testLoop` | Boucle d'essais (thermohydraulique, endurance) | Test loop |  |
| `hotWorkshop` | Atelier chaud (équipements contaminés) | Hot workshop (contaminated equipment) |  |

## inspectionPoint

**Point d'inspection** / Inspection point

Point d'arrêt (H) : l'opération ne peut se poursuivre sans levée formelle ; point de notification (W) : la partie est convoquée ; revue (R) : revue documentaire.

Utilisée par : `verificationCase.inspectionPoint`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `none` | Aucun | None | ✔ |
| `hold` | H – Point d'arrêt | H – Hold point |  |
| `witness` | W – Point de notification / témoin | W – Witness point |  |
| `review` | R – Revue documentaire | R – Document review |  |

## witnessParty

**Partie convoquée** / Witness party

Utilisée par : `verificationCase.witnessParties`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `internalQa` | Qualité interne | Internal QA |  |
| `customer` | Client (surveillance) | Customer (oversight) |  |
| `notifiedBody` | Organisme notifié / agréé (ESPN) | Notified / approved body |  |
| `regulator` | Autorité de sûreté | Safety regulator |  |
| `thirdParty` | Tierce partie / inspecteur indépendant | Third-party inspector |  |
| `supplier` | Fournisseur | Supplier |  |

## independenceLevel

**Niveau d'indépendance** / Independence level

Contrôle technique des AIP : réalisé par des personnes différentes de celles ayant accompli l'activité (arrêté INB). Les niveaux supérieurs sont requis pour le logiciel de catégorie A (IEC 60880).

Utilisée par : `verificationCase.independenceLevel`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `selfCheck` | Autocontrôle (non suffisant pour AIP) | Self-check (not sufficient for AIP) |  |
| `differentPerson` | Personne différente (contrôle technique) | Different person (technical check) | ✔ |
| `differentTeam` | Équipe différente | Different team |  |
| `independentOrg` | Organisation indépendante (V&V indépendante) | Independent organisation (IV&V) |  |

## yesNoTbd

**Oui / Non / À déterminer** / Yes / No / TBD

Utilisée par : `analysis.aip`, `anomaly.safetyImpact`, `assumption.safetyRelevant`, `changeRequest.affectsEip`, `changeRequest.customerApprovalRequired`, `changeRequest.safetyImpact`, `changeRequest.safetyReportImpact`, `deliverable.aip`, `equipmentRequirement.customerApprovalRequired`, `equipmentRequirement.definedRequirement`, `equipmentRequirement.espnRelevant`, `equipmentRequirement.safetyRelevant` …

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `tbd` | À déterminer | To be determined | ✔ |
| `yes` | Oui | Yes |  |
| `no` | Non | No |  |

## safetyClassScheme

**Référentiel de classement** / Classification scheme — confiance **P**

Le schéma de classement diffère selon le palier et le pays : on trace le schéma utilisé plutôt que d'imposer une table unique.

Utilisée par : `equipmentRequirement.safetyClassScheme`, `function.safetyClassScheme`, `hardwareRequirement.safetyClassScheme`, `physicalComponent.safetyClassScheme`, `safetyRequirement.safetyClassScheme`, `softwareRequirement.safetyClassScheme`, `stakeholderRequirement.safetyClassScheme`, `systemRequirement.safetyClassScheme`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `frLegacy` | Parc REP France (IPS / EIP, classes M/E, K1-K3) | French PWR fleet (IPS / EIP, M/E classes, K1-K3) |  |
| `eprFr` | EPR France – classement FA3 (F1A/F1B/F2) | EPR France – FA3 classification (F1A/F1B/F2) |  |
| `eprUk` | UK EPR (catégorisation ONR) | UK EPR (ONR categorisation) |  |
| `epr2` | EPR2 (référentiel projet) | EPR2 (project scheme) |  |
| `iaeaSsg30` | AIEA SSG-30 (NUWARD / export) | IAEA SSG-30 (NUWARD / export) |  |
| `iec61226` | IEC 61226 (fonctions C-C, cat. A/B/C) | IEC 61226 (I&C functions, cat. A/B/C) |  |
| `usNrc` | US NRC (safety-related / 1E) | US NRC (safety-related / 1E) |  |
| `deKta` | Allemagne – KTA | Germany – KTA |  |
| `caCnsc` | Canada – CNSC / CSA N290.14 | Canada – CNSC / CSA |  |
| `other` | Autre (préciser dans la justification) | Other (see rationale) |  |

## functionCategory

**Catégorie de fonction** / Function category — confiance **P**

Utilisée par : `equipmentRequirement.functionCategory`, `function.functionCategory`, `hardwareRequirement.functionCategory`, `logicalComponent.functionCategory`, `safetyRequirement.functionCategory`, `softwareRequirement.functionCategory`, `stakeholderRequirement.functionCategory`, `systemRequirement.functionCategory`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `f1a` | F1A (EPR – atteinte de l'état contrôlé) | F1A (EPR – reach controlled state) |  |
| `f1b` | F1B (EPR – atteinte de l'état sûr) | F1B (EPR – reach safe state) |  |
| `f2` | F2 (EPR – autres fonctions de sûreté) | F2 (EPR – other safety functions) |  |
| `iaeaCat1` | Catégorie 1 (EPR2 / AIEA SSG-30) | Category 1 (EPR2 / IAEA SSG-30) |  |
| `iaeaCat2` | Catégorie 2 (EPR2 / AIEA SSG-30) | Category 2 (EPR2 / IAEA SSG-30) |  |
| `iaeaCat3` | Catégorie 3 (EPR2 / AIEA SSG-30) | Category 3 (EPR2 / IAEA SSG-30) |  |
| `iecCatA` | Catégorie A (IEC 61226) | Category A (IEC 61226) |  |
| `iecCatB` | Catégorie B (IEC 61226) | Category B (IEC 61226) |  |
| `iecCatC` | Catégorie C (IEC 61226) | Category C (IEC 61226) |  |
| `nc` | Non catégorisée | Not categorised | ✔ |

## safetyClass

**Classe de sûreté (SSC)** / Safety class (SSC) — confiance **P**

Utilisée par : `equipmentRequirement.safetyClass`, `hardwareRequirement.safetyClass`, `physicalComponent.safetyClass`, `safetyRequirement.safetyClass`, `softwareRequirement.safetyClass`, `stakeholderRequirement.safetyClass`, `systemRequirement.safetyClass`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `sc1` | S1 / classe de sûreté 1 (EPR2, SSG-30) | S1 / safety class 1 (EPR2, SSG-30) |  |
| `sc2` | S2 / classe de sûreté 2 | S2 / safety class 2 |  |
| `sc3` | S3 / classe de sûreté 3 | S3 / safety class 3 |  |
| `ncReq` | Non classé avec exigences (IPS-NC) | Non-classified with requirements |  |
| `nc` | Non classé | Non-classified | ✔ |

## mechanicalClass

**Classe mécanique (code)** / Mechanical class (code) — confiance **C**

Classe de construction RCC-M / ASME III.

Utilisée par : `physicalComponent.mechanicalClass`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `m1` | Classe 1 (RCC-M / ASME III NB) | Class 1 (RCC-M / ASME III NB) |  |
| `m2` | Classe 2 (RCC-M / ASME III NC) | Class 2 (RCC-M / ASME III NC) |  |
| `m3` | Classe 3 (RCC-M / ASME III ND) | Class 3 (RCC-M / ASME III ND) |  |
| `ncCode` | Non classé – code conventionnel | Non-classified – conventional code |  |
| `na` | Non applicable | Not applicable | ✔ |

## electricalClass

**Classe électrique** / Electrical class — confiance **P**

EPR (source IRSN) : classes électriques EE1/EE2 et classes C-C E1A/E1B/E2 ; US : Class 1E (IEEE 308). Désignations du parc et d'EPR2 à confirmer (cf. plan de recherche).

Utilisée par : `physicalComponent.electricalClass`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `ee1` | EE1 (EPR – électrique) | EE1 (EPR – electrical) |  |
| `ee2` | EE2 (EPR – électrique) | EE2 (EPR – electrical) |  |
| `e1a` | E1A (EPR – contrôle-commande) | E1A (EPR – I&C) |  |
| `e1b` | E1B (EPR – contrôle-commande) | E1B (EPR – I&C) |  |
| `e2` | E2 (EPR – contrôle-commande) | E2 (EPR – I&C) |  |
| `c1e` | Class 1E (US / IEEE) | Class 1E (US / IEEE) |  |
| `nc` | Non classé | Non-classified |  |
| `na` | Non applicable | Not applicable | ✔ |

## qualificationClass

**Classe de qualification (conditions)** / Qualification class (conditions) — confiance **P**

Pratique française : K1 (bâtiment réacteur, conditions normales + accidentelles + post-accidentelles + séisme), K2 (conditions normales avec irradiation + séisme), K3 (conditions normales + séisme, hors BR). 'AG' : K1 renforcé accident grave (EPR).

Utilisée par : `physicalComponent.qualificationClass`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `k1` | K1 | K1 |  |
| `k2` | K2 | K2 |  |
| `k3` | K3 | K3 |  |
| `sa` | AG – K1 renforcé accident grave (EPR) | SA – severe-accident qualified (EPR) |  |
| `harshUs` | Harsh environment (IEEE 323) | Harsh environment (IEEE 323) |  |
| `nq` | Non qualifié | Not qualified |  |
| `na` | Non applicable | Not applicable | ✔ |

## seismicCategory

**Catégorie sismique** / Seismic category — confiance **P**

Utilisée par : `physicalComponent.seismicCategory`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `seis1` | SC1 – fonctionne pendant / après le séisme | SC1 – functional during / after earthquake |  |
| `seis2` | SC2 – non-agression des matériels SC1 | SC2 – no interaction with SC1 items |  |
| `usCatI` | Seismic Category I (US) | Seismic Category I (US) |  |
| `usCatII` | Seismic Category II (US) | Seismic Category II (US) |  |
| `nonSeismic` | Non classé sismique | Non-seismic |  |
| `na` | Non applicable | Not applicable | ✔ |

## seismicCriterion

**Exigence sismique** / Seismic requirement

Utilisée par : `physicalComponent.seismicCriterion`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `operability` | Fonctionnalité / opérabilité | Operability / functionality |  |
| `integrity` | Intégrité / étanchéité | Integrity / leak-tightness |  |
| `stability` | Stabilité (non-agression) | Stability (no interaction) |  |
| `none` | Aucune | None | ✔ |

## espnLevel

**Niveau ESPN** / Nuclear pressure equipment level (ESPN) — confiance **C**

Arrêté du 30 décembre 2015 relatif aux équipements sous pression nucléaires : niveaux N1, N2, N3.

Utilisée par : `physicalComponent.espnLevel`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `n1` | N1 | N1 |  |
| `n2` | N2 | N2 |  |
| `n3` | N3 | N3 |  |
| `notEspn` | Non ESPN | Not ESPN |  |
| `tbd` | À déterminer | To be determined | ✔ |

## espnCategory

**Catégorie ESP / ESPN** / Pressure equipment category — confiance **P**

Utilisée par : `physicalComponent.espnCategory`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `cat0` | Catégorie 0 | Category 0 |  |
| `catI` | Catégorie I | Category I |  |
| `catII` | Catégorie II | Category II |  |
| `catIII` | Catégorie III | Category III |  |
| `catIV` | Catégorie IV | Category IV |  |
| `na` | Non applicable | Not applicable | ✔ |

## icSystemClass

**Classe de système C-C (IEC 61513)** / I&C system class (IEC 61513) — confiance **C**

Utilisée par : `logicalComponent.icSystemClass`, `physicalComponent.icSystemClass`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `class1` | Classe 1 | Class 1 |  |
| `class2` | Classe 2 | Class 2 |  |
| `class3` | Classe 3 | Class 3 |  |
| `nc` | Non classé | Not classified |  |
| `na` | Non applicable | Not applicable | ✔ |

## securityDegree

**Degré de sécurité (IEC 62645)** / Security degree (IEC 62645) — confiance **P**

Utilisée par : `function.securityDegree`, `physicalComponent.securityDegree`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `s1` | S1 (le plus exigeant) | S1 (most stringent) |  |
| `s2` | S2 | S2 |  |
| `s3` | S3 | S3 |  |
| `na` | Non applicable | Not applicable | ✔ |

## qaProgramLevel

**Programme qualité applicable** / Applicable QA programme

Utilisée par : `physicalComponent.qaProgramLevel`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `iso19443Itns` | ISO 19443 – ITNS (important pour la sûreté) | ISO 19443 – ITNS |  |
| `nqa1AppB` | NQA-1 / 10 CFR 50 App. B (safety-related) | NQA-1 / 10 CFR 50 App. B (safety-related) |  |
| `augmented` | Qualité renforcée (augmented quality) | Augmented quality |  |
| `commercialGrade` | Commercial grade + dédicace (CGD) | Commercial grade dedication |  |
| `iso9001` | ISO 9001 standard | ISO 9001 standard | ✔ |

## protectedInterest

**Intérêt protégé** / Protected interest — confiance **P**

Intérêts mentionnés à l'article L.593-1 du Code de l'environnement, déclinés opérationnellement.

Utilisée par : `equipmentRequirement.protectedInterests`, `function.protectedInterests`, `hardwareRequirement.protectedInterests`, `physicalComponent.protectedInterests`, `safetyRequirement.protectedInterests`, `softwareRequirement.protectedInterests`, `stakeholderRequirement.protectedInterests`, `systemRequirement.protectedInterests`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `nuclearSafety` | Sûreté nucléaire (prévention / limitation des accidents) | Nuclear safety |  |
| `radiationProtection` | Radioprotection | Radiation protection |  |
| `environmentNuisances` | Inconvénients / environnement (rejets, déchets) | Nuisances / environment |  |
| `nonRadiologicalRisks` | Risques non radiologiques | Non-radiological risks |  |

## fundamentalSafetyFunction

**Fonction fondamentale de sûreté** / Fundamental safety function — confiance **C**

AIEA SSR-2/1 : maîtrise de la réactivité, évacuation de la chaleur, confinement des matières radioactives.

Utilisée par : `function.fundamentalSafetyFunction`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `reactivity` | Maîtrise de la réactivité | Control of reactivity |  |
| `heatRemoval` | Évacuation de la puissance (refroidissement) | Heat removal |  |
| `confinement` | Confinement des matières radioactives | Confinement of radioactive material |  |
| `none` | Aucune (fonction support / exploitation) | None (support / operational) | ✔ |

## plantState

**État / domaine d'exploitation** / Plant operating state — confiance **P**

Terminologie REP France ; équivalents génériques entre parenthèses. À aligner avec le référentiel client.

Utilisée par : `equipmentRequirement.plantStates`, `function.plantStates`, `hardwareRequirement.plantStates`, `hazard.plantStates`, `operationalScenario.plantStates`, `safetyRequirement.plantStates`, `softwareRequirement.plantStates`, `stakeholderRequirement.plantStates`, `systemRequirement.plantStates`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `rp` | RP – Réacteur en production (puissance) | Power operation |  |
| `angv` | AN/GV – Arrêt normal sur GV (arrêt à chaud) | Hot shutdown on SGs |  |
| `anrra` | AN/RRA – Arrêt normal sur RRA | Shutdown on RHR |  |
| `api` | API – Arrêt pour intervention (circuit fermé/ouvert) | Maintenance cold shutdown |  |
| `apr` | APR – Arrêt pour rechargement | Refuelling shutdown |  |
| `rcd` | RCD – Réacteur cœur déchargé | Core fully offloaded |  |
| `allStates` | Tous états | All states |  |

## plantCondition

**Condition de fonctionnement** / Plant condition — confiance **P**

Correspondances : PCC (parc), DBC/RRC (EPR), NO/AOO/DBA/DEC (AIEA).

Utilisée par : `equipmentRequirement.plantConditions`, `function.plantConditions`, `hardwareRequirement.plantConditions`, `hazard.plantConditions`, `safetyRequirement.plantConditions`, `softwareRequirement.plantConditions`, `stakeholderRequirement.plantConditions`, `systemRequirement.plantConditions`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `cond1` | PCC-1 / DBC-1 – Fonctionnement normal | Normal operation (PCC-1 / DBC-1) |  |
| `cond2` | PCC-2 / DBC-2 – Incidents (transitoires fréquents) | Anticipated operational occurrences (PCC-2 / DBC-2) |  |
| `cond3` | PCC-3 / DBC-3 – Accidents peu fréquents | Infrequent accidents (PCC-3 / DBC-3) |  |
| `cond4` | PCC-4 / DBC-4 – Accidents hypothétiques | Limiting accidents (PCC-4 / DBC-4) |  |
| `decA` | RRC-A / DEC-A – Conditions additionnelles sans fusion | Design extension without core melt (DEC-A) |  |
| `decB` | RRC-B / DEC-B – Accident grave (fusion du cœur) | Design extension with core melt (DEC-B) |  |
| `hazardCondition` | Situation d'agression | Hazard condition |  |

## defenceInDepthLevel

**Niveau de défense en profondeur** / Defence-in-depth level — confiance **C**

Utilisée par : `function.defenceInDepthLevel`, `safetyRequirement.defenceInDepthLevel`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `did1` | Niveau 1 – Prévention des anomalies | Level 1 – Prevention of abnormal operation |  |
| `did2` | Niveau 2 – Maîtrise des anomalies / incidents | Level 2 – Control of abnormal operation |  |
| `did3` | Niveau 3 – Maîtrise des accidents | Level 3 – Control of accidents |  |
| `did4` | Niveau 4 – Maîtrise des accidents graves | Level 4 – Control of severe conditions |  |
| `did5` | Niveau 5 – Limitation des conséquences radiologiques | Level 5 – Mitigation of radiological consequences |  |
| `na` | Non applicable | Not applicable | ✔ |

## safetyRequirementSource

**Origine de l'exigence de sûreté** / Safety requirement origin

Utilisée par : `safetyRequirement.safetyRequirementSource`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `deterministicAnalysis` | Études d'accidents déterministes | Deterministic accident analysis |  |
| `psa` | Études probabilistes (EPS) | Probabilistic safety assessment |  |
| `hazardAnalysis` | Analyse des agressions | Hazard analysis |  |
| `classificationRule` | Règle de classement / exigence associée | Classification rule |  |
| `defenceInDepth` | Défense en profondeur / indépendance des niveaux | Defence in depth |  |
| `regulation` | Réglementation / guide | Regulation / guide |  |
| `operatingExperience` | REX / événements | Operating experience |  |
| `severeAccident` | Études d'accident grave | Severe accident studies |  |

## informationClassification

**Classification de l'information** / Information classification

Les informations 'Diffusion Restreinte' et 'sensibles sécurité nucléaire' sont INTERDITES sur l'instance standard (contrôle par condition de workflow + audit).

Utilisée par : `action.informationClassification`, `analysis.informationClassification`, `anomaly.informationClassification`, `assumption.informationClassification`, `changeRequest.informationClassification`, `deliverable.informationClassification`, `designDecision.informationClassification`, `designParameter.informationClassification`, `equipmentRequirement.informationClassification`, `fmeaItem.informationClassification`, `function.informationClassification`, `hardwareRequirement.informationClassification` …

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `public` | Public | Public |  |
| `internal` | Usage interne | Internal | ✔ |
| `confidential` | Confidentiel (besoin d'en connaître) | Confidential (need to know) |  |
| `customerConfidential` | Confidentiel client / partenaire | Customer / partner confidential |  |
| `sensitiveSecurity` | Sensible sécurité nucléaire – interdit instance standard | Nuclear security sensitive – forbidden on standard instance |  |
| `restricted` | Diffusion Restreinte – interdit instance standard | Restricted (DR) – forbidden on standard instance |  |

## exportControl

**Contrôle export** / Export control

Résultat du screening export (biens/technologies à double usage UE cat. 0, réglementations US). Détermine les droits d'accès cross-entités.

Utilisée par : `action.exportControl`, `analysis.exportControl`, `anomaly.exportControl`, `assumption.exportControl`, `changeRequest.exportControl`, `deliverable.exportControl`, `designDecision.exportControl`, `designParameter.exportControl`, `equipmentRequirement.exportControl`, `fmeaItem.exportControl`, `function.exportControl`, `hardwareRequirement.exportControl` …

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `toBeScreened` | À évaluer | To be screened |  |
| `notControlled` | Non contrôlé | Not controlled | ✔ |
| `euDualUse` | UE double usage (Règl. 2021/821, cat. 0) | EU dual-use (Reg. 2021/821, cat. 0) |  |
| `frNational` | Contrôle national français | French national control |  |
| `us810` | US 10 CFR 810 (assistance technique) | US 10 CFR 810 (technical assistance) |  |
| `us110` | US 10 CFR 110 (équipements/matières) | US 10 CFR 110 (equipment/material) |  |
| `usEar` | US EAR | US EAR |  |
| `deAwg` | Allemagne AWG/AWV | Germany AWG/AWV |  |
| `frPpst` | France PPST / ZRR (accès restreint) | France PPST / restricted zone |  |

## functionLevel

**Niveau de fonction** / Function level

Utilisée par : `function.functionLevel`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `plant` | Installation (fonction de tranche) | Plant |  |
| `system` | Système | System |  |
| `subsystem` | Sous-système | Subsystem |  |
| `equipment` | Équipement | Equipment |  |
| `software` | Fonction logicielle / applicative | Software / application function |  |

## functionType

**Type de fonction** / Function type

Utilisée par : `function.functionType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `operational` | Fonction d'exploitation | Operational |  |
| `safety` | Fonction de sûreté | Safety |  |
| `protection` | Protection (arrêt automatique, sauvegarde) | Protection (trip, ESF actuation) |  |
| `control` | Régulation / pilotage | Control |  |
| `monitoring` | Surveillance / mesure | Monitoring |  |
| `hmi` | IHM / conduite | HMI / operation |  |
| `support` | Support (alimentations, refroidissement, ventilation) | Support |  |
| `maintenance` | Maintenance / intervention | Maintenance / intervention |  |
| `handling` | Manutention / logistique | Handling / logistics |  |
| `toolFunction` | Fonction outillage (FAST / APTE) | Tooling function |  |

## logicalType

**Type d'élément logique** / Logical element type

Utilisée par : `logicalComponent.logicalType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `elementarySystem` | Système élémentaire | Elementary system |  |
| `subsystem` | Sous-système / train / division | Subsystem / train / division |  |
| `icSystem` | Système C-C | I&C system |  |
| `softwareLogical` | Composant logiciel logique | Logical software component |  |
| `humanAction` | Action humaine / organisation | Human action / organisation |  |
| `toolModule` | Module d'outillage | Tooling module |  |
| `externalSystem` | Système externe (hors fourniture) | External system (out of scope) |  |

## componentNature

**Nature de l'élément physique** / Physical element nature

Utilisée par : `physicalComponent.componentNature`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `site` | Site / installation | Site / installation |  |
| `building` | Bâtiment | Building |  |
| `room` | Local / zone | Room / area |  |
| `system` | Système physique | Physical system |  |
| `equipment` | Équipement / matériel | Equipment |  |
| `component` | Composant / pièce | Component / part |  |
| `pipingLine` | Ligne de tuyauterie | Piping line |  |
| `structure` | Structure / support | Structure / support |  |
| `instrument` | Capteur / instrument | Sensor / instrument |  |
| `cabinet` | Armoire / châssis électronique | Cabinet / rack |  |
| `softwareItem` | Article logiciel | Software item |  |
| `hdlDevice` | Composant HDL / FPGA | HDL device / FPGA |  |
| `fuelAssembly` | Assemblage combustible / crayon | Fuel assembly / rod |  |
| `tool` | Outillage / machine | Tool / machine |  |
| `consumable` | Consommable / produit | Consumable / product |  |
| `simulatorAsset` | Simulateur / modèle de simulation | Simulator / simulation model |  |
| `irradiationTarget` | Cible d'irradiation / capsule | Irradiation target / capsule |  |

## pbsLevel

**Niveau PBS** / PBS level

Utilisée par : `physicalComponent.pbsLevel`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `l0` | N0 – Site / installation | L0 – Site / installation |  |
| `l1` | N1 – Tranche / unité | L1 – Unit |  |
| `l2` | N2 – Bâtiment / îlot | L2 – Building / island |  |
| `l3` | N3 – Système | L3 – System |  |
| `l4` | N4 – Équipement | L4 – Equipment |  |
| `l5` | N5 – Sous-ensemble | L5 – Sub-assembly |  |
| `l6` | N6 – Pièce / article | L6 – Part / item |  |

## qualificationStatus

**Statut de qualification** / Qualification status

Utilisée par : `physicalComponent.qualificationStatus`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `notRequired` | Non requise | Not required |  |
| `notStarted` | Non démarrée | Not started | ✔ |
| `inProgress` | En cours | In progress |  |
| `qualified` | Qualifié | Qualified |  |
| `qualifiedWithReserves` | Qualifié avec réserves | Qualified with reserves |  |
| `expired` | Échue / à renouveler | Expired / to renew |  |

## ageingMechanism

**Mécanisme de vieillissement** / Ageing mechanism

Utilisée par : `analysis.ageingMechanisms`, `physicalComponent.ageingMechanisms`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `fatigue` | Fatigue (thermique, mécanique) | Fatigue |  |
| `irradiationEmbrittlement` | Fragilisation sous irradiation | Irradiation embrittlement |  |
| `thermalAgeing` | Vieillissement thermique | Thermal ageing |  |
| `scc` | Corrosion sous contrainte | Stress corrosion cracking |  |
| `generalCorrosion` | Corrosion généralisée / FAC | General corrosion / FAC |  |
| `wear` | Usure / fretting | Wear / fretting |  |
| `polymerAgeing` | Vieillissement des polymères / câbles | Polymer / cable ageing |  |
| `obsolescence` | Obsolescence technologique | Technological obsolescence |  |
| `concreteAgeing` | Vieillissement des bétons | Concrete ageing |  |

## interfaceType

**Type d'interface** / Interface type

Utilisée par : `interface.interfaceType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `mechanical` | Mécanique (liaison, efforts) | Mechanical (connection, loads) |  |
| `fluid` | Fluide / procédé | Fluid / process |  |
| `electricalPower` | Électrique (puissance) | Electrical power |  |
| `icSignal` | Signal C-C / données | I&C signal / data |  |
| `civil` | Génie civil (ancrages, traversées, charges) | Civil (anchors, penetrations, loads) |  |
| `hvac` | Ventilation / thermique d'ambiance | HVAC / ambient thermal |  |
| `layout` | Implantation / encombrement | Layout / space |  |
| `radiological` | Radiologique (débit de dose, zonage) | Radiological (dose rate, zoning) |  |
| `software` | Logiciel / échange de données | Software / data exchange |  |
| `humanMachine` | Homme-machine | Human-machine |  |
| `handling` | Manutention / logistique | Handling / logistics |  |
| `organisational` | Organisationnelle / contractuelle | Organisational / contractual |  |

## interfaceScope

**Portée de l'interface** / Interface scope

Utilisée par : `interface.interfaceScope`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `internal` | Interne au projet | Internal to project |  |
| `interBu` | Inter-BU / inter-projets Framatome | Inter-BU / inter-project |  |
| `customer` | Client / architecte-ensemblier | Customer / architect-engineer |  |
| `partnerOem` | Autre constructeur (îlot conventionnel, GC...) | Partner OEM |  |
| `supplier` | Fournisseur | Supplier |  |
| `plantExisting` | Installation existante (base installée) | Existing plant |  |

## scenarioType

**Type de scénario** / Scenario type

Utilisée par : `operationalScenario.scenarioType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `normalOperation` | Exploitation normale | Normal operation |  |
| `transient` | Transitoire / incident | Transient / incident |  |
| `accident` | Accident | Accident |  |
| `maintenance` | Maintenance | Maintenance |  |
| `refuelling` | Rechargement | Refuelling |  |
| `intervention` | Séquence d'intervention (outillage, RGV) | Intervention sequence (tooling, SGR) |  |
| `commissioning` | Mise en service | Commissioning |  |
| `transport` | Transport / manutention | Transport / handling |  |
| `decommissioning` | Démantèlement | Decommissioning |  |

## designParameterType

**Type de paramètre** / Parameter type

Utilisée par : `designParameter.designParameterType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `performance` | Performance (TPM) | Performance (TPM) |  |
| `safetyLimit` | Limite / critère de sûreté | Safety limit / criterion |  |
| `operatingLimit` | Limite d'exploitation (STE) | Operating limit (tech specs) |  |
| `setpoint` | Seuil / point de consigne de protection | Protection setpoint |  |
| `designMargin` | Marge de conception | Design margin |  |
| `budget` | Budget (masse, puissance, charge thermique, dose) | Budget (mass, power, heat load, dose) |  |
| `coreParameter` | Paramètre de cœur (recharge) | Core parameter (reload) |  |
| `siteData` | Donnée de site | Site data |  |
| `processWindow` | Fenêtre de paramètre de procédé | Process parameter window |  |

## hazardType

**Type d'agression / événement** / Hazard / event type

Utilisée par : `hazard.hazardType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `initiatingEvent` | Événement initiateur interne (transitoire, brèche...) | Postulated initiating event |  |
| `intFire` | Agression interne – incendie | Internal hazard – fire |  |
| `intFlooding` | Agression interne – inondation | Internal hazard – flooding |  |
| `intExplosion` | Agression interne – explosion | Internal hazard – explosion |  |
| `intMissile` | Agression interne – projectiles | Internal hazard – missiles |  |
| `pipeBreak` | Rupture de tuyauterie HE (fouettement, jet) | High-energy line break |  |
| `loadDrop` | Chute de charge | Heavy load drop |  |
| `emi` | Interférences électromagnétiques | Electromagnetic interference |  |
| `earthquake` | Agression externe – séisme | External hazard – earthquake |  |
| `extFlooding` | Agression externe – inondation externe | External hazard – flooding |  |
| `extremeWeather` | Agression externe – conditions climatiques extrêmes | External hazard – extreme weather |  |
| `aircraftCrash` | Agression externe – chute d'avion | External hazard – aircraft crash |  |
| `industrialHazard` | Agression externe – risques industriels / explosion | External hazard – industrial / explosion |  |
| `biological` | Agression externe – colmatage / biologique | External hazard – biological / clogging |  |
| `radiological` | Risque radiologique (exposition, contamination) | Radiological risk |  |
| `machinery` | Risque machine / intervention (EN ISO 12100) | Machinery / intervention risk |  |
| `industrialSafety` | Sécurité classique (chute, levage, chimique) | Industrial safety |  |
| `cyberThreat` | Menace / vulnérabilité cyber | Cyber threat / vulnerability |  |
| `criticality` | Risque de criticité | Criticality risk |  |

## initiatingEventFrequency

**Bande de fréquence (indicative)** / Frequency band (indicative) — confiance **H**

Bandes indicatives ; les bornes réelles dépendent du référentiel du palier/projet.

Utilisée par : `hazard.frequencyBand`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `f1` | > 1E-2 /an | > 1E-2 /yr |  |
| `f2` | 1E-4 à 1E-2 /an | 1E-4 to 1E-2 /yr |  |
| `f3` | 1E-6 à 1E-4 /an | 1E-6 to 1E-4 /yr |  |
| `f4` | < 1E-6 /an (résiduel) | < 1E-6 /yr (residual) |  |
| `na` | Non applicable | Not applicable | ✔ |

## hazardScreening

**Décision de criblage** / Screening decision

Utilisée par : `hazard.screening`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `retained` | Retenu | Retained | ✔ |
| `bounded` | Enveloppé par un autre cas | Bounded by another case |  |
| `excludedFrequency` | Exclu (fréquence) | Screened out (frequency) |  |
| `excludedConsequence` | Exclu (conséquences) | Screened out (consequence) |  |
| `practicallyEliminated` | Pratiquement éliminé (justifié) | Practically eliminated (justified) |  |

## gsnElementType

**Élément d'argumentaire (GSN/CAE)** / Argument element (GSN/CAE)

Utilisée par : `safetyClaim.gsnElementType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `goal` | Revendication / objectif (claim) | Goal / claim | ✔ |
| `strategy` | Stratégie / argument | Strategy / argument |  |
| `context` | Contexte | Context |  |
| `justification` | Justification | Justification |  |

## confidenceLevel

**Niveau de confiance** / Confidence level

Utilisée par : `safetyClaim.confidence`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `low` | Faible | Low |  |
| `medium` | Moyen | Medium | ✔ |
| `high` | Élevé | High |  |

## riskCategory

**Catégorie de risque** / Risk category

Utilisée par : `risk.riskCategory`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `technical` | Technique | Technical |  |
| `licensing` | Sûreté / licensing | Safety / licensing |  |
| `schedule` | Planning | Schedule |  |
| `cost` | Coût | Cost |  |
| `supplyChain` | Chaîne d'approvisionnement | Supply chain |  |
| `contractual` | Contractuel | Contractual |  |
| `interface` | Interface | Interface |  |
| `quality` | Qualité / CFSI | Quality / CFSI |  |
| `cyber` | Cybersécurité | Cybersecurity |  |
| `skills` | Compétences / ressources | Skills / resources |  |
| `industrial` | Industriel (fabrication, site) | Industrial (manufacturing, site) |  |
| `radiological` | Radiologique (dosimétrie intervention) | Radiological (intervention dose) |  |

## riskLevel

**Niveau de risque** / Risk level

Utilisée par : `risk.riskLevel`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `low` | Faible | Low |  |
| `medium` | Moyen | Medium |  |
| `high` | Élevé | High |  |
| `critical` | Critique | Critical |  |

## riskStrategy

**Stratégie de traitement** / Treatment strategy

Utilisée par : `risk.riskStrategy`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `avoid` | Éviter | Avoid |  |
| `reduce` | Réduire | Reduce | ✔ |
| `transfer` | Transférer | Transfer |  |
| `accept` | Accepter | Accept |  |
| `exploit` | Exploiter (opportunité) | Exploit (opportunity) |  |

## fmeaType

**Type d'AMDEC** / FMEA type

Utilisée par : `fmeaItem.fmeaType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `functional` | AMDE(C) fonctionnelle | Functional FMEA |  |
| `design` | AMDEC produit / conception | Design FMEA |  |
| `process` | AMDEC procédé (fabrication) | Process FMEA |  |
| `intervention` | AMDEC intervention / outillage | Intervention / tooling FMEA |  |
| `software` | AMDE logicielle | Software FMEA |  |

## actionPriority

**Priorité d'action (AMDEC)** / Action priority (FMEA)

Utilisée par : `fmeaItem.actionPriority`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `high` | Haute | High |  |
| `medium` | Moyenne | Medium |  |
| `low` | Basse | Low |  |

## analysisType

**Type d'analyse** / Analysis type

Utilisée par : `analysis.analysisType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `deterministicSafety` | Études d'accidents (déterministe) | Deterministic accident analysis |  |
| `psa` | EPS niveau 1 / 2 | PSA level 1 / 2 |  |
| `hazardAnalysis` | Analyse des agressions | Hazard analysis |  |
| `mechanicalStress` | Analyse mécanique (RCC-M / ASME) | Stress analysis (RCC-M / ASME) |  |
| `fatigue` | Fatigue | Fatigue |  |
| `fractureMechanics` | Mécanique de la rupture / nocivité de défaut | Fracture mechanics / flaw evaluation |  |
| `seismic` | Analyse sismique | Seismic analysis |  |
| `thermalHydraulic` | Thermohydraulique | Thermal-hydraulics |  |
| `neutronic` | Neutronique / études de cœur | Neutronics / core design |  |
| `fuelThermomechanical` | Thermomécanique combustible | Fuel thermo-mechanics |  |
| `radiological` | Radiologique / protections biologiques | Radiological / shielding |  |
| `doseAlara` | Dosimétrie prévisionnelle (ALARA) | Dose estimate (ALARA) |  |
| `humanFactors` | Analyse FOH (tâches, IHM) | Human factors analysis |  |
| `fmea` | AMDEC | FMEA |  |
| `fta` | Arbre de défaillances | Fault tree |  |
| `ccfDiversity` | MCC / diversité (D3) | CCF / diversity (D3) |  |
| `cyberRisk` | Analyse de risques cyber | Cyber risk assessment |  |
| `reliability` | Fiabilité / disponibilité | Reliability / availability |  |
| `machineryRisk` | Analyse de risques machine (EN ISO 12100) | Machinery risk assessment (EN ISO 12100) |  |
| `structural` | Génie civil / structures | Structural |  |
| `electricalStudy` | Études électriques (bilans, sélectivité) | Electrical studies |  |
| `hvacStudy` | Bilans thermiques / ventilation | HVAC / heat load |  |
| `chemistry` | Chimie / matériaux | Chemistry / materials |  |
| `wasteEnvironment` | Déchets / rejets / impact | Waste / discharges / impact |  |
| `ageingLto` | Vieillissement / aptitude à la poursuite de fonctionnement | Ageing / LTO |  |
| `tradeOff` | Analyse multicritère / trade-off | Trade-off study |  |
| `criticality` | Études de criticité | Criticality analysis |  |
| `codeValidation` | Validation de code de calcul (matrice expérimentale) | Calculation code validation |  |
| `equivalence` | Évaluation d'équivalence / dédicace commerciale (CGD) | Equivalency evaluation / commercial grade dedication |  |

## codeQualification

**Statut du code de calcul** / Calculation code status

Utilisée par : `analysis.codeQualification`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `qualified` | Qualifié pour le domaine d'application | Qualified for application domain |  |
| `validated` | Validé (interne) | Validated (internal) |  |
| `commercial` | Outil commercial standard | Standard commercial tool |  |
| `notQualified` | Non qualifié (justification requise) | Not qualified (justification required) |  |
| `na` | Non applicable | Not applicable | ✔ |

## analysisResult

**Conclusion d'analyse** / Analysis conclusion

Utilisée par : `analysis.analysisResult`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `inProgress` | En cours | In progress | ✔ |
| `compliant` | Critères respectés | Criteria met |  |
| `compliantWithReserves` | Respectés avec réserves | Met with reserves |  |
| `nonCompliant` | Critères non respectés | Criteria not met |  |

## commitmentSource

**Origine de l'engagement** / Commitment origin

Utilisée par : `regulatoryCommitment.commitmentSource`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `regulatorDecision` | Décision / prescription de l'autorité | Regulator decision / prescription |  |
| `inspectionLetter` | Lettre de suite d'inspection | Inspection follow-up letter |  |
| `positionLetter` | Courrier de position / instruction | Position letter / review |  |
| `licensingSubmission` | Engagement pris dans un dossier | Commitment in a submittal |  |
| `customerRequest` | Demande client | Customer request |  |
| `internationalReview` | Revue internationale (AIEA, WANO...) | International review |  |
| `internalAudit` | Audit interne | Internal audit |  |

## requestCategory

**Nature de la demande** / Request category

Utilisée par : `regulatoryCommitment.requestCategory`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `prescription` | Prescription (opposable) | Prescription (binding) |  |
| `correctiveAction` | Demande d'action corrective | Corrective action request |  |
| `informationRequest` | Demande de complément d'information | Information request |  |
| `observation` | Observation | Observation |  |
| `voluntaryCommitment` | Engagement volontaire | Voluntary commitment |  |

## authority

**Autorité / organisme** / Authority / body

Utilisée par : `regulatoryCommitment.authority`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `asnr` | ASNR (France) | ASNR (France) |  |
| `dgprNotified` | Organisme agréé / habilité ESPN | ESPN approved body |  |
| `onr` | ONR (Royaume-Uni) | ONR (UK) |  |
| `nrc` | NRC (États-Unis) | NRC (US) |  |
| `stuk` | STUK (Finlande) | STUK (Finland) |  |
| `sujb` | SÚJB (Rép. tchèque) | SÚJB (Czech Rep.) |  |
| `nnsa` | NNSA (Chine) | NNSA (China) |  |
| `germanAuthority` | Autorité allemande (Land / BASE) | German authority |  |
| `cnsc` | CCSN / CNSC (Canada) | CNSC (Canada) |  |
| `healthAuthority` | Autorité de santé (ANSM, FDA, Santé Canada – BPF) | Health authority (GMP) |  |
| `customer` | Client | Customer |  |
| `other` | Autre | Other |  |

## changeOrigin

**Origine de la modification** / Change origin

Utilisée par : `changeRequest.changeOrigin`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `customerRequest` | Demande client | Customer request |  |
| `nonConformance` | Suite à écart / FNC | Non-conformance |  |
| `regulatory` | Exigence / demande réglementaire | Regulatory |  |
| `operatingExperience` | REX | Operating experience |  |
| `designImprovement` | Amélioration de conception | Design improvement |  |
| `obsolescence` | Obsolescence | Obsolescence |  |
| `costReduction` | Réduction de coût / délai | Cost / schedule reduction |  |
| `supplier` | Demande fournisseur | Supplier request |  |
| `interface` | Évolution d'interface | Interface evolution |  |

## changeClass

**Classe de modification (GdC)** / Change class (CM)

ISO 10007 / EIA-649 : classe I (impact forme-ajustement-fonction, sûreté, contrat, référence approuvée) ; classe II (mineure) ; éditoriale.

Utilisée par : `changeRequest.changeClass`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `classI` | Classe I – majeure | Class I – major |  |
| `classII` | Classe II – mineure | Class II – minor |  |
| `editorial` | Éditoriale (sans impact technique) | Editorial |  |
| `tbd` | À classer | To be classified | ✔ |

## regulatoryModificationClass

**Classement réglementaire de la modification (INB)** / Regulatory modification class (INB) — confiance **P**

Code de l'environnement (L.593-14 substantielle, L.593-15 notable ; R.593-55 à R.593-60) et décision ASN 2017-DC-0616 modifiée (2023-DC-0770) : la qualification relève de l'exploitant ; Framatome documente les éléments d'appréciation.

Utilisée par : `changeRequest.regulatoryModificationClass`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `tbd` | À évaluer | To be assessed | ✔ |
| `nonNotable` | Non notable | Not notable |  |
| `notableDeclaration` | Notable – soumise à déclaration | Notable – declaration |  |
| `notableAuthorization` | Notable – soumise à autorisation | Notable – authorisation |  |
| `substantial` | Substantielle (nouvelle autorisation) | Substantial (new licence) |  |
| `notApplicable` | Non applicable (hors INB / export) | Not applicable |  |

## ccbDecision

**Décision CCB** / CCB decision

Utilisée par : `changeRequest.ccbDecision`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `pending` | En attente | Pending | ✔ |
| `approved` | Approuvée | Approved |  |
| `approvedWithConditions` | Approuvée sous conditions | Approved with conditions |  |
| `rejected` | Rejetée | Rejected |  |
| `deferred` | Reportée | Deferred |  |
| `moreInfo` | Complément demandé | More information required |  |

## ncOrigin

**Origine de l'écart** / Non-conformance origin

Utilisée par : `nonConformance.ncOrigin`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `design` | Conception | Design |  |
| `manufacturing` | Fabrication | Manufacturing |  |
| `supplier` | Fournisseur / sous-traitant | Supplier |  |
| `site` | Montage / intervention site | Site works |  |
| `operation` | Exploitation / maintenance | Operation / maintenance |  |
| `documentation` | Documentation | Documentation |  |
| `software` | Logiciel | Software |  |
| `test` | Essais | Testing |  |

## ncDetectionPhase

**Phase de détection** / Detection phase

Utilisée par : `nonConformance.ncDetectionPhase`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `designReview` | Revue de conception | Design review |  |
| `receiving` | Contrôle de réception | Receiving inspection |  |
| `manufacturing` | Contrôle en fabrication | In-process inspection |  |
| `fat` | Essais usine | FAT |  |
| `site` | Site / montage | Site / erection |  |
| `commissioning` | Mise en service | Commissioning |  |
| `inService` | En service (ISI, exploitation) | In service |  |
| `audit` | Audit / surveillance client | Audit / customer oversight |  |
| `inspection` | Inspection de l'autorité | Regulator inspection |  |

## ncSeverity

**Gravité de l'écart** / Non-conformance severity

Utilisée par : `nonConformance.ncSeverity`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `minor` | Mineure | Minor |  |
| `major` | Majeure | Major |  |
| `critical` | Critique | Critical |  |

## ncDisposition

**Traitement (disposition)** / Disposition

Utilisée par : `nonConformance.ncDisposition`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `pending` | En attente de décision | Pending | ✔ |
| `useAsIs` | Acceptation en l'état | Use as is |  |
| `repair` | Réparation | Repair |  |
| `rework` | Reprise / retouche | Rework |  |
| `reject` | Rebut | Scrap / reject |  |
| `returnToSupplier` | Retour fournisseur | Return to supplier |  |
| `regrade` | Déclassement / réaffectation | Regrade |  |
| `designChange` | Modification de la définition | Design change |  |

## significantEventType

**Événement significatif (exploitant)** / Significant event (licensee) — confiance **P**

Déclaration relevant de l'exploitant ; Framatome trace l'information utile.

Utilisée par : `nonConformance.significantEventType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `none` | Aucun | None | ✔ |
| `tbd` | À évaluer par l'exploitant | To be assessed by licensee |  |
| `ess` | ESS – significatif sûreté | Safety significant event |  |
| `esr` | ESR – significatif radioprotection | Radiation protection significant event |  |
| `ese` | ESE – significatif environnement | Environment significant event |  |
| `est` | EST – significatif transport | Transport significant event |  |

## rootCauseCategory

**Catégorie de cause racine** / Root cause category

Utilisée par : `anomaly.rootCauseCategory`, `nonConformance.rootCauseCategory`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `human` | Humaine | Human |  |
| `organisational` | Organisationnelle | Organisational |  |
| `designError` | Erreur de conception | Design error |  |
| `material` | Matière / matériau | Material |  |
| `method` | Méthode / procédure | Method / procedure |  |
| `environment` | Environnement / milieu | Environment |  |
| `supplier` | Fournisseur | Supplier |  |
| `cfsi` | Fraude / contrefaçon / suspect (CFSI) | CFSI (counterfeit, fraudulent, suspect) |  |
| `software` | Logiciel | Software |  |
| `undetermined` | Indéterminée | Undetermined |  |

## waiverType

**Type de dérogation** / Waiver type

Utilisée par : `waiver.waiverType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `deviationPermit` | Dérogation avant réalisation (deviation permit) | Deviation permit (before) |  |
| `concession` | Concession / acceptation après réalisation | Concession (after) |  |
| `requirementWaiver` | Dérogation à une exigence contractuelle | Contract requirement waiver |  |

## issueCategory

**Catégorie de problème** / Issue category

Utilisée par : `technicalIssue.issueCategory`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `fortuit` | Fortuit (aléa en arrêt de tranche) | Emergent outage issue |  |
| `inServiceFinding` | Indication / constat en service (ISI) | In-service finding |  |
| `genericIssue` | Problème générique (palier / flotte) | Generic issue (series / fleet) |  |
| `operatingExperience` | REX externe à analyser | External OE to assess |  |
| `customerQuery` | Demande technique client | Customer technical query |  |
| `designQuestion` | Question technique interne | Internal technical question |  |

## urgency

**Urgence** / Urgency

Utilisée par : `changeRequest.urgency`, `technicalIssue.urgency`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `immediate` | Immédiate (< 24 h) | Immediate (< 24 h) |  |
| `urgent` | Urgente (< 72 h / chemin critique) | Urgent (< 72 h / critical path) |  |
| `high` | Haute (< 2 semaines) | High (< 2 weeks) |  |
| `normal` | Normale | Normal | ✔ |

## outageType

**Type d'arrêt** / Outage type — confiance **P**

Utilisée par : `technicalIssue.outageType`, `unitDeployment.outageType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `asr` | ASR – Arrêt simple rechargement | Refuelling-only outage |  |
| `vp` | VP – Visite partielle | Partial inspection outage |  |
| `vd` | VD – Visite décennale | Ten-yearly outage |  |
| `forced` | Arrêt fortuit / non programmé | Forced outage |  |
| `inOperation` | Tranche en fonctionnement | Unit in operation |  |
| `na` | Non applicable | Not applicable | ✔ |

## solutionType

**Type de solution** / Solution type

Utilisée par : `technicalIssue.solutionType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `justifyAsIs` | Justification en l'état | Justify as is |  |
| `repair` | Réparation | Repair |  |
| `replace` | Remplacement | Replacement |  |
| `furtherInspection` | Investigation / contrôle complémentaire | Further inspection |  |
| `operatingRestriction` | Restriction / mesure compensatoire d'exploitation | Operating restriction / compensatory measure |  |
| `temporaryModification` | Modification temporaire | Temporary modification |  |
| `tbd` | À définir | To be defined | ✔ |

## anomalyType

**Type d'anomalie** / Anomaly type

Utilisée par : `anomaly.anomalyType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `software` | Logiciel | Software |  |
| `hardware` | Matériel | Hardware |  |
| `configuration` | Configuration / paramétrage | Configuration / parameters |  |
| `documentation` | Documentation | Documentation |  |
| `testSpec` | Spécification d'essai | Test specification |  |
| `testEnvironment` | Environnement d'essai | Test environment |  |

## deliverableType

**Type de livrable** / Deliverable type

Utilisée par : `deliverable.deliverableType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `specification` | Spécification (STB, ST, STE) | Specification |  |
| `designNote` | Note d'étude / de conception | Design note |  |
| `calculationNote` | Note de calcul | Calculation note |  |
| `drawing` | Plan / schéma | Drawing / diagram |  |
| `procedure` | Procédure / mode opératoire | Procedure |  |
| `testProcedure` | Procédure d'essais | Test procedure |  |
| `testReport` | PV / rapport d'essais | Test report |  |
| `justification` | Dossier / note de justification | Justification file |  |
| `safetyReport` | Chapitre de rapport de sûreté | Safety report chapter |  |
| `qualificationFile` | Dossier de qualification | Qualification file |  |
| `manufacturingFile` | Dossier de fabrication / de fin de fabrication | Manufacturing / end-of-manufacturing file |  |
| `espnFile` | Dossier ESPN (notice, dossier technique) | ESPN file |  |
| `manual` | Manuel (exploitation, maintenance) | Manual (operation, maintenance) |  |
| `list` | Liste (EIP, matériels, signaux...) | List (EIP, equipment, signals...) |  |
| `plan` | Plan de management (PQP, PMIS, PGC...) | Management plan |  |
| `certificate` | Certificat / attestation | Certificate |  |
| `softwareRelease` | Livraison logicielle | Software release |  |
| `model` | Modèle (3D, SysML/Capella, calcul) | Model (3D, SysML/Capella, calc) |  |
| `dataPackage` | Lot de données (ReqIF, tableur) | Data package (ReqIF, spreadsheet) |  |
| `licensingSubmittal` | Dossier réglementaire / rapport topique | Licensing submittal / topical report |  |
| `operatingDocument` | Document d'exploitation impacté (RGE, procédure, gamme) | Impacted operating document |  |
| `asBuiltFile` | Dossier tel que construit / réalisé | As-built file |  |

## customerVisa

**Visa client** / Customer visa — confiance **P**

VSO ('Vu sans observation') et VSO-SR attestés dans des sources publiques ; VAO probable ; VAOB et REF à confirmer contractuellement par client.

Utilisée par : `deliverable.customerVisa`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `pending` | En attente | Pending | ✔ |
| `vso` | VSO – Vu sans observation | Seen without comment |  |
| `vsoSr` | VSO-SR – Vu sans observation sous réserve | Seen without comment, with reservation |  |
| `vao` | VAO – Vu avec observations | Seen with comments |  |
| `vaob` | VAOB – Vu avec observations bloquantes (à confirmer) | Seen with blocking comments (TBC) |  |
| `ref` | REF – Refusé (à confirmer) | Rejected (TBC) |  |
| `forInformation` | Pour information (sans visa) | For information |  |

## reviewType

**Type de revue** / Review type

Utilisée par : `review.reviewType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `kickoff` | Lancement / revue de contrat | Kick-off / contract review |  |
| `requirementsReview` | Revue des exigences (SRR) | System requirements review |  |
| `preliminaryDesign` | Revue de conception préliminaire (PDR) | Preliminary design review |  |
| `criticalDesign` | Revue de conception détaillée (CDR) | Critical design review |  |
| `manufacturingReadiness` | Revue avant fabrication | Manufacturing readiness review |  |
| `testReadiness` | Revue d'aptitude aux essais (TRR) | Test readiness review |  |
| `qualificationReview` | Revue de qualification | Qualification review |  |
| `interventionReadiness` | Revue d'aptitude à l'intervention | Intervention readiness review |  |
| `acceptance` | Revue de réception | Acceptance review |  |
| `safetyReview` | Revue de sûreté indépendante | Independent safety review |  |
| `gate` | Jalon décisionnel (go / no-go) | Decision gate |  |
| `peerReview` | Revue par les pairs | Peer review |  |
| `documentReview` | Relecture documentaire | Document review |  |
| `lessonsLearned` | Retour d'expérience (REX) | Lessons learned |  |
| `functionalConfigAudit` | Audit de configuration fonctionnel (FCA) | Functional configuration audit |  |
| `physicalConfigAudit` | Audit de configuration physique (PCA) | Physical configuration audit |  |

## reviewDecision

**Décision de revue** / Review decision

Utilisée par : `review.reviewDecision`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `pending` | En attente | Pending | ✔ |
| `passed` | Prononcée | Passed |  |
| `passedWithReserves` | Prononcée avec réserves | Passed with reserves |  |
| `failed` | Non prononcée (à reprogrammer) | Failed (reschedule) |  |

## findingSeverity

**Gravité de la remarque** / Finding severity

Utilisée par : `reviewFinding.findingSeverity`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `blocking` | Bloquante | Blocking |  |
| `major` | Majeure | Major |  |
| `minor` | Mineure | Minor |  |
| `question` | Question / clarification | Question |  |
| `editorial` | Éditoriale | Editorial |  |

## findingOrigin

**Émetteur de la remarque** / Finding originator

Utilisée par : `reviewFinding.findingOrigin`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `internal` | Interne | Internal |  |
| `customer` | Client | Customer |  |
| `regulator` | Autorité / appui technique | Regulator / TSO |  |
| `independent` | Revue indépendante | Independent review |  |
| `supplier` | Fournisseur | Supplier |  |

## actionType

**Type d'action** / Action type

Utilisée par : `action.actionType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `containment` | Action conservatoire / immédiate | Containment / immediate |  |
| `corrective` | Corrective | Corrective |  |
| `preventive` | Préventive | Preventive |  |
| `improvement` | Amélioration | Improvement |  |
| `reviewAction` | Action de revue | Review action |  |
| `openPoint` | Point ouvert | Open point |  |
| `surveillance` | Surveillance (fournisseur, intervenant) | Oversight (supplier) |  |
| `changeImplementation` | Mise en œuvre de modification | Change implementation |  |
| `changeOrder` | Ordre de modification (ECO, CMII) | Change order (ECO, CMII) |  |
| `verification` | Vérification d'efficacité | Effectiveness check |  |

## operationalUnit

**Unité opérationnelle (UO : site, usine, centre technique, filiale)** / Operational unit (site, plant, technical centre, subsidiary) — *surchargée au niveau projet* — confiance **P**

Niveau sous la Business Line : sites industriels, centres d'ingénierie, centres techniques, filiales et partenaires. Les sites sont publics ([C], pages « implantations » de framatome.com, annexe C § 1) ; le découpage interne en UO et ses codes ne le sont pas : la liste est une amorce à remplacer par le référentiel organisationnel (Q-ORG-01) et restreinte dans chaque projet aux UO déclarées au provisioning (règle D12).

Utilisée par : `action.performingUnit`, `action.responsibleUnit`, `analysis.performingUnit`, `analysis.responsibleUnit`, `anomaly.performingUnit`, `anomaly.responsibleUnit`, `assumption.performingUnit`, `assumption.responsibleUnit`, `changeRequest.performingUnit`, `changeRequest.responsibleUnit`, `deliverable.performingUnit`, `deliverable.responsibleUnit` …

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `tbd` | À définir | To be defined | ✔ |
| `laDefense` | Courbevoie / La Défense (siège, DTI, EPR2) | Courbevoie / La Défense (HQ, DTI, EPR2) |  |
| `lyonGerland` | Lyon-Gerland (IB-F, IBE, IBS, physique du cœur, DTI) | Lyon-Gerland |  |
| `chalon` | Chalon-sur-Saône (IBM-F, IBT, CEDEM, centre technique) | Chalon-sur-Saône |  |
| `cetic` | CETIC Chalon (centre d'essais sur maquettes, JV Framatome / EDF) | CETIC Chalon (mock-up test centre, JV with EDF) |  |
| `cedem` | CEDEM Chalon (développement des machines d'intervention, IBSED-F) | CEDEM Chalon (intervention machine development) |  |
| `marseilleCadarache` | Antennes IBE (Marseille, Cadarache, Marcoule, Creys-Malville) | IBE offices (Marseille, Cadarache, Marcoule, Creys-Malville) |  |
| `sully` | Sully-sur-Loire (atelier BI, piscine, CEDOS) | Sully-sur-Loire (IB workshop, pool, CEDOS) |  |
| `maubeuge` | Maubeuge (ex-SOMANU, maintenance nucléaire, ICPE) | Maubeuge (ex-SOMANU, nuclear maintenance) |  |
| `rungis` | Rungis (siège Intercontrôle) | Rungis (Intercontrôle HQ) |  |
| `beaumontHague` | Beaumont-Hague (Framatome ARC, soudage) | Beaumont-Hague (Framatome ARC, welding) |  |
| `saintMarcel` | Saint-Marcel (composants lourds) | Saint-Marcel (heavy components) |  |
| `leCreusot` | Le Creusot (forge, internes, centre technique) | Le Creusot (forge, internals, technical centre) |  |
| `jeumont` | Jeumont (équipements mobiles, pompes, mécanismes) | Jeumont (mobile equipment, pumps, mechanisms) |  |
| `montbard` | Montbard (tubes GV, ex-Valinox) | Montbard (SG tubes, ex-Valinox) |  |
| `jeumontElectric` | Jeumont Electric (filiale avec Naval Group) | Jeumont Electric (JV with Naval Group) |  |
| `saintVictoret` | Saint-Victoret (Sebim, robinetterie) | Saint-Victoret (Sebim, valves) |  |
| `vendinLeVieil` | Vendin-le-Vieil (Sebim, robinetterie) | Vendin-le-Vieil (Sebim, valves) |  |
| `romans` | Romans-sur-Isère (assemblages REP, CERCA) | Romans-sur-Isère (PWR assemblies, CERCA) |  |
| `jarrie` | Jarrie (éponge de zirconium, chimie) | Jarrie (zirconium sponge, chemistry) |  |
| `ugine` | Ugine (alliages de zirconium, forge) | Ugine (zirconium alloys, forge) |  |
| `rugles` | Rugles (tôles et feuillards) | Rugles (sheets and strips) |  |
| `montreuilJuigne` | Montreuil-Juigné (tubes, barres, fils) | Montreuil-Juigné (tubes, bars, wires) |  |
| `paimboeuf` | Paimboeuf (tubes de gainage) | Paimboeuf (cladding tubes) |  |
| `grenobleMontbonnot` | Grenoble / Meylan / Montbonnot (C-C, ex-Rolls-Royce) | Grenoble / Meylan / Montbonnot (I&C) |  |
| `erlangen` | Erlangen (Framatome GmbH : ingénierie, I&C, FCEE, labos) | Erlangen (Framatome GmbH) |  |
| `karlstein` | Karlstein (ANF composants, I&C sûreté, centre technique) | Karlstein (ANF components, safety I&C, technical centre) |  |
| `lingen` | Lingen (ANF, usine d'assemblages) | Lingen (ANF fuel assembly plant) |  |
| `lynchburg` | Lynchburg, VA (Framatome Inc. : IB, Fuel, I&C) | Lynchburg, VA (Framatome Inc.) |  |
| `richland` | Richland, WA (fabrication combustible) | Richland, WA (fuel manufacturing) |  |
| `cranberry` | Cranberry Township, PA (bureaux) | Cranberry Township, PA (offices) |  |
| `avonmouth` | Avonmouth / Bristol (Framatome Ltd) | Avonmouth / Bristol (Framatome Ltd) |  |
| `cranfield` | Cranfield (Framatome Ltd) | Cranfield (Framatome Ltd) |  |
| `hinkleyPointC` | Hinkley Point C (chantier) | Hinkley Point C (site) |  |
| `sizewell` | Sizewell (B / C) | Sizewell (B / C) |  |
| `pickering` | Pickering, ON (Framatome Canada) | Pickering, ON (Framatome Canada) |  |
| `kincardine` | Kincardine, ON (Framatome Canada, Bruce) | Kincardine, ON (Framatome Canada, Bruce) |  |
| `montreal` | Montréal, QC (Framatome Canada) | Montréal, QC (Framatome Canada) |  |
| `reaktortest` | Reaktortest (Slovaquie, CND) | Reaktortest (Slovakia, NDE) |  |
| `pragueBeijingShenzhen` | Prague, Pékin, Shenzhen (C-C, ex-Rolls-Royce) | Prague, Beijing, Shenzhen (I&C) |  |
| `edvance` | Edvance (co-entreprise EDF 80 % / Framatome 20 %, mise à disposition) | Edvance (EDF 80 % / Framatome 20 % JV, secondment) |  |
| `externalPartner` | Partenaire externe (consortium, co-traitant) | External partner (consortium, co-contractor) |  |
| `externalSupplier` | Fournisseur externe | External supplier |  |

## regulatoryFramework

**Cadre réglementaire (pack)** / Regulatory framework (pack)

Choisi au provisioning du projet ; pilote le pack d'attributs affichés, les bibliothèques branchées et le schéma de classement par défaut (model/regulatory_packs.yaml).

Utilisée par : `regulatoryCommitment.regulatoryFramework`, `regulatoryRequirement.regulatoryFramework`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `frAsnr` | France – ASNR / INB / ESPN / AFCEN | France – ASNR / INB / ESPN / AFCEN | ✔ |
| `usNrc` | États-Unis – NRC / 10 CFR / ASME / IEEE | USA – NRC / 10 CFR / ASME / IEEE |  |
| `deKta` | Allemagne – autorités Länder / KTA | Germany – Länder authorities / KTA |  |
| `ukOnr` | Royaume-Uni – ONR (SAPs, TAGs) | UK – ONR (SAPs, TAGs) |  |
| `caCnsc` | Canada – CNSC / CSA N285-N290 | Canada – CNSC / CSA |  |
| `intlIaea` | International – AIEA / IEC / pays tiers | International – IAEA / IEC / third countries |  |
| `medicalGmp` | Santé – BPF / GMP (EMA, FDA) + sûreté nucléaire | Healthcare – GMP + nuclear safety |  |
| `defense` | Défense – instance isolée (hors instance standard) | Defence – isolated instance only |  |

## reactorTechnology

**Filière / technologie** / Reactor / facility technology

Abstraction de la filière : ne jamais coder le vocabulaire REP français dans la structure (BWR, CANDU, VVER, MTR, Gen IV, installations non-réacteur).

Utilisée par : `action.applicableTechnologies`, `analysis.applicableTechnologies`, `anomaly.applicableTechnologies`, `assumption.applicableTechnologies`, `changeRequest.applicableTechnologies`, `deliverable.applicableTechnologies`, `designDecision.applicableTechnologies`, `designParameter.applicableTechnologies`, `equipmentRequirement.applicableTechnologies`, `fmeaItem.applicableTechnologies`, `function.applicableTechnologies`, `hardwareRequirement.applicableTechnologies` …

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `pwrFramatome` | REP – conception Framatome / EDF | PWR – Framatome / EDF design |  |
| `pwrOther` | REP – autres conceptions (Westinghouse, CE, B&W, KWU...) | PWR – other designs |  |
| `bwr` | REB / BWR | BWR |  |
| `vver` | VVER | VVER |  |
| `candu` | CANDU / PHWR | CANDU / PHWR |  |
| `agr` | AGR (Royaume-Uni) | AGR (UK) |  |
| `smr` | SMR (NUWARD, autres) | SMR (NUWARD, other) |  |
| `researchReactor` | Réacteur de recherche / MTR | Research reactor / MTR |  |
| `genIV` | Génération IV (RNR-Na, HTR, sels fondus) | Gen IV (SFR, HTGR, MSR) |  |
| `naval` | Propulsion navale (instance défense) | Naval propulsion (defence instance) |  |
| `nonReactor` | Installation non-réacteur (usine, labo, transport, isotopes) | Non-reactor facility (plant, lab, transport, isotopes) |  |

## cfr5059Screening

**10 CFR 50.59 – criblage** / 10 CFR 50.59 – screening — confiance **P**

Utilisée par : `changeRequest.cfr5059Screening`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `na` | Non applicable (hors US) | Not applicable (non-US) | ✔ |
| `screenedOut` | Criblée hors 50.59 | Screened out |  |
| `evaluationRequired` | Évaluation 50.59 requise | 50.59 evaluation required |  |

## cfr5059Outcome

**10 CFR 50.59 – conclusion de l'évaluation** / 10 CFR 50.59 – evaluation outcome — confiance **P**

Utilisée par : `changeRequest.cfr5059Outcome`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `na` | Non applicable | Not applicable | ✔ |
| `noPriorApproval` | Pas d'accord préalable NRC requis | No prior NRC approval |  |
| `licenseAmendment` | Amendement de licence requis (accord NRC) | License amendment required |  |

## requirementPattern

**Gabarit de rédaction (EARS)** / Writing pattern (EARS)

Easy Approach to Requirements Syntax : guide la rédaction et les contrôles automatiques.

Utilisée par : `equipmentRequirement.requirementPattern`, `hardwareRequirement.requirementPattern`, `safetyRequirement.requirementPattern`, `softwareRequirement.requirementPattern`, `stakeholderRequirement.requirementPattern`, `systemRequirement.requirementPattern`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `ubiquitous` | Permanente (Le <système> doit…) | Ubiquitous |  |
| `eventDriven` | Sur événement (Lorsque <déclencheur>, le <système> doit…) | Event-driven |  |
| `stateDriven` | Dans un état (Tant que <état>, le <système> doit…) | State-driven |  |
| `unwanted` | Comportement indésirable (Si <défaillance>, alors…) | Unwanted behaviour |  |
| `optional` | Option (Si <option présente>, le <système> doit…) | Optional feature |  |
| `complex` | Combinée | Complex |  |
| `notApplied` | Non appliqué (texte d'entrée, information) | Not applied | ✔ |

## wasteClass

**Catégorie de déchet radioactif prévisionnelle** / Expected radioactive waste class — confiance **H**

Classement prévisionnel des déchets (démantèlement, atelier chaud, réparations). Correspondance France (TFA, FMA-VC, FA-VL, MA-VL, HA) / AIEA GSG-1 (VLLW, LLW, ILW, HLW). Nota : la France n'applique pas de seuil de libération générique (zonage déchets) ; la valeur 'conventional' n'est permise qu'en zone à déchets conventionnels.

Utilisée par : `physicalComponent.expectedWasteClass`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `tbd` | À déterminer | To be determined | ✔ |
| `conventional` | Conventionnel (zone à déchets conventionnels) | Conventional (non-nuclear waste zone) |  |
| `vllw` | TFA – très faible activité (VLLW) | VLLW – very low level |  |
| `llwShort` | FMA-VC – faible / moyenne activité à vie courte | LLW/ILW short-lived |  |
| `llwLong` | FA-VL – faible activité à vie longue | LLW long-lived |  |
| `ilwLong` | MA-VL – moyenne activité à vie longue | ILW long-lived |  |
| `hlw` | HA – haute activité | HLW – high level |  |

## submittalPurpose

**Objet de la transmission (SDRL / liste de documents contractuels)** / Submittal purpose (SDRL / contract data requirements)

Utilisée par : `deliverable.submittalPurpose`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `tbd` | À déterminer | To be determined | ✔ |
| `forApproval` | Pour approbation (visa) | For approval |  |
| `forReview` | Pour avis / commentaires | For review |  |
| `forInformation` | Pour information | For information |  |
| `forRecord` | Pour archivage (dossier final) | For record (final file) |  |
| `notContractual` | Non contractuel | Not contractual |  |

## workPackageType

**Nature du lot de travaux** / Work package type

Utilisée par : `workPackage.workPackageType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `engineering` | Études / ingénierie | Engineering |  |
| `safetyStudies` | Études de sûreté / licensing | Safety studies / licensing |  |
| `manufacturing` | Fabrication (usine) | Manufacturing (plant) |  |
| `procurement` | Approvisionnement / sous-traitance | Procurement / subcontracting |  |
| `testing` | Essais / qualification | Testing / qualification |  |
| `siteWorks` | Intervention / montage sur site | Site works / erection |  |
| `tooling` | Outillage / moyens | Tooling / equipment |  |
| `software` | Développement logiciel / C-C | Software / I&C development |  |
| `documentation` | Documentation / dossier final | Documentation / final file |  |

## habilitationDomain

**Domaine d'habilitation requis pour signer** / Qualification domain required to sign

Domaine de compétence exigé du vérificateur / approbateur (habilitation nominative tenue dans le référentiel RH-compétences et synchronisée en groupes d'annuaire HAB-<domaine>-<niveau>). Vide = politique 'rôle seul' du projet.

Utilisée par : `analysis.requiredHabilitation`, `deliverable.requiredHabilitation`, `verificationCase.requiredHabilitation`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `none` | Aucune habilitation spécifique | No specific qualification | ✔ |
| `safetyAnalysis` | Études de sûreté | Safety analysis |  |
| `pressureEquipment` | Équipements sous pression (ESPN / code) | Pressure equipment (code) |  |
| `welding` | Soudage / procédés spéciaux | Welding / special processes |  |
| `nde` | CND (certification COFREND / ISO 9712 / SNT-TC-1A) | NDE (ISO 9712 / SNT-TC-1A) |  |
| `safetyIc` | C-C de sûreté (logiciel catégorie A) | Safety I&C (category A software) |  |
| `criticality` | Sûreté-criticité | Criticality safety |  |
| `radiationProtection` | Radioprotection | Radiation protection |  |
| `coreDesign` | Études de cœur / combustible | Core / fuel design |  |
| `cgd` | Dédicace commerciale (CGD) | Commercial grade dedication |  |
| `cybersecurity` | Cybersécurité | Cybersecurity |  |
| `gmp` | Pharmaceutique (BPF / GMP) | Pharmaceutical (GMP) |  |

## testResult

**Résultat d'exécution (Test Record)** / Execution result (test record)

Miroir des résultats de Test Record (testRecordResults dans workflows.yaml) pour le champ calculé lastResult.

Utilisée par : `verificationCase.lastResult`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `notRun` | Non exécuté | Not run | ✔ |
| `passed` | Satisfaisant | Passed |  |
| `passedWithReserves` | Satisfaisant avec réserves | Passed with reserves |  |
| `failed` | Non satisfaisant | Failed |  |
| `blocked` | Bloqué | Blocked |  |
| `notApplicable` | Non applicable (justifié) | Not applicable (justified) |  |

## assumptionType

**Nature d'une hypothèse / donnée d'entrée** / Assumption / design input kind

Utilisée par : `assumption.assumptionType`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `tbd` | À déterminer | To be determined | ✔ |
| `siteData` | Donnée de site | Site data |  |
| `customerData` | Donnée client | Customer data |  |
| `supplierData` | Donnée fournisseur | Supplier data |  |
| `studyAssumption` | Hypothèse d'étude | Study assumption |  |
| `operatingAssumption` | Hypothèse d'exploitation | Operating assumption |  |
| `osintHypothesis` | Hypothèse OSINT (registre de cadrage, doc. 05) | OSINT hypothesis (scoping register) |  |

## lessonCategory

**Catégorie de REX** / Lesson category

Utilisée par : `lessonLearned.lessonCategory`

| id | Libellé FR | Libellé EN | Défaut |
|---|---|---|---|
| `technical` | Technique / conception | Technical / design |  |
| `safety` | Sûreté / radioprotection | Safety / radiation protection |  |
| `intervention` | Intervention / outillage | Intervention / tooling |  |
| `manufacturing` | Fabrication / qualité fournisseur | Manufacturing / supplier quality |  |
| `organisational` | Organisationnel / interfaces | Organisational / interfaces |  |
| `regulatory` | Réglementaire / licensing | Regulatory / licensing |  |
| `tooling` | Outil ALM / méthode IS | ALM tool / SE method |  |

