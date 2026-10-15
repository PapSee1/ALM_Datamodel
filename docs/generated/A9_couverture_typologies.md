# Annexe A9 — Matrice de couverture du modèle par typologie de projet

> Document **généré** par `tools/generate_docs.py` depuis `model/*.yaml` — ne pas éditer à la main.

Chaque typologie de projet est décrite par un **scénario de couverture** (`model/coverage_scenarios.yaml`) : types, documents, chaînes de traçabilité, attributs et valeurs d'énumération indispensables. Le validateur vérifie à chaque modification que le **profil effectif** de la typologie (classe de tailoring ∪ compléments) et les **règles de liens** permettent le scénario. Une trace marquée *xp* vise un élément d'un autre projet (bibliothèque, ligne de produits, référentiel du parc).

## Synthèse

| Typologie | Classe | Types requis | Documents | Traces | Attributs | Valeurs | Statut |
|---|---|---|---|---|---|---|---|
| Nouveau nucléaire – grand réacteur (EPR, EPR2) | classA | 28/28 | 10/10 | 20/20 | 21/21 | 9/9 | ✅ couvert |
| Nouveau nucléaire – SMR (NUWARD) | classA | 23/23 | 7/7 | 10/10 | 10/10 | 8/8 | ✅ couvert |
| Remplacement de gros composants (RGV/SGR, MCR CANDU, couvercles...) | classB | 17/17 | 4/4 | 9/9 | 4/4 | 4/4 | ✅ couvert |
| Réexamen périodique / VD / rapport de conclusions du réexamen | classB | 10/10 | 3/3 | 8/8 | 7/7 | 4/4 | ✅ couvert |
| Étude de modification base installée | classC | 13/13 | 3/3 | 7/7 | 6/6 | 3/3 | ✅ couvert |
| Fortuit / aléa en arrêt de tranche (cycle court) | classD | 15/15 | 2/2 | 11/11 | 6/6 | 5/5 | ✅ couvert |
| Outillage spécial (mécatronique, robotique, manutention) | classC | 15/15 | 4/4 | 10/10 | 3/3 | 5/5 | ✅ couvert |
| Prestation d'inspection / CND / ISI | classC | 10/10 | 3/3 | 3/3 | 2/2 | 2/2 | ✅ couvert |
| Conception combustible (nouvel assemblage, ATF) | classA | 11/11 | 4/4 | 5/5 | 2/2 | 4/4 | ✅ couvert |
| Contrat de recharge (études de cœur) | classC | 8/8 | 1/1 | 6/6 | 6/6 | 2/2 | ✅ couvert |
| Plateforme C-C (produit générique) | classA | 10/10 | 3/3 | 6/6 | 2/2 | 3/3 | ✅ couvert |
| Application / projet C-C | classB | 12/12 | 6/6 | 7/7 | 5/5 | 8/8 | ✅ couvert |
| Rénovation C-C base installée | classB | 10/10 | 4/4 | 4/4 | 2/2 | 0/0 | ✅ couvert |
| Conception de composant (GV, pressuriseur, RCP, MCG...) | classB | 7/7 | 2/2 | 4/4 | 5/5 | 2/2 | ✅ couvert |
| Fabrication de composant (ESPN) | classC | 10/10 | 5/5 | 7/7 | 12/12 | 9/9 | ✅ couvert |
| Programme R&D / innovation | classC | 7/7 | 1/1 | 3/3 | 0/0 | 0/0 | ✅ couvert |
| Projet bibliothèque / référentiel | classA | 5/5 | 3/3 | 2/2 | 0/0 | 0/0 | ✅ couvert |
| Augmentation de puissance d'une tranche existante | classB | 11/11 | 6/6 | 12/12 | 9/9 | 8/8 | ✅ couvert |
| Pièces de rechange, obsolescence, qualification d'équivalents (CGD) | classC | 10/10 | 3/3 | 10/10 | 9/9 | 7/7 | ✅ couvert |
| Réparation en atelier chaud (équipements contaminés) | classC | 12/12 | 2/2 | 9/9 | 6/6 | 6/6 | ✅ couvert |
| Démantèlement / découpe (cycle en V inversé) | classB | 16/16 | 5/5 | 11/11 | 5/5 | 10/10 | ✅ couvert |
| Services combustible sur site (inspection, réparation d'assemblages) | classC | 12/12 | 3/3 | 10/10 | 5/5 | 7/7 | ✅ couvert |
| Combustible et cibles de réacteurs de recherche (MTR) | classC | 11/11 | 3/3 | 10/10 | 7/7 | 8/8 | ✅ couvert |
| Licensing usine / transport (criticité, LEU+/HALEU, emballages) | classB | 11/11 | 3/3 | 10/10 | 11/11 | 10/10 | ✅ couvert |
| Qualification de procédé / matériau (alliage Zr, fabrication additive, soudage) | classC | 10/10 | 4/4 | 9/9 | 8/8 | 8/8 | ✅ couvert |
| Simulateur pleine échelle / plateforme de validation | classB | 12/12 | 5/5 | 11/11 | 5/5 | 7/7 | ✅ couvert |
| Mise en conformité cybersécurité d'une installation | classB | 12/12 | 4/4 | 10/10 | 4/4 | 7/7 | ✅ couvert |
| Développement et qualification d'un code de calcul scientifique | classB | 11/11 | 4/4 | 11/11 | 9/9 | 5/5 | ✅ couvert |
| Essais de laboratoire / cellules chaudes (ISO/IEC 17025) | classC | 9/9 | 2/2 | 7/7 | 7/7 | 5/5 | ✅ couvert |
| Produit catalogue configuré à la commande (FCCS, PAR, instrumentation...) | classC | 10/10 | 3/3 | 8/8 | 5/5 | 3/3 | ✅ couvert |
| Système de production d'isotopes médicaux (sûreté + BPF/GMP) | classB | 17/17 | 6/6 | 9/9 | 3/3 | 12/12 | ✅ couvert |
| Programme défense / propulsion (instance dédiée isolée) | classA | 5/5 | 2/2 | 2/2 | 2/2 | 4/4 | ✅ couvert |

## Nouveau nucléaire – grand réacteur (EPR, EPR2) (`newBuildLarge`)

*Grand réacteur neuf (EPR2, UK EPR) – périmètre chaudière et C-C de sûreté*

- **Types** : `sourceRequirement`, `regulatoryRequirement`, `stakeholderRequirement`, `systemRequirement`, `equipmentRequirement`, `safetyRequirement`, `softwareRequirement`, `hardwareRequirement`, `assumption`, `function`, `logicalComponent`, `physicalComponent`, `interface`, `designParameter`, `designDecision`, `hazard`, `safetyClaim`, `analysis`, `regulatoryCommitment`, `verificationCase`, `anomaly`, `changeRequest`, `nonConformance`, `waiver`, `deliverable`, `review`, `unitDeployment`, `workPackage`
- **Documents** : `stakeholderSpec`, `systemSpec`, `systemDesignManual`, `equipmentSpec`, `interfaceControlDocument`, `safetyCase`, `classificationList`, `complianceMatrix`, `vvPlan`, `testProcedure`
- **Attributs** : `physicalComponent` → safetyClassScheme, safetyClass, eip, espnLevel, mechanicalClass, electricalClass, qualificationClass, seismicCategory, plmItemId; `workPackage` → performingUnit, responsibleUnit, workPackageType, handoverCriteria; `deliverable` → sdrlReference, submittalPurpose; `function` → functionCategory, fundamentalSafetyFunction, defenceInDepthLevel; `systemRequirement` → definedRequirement, verificationMethods, applicableUnits
- **Valeurs** : `safetyClassScheme` ∋ eprFr, eprUk, epr2; `functionCategory` ∋ f1a, f1b, f2, iaeaCat1; `electricalClass` ∋ ee1, e1a

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `stakeholderRequirement` | `flowsDownFrom` | `sourceRequirement` |  |
| `systemRequirement` | `flowsDownFrom` | `stakeholderRequirement` |  |
| `systemRequirement` | `flowsDownFrom` | `regulatoryRequirement` | oui |
| `safetyRequirement` | `flowsDownFrom` | `analysis` |  |
| `safetyRequirement` | `mitigates` | `hazard` |  |
| `equipmentRequirement` | `flowsDownFrom` | `systemRequirement` |  |
| `function` | `satisfies` | `systemRequirement` |  |
| `logicalComponent` | `realizes` | `function` |  |
| `physicalComponent` | `realizes` | `logicalComponent` |  |
| `interface` | `sideA` | `physicalComponent` |  |
| `interface` | `sideB` | `physicalComponent` | oui |
| `verificationCase` | `verifies` | `equipmentRequirement` |  |
| `safetyClaim` | `supportedBy` | `analysis` |  |
| `safetyClaim` | `supportedBy` | `verificationCase` |  |
| `changeRequest` | `impacts` | `systemRequirement` |  |
| `unitDeployment` | `parent` | `changeRequest` |  |
| `systemRequirement` | `branched_from` | `systemRequirement` | oui |
| `deliverable` | `resolves` | `regulatoryCommitment` |  |
| `deliverable` | `inWorkPackage` | `workPackage` |  |
| `workPackage` | `dependsOn` | `workPackage` | oui |

## Nouveau nucléaire – SMR (NUWARD) (`newBuildSmr`)

*SMR NUWARD – produit générique multi-réglementations, variantes de site*

- **Types** : `sourceRequirement`, `regulatoryRequirement`, `stakeholderRequirement`, `systemRequirement`, `equipmentRequirement`, `safetyRequirement`, `assumption`, `operationalScenario`, `function`, `logicalComponent`, `physicalComponent`, `interface`, `designParameter`, `designDecision`, `hazard`, `safetyClaim`, `analysis`, `regulatoryCommitment`, `verificationCase`, `changeRequest`, `waiver`, `risk`, `review`
- **Documents** : `stakeholderSpec`, `systemSpec`, `systemDesignManual`, `safetyCase`, `interfaceControlDocument`, `genericProductSpec`, `vvPlan`
- **Attributs** : `regulatoryRequirement` → jurisdiction, edition, regulatoryFramework, applicableTechnologies; `function` → functionCategory, modelElementId; `systemRequirement` → requirementPattern, requirementQualityScore; `designDecision` → alternatives, decisionRationale
- **Valeurs** : `safetyClassScheme` ∋ iaeaSsg30; `waiverType` ∋ requirementWaiver; `regulatoryFramework` ∋ frAsnr, usNrc, ukOnr, caCnsc, intlIaea; `reactorTechnology` ∋ smr

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `operationalScenario` | `refines` | `stakeholderRequirement` |  |
| `systemRequirement` | `flowsDownFrom` | `stakeholderRequirement` |  |
| `systemRequirement` | `assumes` | `assumption` |  |
| `designDecision` | `satisfies` | `systemRequirement` |  |
| `logicalComponent` | `realizes` | `function` |  |
| `interface` | `sideA` | `logicalComponent` |  |
| `systemRequirement` | `flowsDownFrom` | `regulatoryRequirement` | oui |
| `safetyClaim` | `supportedBy` | `safetyClaim` |  |
| `waiver` | `impacts` | `systemRequirement` |  |
| `systemRequirement` | `mitigates` | `risk` |  |

## Remplacement de gros composants (RGV/SGR, MCR CANDU, couvercles...) (`steamGeneratorReplacement`)

*Remplacement de générateurs de vapeur (RGV / SGR)*

- **Types** : `sourceRequirement`, `systemRequirement`, `equipmentRequirement`, `assumption`, `operationalScenario`, `physicalComponent`, `interface`, `hazard`, `fmeaItem`, `analysis`, `verificationCase`, `nonConformance`, `waiver`, `changeRequest`, `unitDeployment`, `deliverable`, `review`
- **Documents** : `equipmentSpec`, `testProcedure`, `fmeaWorksheet`, `justificationNote`
- **Attributs** : `operationalScenario` → doseEstimate, scenarioType; `unitDeployment` → deploymentUnit, outageReference
- **Valeurs** : `vvStage` ∋ requalification, siteInstallation; `fmeaType` ∋ intervention; `scenarioType` ∋ intervention

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `operationalScenario` | `refines` | `systemRequirement` |  |
| `systemRequirement` | `mitigates` | `fmeaItem` |  |
| `fmeaItem` | `causes` | `hazard` |  |
| `physicalComponent` | `satisfies` | `equipmentRequirement` |  |
| `equipmentRequirement` | `assumes` | `assumption` |  |
| `interface` | `sideB` | `physicalComponent` | oui |
| `verificationCase` | `verifies` | `unitDeployment` |  |
| `unitDeployment` | `parent` | `changeRequest` |  |
| `nonConformance` | `impacts` | `physicalComponent` |  |

## Réexamen périodique / VD / rapport de conclusions du réexamen (`periodicSafetyReview`)

*Réexamen périodique / VD (prescriptions, conformité, réévaluation, vieillissement)*

- **Types** : `regulatoryRequirement`, `regulatoryCommitment`, `analysis`, `nonConformance`, `changeRequest`, `unitDeployment`, `physicalComponent`, `deliverable`, `safetyClaim`, `safetyRequirement`
- **Documents** : `safetyCase`, `complianceMatrix`, `justificationNote`
- **Attributs** : `physicalComponent` → ageingMechanisms, designLifeYears; `analysis` → ageingMechanisms, analysisType; `regulatoryCommitment` → requestCategory, authorityReference, commitmentDueDate
- **Valeurs** : `analysisType` ∋ ageingLto, fractureMechanics, fatigue; `requestCategory` ∋ prescription

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `deliverable` | `resolves` | `regulatoryCommitment` |  |
| `analysis` | `resolves` | `regulatoryCommitment` |  |
| `changeRequest` | `resolves` | `regulatoryCommitment` |  |
| `unitDeployment` | `parent` | `regulatoryCommitment` |  |
| `nonConformance` | `impacts` | `physicalComponent` | oui |
| `analysis` | `satisfies` | `regulatoryRequirement` | oui |
| `safetyClaim` | `supportedBy` | `analysis` |  |
| `regulatoryCommitment` | `impacts` | `physicalComponent` | oui |

## Étude de modification base installée (`plantModification`)

*Étude de modification base installée*

- **Types** : `changeRequest`, `systemRequirement`, `equipmentRequirement`, `safetyRequirement`, `regulatoryRequirement`, `physicalComponent`, `interface`, `function`, `hazard`, `analysis`, `verificationCase`, `unitDeployment`, `deliverable`
- **Documents** : `modificationFile`, `systemSpec`, `testProcedure`
- **Attributs** : `changeRequest` → regulatoryModificationClass, effectivity, impactAnalysis, safetyReportImpact, cfr5059Screening, cfr5059Outcome
- **Valeurs** : `deliverableType` ∋ operatingDocument; `regulatoryModificationClass` ∋ notableDeclaration, notableAuthorization

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `changeRequest` | `impacts` | `physicalComponent` | oui |
| `systemRequirement` | `flowsDownFrom` | `regulatoryRequirement` | oui |
| `interface` | `sideA` | `physicalComponent` | oui |
| `verificationCase` | `verifies` | `systemRequirement` |  |
| `unitDeployment` | `parent` | `changeRequest` |  |
| `deliverable` | `documents` | `changeRequest` |  |
| `safetyRequirement` | `mitigates` | `hazard` |  |

## Fortuit / aléa en arrêt de tranche (cycle court) (`fortuit`)

*Fortuit en arrêt de tranche (cycle court, justification / réparation)*

- **Types** : `technicalIssue`, `physicalComponent`, `regulatoryRequirement`, `equipmentRequirement`, `assumption`, `analysis`, `deliverable`, `verificationCase`, `nonConformance`, `waiver`, `changeRequest`, `lessonLearned`, `hazard`, `fmeaItem`, `action`
- **Documents** : `justificationNote`, `testProcedure`
- **Attributs** : `technicalIssue` → urgency, responseDueDate, outageCriticalPath, genericImpact, affectsEip, espnImpact
- **Valeurs** : `issueCategory` ∋ fortuit, inServiceFinding, genericIssue; `solutionType` ∋ justifyAsIs, repair

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `technicalIssue` | `impacts` | `physicalComponent` | oui |
| `analysis` | `resolves` | `technicalIssue` |  |
| `analysis` | `satisfies` | `regulatoryRequirement` | oui |
| `analysis` | `assumes` | `assumption` |  |
| `deliverable` | `documents` | `analysis` |  |
| `verificationCase` | `verifies` | `equipmentRequirement` |  |
| `nonConformance` | `impacts` | `physicalComponent` | oui |
| `waiver` | `resolves` | `nonConformance` |  |
| `lessonLearned` | `capitalizes` | `technicalIssue` |  |
| `technicalIssue` | `duplicates` | `technicalIssue` |  |
| `fmeaItem` | `causes` | `hazard` |  |

## Outillage spécial (mécatronique, robotique, manutention) (`specialTooling`)

*Outillage spécial (mécatronique, robotique, manutention)*

- **Types** : `stakeholderRequirement`, `systemRequirement`, `operationalScenario`, `function`, `logicalComponent`, `physicalComponent`, `interface`, `hazard`, `fmeaItem`, `designDecision`, `verificationCase`, `deliverable`, `review`, `unitDeployment`, `lessonLearned`
- **Documents** : `toolingSpec`, `fmeaWorksheet`, `testProcedure`, `vvPlan`
- **Attributs** : `physicalComponent` → serialNumber, isConfigurationItem, qualificationStatus
- **Valeurs** : `hazardType` ∋ machinery, radiological; `componentNature` ∋ tool; `testEnvironment` ∋ mockup; `functionType` ∋ toolFunction

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `function` | `satisfies` | `stakeholderRequirement` |  |
| `logicalComponent` | `realizes` | `function` |  |
| `physicalComponent` | `realizes` | `logicalComponent` |  |
| `systemRequirement` | `mitigates` | `hazard` |  |
| `fmeaItem` | `causes` | `hazard` |  |
| `verificationCase` | `verifies` | `systemRequirement` |  |
| `verificationCase` | `validates` | `operationalScenario` |  |
| `interface` | `sideA` | `physicalComponent` |  |
| `deliverable` | `documents` | `physicalComponent` |  |
| `unitDeployment` | `parent` | `deliverable` |  |

## Prestation d'inspection / CND / ISI (`inspectionService`)

*Prestation d'inspection / CND (procédés qualifiés)*

- **Types** : `stakeholderRequirement`, `systemRequirement`, `regulatoryRequirement`, `function`, `physicalComponent`, `verificationCase`, `hazard`, `fmeaItem`, `deliverable`, `unitDeployment`
- **Documents** : `toolingSpec`, `testProcedure`, `vvPlan`
- **Attributs** : `verificationCase` → qualificationStandard, independenceLevel
- **Valeurs** : `vvStage` ∋ qualification, inService

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `verificationCase` | `verifies` | `regulatoryRequirement` | oui |
| `systemRequirement` | `flowsDownFrom` | `regulatoryRequirement` | oui |
| `unitDeployment` | `parent` | `deliverable` |  |

## Conception combustible (nouvel assemblage, ATF) (`fuelDesign`)

*Conception d'un produit combustible (dont ATF) et licensing*

- **Types** : `stakeholderRequirement`, `systemRequirement`, `equipmentRequirement`, `physicalComponent`, `analysis`, `verificationCase`, `regulatoryCommitment`, `deliverable`, `designDecision`, `risk`, `assumption`
- **Documents** : `systemSpec`, `equipmentSpec`, `safetyCase`, `vvPlan`
- **Attributs** : `analysis` → codeQualification, calculationCode
- **Valeurs** : `reqCategory` ∋ designCriterion; `componentNature` ∋ fuelAssembly; `testEnvironment` ∋ reactor; `deliverableType` ∋ licensingSubmittal

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `equipmentRequirement` | `flowsDownFrom` | `systemRequirement` |  |
| `analysis` | `satisfies` | `equipmentRequirement` |  |
| `verificationCase` | `verifies` | `equipmentRequirement` |  |
| `deliverable` | `documents` | `analysis` |  |
| `deliverable` | `resolves` | `regulatoryCommitment` |  |

## Contrat de recharge (études de cœur) (`fuelReload`)

*Contrat de recharge (tranche × cycle)*

- **Types** : `designParameter`, `analysis`, `verificationCase`, `assumption`, `safetyRequirement`, `unitDeployment`, `deliverable`, `nonConformance`
- **Documents** : `reloadSafetyReport`
- **Attributs** : `designParameter` → limitValue, calculatedValue, margin, cycleOrConfiguration; `unitDeployment` → cycleNumber, deploymentUnit
- **Valeurs** : `vvStage` ∋ reloadStartupPhysics; `designParameterType` ∋ coreParameter

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `designParameter` | `refines` | `safetyRequirement` | oui |
| `analysis` | `satisfies` | `safetyRequirement` | oui |
| `verificationCase` | `verifies` | `designParameter` |  |
| `designParameter` | `assumes` | `assumption` |  |
| `unitDeployment` | `parent` | `deliverable` |  |
| `deliverable` | `documents` | `analysis` |  |

## Plateforme C-C (produit générique) (`icPlatform`)

*Plateforme de C-C qualifiée (produit générique)*

- **Types** : `systemRequirement`, `softwareRequirement`, `hardwareRequirement`, `regulatoryRequirement`, `logicalComponent`, `physicalComponent`, `verificationCase`, `anomaly`, `changeRequest`, `analysis`
- **Documents** : `softwareRequirementsSpec`, `vvPlan`, `genericProductSpec`
- **Attributs** : `physicalComponent` → icSystemClass, securityDegree
- **Valeurs** : `componentNature` ∋ softwareItem, hdlDevice; `independenceLevel` ∋ independentOrg

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `softwareRequirement` | `flowsDownFrom` | `systemRequirement` |  |
| `hardwareRequirement` | `flowsDownFrom` | `systemRequirement` |  |
| `physicalComponent` | `realizes` | `logicalComponent` |  |
| `verificationCase` | `verifies` | `softwareRequirement` |  |
| `changeRequest` | `resolves` | `anomaly` |  |
| `anomaly` | `impacts` | `physicalComponent` | oui |

## Application / projet C-C (`icApplication`)

*Projet de C-C (application) – cycle IEC 61513*

- **Types** : `systemRequirement`, `safetyRequirement`, `softwareRequirement`, `hardwareRequirement`, `function`, `logicalComponent`, `physicalComponent`, `interface`, `analysis`, `verificationCase`, `anomaly`, `changeRequest`
- **Documents** : `systemSpec`, `softwareRequirementsSpec`, `systemDesignManual`, `vvPlan`, `testProcedure`, `interfaceControlDocument`
- **Attributs** : `function` → functionCategory, securityDegree; `logicalComponent` → icSystemClass; `softwareRequirement` → softwareItem, selfMonitoring
- **Valeurs** : `functionCategory` ∋ iecCatA, iecCatB, iecCatC; `vvStage` ∋ integration, fat, sat; `analysisType` ∋ ccfDiversity, cyberRisk

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `logicalComponent` | `realizes` | `function` |  |
| `function` | `satisfies` | `safetyRequirement` |  |
| `softwareRequirement` | `flowsDownFrom` | `systemRequirement` |  |
| `softwareRequirement` | `flowsDownFrom` | `softwareRequirement` |  |
| `verificationCase` | `verifies` | `softwareRequirement` |  |
| `analysis` | `satisfies` | `systemRequirement` |  |
| `interface` | `sideA` | `logicalComponent` |  |

## Rénovation C-C base installée (`icRefurbishment`)

*Rénovation de C-C sur la base installée*

- **Types** : `systemRequirement`, `softwareRequirement`, `function`, `logicalComponent`, `physicalComponent`, `interface`, `verificationCase`, `anomaly`, `unitDeployment`, `changeRequest`
- **Documents** : `systemSpec`, `softwareRequirementsSpec`, `vvPlan`, `testProcedure`
- **Attributs** : `unitDeployment` → outageReference, deploymentUnit

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `logicalComponent` | `realizes` | `function` |  |
| `unitDeployment` | `parent` | `changeRequest` |  |
| `verificationCase` | `verifies` | `unitDeployment` |  |
| `interface` | `sideB` | `physicalComponent` | oui |

## Conception de composant (GV, pressuriseur, RCP, MCG...) (`componentDesign`)

*Conception de composant (GV, pressuriseur, pompes, mécanismes...)*

- **Types** : `equipmentRequirement`, `regulatoryRequirement`, `physicalComponent`, `analysis`, `verificationCase`, `designDecision`, `interface`
- **Documents** : `equipmentSpec`, `systemDesignManual`
- **Attributs** : `physicalComponent` → espnLevel, espnCategory, mechanicalClass; `equipmentRequirement` → designCode, espnRelevant
- **Valeurs** : `analysisType` ∋ mechanicalStress, fatigue

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `equipmentRequirement` | `flowsDownFrom` | `regulatoryRequirement` | oui |
| `analysis` | `satisfies` | `equipmentRequirement` |  |
| `physicalComponent` | `satisfies` | `equipmentRequirement` |  |
| `verificationCase` | `verifies` | `equipmentRequirement` |  |

## Fabrication de composant (ESPN) (`componentManufacturing`)

*Fabrication de composant ESPN (points d'arrêt, FNC, dossier final)*

- **Types** : `equipmentRequirement`, `regulatoryRequirement`, `physicalComponent`, `verificationCase`, `nonConformance`, `waiver`, `fmeaItem`, `deliverable`, `regulatoryCommitment`, `workPackage`
- **Documents** : `equipmentSpec`, `complianceMatrix`, `testProcedure`, `vvPlan`, `fmeaWorksheet`
- **Attributs** : `verificationCase` → inspectionPoint, witnessParties, evidenceReference, requiredHabilitation; `workPackage` → performingUnit, internalOrderReference; `equipmentRequirement` → supplierComplianceStatus, supplierDocumentReference; `nonConformance` → cfsiSuspected, authorityNotificationRequired, serialNumbers; `physicalComponent` → serialNumber
- **Valeurs** : `fmeaType` ∋ process; `deliverableType` ∋ manufacturingFile, espnFile; `inspectionPoint` ∋ hold, witness; `workPackageType` ∋ manufacturing; `habilitationDomain` ∋ nde, welding, pressureEquipment

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `verificationCase` | `verifies` | `equipmentRequirement` |  |
| `nonConformance` | `impacts` | `physicalComponent` |  |
| `waiver` | `resolves` | `nonConformance` |  |
| `deliverable` | `documents` | `physicalComponent` |  |
| `deliverable` | `resolves` | `regulatoryCommitment` |  |
| `verificationCase` | `inWorkPackage` | `workPackage` |  |
| `nonConformance` | `inWorkPackage` | `workPackage` |  |

## Programme R&D / innovation (`rdProgram`)

*Programme R&D / innovation*

- **Types** : `stakeholderRequirement`, `systemRequirement`, `designDecision`, `analysis`, `verificationCase`, `risk`, `assumption`
- **Documents** : `systemSpec`

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `designDecision` | `satisfies` | `systemRequirement` |  |
| `systemRequirement` | `assumes` | `assumption` |  |
| `systemRequirement` | `mitigates` | `risk` |  |

## Projet bibliothèque / référentiel (`library`)

*Bibliothèques (réglementaire, terminologie, agressions, cas V&V, REX)*

- **Types** : `regulatoryRequirement`, `term`, `hazard`, `verificationCase`, `lessonLearned`
- **Documents** : `regulatoryLibrary`, `glossary`, `genericProductSpec`

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `regulatoryRequirement` | `supersedes` | `regulatoryRequirement` |  |
| `term` | `supersedes` | `term` |  |

## Augmentation de puissance d'une tranche existante (`powerUprate`)

*Augmentation de puissance (réévaluation des marges, licensing, déploiement par tranche)*

- **Types** : `designParameter`, `safetyRequirement`, `equipmentRequirement`, `analysis`, `assumption`, `physicalComponent`, `changeRequest`, `regulatoryCommitment`, `deliverable`, `unitDeployment`, `verificationCase`
- **Documents** : `systemSpec`, `equipmentSpec`, `safetyCase`, `modificationFile`, `complianceMatrix`, `testProcedure`
- **Attributs** : `designParameter` → designParameterType, limitValue, calculatedValue, margin; `changeRequest` → regulatoryModificationClass, safetyReportImpact, cfr5059Screening; `analysis` → analysisType, codeQualification
- **Valeurs** : `analysisType` ∋ thermalHydraulic, deterministicSafety, mechanicalStress, neutronic; `designParameterType` ∋ designMargin, safetyLimit; `vvStage` ∋ startup; `regulatoryModificationClass` ∋ notableAuthorization

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `designParameter` | `refines` | `safetyRequirement` |  |
| `analysis` | `satisfies` | `safetyRequirement` |  |
| `designParameter` | `allocatedTo` | `physicalComponent` |  |
| `analysis` | `assumes` | `assumption` |  |
| `changeRequest` | `impacts` | `designParameter` |  |
| `regulatoryCommitment` | `impacts` | `analysis` |  |
| `deliverable` | `resolves` | `regulatoryCommitment` |  |
| `unitDeployment` | `parent` | `changeRequest` |  |
| `verificationCase` | `verifies` | `designParameter` |  |
| `physicalComponent` | `satisfies` | `equipmentRequirement` |  |
| `equipmentRequirement` | `flowsDownFrom` | `equipmentRequirement` | oui |
| `physicalComponent` | `branched_from` | `physicalComponent` | oui |

## Pièces de rechange, obsolescence, qualification d'équivalents (CGD) (`sparePartsEquivalence`)

*Pièces de rechange / obsolescence : équivalence et dédicace commerciale (CGD)*

- **Types** : `equipmentRequirement`, `physicalComponent`, `analysis`, `verificationCase`, `fmeaItem`, `deliverable`, `nonConformance`, `changeRequest`, `waiver`, `unitDeployment`
- **Documents** : `qualificationDossier`, `equipmentSpec`, `justificationNote`
- **Attributs** : `physicalComponent` → commercialGradeDedication, criticalCharacteristics, serialNumber, supplier, qualificationStatus; `equipmentRequirement` → supplierComplianceStatus, supplierComplianceStatement; `nonConformance` → part21Evaluation, cfsiSuspected
- **Valeurs** : `changeOrigin` ∋ obsolescence; `verificationMethod` ∋ commercialGradeSurvey, sourceVerification, performanceHistory, test; `analysisType` ∋ equivalence; `habilitationDomain` ∋ cgd

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `equipmentRequirement` | `flowsDownFrom` | `equipmentRequirement` | oui |
| `physicalComponent` | `satisfies` | `equipmentRequirement` |  |
| `physicalComponent` | `supersedes` | `physicalComponent` | oui |
| `analysis` | `satisfies` | `equipmentRequirement` |  |
| `equipmentRequirement` | `mitigates` | `fmeaItem` |  |
| `verificationCase` | `verifies` | `physicalComponent` |  |
| `changeRequest` | `impacts` | `physicalComponent` | oui |
| `deliverable` | `documents` | `analysis` |  |
| `nonConformance` | `impacts` | `physicalComponent` |  |
| `unitDeployment` | `parent` | `changeRequest` |  |

## Réparation en atelier chaud (équipements contaminés) (`hotWorkshopRepair`)

*Réparation en atelier chaud (équipement contaminé suivi par n° de série)*

- **Types** : `technicalIssue`, `physicalComponent`, `operationalScenario`, `hazard`, `systemRequirement`, `analysis`, `verificationCase`, `nonConformance`, `deliverable`, `unitDeployment`, `lessonLearned`, `action`
- **Documents** : `justificationNote`, `testProcedure`
- **Attributs** : `physicalComponent` → serialNumber, plantLocation, expectedWasteClass; `operationalScenario` → doseEstimate, scenarioType; `verificationCase` → testEnvironment
- **Valeurs** : `testEnvironment` ∋ hotWorkshop; `hazardType` ∋ radiological; `analysisType` ∋ doseAlara; `scenarioType` ∋ maintenance; `wasteClass` ∋ vllw, llwShort

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `technicalIssue` | `impacts` | `physicalComponent` |  |
| `analysis` | `resolves` | `technicalIssue` |  |
| `operationalScenario` | `refines` | `systemRequirement` |  |
| `systemRequirement` | `mitigates` | `hazard` |  |
| `verificationCase` | `verifies` | `physicalComponent` |  |
| `nonConformance` | `impacts` | `physicalComponent` |  |
| `deliverable` | `documents` | `physicalComponent` |  |
| `unitDeployment` | `parent` | `deliverable` |  |
| `lessonLearned` | `capitalizes` | `technicalIssue` |  |

## Démantèlement / découpe (cycle en V inversé) (`decommissioning`)

*Démantèlement (V inversé : état initial, scénarios de découpe, déchets, état final)*

- **Types** : `stakeholderRequirement`, `systemRequirement`, `regulatoryRequirement`, `safetyRequirement`, `operationalScenario`, `physicalComponent`, `hazard`, `analysis`, `assumption`, `verificationCase`, `regulatoryCommitment`, `deliverable`, `changeRequest`, `nonConformance`, `risk`, `workPackage`
- **Documents** : `stakeholderSpec`, `systemSpec`, `toolingSpec`, `safetyCase`, `vvPlan`
- **Attributs** : `physicalComponent` → plantLocation, expectedWasteClass; `operationalScenario` → scenarioType, doseEstimate; `analysis` → analysisType
- **Valeurs** : `scenarioType` ∋ decommissioning; `lifecyclePhase` ∋ decommissioning; `analysisType` ∋ radiological, wasteEnvironment; `reqCategory` ∋ decommissioning; `hazardType` ∋ radiological, intFire; `wasteClass` ∋ vllw, llwLong, ilwLong

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `operationalScenario` | `refines` | `stakeholderRequirement` |  |
| `systemRequirement` | `flowsDownFrom` | `regulatoryRequirement` | oui |
| `systemRequirement` | `flowsDownFrom` | `stakeholderRequirement` |  |
| `analysis` | `satisfies` | `systemRequirement` |  |
| `safetyRequirement` | `mitigates` | `hazard` |  |
| `physicalComponent` | `branched_from` | `physicalComponent` | oui |
| `verificationCase` | `validates` | `operationalScenario` |  |
| `verificationCase` | `verifies` | `physicalComponent` |  |
| `deliverable` | `resolves` | `regulatoryCommitment` |  |
| `analysis` | `assumes` | `assumption` |  |
| `deliverable` | `inWorkPackage` | `workPackage` |  |

## Services combustible sur site (inspection, réparation d'assemblages) (`fuelSiteServices`)

*Services combustible sur site (inspection, réparation, campagnes par arrêt)*

- **Types** : `systemRequirement`, `regulatoryRequirement`, `operationalScenario`, `hazard`, `fmeaItem`, `physicalComponent`, `verificationCase`, `technicalIssue`, `analysis`, `nonConformance`, `deliverable`, `unitDeployment`
- **Documents** : `testProcedure`, `justificationNote`, `fmeaWorksheet`
- **Attributs** : `physicalComponent` → serialNumber, componentNature; `unitDeployment` → outageReference, deploymentUnit, cycleNumber
- **Valeurs** : `componentNature` ∋ fuelAssembly, tool; `hazardType` ∋ loadDrop, criticality, radiological; `scenarioType` ∋ refuelling, intervention

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `systemRequirement` | `flowsDownFrom` | `regulatoryRequirement` | oui |
| `operationalScenario` | `refines` | `systemRequirement` |  |
| `systemRequirement` | `mitigates` | `hazard` |  |
| `fmeaItem` | `causes` | `hazard` |  |
| `verificationCase` | `verifies` | `physicalComponent` |  |
| `technicalIssue` | `impacts` | `physicalComponent` |  |
| `analysis` | `resolves` | `technicalIssue` |  |
| `nonConformance` | `impacts` | `physicalComponent` |  |
| `unitDeployment` | `parent` | `deliverable` |  |
| `physicalComponent` | `branched_from` | `physicalComponent` | oui |

## Combustible et cibles de réacteurs de recherche (MTR) (`researchReactorFuel`)

*Combustible et cibles de réacteurs de recherche (commande, série, export)*

- **Types** : `sourceRequirement`, `equipmentRequirement`, `physicalComponent`, `analysis`, `verificationCase`, `nonConformance`, `waiver`, `deliverable`, `changeRequest`, `regulatoryCommitment`, `unitDeployment`
- **Documents** : `equipmentSpec`, `complianceMatrix`, `qualificationDossier`
- **Attributs** : `physicalComponent` → componentNature, serialNumber, applicableTechnologies; `nonConformance` → serialNumbers; `deliverable` → sdrlReference, submittalPurpose; `sourceRequirement` → complianceStatus
- **Valeurs** : `componentNature` ∋ fuelAssembly, irradiationTarget; `exportControl` ∋ euDualUse, us810; `reactorTechnology` ∋ researchReactor; `deliverableType` ∋ certificate, manufacturingFile; `submittalPurpose` ∋ forRecord

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `equipmentRequirement` | `flowsDownFrom` | `sourceRequirement` |  |
| `equipmentRequirement` | `flowsDownFrom` | `equipmentRequirement` | oui |
| `physicalComponent` | `satisfies` | `equipmentRequirement` |  |
| `analysis` | `satisfies` | `equipmentRequirement` |  |
| `verificationCase` | `verifies` | `equipmentRequirement` |  |
| `nonConformance` | `impacts` | `physicalComponent` |  |
| `waiver` | `resolves` | `nonConformance` |  |
| `deliverable` | `documents` | `physicalComponent` |  |
| `deliverable` | `resolves` | `regulatoryCommitment` |  |
| `unitDeployment` | `parent` | `deliverable` |  |

## Licensing usine / transport (criticité, LEU+/HALEU, emballages) (`facilityLicensing`)

*Licensing d'usine combustible / d'emballage de transport (criticité, LEU+ / HALEU)*

- **Types** : `regulatoryRequirement`, `safetyRequirement`, `hazard`, `analysis`, `designParameter`, `verificationCase`, `regulatoryCommitment`, `safetyClaim`, `deliverable`, `assumption`, `changeRequest`
- **Documents** : `safetyCase`, `complianceMatrix`, `justificationNote`
- **Attributs** : `designParameter` → limitValue, calculatedValue, margin, uncertainty; `analysis` → calculationCode, codeVersion, codeQualification, requiredHabilitation; `regulatoryRequirement` → regulatoryFramework; `regulatoryCommitment` → regulatoryFramework, authority
- **Valeurs** : `hazardType` ∋ criticality; `analysisType` ∋ criticality, radiological, codeValidation; `reqCategory` ∋ criticalitySafety, transportPackage; `regulatoryDocType` ∋ iaeaStandard; `authority` ∋ asnr, nrc; `habilitationDomain` ∋ criticality

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `safetyRequirement` | `flowsDownFrom` | `regulatoryRequirement` | oui |
| `safetyRequirement` | `mitigates` | `hazard` |  |
| `analysis` | `satisfies` | `safetyRequirement` |  |
| `designParameter` | `refines` | `safetyRequirement` |  |
| `analysis` | `assumes` | `assumption` |  |
| `verificationCase` | `verifies` | `designParameter` |  |
| `safetyClaim` | `supportedBy` | `analysis` |  |
| `deliverable` | `resolves` | `regulatoryCommitment` |  |
| `analysis` | `dependsOn` | `analysis` |  |
| `analysis` | `satisfies` | `regulatoryRequirement` | oui |

## Qualification de procédé / matériau (alliage Zr, fabrication additive, soudage) (`processQualification`)

*Qualification de procédé / matériau (alliage de zirconium, fabrication additive, soudage)*

- **Types** : `equipmentRequirement`, `regulatoryRequirement`, `designParameter`, `verificationCase`, `analysis`, `fmeaItem`, `designDecision`, `deliverable`, `nonConformance`, `review`
- **Documents** : `qualificationDossier`, `fmeaWorksheet`, `vvPlan`, `testProcedure`
- **Attributs** : `designParameter` → designParameterType, minValue, maxValue, unit; `verificationCase` → qualificationStandard, testEnvironment, witnessParties, requiredHabilitation
- **Valeurs** : `designParameterType` ∋ processWindow; `fmeaType` ∋ process; `testEnvironment` ∋ laboratory; `witnessParty` ∋ notifiedBody, customer; `reviewType` ∋ qualificationReview; `habilitationDomain` ∋ welding, nde

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `equipmentRequirement` | `flowsDownFrom` | `regulatoryRequirement` | oui |
| `designParameter` | `refines` | `equipmentRequirement` |  |
| `verificationCase` | `verifies` | `designParameter` |  |
| `verificationCase` | `verifies` | `equipmentRequirement` |  |
| `analysis` | `satisfies` | `equipmentRequirement` |  |
| `equipmentRequirement` | `mitigates` | `fmeaItem` |  |
| `designDecision` | `satisfies` | `equipmentRequirement` |  |
| `deliverable` | `documents` | `verificationCase` |  |
| `nonConformance` | `impacts` | `designParameter` |  |

## Simulateur pleine échelle / plateforme de validation (`simulator`)

*Simulateur pleine échelle (fidélité, validation, synchronisation avec la tranche de référence)*

- **Types** : `sourceRequirement`, `stakeholderRequirement`, `systemRequirement`, `softwareRequirement`, `function`, `logicalComponent`, `physicalComponent`, `operationalScenario`, `verificationCase`, `anomaly`, `changeRequest`, `interface`
- **Documents** : `stakeholderSpec`, `systemSpec`, `softwareRequirementsSpec`, `vvPlan`, `testProcedure`
- **Attributs** : `systemRequirement` → reqCategory; `verificationCase` → vvStage, testEnvironment; `anomaly` → anomalyType, configurationVersion
- **Valeurs** : `reqCategory` ∋ simulatorFidelity; `componentNature` ∋ simulatorAsset; `testEnvironment` ∋ simulator; `scenarioType` ∋ transient, accident, normalOperation; `vvStage` ∋ sat

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `systemRequirement` | `flowsDownFrom` | `sourceRequirement` |  |
| `softwareRequirement` | `flowsDownFrom` | `systemRequirement` |  |
| `logicalComponent` | `realizes` | `function` |  |
| `function` | `satisfies` | `systemRequirement` |  |
| `verificationCase` | `verifies` | `systemRequirement` |  |
| `verificationCase` | `validates` | `operationalScenario` |  |
| `anomaly` | `impacts` | `logicalComponent` |  |
| `changeRequest` | `resolves` | `anomaly` |  |
| `changeRequest` | `dependsOn` | `changeRequest` | oui |
| `physicalComponent` | `branched_from` | `physicalComponent` | oui |
| `interface` | `sideA` | `logicalComponent` |  |

## Mise en conformité cybersécurité d'une installation (`cybersecurityCompliance`)

*Mise en conformité cybersécurité d'une installation (actifs numériques critiques, mesures, évaluation) – instance SENS*

- **Types** : `regulatoryRequirement`, `systemRequirement`, `physicalComponent`, `logicalComponent`, `hazard`, `risk`, `analysis`, `verificationCase`, `waiver`, `nonConformance`, `changeRequest`, `unitDeployment`
- **Documents** : `systemSpec`, `complianceMatrix`, `vvPlan`, `justificationNote`
- **Attributs** : `physicalComponent` → securityDegree, icSystemClass; `systemRequirement` → securityRelevant; `analysis` → analysisType
- **Valeurs** : `hazardType` ∋ cyberThreat; `analysisType` ∋ cyberRisk; `reqCategory` ∋ cybersecurity; `informationClassification` ∋ sensitiveSecurity; `securityDegree` ∋ s1, s2; `habilitationDomain` ∋ cybersecurity

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `systemRequirement` | `flowsDownFrom` | `regulatoryRequirement` | oui |
| `systemRequirement` | `flowsDownFrom` | `analysis` |  |
| `physicalComponent` | `satisfies` | `systemRequirement` |  |
| `systemRequirement` | `mitigates` | `hazard` |  |
| `hazard` | `causes` | `risk` |  |
| `verificationCase` | `verifies` | `systemRequirement` |  |
| `verificationCase` | `verifies` | `physicalComponent` |  |
| `waiver` | `impacts` | `physicalComponent` |  |
| `physicalComponent` | `realizes` | `logicalComponent` |  |
| `unitDeployment` | `parent` | `changeRequest` |  |

## Développement et qualification d'un code de calcul scientifique (`calculationCode`)

*Code de calcul scientifique (usages visés, V&V&UQ, versions qualifiées, propagation des anomalies)*

- **Types** : `stakeholderRequirement`, `softwareRequirement`, `assumption`, `logicalComponent`, `designParameter`, `designDecision`, `verificationCase`, `analysis`, `anomaly`, `changeRequest`, `deliverable`
- **Documents** : `stakeholderSpec`, `softwareRequirementsSpec`, `vvPlan`, `qualificationDossier`
- **Attributs** : `analysis` → calculationCode, codeVersion, codeQualification; `anomaly` → configurationVersion, fixVersion, safetyImpact; `designParameter` → minValue, maxValue, uncertainty
- **Valeurs** : `analysisType` ∋ codeValidation; `codeQualification` ∋ qualified, validated; `deliverableType` ∋ softwareRelease; `habilitationDomain` ∋ coreDesign

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `softwareRequirement` | `flowsDownFrom` | `stakeholderRequirement` |  |
| `softwareRequirement` | `assumes` | `assumption` |  |
| `verificationCase` | `verifies` | `softwareRequirement` |  |
| `verificationCase` | `validates` | `stakeholderRequirement` |  |
| `analysis` | `satisfies` | `stakeholderRequirement` |  |
| `designParameter` | `refines` | `stakeholderRequirement` |  |
| `designParameter` | `allocatedTo` | `logicalComponent` |  |
| `designDecision` | `satisfies` | `softwareRequirement` |  |
| `changeRequest` | `resolves` | `anomaly` |  |
| `anomaly` | `impacts` | `analysis` | oui |
| `deliverable` | `documents` | `softwareRequirement` |  |

## Essais de laboratoire / cellules chaudes (ISO/IEC 17025) (`labTesting`)

*Essais de laboratoire / cellules chaudes (demande, échantillons, incertitudes, rapport – ISO/IEC 17025)*

- **Types** : `sourceRequirement`, `verificationCase`, `physicalComponent`, `analysis`, `designParameter`, `deliverable`, `nonConformance`, `assumption`, `action`
- **Documents** : `testProcedure`, `vvPlan`
- **Attributs** : `verificationCase` → testEnvironment, procedureReference, evidenceReference, qualificationStandard; `designParameter` → uncertainty, unit; `physicalComponent` → serialNumber
- **Valeurs** : `testEnvironment` ∋ laboratory, hotCell, testLoop; `deliverableType` ∋ testReport; `ncOrigin` ∋ test

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `verificationCase` | `verifies` | `sourceRequirement` |  |
| `verificationCase` | `verifies` | `physicalComponent` |  |
| `designParameter` | `allocatedTo` | `physicalComponent` |  |
| `analysis` | `satisfies` | `sourceRequirement` |  |
| `deliverable` | `documents` | `verificationCase` |  |
| `nonConformance` | `impacts` | `verificationCase` |  |
| `verificationCase` | `assumes` | `assumption` |  |

## Produit catalogue configuré à la commande (FCCS, PAR, instrumentation...) (`configureToOrder`)

*Produit catalogue configuré à la commande (branche de la spécification maître, qualification de type réutilisée)*

- **Types** : `sourceRequirement`, `equipmentRequirement`, `physicalComponent`, `designParameter`, `designDecision`, `verificationCase`, `deliverable`, `nonConformance`, `waiver`, `changeRequest`
- **Documents** : `equipmentSpec`, `complianceMatrix`, `testProcedure`
- **Attributs** : `physicalComponent` → serialNumber, qualificationStatus, plmItemId; `equipmentRequirement` → applicabilityCondition, supplierComplianceStatus
- **Valeurs** : `verificationMethod` ∋ similarity, qualificationTest; `vvStage` ∋ fat

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `equipmentRequirement` | `branched_from` | `equipmentRequirement` | oui |
| `equipmentRequirement` | `flowsDownFrom` | `sourceRequirement` |  |
| `physicalComponent` | `satisfies` | `equipmentRequirement` |  |
| `verificationCase` | `verifies` | `equipmentRequirement` | oui |
| `designParameter` | `refines` | `equipmentRequirement` |  |
| `designDecision` | `satisfies` | `equipmentRequirement` |  |
| `deliverable` | `documents` | `physicalComponent` |  |
| `waiver` | `impacts` | `equipmentRequirement` |  |

## Système de production d'isotopes médicaux (sûreté + BPF/GMP) (`isotopeProduction`)

*Système de production d'isotopes médicaux en réacteur hôte (sûreté nucléaire + BPF)*

- **Types** : `sourceRequirement`, `regulatoryRequirement`, `stakeholderRequirement`, `systemRequirement`, `safetyRequirement`, `physicalComponent`, `logicalComponent`, `interface`, `hazard`, `fmeaItem`, `analysis`, `verificationCase`, `changeRequest`, `nonConformance`, `deliverable`, `regulatoryCommitment`, `unitDeployment`
- **Documents** : `stakeholderSpec`, `systemSpec`, `interfaceControlDocument`, `safetyCase`, `vvPlan`, `qualificationDossier`
- **Attributs** : `systemRequirement` → reqCategory; `verificationCase` → vvStage; `regulatoryRequirement` → regulatoryFramework
- **Valeurs** : `reqCategory` ∋ pharmaceuticalGmp; `componentNature` ∋ irradiationTarget; `regulatoryFramework` ∋ medicalGmp, caCnsc; `safetyClassScheme` ∋ caCnsc; `vvStage` ∋ installationQualification, operationalQualification, performanceQualification; `authority` ∋ cnsc, healthAuthority; `reactorTechnology` ∋ candu; `habilitationDomain` ∋ gmp

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `systemRequirement` | `flowsDownFrom` | `regulatoryRequirement` | oui |
| `systemRequirement` | `flowsDownFrom` | `stakeholderRequirement` |  |
| `interface` | `sideB` | `physicalComponent` | oui |
| `safetyRequirement` | `mitigates` | `hazard` |  |
| `systemRequirement` | `mitigates` | `fmeaItem` |  |
| `verificationCase` | `verifies` | `systemRequirement` |  |
| `physicalComponent` | `realizes` | `logicalComponent` |  |
| `unitDeployment` | `parent` | `deliverable` |  |
| `deliverable` | `resolves` | `regulatoryCommitment` |  |

## Programme défense / propulsion (instance dédiée isolée) (`defenseProgram`)

*Programme défense – principe seul (instance DEF) ; contenu volontairement non modélisé (OSINT, secret)*

- **Types** : `sourceRequirement`, `systemRequirement`, `verificationCase`, `nonConformance`, `deliverable`
- **Documents** : `systemSpec`, `vvPlan`
- **Attributs** : `systemRequirement` → informationClassification, exportControl
- **Valeurs** : `informationClassification` ∋ restricted; `regulatoryFramework` ∋ defense; `exportControl` ∋ frNational, frPpst

| Source | Rôle | Cible | Inter-projets |
|---|---|---|---|
| `systemRequirement` | `flowsDownFrom` | `sourceRequirement` |  |
| `verificationCase` | `verifies` | `systemRequirement` |  |

## Scénarios transverses

- **Analyse d'impact d'une demande de modification (cône d'impact)** : `changeRequest` —impacts→ `systemRequirement` ; `verificationCase` —verifies→ `systemRequirement` ; `deliverable` —documents→ `systemRequirement`
- **Évolution d'une bibliothèque réglementaire propagée aux projets** : `regulatoryRequirement` —supersedes→ `regulatoryRequirement` ; `regulatoryRequirement` —branched_from→ `regulatoryRequirement`
- **Anomalie générique de plateforme propagée aux projets C-C** : `anomaly` —impacts→ `softwareRequirement` ; `changeRequest` —resolves→ `anomaly`
- **Demande de l'autorité soldée par preuves** : `analysis` —resolves→ `regulatoryCommitment` ; `deliverable` —resolves→ `regulatoryCommitment`
- **REX transverse** : `lessonLearned` —capitalizes→ `nonConformance` ; `lessonLearned` —capitalizes→ `anomaly` ; `action` —parent→ `lessonLearned`
- **Organisation matricielle BU × UO : lots confiés, dépendances inter-projets, actions de lot** : `deliverable` —inWorkPackage→ `workPackage` ; `analysis` —inWorkPackage→ `workPackage` ; `workPackage` —parent→ `workPackage` ; `workPackage` —dependsOn→ `workPackage` ; `action` —parent→ `workPackage`
- **Anomalie d'un code de calcul propagée aux études utilisatrices d'autres projets** : `anomaly` —impacts→ `analysis` ; `changeRequest` —resolves→ `anomaly`
- **Obsolescence : article de remplacement qui remplace l'article d'origine du référentiel parc** : `physicalComponent` —supersedes→ `physicalComponent` ; `verificationCase` —verifies→ `physicalComponent`
