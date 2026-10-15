# Annexe A3 — Rôles de liens, règles et matrice de traçabilité

> Document **généré** par `tools/generate_docs.py` depuis `model/*.yaml` — ne pas éditer à la main.

Convention : le lien est créé depuis l'artefact **aval** (source) vers l'artefact **amont** (cible). Une modification de la cible rend le lien suspect côté source.

## Rôles de liens

| id | Libellé (sens direct) | Libellé (sens inverse) | Suspicion | Sémantique |
|---|---|---|---|---|
| `parent` | a pour parent / *has parent* | a pour enfant / *is parent of* | non | Décomposition hiérarchique (FBS, PBS, arborescence d'argumentaire, d'actions). Nota : la suspicion native ne s'applique pas aux liens parent ; la cohérence parent/enfant est contrôlée par rapport. |
| `flowsDownFrom` | découle de / *flows down from* | se décline en / *flows down to* | oui | SysML «deriveReqt» (déclinaison / flow-down) : exigence aval obtenue par transformation ou allocation d'une exigence amont. Identifiant volontairement distinct du rôle système Polarion 'derived_from' (réutilisation de documents). |
| `refines` | précise / *refines* | est précisée par / *is refined by* | oui | SysML «refine» : un scénario, un paramètre ou une hypothèse détaille / quantifie une exigence sans en dériver une nouvelle. |
| `satisfies` | satisfait / *satisfies* | est satisfaite par / *is satisfied by* | oui | SysML «satisfy» : un élément de conception répond à l'exigence (sens inverse = matrice d'allocation). |
| `realizes` | réalise / *realizes* | est réalisé par / *is realized by* | oui | Allocation R-F-L-P : élément logique → fonction ; élément physique → élément logique / fonction. |
| `allocatedTo` | est alloué à / *is allocated to* | porte / *carries* | oui | Allocation d'un paramètre, d'une marge ou d'un budget à un élément d'architecture. |
| `verifies` | vérifie / *verifies* | est vérifiée par / *is verified by* | oui | SysML «verify». Rôle à déclarer dans la configuration Testing de Polarion (couverture). |
| `validates` | valide / *validates* | est validée par / *is validated by* | oui | Validation : le produit répond au besoin dans son contexte d'emploi. |
| `mitigates` | maîtrise / *mitigates* | est maîtrisé par / *is mitigated by* | oui | Parade / exigence / disposition de conception / action couvrant un danger, un risque ou un mode de défaillance. |
| `causes` | cause / *causes* | est causé par / *is caused by* | non | Chaîne causale (AMDEC, agressions induites, risques en cascade). |
| `supportedBy` | est étayée par / *is supported by* | étaye / *supports* | oui | Argumentaire CAE/GSN : revendication → sous-revendication / preuve. La modification d'une preuve rend la revendication suspecte. |
| `assumes` | s'appuie sur l'hypothèse / *relies on assumption* | est une hypothèse de / *is assumption for* | oui | Dépendance à une hypothèse / donnée d'entrée : toute évolution de l'hypothèse interpelle les dépendants. |
| `impacts` | impacte / *impacts* | est impacté par / *is impacted by* | non | Périmètre d'impact d'une modification, d'un écart, d'une dérogation, d'un fortuit ou d'une demande d'autorité. |
| `resolves` | résout / *resolves* | est résolu par / *is resolved by* | non | Clôture : modification / action / livrable / analyse / dérogation qui traite un écart, une anomalie, une remarque, une demande. |
| `sideA` | a pour côté A / *has side A* | est côté A de / *is side A of* | oui | Extrémité A d'une interface (fournisseur de la donnée / du flux par convention). |
| `sideB` | a pour côté B / *has side B* | est côté B de / *is side B of* | oui | Extrémité B d'une interface (récepteur par convention). |
| `documents` | documente / *documents* | est documenté dans / *is documented in* | oui | Livrable → artefacts qu'il décrit ou justifie : toute évolution des artefacts interpelle le rédacteur du livrable. |
| `dependsOn` | dépend de / *depends on* | est un prérequis de / *is prerequisite for* | oui | Dépendance d'enchaînement (livrables, cas V&V, actions, modifications, lots). Inter-projets autorisé (v0.3) : livrable d'une UO attendu par un autre projet, mise à jour du simulateur dépendant d'une modification de la tranche de référence. |
| `supersedes` | remplace / *supersedes* | est remplacé par / *is superseded by* | non | Remplacement (nouvelle édition de norme, exigence reformulée, document annulé et remplacé). |
| `raisedIn` | est émise lors de / *is raised in* | a donné lieu à / *raises* | non | Rattachement d'une remarque à une revue ou à un livrable relu ; d'une action à une revue. |
| `capitalizes` | capitalise / *captures lesson from* | est capitalisé dans / *has lesson learned* | non | Fiche REX → événement(s) dont elle tire les enseignements (fortuit, écart, anomalie, revue, modification, risque survenu, demande d'autorité). |
| `duplicates` | duplique / *duplicates* | est dupliqué par / *is duplicated by* | non | Doublon (fiches multiples pour un même sujet). |
| `inWorkPackage` | relève du lot / *belongs to work package* | comprend / *includes* | non | Rattachement d'un artefact produit à un lot de travaux confié à une UO (organisation matricielle). Non suspect : le lot n'est pas une donnée d'entrée technique. |
| `branched_from` | est une branche de / *is branched from* | a pour branche / *has branch* | oui | Rôle système Polarion créé par le branchement de documents (bibliothèque / produit générique → projet). La fusion 3-way (2404+) et la suspicion signalent les évolutions de la référence. |
| `derived_from` | est réutilisé de (document dérivé) / *is derived from (reuse)* | est réutilisé dans / *has derived item* | oui | Rôle système Polarion créé par la réutilisation en 'document dérivé' (lecture seule hors champs autorisés, mise à jour depuis la source). Ne pas employer manuellement. |
| `relates_to` | est en relation avec / *relates to* | est en relation avec / *relates to* | non | Relation informative non qualifiée. Ne doit JAMAIS être utilisée pour justifier une couverture. |

## Règles d'autorisation (source → cibles)

### `parent`

- **REQ_ALL** → même type
- **assumption, operationalScenario, function, logicalComponent, physicalComponent, interface, designParameter, designDecision** → même type
- **hazard, safetyClaim, fmeaItem, analysis, risk, verificationCase, deliverable, review, term** → même type
- **action** → action, changeRequest, nonConformance, technicalIssue, regulatoryCommitment, review, reviewFinding, risk, anomaly
- **reviewFinding** → review
- **changeRequest, nonConformance, technicalIssue, anomaly** → même type
- **unitDeployment** → changeRequest, regulatoryCommitment, technicalIssue, waiver, deliverable, designDecision
- **action** → unitDeployment, lessonLearned, workPackage
- **workPackage** → même type
- **ALL_TYPES** → heading
- **heading** → heading

### `flowsDownFrom`

- **stakeholderRequirement** → sourceRequirement, regulatoryRequirement, stakeholderRequirement
- **safetyRequirement** → sourceRequirement, regulatoryRequirement, stakeholderRequirement, safetyRequirement, analysis, hazard
- **systemRequirement** → sourceRequirement, regulatoryRequirement, stakeholderRequirement, safetyRequirement, systemRequirement, analysis
- **equipmentRequirement** → sourceRequirement, regulatoryRequirement, systemRequirement, safetyRequirement, equipmentRequirement, analysis
- **softwareRequirement** → sourceRequirement, stakeholderRequirement, systemRequirement, safetyRequirement, equipmentRequirement, softwareRequirement, regulatoryRequirement
- **hardwareRequirement** → systemRequirement, safetyRequirement, equipmentRequirement, hardwareRequirement, regulatoryRequirement

### `refines`

- **operationalScenario** → sourceRequirement, stakeholderRequirement, systemRequirement
- **designParameter** → REQ_ALL

### `satisfies`

- **function, logicalComponent, physicalComponent, interface, designParameter, designDecision** → REQ_ALL
- **analysis, deliverable** → REQ_ALL

### `realizes`

- **logicalComponent** → function
- **physicalComponent** → logicalComponent, function

### `allocatedTo`

- **designParameter** → function, logicalComponent, physicalComponent, interface

### `verifies`

- **verificationCase** → REQ_ALL
- **verificationCase** → function, logicalComponent, physicalComponent, interface, designParameter, assumption, unitDeployment

### `validates`

- **verificationCase** → sourceRequirement, stakeholderRequirement, operationalScenario

### `mitigates`

- **REQ_AUTHORED** → hazard, risk, fmeaItem
- **function, logicalComponent, physicalComponent, designDecision, action, verificationCase** → hazard, risk, fmeaItem

### `causes`

- **fmeaItem** → fmeaItem, hazard, risk
- **hazard** → hazard, risk

### `supportedBy`

- **safetyClaim** → safetyClaim, analysis, verificationCase, deliverable, designDecision, safetyRequirement, regulatoryCommitment

### `assumes`

- **REQ_AUTHORED** → assumption
- **analysis, designParameter, designDecision, safetyClaim, function, physicalComponent, interface, verificationCase** → assumption

### `impacts`

- **ISSUES** → ENGINEERING

### `resolves`

- **changeRequest, action, deliverable, analysis, waiver, verificationCase** → nonConformance, technicalIssue, anomaly, reviewFinding, regulatoryCommitment

### `sideA`

- **interface** → function, logicalComponent, physicalComponent

### `sideB`

- **interface** → function, logicalComponent, physicalComponent

### `documents`

- **deliverable** → ENGINEERING
- **deliverable** → changeRequest, nonConformance, waiver, technicalIssue, regulatoryCommitment

### `dependsOn`

- **deliverable, verificationCase, action, changeRequest, analysis, review, workPackage** → même type
- **review** → deliverable, verificationCase, analysis
- **deliverable** → analysis, verificationCase, assumption

### `supersedes`

- **REQ_ALL** → même type
- **deliverable, analysis, designDecision, term, physicalComponent** → même type

### `raisedIn`

- **reviewFinding** → review, deliverable
- **action, nonConformance, anomaly** → review

### `capitalizes`

- **lessonLearned** → technicalIssue, nonConformance, anomaly, review, changeRequest, risk, waiver, regulatoryCommitment, reviewFinding, unitDeployment

### `duplicates`

- **ISSUES** → même type

### `inWorkPackage`

- **deliverable, analysis, verificationCase, action, unitDeployment, designDecision, physicalComponent, changeRequest, nonConformance, technicalIssue, review** → workPackage

### `branched_from`

- **any** → any

### `derived_from`

- **any** → any

### `relates_to`

- **any** → any

## Matrice de traçabilité (ligne = source aval, colonne = cible amont)

Hors `parent`, `relates_to` et rôles système de réutilisation. Abréviations des rôles :

`FD` = flowsDownFrom, `RF` = refines, `SAT` = satisfies, `REA` = realizes, `AL` = allocatedTo, `VER` = verifies, `VAL` = validates, `MIT` = mitigates, `CAU` = causes, `SUP` = supportedBy, `ASM` = assumes, `IMP` = impacts, `RES` = resolves, `A` = sideA, `B` = sideB, `DOC` = documents, `DEP` = dependsOn, `SUPS` = supersedes, `RAI` = raisedIn, `c` = capitalizes, `DUP` = duplicates, `iwp` = inWorkPackage

| source \ cible | `sourceRequirement` | `regulatoryRequirement` | `stakeholderRequirement` | `systemRequirement` | `equipmentRequirement` | `softwareRequirement` | `hardwareRequirement` | `safetyRequirement` | `assumption` | `operationalScenario` | `function` | `logicalComponent` | `physicalComponent` | `interface` | `designParameter` | `designDecision` | `hazard` | `safetyClaim` | `risk` | `fmeaItem` | `analysis` | `regulatoryCommitment` | `verificationCase` | `anomaly` | `changeRequest` | `nonConformance` | `waiver` | `technicalIssue` | `deliverable` | `review` | `reviewFinding` | `action` | `workPackage` | `term` | `unitDeployment` | `lessonLearned` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `sourceRequirement` | SUPS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `regulatoryRequirement` |  | SUPS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `stakeholderRequirement` | FD | FD | FD SUPS |  |  |  |  |  | ASM |  |  |  |  |  |  |  | MIT |  | MIT | MIT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `systemRequirement` | FD | FD | FD | FD SUPS |  |  |  | FD | ASM |  |  |  |  |  |  |  | MIT |  | MIT | MIT | FD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `equipmentRequirement` | FD | FD |  | FD | FD SUPS |  |  | FD | ASM |  |  |  |  |  |  |  | MIT |  | MIT | MIT | FD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `softwareRequirement` | FD | FD | FD | FD | FD | FD SUPS |  | FD | ASM |  |  |  |  |  |  |  | MIT |  | MIT | MIT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `hardwareRequirement` |  | FD |  | FD | FD |  | FD SUPS | FD | ASM |  |  |  |  |  |  |  | MIT |  | MIT | MIT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `safetyRequirement` | FD | FD | FD |  |  |  |  | FD SUPS | ASM |  |  |  |  |  |  |  | FD MIT |  | MIT | MIT | FD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `assumption` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `operationalScenario` | RF |  | RF | RF |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `function` | SAT | SAT | SAT | SAT | SAT | SAT | SAT | SAT | ASM |  |  |  |  |  |  |  | MIT |  | MIT | MIT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `logicalComponent` | SAT | SAT | SAT | SAT | SAT | SAT | SAT | SAT |  |  | REA |  |  |  |  |  | MIT |  | MIT | MIT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `physicalComponent` | SAT | SAT | SAT | SAT | SAT | SAT | SAT | SAT | ASM |  | REA | REA | SUPS |  |  |  | MIT |  | MIT | MIT |  |  |  |  |  |  |  |  |  |  |  |  | iwp |  |  |  |
| `interface` | SAT | SAT | SAT | SAT | SAT | SAT | SAT | SAT | ASM |  | A B | A B | A B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `designParameter` | RF SAT | RF SAT | RF SAT | RF SAT | RF SAT | RF SAT | RF SAT | RF SAT | ASM |  | AL | AL | AL | AL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `designDecision` | SAT | SAT | SAT | SAT | SAT | SAT | SAT | SAT | ASM |  |  |  |  |  |  | SUPS | MIT |  | MIT | MIT |  |  |  |  |  |  |  |  |  |  |  |  | iwp |  |  |  |
| `hazard` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | CAU |  | CAU |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `safetyClaim` |  |  |  |  |  |  |  | SUP | ASM |  |  |  |  |  |  | SUP |  | SUP |  |  | SUP | SUP | SUP |  |  |  |  |  | SUP |  |  |  |  |  |  |  |
| `risk` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `fmeaItem` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | CAU |  | CAU | CAU |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `analysis` | SAT | SAT | SAT | SAT | SAT | SAT | SAT | SAT | ASM |  |  |  |  |  |  |  |  |  |  |  | DEP SUPS | RES |  | RES |  | RES |  | RES |  |  | RES |  | iwp |  |  |  |
| `regulatoryCommitment` | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | DUP | IMP |  |  |  |  |  | IMP |  |  |  |  |  |  |  |
| `verificationCase` | VER VAL | VER | VER VAL | VER | VER | VER | VER | VER | VER ASM | VAL | VER | VER | VER | VER | VER |  | MIT |  | MIT | MIT |  | RES | DEP | RES |  | RES |  | RES |  |  | RES |  | iwp |  | VER |  |
| `anomaly` | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP |  | IMP | DUP |  |  |  |  | IMP | RAI |  |  |  |  |  |  |
| `changeRequest` | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | RES | IMP | RES | DEP DUP | RES |  | RES | IMP |  | RES |  | iwp |  |  |  |
| `nonConformance` | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP |  | IMP |  |  | DUP |  |  | IMP | RAI |  |  | iwp |  |  |  |
| `waiver` | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | RES | IMP | RES |  | RES | DUP | RES | IMP |  | RES |  |  |  |  |  |
| `technicalIssue` | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP |  | IMP |  |  |  |  | DUP | IMP |  |  |  | iwp |  |  |  |
| `deliverable` | SAT DOC | SAT DOC | SAT DOC | SAT DOC | SAT DOC | SAT DOC | SAT DOC | SAT DOC | DOC DEP | DOC | DOC | DOC | DOC | DOC | DOC | DOC | DOC | DOC | DOC | DOC | DOC DEP | RES DOC | DOC DEP | RES | DOC | RES DOC | DOC | RES DOC | DOC DEP SUPS |  | RES |  | iwp |  |  |  |
| `review` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | DEP |  | DEP |  |  |  |  |  | DEP | DEP |  |  | iwp |  |  |  |
| `reviewFinding` | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP | IMP |  | IMP |  |  |  |  |  | IMP RAI | RAI | DUP |  |  |  |  |  |
| `action` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MIT |  | MIT | MIT |  | RES |  | RES |  | RES |  | RES |  | RAI | RES | DEP | iwp |  |  |  |
| `workPackage` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | DEP |  |  |  |
| `term` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | SUPS |  |  |
| `unitDeployment` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | iwp |  |  |  |
| `lessonLearned` |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | c |  |  | c |  | c | c | c | c | c |  | c | c |  |  |  | c |  |

## Politique de déclenchement de la suspicion

- **default** : `title`, `description`
- **sourceRequirement** : `title`, `description`, `originalText`, `bindingLevel`, `applicablePlantSeries`, `applicableUnits`
- **regulatoryRequirement** : `title`, `description`, `edition`, `bindingLevel`, `applicablePlantSeries`, `applicableUnits`
- **REQ_AUTHORED** : `title`, `description`, `acceptanceCriteria`, `verificationMethods`, `bindingLevel`, `definedRequirement`, `safetyClass`, `applicablePlantSeries`, `applicableUnits`, `plantStates`, `plantConditions`
- **function** : `title`, `description`, `functionCategory`, `applicablePlantSeries`
- **logicalComponent** : `title`, `description`, `functionCategory`, `icSystemClass`, `applicablePlantSeries`
- **physicalComponent** : `title`, `description`, `safetyClass`, `eip`, `mechanicalClass`, `electricalClass`, `qualificationClass`, `seismicCategory`, `espnLevel`, `applicablePlantSeries`
- **interface** : `title`, `description`, `interfaceData`, `interfaceType`, `applicablePlantSeries`
- **designParameter** : `title`, `description`, `limitValue`, `nominalValue`, `minValue`, `maxValue`, `unit`
- **assumption** : `title`, `description`
- **hazard** : `title`, `description`, `frequencyBand`, `screening`, `decouplingCriteria`
- **analysis** : `title`, `description`, `conclusion`, `analysisResult`, `revisionIndex`
- **verificationCase** : `title`, `description`, `acceptanceCriteria`
- **deliverable** : `title`, `description`, `revisionIndex`

## Règles de complétude de la traçabilité

| id | Règle | S'applique à | Sévérité |
|---|---|---|---|
| TR-01 | Toute exigence rédigée approuvée découle d'au moins une exigence amont, sauf exigence d'origine interne justifiée (rationale). | systemRequirement, equipmentRequirement, softwareRequirement, hardwareRequirement | warn |
| TR-02 | Toute exigence d'entrée acceptée a un statut de conformité différent de 'À évaluer' et est dérivée ou couverte. | sourceRequirement | block |
| TR-03 | Toute exigence avec definedRequirement = Oui est vérifiée par au moins un cas de vérification approuvé. | REQ_AUTHORED | block |
| TR-04 | Toute exigence approuvée a au moins une méthode de vérification et est vérifiée (ou validée) par au moins un cas. | REQ_AUTHORED | warn |
| TR-05 | Toute exigence de sûreté est satisfaite par au moins un élément d'architecture ou une analyse. | safetyRequirement | block |
| TR-06 | Toute fonction catégorisée (≠ NC) est réalisée par au moins un élément logique ou physique. | function | warn |
| TR-07 | Tout élément physique EIP porte un classement validé par la Sûreté et satisfait au moins une exigence. | physicalComponent | block |
| TR-08 | Toute interface a exactement un côté A et un côté B. | interface | block |
| TR-09 | Tout danger retenu est maîtrisé par au moins une exigence ou disposition. | hazard | block |
| TR-10 | Tout cas de vérification vérifie ou valide au moins un élément. | verificationCase | block |
| TR-11 | Toute FNC / dérogation affectant un EIP identifie les artefacts impactés. | nonConformance, waiver | block |
| TR-12 | Toute demande de modification de classe I identifie son périmètre d'impact avant passage en CCB. | changeRequest | block |
| TR-13 | Toute revendication de sûreté de type 'goal' est étayée (supportedBy) par au moins une preuve ou sous-revendication. | safetyClaim | warn |
| TR-14 | Aucun lien suspect ne subsiste au passage d'un LiveDoc en 'approuvé' ou à la clôture d'une demande de modification. | document, changeRequest | block |
| TR-15 | Toute demande d'autorité est résolue par au moins un livrable, une analyse ou une action avant clôture. | regulatoryCommitment | block |
| TR-16 | Toute hypothèse confirmée l'est par une preuve (verificationCase validant ou document). | assumption | warn |
| TR-17 | Le lien 'relates_to' n'est jamais compté dans les indicateurs de couverture. | REQ_ALL | info |
| TR-18 | Organisation matricielle : tout livrable d'un projet comportant des lots relève d'un lot de travaux (UO réalisatrice identifiée). | deliverable | warn |
| TR-19 | Pack réglementaire US : toute demande de modification présentée en CCB porte un criblage 10 CFR 50.59 renseigné (≠ 'non applicable'). | changeRequest | block |
| TR-20 | Tout article commercial dédicacé (CGD) est vérifié par au moins un cas de vérification approuvé portant sur ses caractéristiques critiques. | physicalComponent | block |
