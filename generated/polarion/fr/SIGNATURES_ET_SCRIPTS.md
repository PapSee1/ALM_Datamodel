# Manifeste de la configuration générée (fr)

> Document **généré** par `tools/generate_polarion.py`. Il liste ce que la configuration attend de l'instance Polarion : scripts de workflow à développer, points de signature électronique à activer, constructions à confirmer au spike S1 (docs/partie4/23).

## Scripts de workflow appelés

| Script | Workflows ou documents concernés (nombre) | Liste |
|---|---|---|
| `fra-baseline.js` | 23 | changeRequest, classificationList, complianceMatrix, equipmentSpec, fmeaWorksheet, genericProductSpec, glossary, interfaceControlDocument, justificationNote, managementPlan, modificationFile, qualificationDossier … |
| `fra-classification.js` | 11 | designParameter, equipmentRequirement, function, hardwareRequirement, logicalComponent, operationalScenario, physicalComponent, safetyRequirement, softwareRequirement, stakeholderRequirement, systemRequirement |
| `fra-document-owner.js` | 19 | classificationList, complianceMatrix, equipmentSpec, fmeaWorksheet, interfaceControlDocument, justificationNote, managementPlan, modificationFile, qualificationDossier, reloadSafetyReport, safetyCase, softwareRequirementsSpec … |
| `fra-export-edms.js` | 20 | classificationList, complianceMatrix, deliverable, equipmentSpec, fmeaWorksheet, interfaceControlDocument, justificationNote, managementPlan, modificationFile, qualificationDossier, reloadSafetyReport, safetyCase … |
| `fra-field-rule.js` | 17 | action, analysis, anomaly, changeRequest, deliverable, equipmentRequirement, hardwareRequirement, nonConformance, physicalComponent, safetyRequirement, softwareRequirement, sourceRequirement … |
| `fra-habilitation.js` | 22 | analysis, classificationList, complianceMatrix, deliverable, equipmentSpec, fmeaWorksheet, interfaceControlDocument, justificationNote, managementPlan, modificationFile, qualificationDossier, reloadSafetyReport … |
| `fra-independence.js` | 54 | action, analysis, anomaly, assumption, changeRequest, classificationList, complianceMatrix, deliverable, designDecision, designParameter, equipmentRequirement, equipmentSpec … |
| `fra-link-cardinality.js` | 17 | anomaly, designParameter, equipmentRequirement, function, hardwareRequirement, interface, logicalComponent, nonConformance, operationalScenario, physicalComponent, risk, safetyRequirement … |
| `fra-link-status.js` | 4 | changeRequest, nonConformance, review, workPackage |
| `fra-no-suspect.js` | 17 | analysis, changeRequest, deliverable, designParameter, equipmentRequirement, function, hardwareRequirement, interface, logicalComponent, operationalScenario, physicalComponent, safetyClaim … |
| `fra-notify.js` | 8 | assumption, genericProductSpec, glossary, lessonLearned, nonConformance, regulatoryLibrary, technicalIssue, workPackage |
| `fra-request-safety-approval.js` | 9 | equipmentRequirement, fmeaItem, hardwareRequirement, hazard, safetyClaim, safetyRequirement, softwareRequirement, stakeholderRequirement, systemRequirement |
| `fra-revision-index.js` | 23 | classificationList, complianceMatrix, deliverable, equipmentSpec, fmeaWorksheet, genericProductSpec, glossary, interfaceControlDocument, justificationNote, managementPlan, modificationFile, qualificationDossier … |
| `fra-safety-approval.js` | 10 | changeRequest, equipmentRequirement, hardwareRequirement, nonConformance, safetyRequirement, softwareRequirement, stakeholderRequirement, systemRequirement, technicalIssue, waiver |
| `fra-set-if-empty.js` | 6 | equipmentRequirement, hardwareRequirement, safetyRequirement, softwareRequirement, stakeholderRequirement, systemRequirement |
| `fra-sla.js` | 2 | nonConformance, technicalIssue |
| `fra-verification-status.js` | 6 | equipmentRequirement, hardwareRequirement, safetyRequirement, softwareRequirement, stakeholderRequirement, systemRequirement |

## Points de signature électronique

| Workflow / type | Action | Signification | Note |
|---|---|---|---|
| assumption | `confirm` | verified | intention conditionnelle (safetyRelevant = yes) rendue systématique (la signature Polarion n'est pas conditionnelle) |
| interface | `agree` | approved | signature systématique |
| designDecision | `decide` | approved | signature systématique |
| analysis | `submit` | authored | signature systématique |
| analysis | `approve` | verified | signature systématique |
| regulatoryCommitment | `submitResponse` | approved | signature systématique |
| regulatoryCommitment | `cancel` | approved | signature systématique |
| anomaly | `close` | accepted | intention conditionnelle (safetyImpact = yes) rendue systématique (la signature Polarion n'est pas conditionnelle) |
| changeRequest | `approveClassII` | ccb | signature systématique |
| changeRequest | `approve` | ccb | signature systématique |
| changeRequest | `reject` | ccb | signature systématique |
| changeRequest | `close` | approved | signature systématique |
| nonConformance | `approveDisposition` | approved | signature systématique |
| nonConformance | `close` | quality | signature systématique |
| nonConformance | `cancel` | quality | signature systématique |
| waiver | `toExternal` | verified | signature systématique |
| waiver | `approveInternal` | approved | signature systématique |
| waiver | `approveExternal` | approved | signature systématique |
| technicalIssue | `propose` | verified | intention conditionnelle (affectsEip = yes OR safetyImpact = yes) rendue systématique (la signature Polarion n'est pas conditionnelle) |
| deliverable | `submit` | authored | signature systématique |
| deliverable | `approve` | approved | signature systématique |
| review | `close` | approved | signature systématique |
| workPackage | `agree` | agreed | signature systématique |
| workPackage | `deliver` | authored | signature systématique |
| workPackage | `accept` | accepted | signature systématique |
| unitDeployment | `requalify` | verified | signature systématique |
| stakeholderSpec | `submitVerification` | authored | signature systématique |
| stakeholderSpec | `verify` | verified | signature systématique |
| stakeholderSpec | `approve` | approved | signature systématique |
| systemSpec | `submitVerification` | authored | signature systématique |
| systemSpec | `verify` | verified | signature systématique |
| systemSpec | `approve` | approved | signature systématique |
| systemDesignManual | `submitVerification` | authored | signature systématique |
| systemDesignManual | `verify` | verified | signature systématique |
| systemDesignManual | `approve` | approved | signature systématique |
| equipmentSpec | `submitVerification` | authored | signature systématique |
| equipmentSpec | `verify` | verified | signature systématique |
| equipmentSpec | `approve` | approved | signature systématique |
| softwareRequirementsSpec | `submitVerification` | authored | signature systématique |
| softwareRequirementsSpec | `verify` | verified | signature systématique |
| softwareRequirementsSpec | `approve` | approved | signature systématique |
| interfaceControlDocument | `submitVerification` | authored | signature systématique |
| interfaceControlDocument | `verify` | verified | signature systématique |
| interfaceControlDocument | `approve` | approved | signature systématique |
| safetyCase | `submitVerification` | authored | signature systématique |
| safetyCase | `verify` | verified | signature systématique |
| safetyCase | `approve` | approved | signature systématique |
| classificationList | `submitVerification` | authored | signature systématique |
| classificationList | `verify` | verified | signature systématique |
| classificationList | `approve` | approved | signature systématique |
| complianceMatrix | `submitVerification` | authored | signature systématique |
| complianceMatrix | `verify` | verified | signature systématique |
| complianceMatrix | `approve` | approved | signature systématique |
| vvPlan | `submitVerification` | authored | signature systématique |
| vvPlan | `verify` | verified | signature systématique |
| vvPlan | `approve` | approved | signature systématique |
| testProcedure | `submitVerification` | authored | signature systématique |
| testProcedure | `verify` | verified | signature systématique |
| testProcedure | `approve` | approved | signature systématique |
| toolingSpec | `submitVerification` | authored | signature systématique |
| toolingSpec | `verify` | verified | signature systématique |
| toolingSpec | `approve` | approved | signature systématique |
| fmeaWorksheet | `submitVerification` | authored | signature systématique |
| fmeaWorksheet | `verify` | verified | signature systématique |
| fmeaWorksheet | `approve` | approved | signature systématique |
| justificationNote | `submit` | authored | signature systématique |
| justificationNote | `approve` | approved | signature systématique |
| reloadSafetyReport | `submitVerification` | authored | signature systématique |
| reloadSafetyReport | `verify` | verified | signature systématique |
| reloadSafetyReport | `approve` | approved | signature systématique |
| modificationFile | `submitVerification` | authored | signature systématique |
| modificationFile | `verify` | verified | signature systématique |
| modificationFile | `approve` | approved | signature systématique |
| managementPlan | `submitVerification` | authored | signature systématique |
| managementPlan | `verify` | verified | signature systématique |
| managementPlan | `approve` | approved | signature systématique |
| regulatoryLibrary | `submit` | authored | signature systématique |
| regulatoryLibrary | `publish` | approved | signature systématique |
| genericProductSpec | `submit` | authored | signature systématique |
| genericProductSpec | `publish` | approved | signature systématique |
| glossary | `submit` | authored | signature systématique |
| glossary | `publish` | approved | signature systématique |
| qualificationDossier | `submitVerification` | authored | signature systématique |
| qualificationDossier | `verify` | verified | signature systématique |
| qualificationDossier | `approve` | approved | signature systématique |
| workPackageHandover | `submit` | authored | signature systématique |
| workPackageHandover | `approve` | approved | signature systématique |

## Constructions à confirmer sur la version cible

- Bloc `<signatures><signature-policy name="all"/></signatures>` sur une action (documents et Work Items) : format et effet à confirmer
- Configuration Testing : nom du fichier des résultats de Test Record (`testrecord-result-enum.xml` supposé), type de cas de test (`verificationCase`, `polarionTestCase: true`) et rôle de couverture `verifies` à déclarer dans l'administration Testing
- Fichiers `documents/fields/document-type-enum.xml`, `document-status-enum.xml` et `documents/workflow/<type>-workflow.xml` (prototype Module) : emplacement et noms
- Paramètres additionnels de ScriptCondition / ScriptFunction (`rule`, `roles`, `args`, `projectParameter`) et moteur `js`
- Règles de liens `<rule from to>` imbriquées dans les options de `workitem-link-role-enum.xml`, et jeton `__other` pour l'inter-projets
- Rôle « propriétaire du document » : réalisé par ScriptCondition `fra-document-owner.js` (aucun rôle spécial Polarion connu pour l'auteur d'un document) ; les rôles alternatifs d'une même transition lui sont passés en paramètre `orRoles` (OU)
- Rôles spéciaux `workitem.assignee` / `workitem.author` dans RoleCondition
- Types de champs `text`, `date-time`, `struct:TestSteps`, `enum:@user` ; attributs `sortOrder` / `description` des options d'énumération
- `InvokeAction(statusId, actionId, query)` : comportement lorsque l'action n'est pas disponible pour un élément de la requête
