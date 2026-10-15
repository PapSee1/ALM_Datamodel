# Annexe A1 — Catalogue des types de Work Items et de leurs attributs

> Document **généré** par `tools/generate_docs.py` depuis `model/*.yaml` — ne pas éditer à la main.

## Synthèse

| Famille | Type (id) | Libellé | Workflow | Nb attributs |
|---|---|---|---|---|
| Exigences | `sourceRequirement` | Exigence d'entrée | `wfInputRequirement` | 26 |
| Exigences | `regulatoryRequirement` | Exigence réglementaire / normative | `wfLibraryItem` | 27 |
| Exigences | `stakeholderRequirement` | Exigence de besoin (parties prenantes) | `wfRequirement` | 38 |
| Exigences | `systemRequirement` | Exigence système | `wfRequirement` | 37 |
| Exigences | `equipmentRequirement` | Exigence équipement | `wfRequirement` | 43 |
| Exigences | `softwareRequirement` | Exigence logicielle | `wfRequirement` | 41 |
| Exigences | `hardwareRequirement` | Exigence matérielle / HDL | `wfRequirement` | 40 |
| Exigences | `safetyRequirement` | Exigence de sûreté | `wfRequirement` | 40 |
| Exigences | `assumption` | Hypothèse / donnée d'entrée | `wfAssumption` | 21 |
| Architecture (RFLP) | `operationalScenario` | Scénario opérationnel | `wfArchitecture` | 21 |
| Architecture (RFLP) | `function` | Fonction | `wfArchitecture` | 28 |
| Architecture (RFLP) | `logicalComponent` | Élément logique | `wfArchitecture` | 20 |
| Architecture (RFLP) | `physicalComponent` | Élément physique (SSC) | `wfArchitecture` | 49 |
| Architecture (RFLP) | `interface` | Interface | `wfInterface` | 26 |
| Architecture (RFLP) | `designParameter` | Paramètre de conception | `wfArchitecture` | 26 |
| Architecture (RFLP) | `designDecision` | Décision de conception | `wfDecision` | 21 |
| Sûreté, risques, analyses | `hazard` | Agression / événement initiateur | `wfSafetyAnalysisItem` | 22 |
| Sûreté, risques, analyses | `safetyClaim` | Revendication de sûreté (argumentaire) | `wfSafetyAnalysisItem` | 20 |
| Sûreté, risques, analyses | `risk` | Risque / opportunité | `wfRisk` | 27 |
| Sûreté, risques, analyses | `fmeaItem` | Ligne d'AMDEC (mode de défaillance) | `wfSafetyAnalysisItem` | 30 |
| Sûreté, risques, analyses | `analysis` | Analyse / étude / calcul | `wfAnalysis` | 30 |
| Sûreté, risques, analyses | `regulatoryCommitment` | Engagement / demande de l'autorité | `wfCommitment` | 25 |
| Vérification & validation | `verificationCase` | Cas de vérification / validation | `wfVerificationCase` | 33 |
| Vérification & validation | `anomaly` | Fiche d'anomalie (V&V) | `wfAnomaly` | 22 |
| Modifications, écarts, fortuits | `changeRequest` | Demande de modification | `wfChangeRequest` | 37 |
| Modifications, écarts, fortuits | `nonConformance` | Écart / fiche de non-conformité (FNC) | `wfNonConformance` | 37 |
| Modifications, écarts, fortuits | `waiver` | Dérogation / concession | `wfWaiver` | 22 |
| Modifications, écarts, fortuits | `technicalIssue` | Problème technique / fortuit | `wfTechnicalIssue` | 30 |
| Projet, livrables, revues | `deliverable` | Livrable / document | `wfDeliverable` | 31 |
| Projet, livrables, revues | `review` | Revue / jalon | `wfReview` | 23 |
| Projet, livrables, revues | `reviewFinding` | Remarque de revue / observation client | `wfReviewFinding` | 20 |
| Projet, livrables, revues | `action` | Action | `wfAction` | 18 |
| Projet, livrables, revues | `workPackage` | Lot de travaux (UO réalisatrice) | `wfWorkPackage` | 22 |
| Bibliothèque | `term` | Terme du glossaire | `wfLibraryItem` | 7 |
| Modifications, écarts, fortuits | `unitDeployment` | Déploiement par tranche / cycle (effectivité) | `wfUnitDeployment` | 24 |
| Projet, livrables, revues | `lessonLearned` | Fiche REX (retour d'expérience) | `wfLessonLearned` | 20 |

**Total : 36 types personnalisés** (+ type natif `heading`).

## Jeux d'attributs réutilisables (fieldSets)

### `common` — Attributs transverses à tous les artefacts d'ingénierie.

| Attribut (id) | Libellé | Type | Obligatoire | Règle |
|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | à la soumission (`submitState` du workflow) |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  |  |
| `externalId` | Identifiant externe | string |  | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui |  |
| `wbsCode` | Code WBS / OTP | string |  |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |

### `requirementCore` — Attributs de toute exigence rédigée (hors exigences d'entrée verbatim).

| Attribut (id) | Libellé | Type | Obligatoire | Règle |
|---|---|---|---|---|
| `reqCategory` | Catégorie | enum [`reqCategory`](A2_enumerations.md#reqcategory) | à la soumission (`submitState` du workflow) |  |
| `bindingLevel` | Force | enum [`bindingLevel`](A2_enumerations.md#bindinglevel) |  |  |
| `rationale` | Justification (rationale) | richtext |  |  |
| `acceptanceCriteria` | Critères d'acceptation | richtext |  |  |
| `verificationMethods` | Méthodes de vérification | enum [`verificationMethod`](A2_enumerations.md#verificationmethod) (multi) | à l'état `approved` |  |
| `verificationMethodRationale` | Justification du choix de méthode | text |  | Pourquoi essai plutôt qu'analyse, etc. (INCOSE / ISO 29148) ; obligatoire par rapport pour les exigences définies. |
| `vvStagesPlanned` | Étapes V&V prévues | enum [`vvStage`](A2_enumerations.md#vvstage) (multi) |  |  |
| `maturity` | Maturité | enum [`maturity`](A2_enumerations.md#maturity) |  |  |
| `plantStates` | États d'exploitation | enum [`plantState`](A2_enumerations.md#plantstate) (multi) |  |  |
| `plantConditions` | Conditions de fonctionnement | enum [`plantCondition`](A2_enumerations.md#plantcondition) (multi) |  |  |
| `verificationStatus` | Statut de vérification (calculé) | enum [`vvStatus`](A2_enumerations.md#vvstatus) |  |  |
| `customerApprovalRequired` | Accord client requis pour modification | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  |  |
| `requirementPattern` | Gabarit de rédaction (EARS) | enum [`requirementPattern`](A2_enumerations.md#requirementpattern) |  |  |
| `requirementQualityScore` | Score qualité de rédaction (calculé) | float |  | Contrôles INCOSE GtWR / ISO 29148 (termes ambigus, 'et/ou', passif, unités, verbe prescriptif) par script ou extension ; indicateur, jamais bloquant. |

### `supplierFlowdown` — Déclinaison vers un fournisseur et réponse de conformité (spécification d'approvisionnement, CCTP).

| Attribut (id) | Libellé | Type | Obligatoire | Règle |
|---|---|---|---|---|
| `supplierComplianceStatus` | Conformité déclarée par le fournisseur | enum [`complianceStatus`](A2_enumerations.md#compliancestatus) |  |  |
| `supplierComplianceStatement` | Réponse du fournisseur | richtext |  |  |
| `supplierDocumentReference` | Référence document fournisseur | string |  |  |

### `requirementSafety` — Pertinence sûreté d'une exigence (le classement détaillé est porté par la fonction / le SSC).

| Attribut (id) | Libellé | Type | Obligatoire | Règle |
|---|---|---|---|---|
| `safetyRelevant` | Pertinente pour la sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui |  |
| `definedRequirement` | Exigence définie (EIP) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | Exigence assignée à un EIP au sens de l'arrêté INB : déclenche le socle non négociable (contrôle technique, traçabilité V&V, gestion d'écart). |
| `protectedInterests` | Intérêts protégés | enum [`protectedInterest`](A2_enumerations.md#protectedinterest) (multi) |  |  |
| `safetyClassScheme` | Référentiel de classement | enum [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) |  |  |
| `safetyClass` | Classe de sûreté héritée | enum [`safetyClass`](A2_enumerations.md#safetyclass) |  | Classe la plus sévère des éléments auxquels l'exigence est allouée (contrôlée par rapport). |
| `functionCategory` | Catégorie de fonction héritée | enum [`functionCategory`](A2_enumerations.md#functioncategory) |  |  |
| `securityRelevant` | Pertinente cybersécurité | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  |  |

### `sscClassification` — Classement complet d'une structure, d'un système ou d'un composant (SSC) – note de classement.

| Attribut (id) | Libellé | Type | Obligatoire | Règle |
|---|---|---|---|---|
| `safetyClassScheme` | Référentiel de classement | enum [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) | à la soumission (`submitState` du workflow) |  |
| `safetyClass` | Classe de sûreté | enum [`safetyClass`](A2_enumerations.md#safetyclass) |  |  |
| `eip` | EIP (élément important pour la protection) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui |  |
| `protectedInterests` | Intérêts protégés | enum [`protectedInterest`](A2_enumerations.md#protectedinterest) (multi) |  |  |
| `ipsLegacy` | IPS (terminologie parc historique) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  |  |
| `itns` | ITNS (ISO 19443) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  |  |
| `qaProgramLevel` | Programme qualité | enum [`qaProgramLevel`](A2_enumerations.md#qaprogramlevel) |  |  |
| `mechanicalClass` | Classe mécanique | enum [`mechanicalClass`](A2_enumerations.md#mechanicalclass) |  |  |
| `electricalClass` | Classe électrique | enum [`electricalClass`](A2_enumerations.md#electricalclass) |  |  |
| `qualificationClass` | Classe de qualification | enum [`qualificationClass`](A2_enumerations.md#qualificationclass) |  |  |
| `seismicCategory` | Catégorie sismique | enum [`seismicCategory`](A2_enumerations.md#seismiccategory) |  |  |
| `seismicCriterion` | Exigence sismique | enum [`seismicCriterion`](A2_enumerations.md#seismiccriterion) |  |  |
| `espnLevel` | Niveau ESPN | enum [`espnLevel`](A2_enumerations.md#espnlevel) |  |  |
| `espnCategory` | Catégorie ESP | enum [`espnCategory`](A2_enumerations.md#espncategory) |  |  |
| `icSystemClass` | Classe système C-C | enum [`icSystemClass`](A2_enumerations.md#icsystemclass) |  |  |
| `securityDegree` | Degré de sécurité cyber | enum [`securityDegree`](A2_enumerations.md#securitydegree) |  |  |
| `classificationRationale` | Justification du classement | richtext |  |  |
| `classificationValidated` | Classement validé par la Sûreté | boolean |  |  |

### `functionSafety` — Catégorisation d'une fonction.

| Attribut (id) | Libellé | Type | Obligatoire | Règle |
|---|---|---|---|---|
| `safetyClassScheme` | Référentiel de classement | enum [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) |  |  |
| `functionCategory` | Catégorie de fonction | enum [`functionCategory`](A2_enumerations.md#functioncategory) | oui |  |
| `fundamentalSafetyFunction` | Fonction fondamentale de sûreté | enum [`fundamentalSafetyFunction`](A2_enumerations.md#fundamentalsafetyfunction) |  |  |
| `defenceInDepthLevel` | Niveaux de défense en profondeur | enum [`defenceInDepthLevel`](A2_enumerations.md#defenceindepthlevel) (multi) |  |  |
| `protectedInterests` | Intérêts protégés | enum [`protectedInterest`](A2_enumerations.md#protectedinterest) (multi) |  |  |
| `plantStates` | États d'exploitation | enum [`plantState`](A2_enumerations.md#plantstate) (multi) |  |  |
| `plantConditions` | Conditions de fonctionnement | enum [`plantCondition`](A2_enumerations.md#plantcondition) (multi) |  |  |
| `securityDegree` | Degré de sécurité cyber | enum [`securityDegree`](A2_enumerations.md#securitydegree) |  |  |
| `categorisationRationale` | Justification de la catégorisation | richtext |  |  |

### `documentReference` — Référencement documentaire (GED = système d'archivage de référence).

| Attribut (id) | Libellé | Type | Obligatoire | Règle |
|---|---|---|---|---|
| `documentNumber` | N° de document | string |  |  |
| `revisionIndex` | Indice | string |  |  |
| `customerDocumentNumber` | N° document client | string |  |  |
| `aip` | Produit d'une AIP | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | Activité importante pour la protection → contrôle technique indépendant obligatoire. |
| `requiredHabilitation` | Habilitation requise du vérificateur / approbateur | enum [`habilitationDomain`](A2_enumerations.md#habilitationdomain) |  | Contrôlée par la condition qualifiedSignatory lorsque le projet a choisi la politique de signature 'habilitationBased' (model/project_setup.yaml). |

## Famille : Exigences

### `sourceRequirement` — Exigence d'entrée / Input requirement

Exigence reçue verbatim (contrat, CCTP, spécification client, EUR, donnée d'entrée) et importée (ReqIF / Word / Excel). Le texte original n'est jamais modifié : on y porte la position de conformité.

- Workflow : [`wfInputRequirement`](A4_workflows.md#wfinputrequirement)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `requirementSourceType` | Nature de la source | enum [`requirementSourceType`](A2_enumerations.md#requirementsourcetype) | oui | local |  |
| `sourceDocument` | Document source | string | oui | local |  |
| `sourceDocumentRevision` | Révision du document source | string |  | local |  |
| `sourceParagraph` | Paragraphe | string |  | local |  |
| `originalText` | Texte original (verbatim) | richtext |  | local |  |
| `sourceIssuer` | Émetteur | enum [`stakeholder`](A2_enumerations.md#stakeholder) |  | local |  |
| `complianceStatus` | Statut de conformité | enum [`complianceStatus`](A2_enumerations.md#compliancestatus) | oui | local |  |
| `complianceStatement` | Position de conformité | richtext |  | local |  |
| `bindingLevel` | Force (doit / devrait / peut) | enum [`bindingLevel`](A2_enumerations.md#bindinglevel) |  | local | Posée par les règles d'import Word W-02..W-04 ; pilote la position de conformité attendue. |
| `safetyRelevant` | Pertinente pour la sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `verificationStatus` | Statut de vérification (calculé) | enum [`vvStatus`](A2_enumerations.md#vvstatus) | calculé | local |  |

### `regulatoryRequirement` — Exigence réglementaire / normative / Regulatory / normative requirement

Exigence extraite d'un texte réglementaire, d'un guide ou d'une norme. Maintenue dans le projet bibliothèque LIB-REG et réutilisée (branche de document) dans les projets. Pour les textes sous droit d'auteur (AFCEN, IEC, ISO), on stocke la référence et une paraphrase, jamais le texte intégral sans licence.

- Workflow : [`wfLibraryItem`](A4_workflows.md#wflibraryitem)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `regulatoryDocType` | Type de texte | enum [`regulatoryDocType`](A2_enumerations.md#regulatorydoctype) | oui | local |  |
| `regulatoryReference` | Référence (texte, article / clause) | string | oui | local |  |
| `edition` | Édition / version | string | oui | local |  |
| `jurisdiction` | Juridiction | enum [`region`](A2_enumerations.md#region) |  | local |  |
| `regulatoryFramework` | Cadre réglementaire (pack) | enum [`regulatoryFramework`](A2_enumerations.md#regulatoryframework) |  | local |  |
| `bindingLevel` | Force | enum [`bindingLevel`](A2_enumerations.md#bindinglevel) |  | local |  |
| `effectiveDate` | Date d'application | date |  | local |  |
| `transitionalProvisions` | Dispositions transitoires | richtext |  | local |  |
| `copyrightRestricted` | Texte protégé (paraphrase) | boolean |  | local |  |
| `complianceStatus` | Statut de conformité (copie projet) | enum [`complianceStatus`](A2_enumerations.md#compliancestatus) |  | local |  |
| `complianceStatement` | Position de conformité (copie projet) | richtext |  | local |  |
| `verificationStatus` | Statut de vérification (calculé) | enum [`vvStatus`](A2_enumerations.md#vvstatus) | calculé | local |  |

### `stakeholderRequirement` — Exigence de besoin (parties prenantes) / Stakeholder requirement

Besoin reformulé, univoque et vérifiable (INCOSE GtWR), niveau STB. Dérivé des exigences d'entrée et réglementaires ; validé par scénarios.

- Workflow : [`wfRequirement`](A4_workflows.md#wfrequirement)
- Jeux d'attributs hérités : `common`, `requirementCore`, `requirementSafety`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `reqCategory` | Catégorie | enum [`reqCategory`](A2_enumerations.md#reqcategory) | `soumission` | requirementCore |  |
| `bindingLevel` | Force | enum [`bindingLevel`](A2_enumerations.md#bindinglevel) |  | requirementCore |  |
| `rationale` | Justification (rationale) | richtext |  | requirementCore |  |
| `acceptanceCriteria` | Critères d'acceptation | richtext |  | requirementCore |  |
| `verificationMethods` | Méthodes de vérification | enum [`verificationMethod`](A2_enumerations.md#verificationmethod) (multi) | `approved` | requirementCore |  |
| `verificationMethodRationale` | Justification du choix de méthode | text |  | requirementCore | Pourquoi essai plutôt qu'analyse, etc. (INCOSE / ISO 29148) ; obligatoire par rapport pour les exigences définies. |
| `vvStagesPlanned` | Étapes V&V prévues | enum [`vvStage`](A2_enumerations.md#vvstage) (multi) |  | requirementCore |  |
| `maturity` | Maturité | enum [`maturity`](A2_enumerations.md#maturity) |  | requirementCore |  |
| `plantStates` | États d'exploitation | enum [`plantState`](A2_enumerations.md#plantstate) (multi) |  | requirementCore |  |
| `plantConditions` | Conditions de fonctionnement | enum [`plantCondition`](A2_enumerations.md#plantcondition) (multi) |  | requirementCore |  |
| `verificationStatus` | Statut de vérification (calculé) | enum [`vvStatus`](A2_enumerations.md#vvstatus) | calculé | requirementCore |  |
| `customerApprovalRequired` | Accord client requis pour modification | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementCore |  |
| `requirementPattern` | Gabarit de rédaction (EARS) | enum [`requirementPattern`](A2_enumerations.md#requirementpattern) |  | requirementCore |  |
| `requirementQualityScore` | Score qualité de rédaction (calculé) | float | calculé | requirementCore | Contrôles INCOSE GtWR / ISO 29148 (termes ambigus, 'et/ou', passif, unités, verbe prescriptif) par script ou extension ; indicateur, jamais bloquant. |
| `safetyRelevant` | Pertinente pour la sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety |  |
| `definedRequirement` | Exigence définie (EIP) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety | Exigence assignée à un EIP au sens de l'arrêté INB : déclenche le socle non négociable (contrôle technique, traçabilité V&V, gestion d'écart). |
| `protectedInterests` | Intérêts protégés | enum [`protectedInterest`](A2_enumerations.md#protectedinterest) (multi) |  | requirementSafety |  |
| `safetyClassScheme` | Référentiel de classement | enum [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) |  | requirementSafety |  |
| `safetyClass` | Classe de sûreté héritée | enum [`safetyClass`](A2_enumerations.md#safetyclass) |  | requirementSafety | Classe la plus sévère des éléments auxquels l'exigence est allouée (contrôlée par rapport). |
| `functionCategory` | Catégorie de fonction héritée | enum [`functionCategory`](A2_enumerations.md#functioncategory) |  | requirementSafety |  |
| `securityRelevant` | Pertinente cybersécurité | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementSafety |  |
| `stakeholder` | Parties prenantes | enum [`stakeholder`](A2_enumerations.md#stakeholder) (multi) | `soumission` | local |  |
| `needStatement` | Énoncé du besoin | richtext |  | local |  |

### `systemRequirement` — Exigence système / System requirement

Exigence de solution aux niveaux installation / système / sous-système (ST, STS, SDM). Le niveau est porté par reqLevel.

- Workflow : [`wfRequirement`](A4_workflows.md#wfrequirement)
- Jeux d'attributs hérités : `common`, `requirementCore`, `requirementSafety`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `reqCategory` | Catégorie | enum [`reqCategory`](A2_enumerations.md#reqcategory) | `soumission` | requirementCore |  |
| `bindingLevel` | Force | enum [`bindingLevel`](A2_enumerations.md#bindinglevel) |  | requirementCore |  |
| `rationale` | Justification (rationale) | richtext |  | requirementCore |  |
| `acceptanceCriteria` | Critères d'acceptation | richtext |  | requirementCore |  |
| `verificationMethods` | Méthodes de vérification | enum [`verificationMethod`](A2_enumerations.md#verificationmethod) (multi) | `approved` | requirementCore |  |
| `verificationMethodRationale` | Justification du choix de méthode | text |  | requirementCore | Pourquoi essai plutôt qu'analyse, etc. (INCOSE / ISO 29148) ; obligatoire par rapport pour les exigences définies. |
| `vvStagesPlanned` | Étapes V&V prévues | enum [`vvStage`](A2_enumerations.md#vvstage) (multi) |  | requirementCore |  |
| `maturity` | Maturité | enum [`maturity`](A2_enumerations.md#maturity) |  | requirementCore |  |
| `plantStates` | États d'exploitation | enum [`plantState`](A2_enumerations.md#plantstate) (multi) |  | requirementCore |  |
| `plantConditions` | Conditions de fonctionnement | enum [`plantCondition`](A2_enumerations.md#plantcondition) (multi) |  | requirementCore |  |
| `verificationStatus` | Statut de vérification (calculé) | enum [`vvStatus`](A2_enumerations.md#vvstatus) | calculé | requirementCore |  |
| `customerApprovalRequired` | Accord client requis pour modification | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementCore |  |
| `requirementPattern` | Gabarit de rédaction (EARS) | enum [`requirementPattern`](A2_enumerations.md#requirementpattern) |  | requirementCore |  |
| `requirementQualityScore` | Score qualité de rédaction (calculé) | float | calculé | requirementCore | Contrôles INCOSE GtWR / ISO 29148 (termes ambigus, 'et/ou', passif, unités, verbe prescriptif) par script ou extension ; indicateur, jamais bloquant. |
| `safetyRelevant` | Pertinente pour la sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety |  |
| `definedRequirement` | Exigence définie (EIP) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety | Exigence assignée à un EIP au sens de l'arrêté INB : déclenche le socle non négociable (contrôle technique, traçabilité V&V, gestion d'écart). |
| `protectedInterests` | Intérêts protégés | enum [`protectedInterest`](A2_enumerations.md#protectedinterest) (multi) |  | requirementSafety |  |
| `safetyClassScheme` | Référentiel de classement | enum [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) |  | requirementSafety |  |
| `safetyClass` | Classe de sûreté héritée | enum [`safetyClass`](A2_enumerations.md#safetyclass) |  | requirementSafety | Classe la plus sévère des éléments auxquels l'exigence est allouée (contrôlée par rapport). |
| `functionCategory` | Catégorie de fonction héritée | enum [`functionCategory`](A2_enumerations.md#functioncategory) |  | requirementSafety |  |
| `securityRelevant` | Pertinente cybersécurité | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementSafety |  |
| `reqLevel` | Niveau | enum [`reqLevel`](A2_enumerations.md#reqlevel) | `soumission` | local |  |

### `equipmentRequirement` — Exigence équipement / Equipment requirement

Exigence au niveau équipement / composant ; base des spécifications d'approvisionnement (STE) et des cahiers des charges fournisseurs.

- Workflow : [`wfRequirement`](A4_workflows.md#wfrequirement)
- Jeux d'attributs hérités : `common`, `requirementCore`, `requirementSafety`, `supplierFlowdown`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `reqCategory` | Catégorie | enum [`reqCategory`](A2_enumerations.md#reqcategory) | `soumission` | requirementCore |  |
| `bindingLevel` | Force | enum [`bindingLevel`](A2_enumerations.md#bindinglevel) |  | requirementCore |  |
| `rationale` | Justification (rationale) | richtext |  | requirementCore |  |
| `acceptanceCriteria` | Critères d'acceptation | richtext |  | requirementCore |  |
| `verificationMethods` | Méthodes de vérification | enum [`verificationMethod`](A2_enumerations.md#verificationmethod) (multi) | `approved` | requirementCore |  |
| `verificationMethodRationale` | Justification du choix de méthode | text |  | requirementCore | Pourquoi essai plutôt qu'analyse, etc. (INCOSE / ISO 29148) ; obligatoire par rapport pour les exigences définies. |
| `vvStagesPlanned` | Étapes V&V prévues | enum [`vvStage`](A2_enumerations.md#vvstage) (multi) |  | requirementCore |  |
| `maturity` | Maturité | enum [`maturity`](A2_enumerations.md#maturity) |  | requirementCore |  |
| `plantStates` | États d'exploitation | enum [`plantState`](A2_enumerations.md#plantstate) (multi) |  | requirementCore |  |
| `plantConditions` | Conditions de fonctionnement | enum [`plantCondition`](A2_enumerations.md#plantcondition) (multi) |  | requirementCore |  |
| `verificationStatus` | Statut de vérification (calculé) | enum [`vvStatus`](A2_enumerations.md#vvstatus) | calculé | requirementCore |  |
| `customerApprovalRequired` | Accord client requis pour modification | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementCore |  |
| `requirementPattern` | Gabarit de rédaction (EARS) | enum [`requirementPattern`](A2_enumerations.md#requirementpattern) |  | requirementCore |  |
| `requirementQualityScore` | Score qualité de rédaction (calculé) | float | calculé | requirementCore | Contrôles INCOSE GtWR / ISO 29148 (termes ambigus, 'et/ou', passif, unités, verbe prescriptif) par script ou extension ; indicateur, jamais bloquant. |
| `safetyRelevant` | Pertinente pour la sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety |  |
| `definedRequirement` | Exigence définie (EIP) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety | Exigence assignée à un EIP au sens de l'arrêté INB : déclenche le socle non négociable (contrôle technique, traçabilité V&V, gestion d'écart). |
| `protectedInterests` | Intérêts protégés | enum [`protectedInterest`](A2_enumerations.md#protectedinterest) (multi) |  | requirementSafety |  |
| `safetyClassScheme` | Référentiel de classement | enum [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) |  | requirementSafety |  |
| `safetyClass` | Classe de sûreté héritée | enum [`safetyClass`](A2_enumerations.md#safetyclass) |  | requirementSafety | Classe la plus sévère des éléments auxquels l'exigence est allouée (contrôlée par rapport). |
| `functionCategory` | Catégorie de fonction héritée | enum [`functionCategory`](A2_enumerations.md#functioncategory) |  | requirementSafety |  |
| `securityRelevant` | Pertinente cybersécurité | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementSafety |  |
| `supplierComplianceStatus` | Conformité déclarée par le fournisseur | enum [`complianceStatus`](A2_enumerations.md#compliancestatus) |  | supplierFlowdown |  |
| `supplierComplianceStatement` | Réponse du fournisseur | richtext |  | supplierFlowdown |  |
| `supplierDocumentReference` | Référence document fournisseur | string |  | supplierFlowdown |  |
| `reqLevel` | Niveau | enum [`reqLevel`](A2_enumerations.md#reqlevel) | `soumission` | local |  |
| `procurementSpec` | Spécification d'approvisionnement | string |  | local |  |
| `designCode` | Code / norme de conception applicable | string |  | local |  |
| `espnRelevant` | Concerne un ESPN | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |

### `softwareRequirement` — Exigence logicielle / Software requirement

Exigence logicielle (C-C IEC 60880 / IEC 62138, logiciels d'outillage). La catégorie de la fonction supportée détermine l'exigence de V&V.

- Workflow : [`wfRequirement`](A4_workflows.md#wfrequirement)
- Jeux d'attributs hérités : `common`, `requirementCore`, `requirementSafety`, `supplierFlowdown`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `reqCategory` | Catégorie | enum [`reqCategory`](A2_enumerations.md#reqcategory) | `soumission` | requirementCore |  |
| `bindingLevel` | Force | enum [`bindingLevel`](A2_enumerations.md#bindinglevel) |  | requirementCore |  |
| `rationale` | Justification (rationale) | richtext |  | requirementCore |  |
| `acceptanceCriteria` | Critères d'acceptation | richtext |  | requirementCore |  |
| `verificationMethods` | Méthodes de vérification | enum [`verificationMethod`](A2_enumerations.md#verificationmethod) (multi) | `approved` | requirementCore |  |
| `verificationMethodRationale` | Justification du choix de méthode | text |  | requirementCore | Pourquoi essai plutôt qu'analyse, etc. (INCOSE / ISO 29148) ; obligatoire par rapport pour les exigences définies. |
| `vvStagesPlanned` | Étapes V&V prévues | enum [`vvStage`](A2_enumerations.md#vvstage) (multi) |  | requirementCore |  |
| `maturity` | Maturité | enum [`maturity`](A2_enumerations.md#maturity) |  | requirementCore |  |
| `plantStates` | États d'exploitation | enum [`plantState`](A2_enumerations.md#plantstate) (multi) |  | requirementCore |  |
| `plantConditions` | Conditions de fonctionnement | enum [`plantCondition`](A2_enumerations.md#plantcondition) (multi) |  | requirementCore |  |
| `verificationStatus` | Statut de vérification (calculé) | enum [`vvStatus`](A2_enumerations.md#vvstatus) | calculé | requirementCore |  |
| `customerApprovalRequired` | Accord client requis pour modification | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementCore |  |
| `requirementPattern` | Gabarit de rédaction (EARS) | enum [`requirementPattern`](A2_enumerations.md#requirementpattern) |  | requirementCore |  |
| `requirementQualityScore` | Score qualité de rédaction (calculé) | float | calculé | requirementCore | Contrôles INCOSE GtWR / ISO 29148 (termes ambigus, 'et/ou', passif, unités, verbe prescriptif) par script ou extension ; indicateur, jamais bloquant. |
| `safetyRelevant` | Pertinente pour la sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety |  |
| `definedRequirement` | Exigence définie (EIP) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety | Exigence assignée à un EIP au sens de l'arrêté INB : déclenche le socle non négociable (contrôle technique, traçabilité V&V, gestion d'écart). |
| `protectedInterests` | Intérêts protégés | enum [`protectedInterest`](A2_enumerations.md#protectedinterest) (multi) |  | requirementSafety |  |
| `safetyClassScheme` | Référentiel de classement | enum [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) |  | requirementSafety |  |
| `safetyClass` | Classe de sûreté héritée | enum [`safetyClass`](A2_enumerations.md#safetyclass) |  | requirementSafety | Classe la plus sévère des éléments auxquels l'exigence est allouée (contrôlée par rapport). |
| `functionCategory` | Catégorie de fonction héritée | enum [`functionCategory`](A2_enumerations.md#functioncategory) |  | requirementSafety |  |
| `securityRelevant` | Pertinente cybersécurité | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementSafety |  |
| `supplierComplianceStatus` | Conformité déclarée par le fournisseur | enum [`complianceStatus`](A2_enumerations.md#compliancestatus) |  | supplierFlowdown |  |
| `supplierComplianceStatement` | Réponse du fournisseur | richtext |  | supplierFlowdown |  |
| `supplierDocumentReference` | Référence document fournisseur | string |  | supplierFlowdown |  |
| `softwareItem` | Article logiciel cible | string |  | local |  |
| `selfMonitoring` | Exigence d'autosurveillance | boolean |  | local |  |

### `hardwareRequirement` — Exigence matérielle / HDL / Hardware / HDL requirement

Exigence de matériel électronique, de module ou de composant HDL/FPGA (IEC 60987, IEC 62566).

- Workflow : [`wfRequirement`](A4_workflows.md#wfrequirement)
- Jeux d'attributs hérités : `common`, `requirementCore`, `requirementSafety`, `supplierFlowdown`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `reqCategory` | Catégorie | enum [`reqCategory`](A2_enumerations.md#reqcategory) | `soumission` | requirementCore |  |
| `bindingLevel` | Force | enum [`bindingLevel`](A2_enumerations.md#bindinglevel) |  | requirementCore |  |
| `rationale` | Justification (rationale) | richtext |  | requirementCore |  |
| `acceptanceCriteria` | Critères d'acceptation | richtext |  | requirementCore |  |
| `verificationMethods` | Méthodes de vérification | enum [`verificationMethod`](A2_enumerations.md#verificationmethod) (multi) | `approved` | requirementCore |  |
| `verificationMethodRationale` | Justification du choix de méthode | text |  | requirementCore | Pourquoi essai plutôt qu'analyse, etc. (INCOSE / ISO 29148) ; obligatoire par rapport pour les exigences définies. |
| `vvStagesPlanned` | Étapes V&V prévues | enum [`vvStage`](A2_enumerations.md#vvstage) (multi) |  | requirementCore |  |
| `maturity` | Maturité | enum [`maturity`](A2_enumerations.md#maturity) |  | requirementCore |  |
| `plantStates` | États d'exploitation | enum [`plantState`](A2_enumerations.md#plantstate) (multi) |  | requirementCore |  |
| `plantConditions` | Conditions de fonctionnement | enum [`plantCondition`](A2_enumerations.md#plantcondition) (multi) |  | requirementCore |  |
| `verificationStatus` | Statut de vérification (calculé) | enum [`vvStatus`](A2_enumerations.md#vvstatus) | calculé | requirementCore |  |
| `customerApprovalRequired` | Accord client requis pour modification | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementCore |  |
| `requirementPattern` | Gabarit de rédaction (EARS) | enum [`requirementPattern`](A2_enumerations.md#requirementpattern) |  | requirementCore |  |
| `requirementQualityScore` | Score qualité de rédaction (calculé) | float | calculé | requirementCore | Contrôles INCOSE GtWR / ISO 29148 (termes ambigus, 'et/ou', passif, unités, verbe prescriptif) par script ou extension ; indicateur, jamais bloquant. |
| `safetyRelevant` | Pertinente pour la sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety |  |
| `definedRequirement` | Exigence définie (EIP) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety | Exigence assignée à un EIP au sens de l'arrêté INB : déclenche le socle non négociable (contrôle technique, traçabilité V&V, gestion d'écart). |
| `protectedInterests` | Intérêts protégés | enum [`protectedInterest`](A2_enumerations.md#protectedinterest) (multi) |  | requirementSafety |  |
| `safetyClassScheme` | Référentiel de classement | enum [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) |  | requirementSafety |  |
| `safetyClass` | Classe de sûreté héritée | enum [`safetyClass`](A2_enumerations.md#safetyclass) |  | requirementSafety | Classe la plus sévère des éléments auxquels l'exigence est allouée (contrôlée par rapport). |
| `functionCategory` | Catégorie de fonction héritée | enum [`functionCategory`](A2_enumerations.md#functioncategory) |  | requirementSafety |  |
| `securityRelevant` | Pertinente cybersécurité | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementSafety |  |
| `supplierComplianceStatus` | Conformité déclarée par le fournisseur | enum [`complianceStatus`](A2_enumerations.md#compliancestatus) |  | supplierFlowdown |  |
| `supplierComplianceStatement` | Réponse du fournisseur | richtext |  | supplierFlowdown |  |
| `supplierDocumentReference` | Référence document fournisseur | string |  | supplierFlowdown |  |
| `hwTechnology` | Technologie | string |  | local | Électronique conventionnelle, microprocesseur, HDL/FPGA, électromécanique. |

### `safetyRequirement` — Exigence de sûreté / Safety requirement

Exigence issue de la démonstration de sûreté (études d'accidents, EPS, agressions, règles de classement, défense en profondeur). Portée par la discipline Sûreté ; allouée aux fonctions et SSC.

- Workflow : [`wfRequirement`](A4_workflows.md#wfrequirement)
- Jeux d'attributs hérités : `common`, `requirementCore`, `requirementSafety`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `reqCategory` | Catégorie | enum [`reqCategory`](A2_enumerations.md#reqcategory) | `soumission` | requirementCore |  |
| `bindingLevel` | Force | enum [`bindingLevel`](A2_enumerations.md#bindinglevel) |  | requirementCore |  |
| `rationale` | Justification (rationale) | richtext |  | requirementCore |  |
| `acceptanceCriteria` | Critères d'acceptation | richtext |  | requirementCore |  |
| `verificationMethods` | Méthodes de vérification | enum [`verificationMethod`](A2_enumerations.md#verificationmethod) (multi) | `approved` | requirementCore |  |
| `verificationMethodRationale` | Justification du choix de méthode | text |  | requirementCore | Pourquoi essai plutôt qu'analyse, etc. (INCOSE / ISO 29148) ; obligatoire par rapport pour les exigences définies. |
| `vvStagesPlanned` | Étapes V&V prévues | enum [`vvStage`](A2_enumerations.md#vvstage) (multi) |  | requirementCore |  |
| `maturity` | Maturité | enum [`maturity`](A2_enumerations.md#maturity) |  | requirementCore |  |
| `plantStates` | États d'exploitation | enum [`plantState`](A2_enumerations.md#plantstate) (multi) |  | requirementCore |  |
| `plantConditions` | Conditions de fonctionnement | enum [`plantCondition`](A2_enumerations.md#plantcondition) (multi) |  | requirementCore |  |
| `verificationStatus` | Statut de vérification (calculé) | enum [`vvStatus`](A2_enumerations.md#vvstatus) | calculé | requirementCore |  |
| `customerApprovalRequired` | Accord client requis pour modification | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementCore |  |
| `requirementPattern` | Gabarit de rédaction (EARS) | enum [`requirementPattern`](A2_enumerations.md#requirementpattern) |  | requirementCore |  |
| `requirementQualityScore` | Score qualité de rédaction (calculé) | float | calculé | requirementCore | Contrôles INCOSE GtWR / ISO 29148 (termes ambigus, 'et/ou', passif, unités, verbe prescriptif) par script ou extension ; indicateur, jamais bloquant. |
| `safetyRelevant` | Pertinente pour la sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety |  |
| `definedRequirement` | Exigence définie (EIP) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | requirementSafety | Exigence assignée à un EIP au sens de l'arrêté INB : déclenche le socle non négociable (contrôle technique, traçabilité V&V, gestion d'écart). |
| `protectedInterests` | Intérêts protégés | enum [`protectedInterest`](A2_enumerations.md#protectedinterest) (multi) |  | requirementSafety |  |
| `safetyClassScheme` | Référentiel de classement | enum [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) |  | requirementSafety |  |
| `safetyClass` | Classe de sûreté héritée | enum [`safetyClass`](A2_enumerations.md#safetyclass) |  | requirementSafety | Classe la plus sévère des éléments auxquels l'exigence est allouée (contrôlée par rapport). |
| `functionCategory` | Catégorie de fonction héritée | enum [`functionCategory`](A2_enumerations.md#functioncategory) |  | requirementSafety |  |
| `securityRelevant` | Pertinente cybersécurité | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | requirementSafety |  |
| `safetyRequirementSource` | Origine | enum [`safetyRequirementSource`](A2_enumerations.md#safetyrequirementsource) | `soumission` | local |  |
| `defenceInDepthLevel` | Niveaux de défense en profondeur | enum [`defenceInDepthLevel`](A2_enumerations.md#defenceindepthlevel) (multi) |  | local |  |
| `singleFailureApplicable` | Critère de défaillance unique applicable | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `analysisReference` | Référence de l'étude support | string |  | local |  |

### `assumption` — Hypothèse / donnée d'entrée / Assumption / design input

Hypothèse de conception ou donnée d'entrée (site, client, fournisseur, hypothèse d'étude) qui doit être confirmée. Toute modification rend suspects les artefacts qui s'appuient dessus (lien 'assumes').

- Workflow : [`wfAssumption`](A4_workflows.md#wfassumption)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `assumptionType` | Nature | enum [`assumptionType`](A2_enumerations.md#assumptiontype) | `soumission` | local |  |
| `dataOwner` | Détenteur de la donnée | string |  | local |  |
| `validationMethod` | Mode de confirmation | richtext |  | local |  |
| `consequenceIfInvalid` | Conséquence si infirmée | richtext |  | local |  |
| `confirmationDueDate` | Échéance de confirmation | date |  | local |  |
| `safetyRelevant` | Pertinente pour la sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |

## Famille : Architecture (RFLP)

### `operationalScenario` — Scénario opérationnel / Operational scenario

Cas d'utilisation / séquence d'exploitation, d'intervention ou de manutention (ConOps).

- Workflow : [`wfArchitecture`](A4_workflows.md#wfarchitecture)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `scenarioType` | Type | enum [`scenarioType`](A2_enumerations.md#scenariotype) | `soumission` | local |  |
| `plantStates` | États d'exploitation | enum [`plantState`](A2_enumerations.md#plantstate) (multi) |  | local |  |
| `actors` | Acteurs | richtext |  | local |  |
| `preconditions` | Préconditions | richtext |  | local |  |
| `estimatedDuration` | Durée estimée | duration |  | local |  |
| `doseEstimate` | Dose collective prévisionnelle (H.mSv) | float |  | local |  |

### `function` — Fonction / Function

Élément de l'architecture fonctionnelle (R-F-L-P), hiérarchisé par lien parent.

- Workflow : [`wfArchitecture`](A4_workflows.md#wfarchitecture)
- Jeux d'attributs hérités : `common`, `functionSafety`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `safetyClassScheme` | Référentiel de classement | enum [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) |  | functionSafety |  |
| `functionCategory` | Catégorie de fonction | enum [`functionCategory`](A2_enumerations.md#functioncategory) | oui | functionSafety |  |
| `fundamentalSafetyFunction` | Fonction fondamentale de sûreté | enum [`fundamentalSafetyFunction`](A2_enumerations.md#fundamentalsafetyfunction) |  | functionSafety |  |
| `defenceInDepthLevel` | Niveaux de défense en profondeur | enum [`defenceInDepthLevel`](A2_enumerations.md#defenceindepthlevel) (multi) |  | functionSafety |  |
| `protectedInterests` | Intérêts protégés | enum [`protectedInterest`](A2_enumerations.md#protectedinterest) (multi) |  | functionSafety |  |
| `plantStates` | États d'exploitation | enum [`plantState`](A2_enumerations.md#plantstate) (multi) |  | functionSafety |  |
| `plantConditions` | Conditions de fonctionnement | enum [`plantCondition`](A2_enumerations.md#plantcondition) (multi) |  | functionSafety |  |
| `securityDegree` | Degré de sécurité cyber | enum [`securityDegree`](A2_enumerations.md#securitydegree) |  | functionSafety |  |
| `categorisationRationale` | Justification de la catégorisation | richtext |  | functionSafety |  |
| `functionLevel` | Niveau | enum [`functionLevel`](A2_enumerations.md#functionlevel) | `soumission` | local |  |
| `functionType` | Type | enum [`functionType`](A2_enumerations.md#functiontype) | `soumission` | local |  |
| `performanceSummary` | Performances attendues | richtext |  | local |  |
| `modelElementId` | ID élément de modèle (MBSE) | string |  | local | UUID Capella / SysML si synchronisé. |

### `logicalComponent` — Élément logique / Logical component

Système élémentaire, train/division, système C-C ou module logique indépendant de la technologie.

- Workflow : [`wfArchitecture`](A4_workflows.md#wfarchitecture)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `logicalType` | Type | enum [`logicalType`](A2_enumerations.md#logicaltype) | `soumission` | local |  |
| `systemCode` | Code système (trigramme / KKS) | string |  | local |  |
| `functionCategory` | Catégorie de fonction la plus élevée | enum [`functionCategory`](A2_enumerations.md#functioncategory) |  | local |  |
| `icSystemClass` | Classe système C-C | enum [`icSystemClass`](A2_enumerations.md#icsystemclass) |  | local |  |
| `modelElementId` | ID élément de modèle (MBSE) | string |  | local |  |

### `physicalComponent` — Élément physique (SSC) / Physical component (SSC)

Proxy ALM d'un élément du PBS : bâtiment, système, équipement, composant, article logiciel, outillage, assemblage combustible. La nomenclature maître reste dans le PLM ; l'ALM porte classement, exigences et V&V.

- Workflow : [`wfArchitecture`](A4_workflows.md#wfarchitecture)
- Jeux d'attributs hérités : `common`, `sscClassification`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `safetyClassScheme` | Référentiel de classement | enum [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) | `soumission` | sscClassification |  |
| `safetyClass` | Classe de sûreté | enum [`safetyClass`](A2_enumerations.md#safetyclass) |  | sscClassification |  |
| `eip` | EIP (élément important pour la protection) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | sscClassification |  |
| `protectedInterests` | Intérêts protégés | enum [`protectedInterest`](A2_enumerations.md#protectedinterest) (multi) |  | sscClassification |  |
| `ipsLegacy` | IPS (terminologie parc historique) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | sscClassification |  |
| `itns` | ITNS (ISO 19443) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | sscClassification |  |
| `qaProgramLevel` | Programme qualité | enum [`qaProgramLevel`](A2_enumerations.md#qaprogramlevel) |  | sscClassification |  |
| `mechanicalClass` | Classe mécanique | enum [`mechanicalClass`](A2_enumerations.md#mechanicalclass) |  | sscClassification |  |
| `electricalClass` | Classe électrique | enum [`electricalClass`](A2_enumerations.md#electricalclass) |  | sscClassification |  |
| `qualificationClass` | Classe de qualification | enum [`qualificationClass`](A2_enumerations.md#qualificationclass) |  | sscClassification |  |
| `seismicCategory` | Catégorie sismique | enum [`seismicCategory`](A2_enumerations.md#seismiccategory) |  | sscClassification |  |
| `seismicCriterion` | Exigence sismique | enum [`seismicCriterion`](A2_enumerations.md#seismiccriterion) |  | sscClassification |  |
| `espnLevel` | Niveau ESPN | enum [`espnLevel`](A2_enumerations.md#espnlevel) |  | sscClassification |  |
| `espnCategory` | Catégorie ESP | enum [`espnCategory`](A2_enumerations.md#espncategory) |  | sscClassification |  |
| `icSystemClass` | Classe système C-C | enum [`icSystemClass`](A2_enumerations.md#icsystemclass) |  | sscClassification |  |
| `securityDegree` | Degré de sécurité cyber | enum [`securityDegree`](A2_enumerations.md#securitydegree) |  | sscClassification |  |
| `classificationRationale` | Justification du classement | richtext |  | sscClassification |  |
| `classificationValidated` | Classement validé par la Sûreté | boolean |  | sscClassification |  |
| `componentNature` | Nature | enum [`componentNature`](A2_enumerations.md#componentnature) | `soumission` | local |  |
| `pbsLevel` | Niveau PBS | enum [`pbsLevel`](A2_enumerations.md#pbslevel) |  | local |  |
| `functionalTag` | Repère fonctionnel (KKS / ECS) | string |  | local |  |
| `plmItemId` | Identifiant PLM | string |  | local |  |
| `plmRevision` | Révision PLM | string |  | local |  |
| `serialNumber` | N° de série (exemplaire) | string |  | local | Pour les exemplaires suivis individuellement (outillages, composants livrés). |
| `plantLocation` | Bâtiment / local | string |  | local |  |
| `supplier` | Fournisseur / fabricant | string |  | local |  |
| `isConfigurationItem` | Article de configuration | boolean |  | local |  |
| `qualificationStatus` | Statut de qualification | enum [`qualificationStatus`](A2_enumerations.md#qualificationstatus) |  | local |  |
| `designLifeYears` | Durée de vie de conception (ans) | integer |  | local |  |
| `ageingMechanisms` | Mécanismes de vieillissement | enum [`ageingMechanism`](A2_enumerations.md#ageingmechanism) (multi) |  | local |  |
| `modelElementId` | ID élément de modèle (MBSE) | string |  | local |  |
| `commercialGradeDedication` | Article commercial à dédicacer (CGD) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `criticalCharacteristics` | Caractéristiques critiques (CGD / équivalence) | richtext |  | local |  |
| `expectedWasteClass` | Catégorie de déchet prévisionnelle | enum [`wasteClass`](A2_enumerations.md#wasteclass) |  | local |  |

### `interface` — Interface / Interface

Entrée du registre d'interfaces (ICD) entre deux éléments (côté A / côté B). Les liens Polarion ne portant pas d'attributs, les données échangées sont portées par l'interface elle-même.

- Workflow : [`wfInterface`](A4_workflows.md#wfinterface)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `interfaceType` | Type(s) | enum [`interfaceType`](A2_enumerations.md#interfacetype) (multi) | `soumission` | local |  |
| `interfaceScope` | Portée | enum [`interfaceScope`](A2_enumerations.md#interfacescope) | `soumission` | local |  |
| `sideAOwner` | Responsable côté A | string |  | local |  |
| `sideBOwner` | Responsable côté B | string |  | local |  |
| `interfaceData` | Données échangées (charges, signaux, débits...) | richtext |  | local |  |
| `icdReference` | Référence ICD | string |  | local |  |
| `contractualInterface` | Interface contractuelle | boolean |  | local |  |
| `maturity` | Maturité | enum [`maturity`](A2_enumerations.md#maturity) |  | local |  |
| `freezeDate` | Date de gel visée | date |  | local |  |
| `verificationMethods` | Méthodes de vérification de l'interface | enum [`verificationMethod`](A2_enumerations.md#verificationmethod) (multi) |  | local |  |
| `interfaceVerificationCriteria` | Critères de vérification de l'interface | richtext |  | local |  |

### `designParameter` — Paramètre de conception / Design parameter

Grandeur suivie (TPM, limite de sûreté, seuil, marge, budget, paramètre de cœur par cycle). Permet le suivi des marges et des budgets.

- Workflow : [`wfArchitecture`](A4_workflows.md#wfarchitecture)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `designParameterType` | Type | enum [`designParameterType`](A2_enumerations.md#designparametertype) | `soumission` | local |  |
| `unit` | Unité | string |  | local |  |
| `nominalValue` | Valeur nominale | float |  | local |  |
| `minValue` | Valeur min. | float |  | local |  |
| `maxValue` | Valeur max. | float |  | local |  |
| `limitValue` | Valeur limite / critère | float |  | local |  |
| `calculatedValue` | Valeur calculée | float |  | local |  |
| `margin` | Marge (calculée) | float | calculé | local |  |
| `uncertainty` | Incertitude | string |  | local |  |
| `cycleOrConfiguration` | Cycle / configuration | string |  | local |  |
| `calculationCode` | Code de calcul | string |  | local |  |

### `designDecision` — Décision de conception / Design decision

Décision d'architecture / trade-off tracée (options, critères, justification) – registre de décisions.

- Workflow : [`wfDecision`](A4_workflows.md#wfdecision)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `alternatives` | Options étudiées | richtext |  | local |  |
| `selectionCriteria` | Critères de choix | richtext |  | local |  |
| `decisionRationale` | Justification | richtext | `decided` | local |  |
| `decisionAuthority` | Instance de décision | string |  | local |  |
| `decisionDate` | Date de décision | date |  | local |  |
| `reversible` | Décision réversible | boolean |  | local |  |

## Famille : Sûreté, risques, analyses

### `hazard` — Agression / événement initiateur / Hazard / initiating event

Événement initiateur postulé, agression interne/externe, danger machine ou radiologique.

- Workflow : [`wfSafetyAnalysisItem`](A4_workflows.md#wfsafetyanalysisitem)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `hazardType` | Type | enum [`hazardType`](A2_enumerations.md#hazardtype) | `soumission` | local |  |
| `plantConditions` | Condition de fonctionnement | enum [`plantCondition`](A2_enumerations.md#plantcondition) (multi) |  | local |  |
| `plantStates` | États d'exploitation concernés | enum [`plantState`](A2_enumerations.md#plantstate) (multi) |  | local |  |
| `frequencyBand` | Bande de fréquence | enum [`initiatingEventFrequency`](A2_enumerations.md#initiatingeventfrequency) |  | local |  |
| `screening` | Criblage | enum [`hazardScreening`](A2_enumerations.md#hazardscreening) |  | local |  |
| `consequences` | Conséquences | richtext |  | local |  |
| `decouplingCriteria` | Critères de découplage / radiologiques | richtext |  | local |  |

### `safetyClaim` — Revendication de sûreté (argumentaire) / Safety claim (argument)

Élément d'argumentaire Claims-Arguments-Evidence / GSN structurant la démonstration de sûreté (attendu notamment au Royaume-Uni, utile partout).

- Workflow : [`wfSafetyAnalysisItem`](A4_workflows.md#wfsafetyanalysisitem)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `gsnElementType` | Élément | enum [`gsnElementType`](A2_enumerations.md#gsnelementtype) | oui | local |  |
| `claimLevel` | Niveau dans l'arborescence | integer |  | local |  |
| `confidence` | Confiance | enum [`confidenceLevel`](A2_enumerations.md#confidencelevel) |  | local |  |
| `context` | Contexte / hypothèses | richtext |  | local |  |
| `evidenceCoverage` | Couverture par preuves (%) | float | calculé | local |  |

### `risk` — Risque / opportunité / Risk / opportunity

Risque projet ou technique (ISO 31000) ; les risques de sûreté de l'installation relèvent de 'hazard'.

- Workflow : [`wfRisk`](A4_workflows.md#wfrisk)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `riskCategory` | Catégorie | enum [`riskCategory`](A2_enumerations.md#riskcategory) | oui | local |  |
| `isOpportunity` | Opportunité | boolean |  | local |  |
| `probability` | Probabilité (1-5) | integer | oui | local |  |
| `impact` | Impact (1-5) | integer | oui | local |  |
| `criticality` | Criticité (P×I) | integer | calculé | local |  |
| `riskLevel` | Niveau | enum [`riskLevel`](A2_enumerations.md#risklevel) | calculé | local |  |
| `riskStrategy` | Stratégie | enum [`riskStrategy`](A2_enumerations.md#riskstrategy) |  | local |  |
| `residualProbability` | Probabilité résiduelle | integer |  | local |  |
| `residualImpact` | Impact résiduel | integer |  | local |  |
| `exposureCost` | Exposition financière | currency |  | local |  |
| `triggerDate` | Date de déclenchement | date |  | local |  |
| `riskOwner` | Propriétaire | user |  | local |  |

### `fmeaItem` — Ligne d'AMDEC (mode de défaillance) / FMEA line (failure mode)

Mode de défaillance analysé (édition tabulaire recommandée via extension type Risksheet).

- Workflow : [`wfSafetyAnalysisItem`](A4_workflows.md#wfsafetyanalysisitem)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `fmeaType` | Type d'AMDEC | enum [`fmeaType`](A2_enumerations.md#fmeatype) | `soumission` | local |  |
| `analysedFunction` | Fonction / étape analysée | richtext |  | local |  |
| `failureMode` | Mode de défaillance | richtext | `soumission` | local |  |
| `localEffect` | Effet local | richtext |  | local |  |
| `systemEffect` | Effet système / installation | richtext |  | local |  |
| `failureCause` | Cause | richtext |  | local |  |
| `severityRating` | Gravité G (1-10) | integer |  | local |  |
| `occurrenceRating` | Occurrence O (1-10) | integer |  | local |  |
| `detectionRating` | Détection D (1-10) | integer |  | local |  |
| `rpn` | Criticité (G×O×D) | integer | calculé | local |  |
| `actionPriority` | Priorité d'action | enum [`actionPriority`](A2_enumerations.md#actionpriority) |  | local |  |
| `detectionMeans` | Moyens de détection | richtext |  | local |  |
| `revisedSeverity` | G après actions | integer |  | local |  |
| `revisedOccurrence` | O après actions | integer |  | local |  |
| `revisedDetection` | D après actions | integer |  | local |  |

### `analysis` — Analyse / étude / calcul / Analysis / study / calculation

Étude d'ingénierie identifiée (étude d'accident, note de calcul, analyse sismique, études de cœur, FOH, dosimétrie...). Produit d'une AIP en général : contrôle technique indépendant obligatoire.

- Workflow : [`wfAnalysis`](A4_workflows.md#wfanalysis)
- Jeux d'attributs hérités : `common`, `documentReference`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `documentNumber` | N° de document | string |  | documentReference |  |
| `revisionIndex` | Indice | string |  | documentReference |  |
| `customerDocumentNumber` | N° document client | string |  | documentReference |  |
| `aip` | Produit d'une AIP | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | documentReference | Activité importante pour la protection → contrôle technique indépendant obligatoire. |
| `requiredHabilitation` | Habilitation requise du vérificateur / approbateur | enum [`habilitationDomain`](A2_enumerations.md#habilitationdomain) |  | documentReference | Contrôlée par la condition qualifiedSignatory lorsque le projet a choisi la politique de signature 'habilitationBased' (model/project_setup.yaml). |
| `analysisType` | Type | enum [`analysisType`](A2_enumerations.md#analysistype) | `soumission` | local |  |
| `calculationCode` | Code / outil de calcul | string |  | local |  |
| `codeVersion` | Version du code | string |  | local |  |
| `codeQualification` | Statut du code | enum [`codeQualification`](A2_enumerations.md#codequalification) |  | local |  |
| `codeQualificationRationale` | Justification de l'emploi d'un code non qualifié | richtext |  | local | Obligatoire pour approuver une analyse dont le code n'est pas qualifié (condition de wfAnalysis.approve). |
| `inputDataSummary` | Données d'entrée | richtext |  | local |  |
| `conclusion` | Conclusion | richtext |  | local |  |
| `analysisResult` | Résultat | enum [`analysisResult`](A2_enumerations.md#analysisresult) |  | local |  |
| `minimumMargin` | Marge minimale obtenue | string |  | local |  |
| `ageingMechanisms` | Mécanismes de vieillissement traités | enum [`ageingMechanism`](A2_enumerations.md#ageingmechanism) (multi) |  | local |  |

### `regulatoryCommitment` — Engagement / demande de l'autorité / Regulatory commitment / request

Demande d'une autorité (prescription, lettre de suite, instruction) ou engagement pris dans un dossier, suivi jusqu'à la clôture.

- Workflow : [`wfCommitment`](A4_workflows.md#wfcommitment)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `authority` | Autorité / émetteur | enum [`authority`](A2_enumerations.md#authority) | oui | local |  |
| `commitmentSource` | Origine | enum [`commitmentSource`](A2_enumerations.md#commitmentsource) | oui | local |  |
| `requestCategory` | Nature | enum [`requestCategory`](A2_enumerations.md#requestcategory) |  | local |  |
| `authorityReference` | Référence du courrier / décision | string | oui | local |  |
| `requestText` | Texte de la demande | richtext |  | local |  |
| `commitmentText` | Réponse / engagement | richtext |  | local |  |
| `commitmentDueDate` | Échéance | date | oui | local |  |
| `responseReference` | Référence de la réponse | string |  | local |  |
| `licensee` | Exploitant concerné | string |  | local |  |
| `regulatoryFramework` | Cadre réglementaire (pack) | enum [`regulatoryFramework`](A2_enumerations.md#regulatoryframework) |  | local |  |

## Famille : Vérification & validation

### `verificationCase` — Cas de vérification / validation / Verification / validation case

Cas V&V unique pour toutes les méthodes (essai, analyse, inspection, revue...). Exécuté et enregistré via les Test Runs Polarion (campagnes), y compris pour les méthodes non 'essai' (enregistrement + preuve).

- Workflow : [`wfVerificationCase`](A4_workflows.md#wfverificationcase)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `verificationMethod` | Méthode | enum [`verificationMethod`](A2_enumerations.md#verificationmethod) | `soumission` | local |  |
| `vvType` | Nature | enum [`vvType`](A2_enumerations.md#vvtype) |  | local |  |
| `vvStage` | Étape | enum [`vvStage`](A2_enumerations.md#vvstage) | `soumission` | local |  |
| `vvLevel` | Niveau | enum [`reqLevel`](A2_enumerations.md#reqlevel) |  | local |  |
| `acceptanceCriteria` | Critères d'acceptation | richtext | `soumission` | local |  |
| `preconditions` | Préconditions / configuration | richtext |  | local |  |
| `testSteps` | Étapes | testSteps |  | local |  |
| `testEnvironment` | Environnement | enum [`testEnvironment`](A2_enumerations.md#testenvironment) |  | local |  |
| `procedureReference` | Procédure / mode opératoire | string |  | local |  |
| `inspectionPoint` | Point d'inspection | enum [`inspectionPoint`](A2_enumerations.md#inspectionpoint) |  | local |  |
| `witnessParties` | Parties convoquées | enum [`witnessParty`](A2_enumerations.md#witnessparty) (multi) |  | local |  |
| `independenceLevel` | Indépendance requise | enum [`independenceLevel`](A2_enumerations.md#independencelevel) |  | local |  |
| `qualificationStandard` | Norme de qualification | string |  | local | Ex. IEC/IEEE 60780-323, IEC/IEEE 60980-344, IEC 62003. |
| `evidenceReference` | Référence de la preuve (PV, note) | string |  | local |  |
| `estimatedDuration` | Durée estimée | duration |  | local |  |
| `regressionRequired` | À rejouer en non-régression | boolean |  | local |  |
| `requiredHabilitation` | Habilitation requise du vérificateur / approbateur | enum [`habilitationDomain`](A2_enumerations.md#habilitationdomain) |  | local |  |
| `lastResult` | Dernier résultat (calculé) | enum [`testResult`](A2_enumerations.md#testresult) | calculé | local |  |

### `anomaly` — Fiche d'anomalie (V&V) / Anomaly report (V&V)

Anomalie détectée en V&V (logiciel, matériel, spécification d'essai). Les écarts produit relèvent de nonConformance.

- Workflow : [`wfAnomaly`](A4_workflows.md#wfanomaly)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `anomalyType` | Type | enum [`anomalyType`](A2_enumerations.md#anomalytype) | `soumission` | local |  |
| `detectedIn` | Détectée en | enum [`vvStage`](A2_enumerations.md#vvstage) |  | local |  |
| `configurationVersion` | Version / configuration testée | string |  | local |  |
| `reproducibility` | Reproductibilité | string |  | local |  |
| `safetyImpact` | Impact sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | local |  |
| `fixVersion` | Version corrective | string |  | local |  |
| `rootCauseCategory` | Cause racine | enum [`rootCauseCategory`](A2_enumerations.md#rootcausecategory) |  | local |  |

## Famille : Modifications, écarts, fortuits

### `changeRequest` — Demande de modification / Change request

Demande de modification d'une référence approuvée (exigences, architecture, documents, produit). Analyse d'impact outillée par les liens 'impacts' et décision en CCB tracée et signée.

- Workflow : [`wfChangeRequest`](A4_workflows.md#wfchangerequest)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `changeOrigin` | Origine | enum [`changeOrigin`](A2_enumerations.md#changeorigin) | oui | local |  |
| `changeClass` | Classe | enum [`changeClass`](A2_enumerations.md#changeclass) | oui | local |  |
| `regulatoryModificationClass` | Classement réglementaire | enum [`regulatoryModificationClass`](A2_enumerations.md#regulatorymodificationclass) |  | local |  |
| `changeJustification` | Justification | richtext | oui | local |  |
| `impactAnalysis` | Analyse d'impact | richtext | `ccbReview` | local |  |
| `impactedDisciplines` | Disciplines impactées | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | local |  |
| `safetyImpact` | Impact sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | local |  |
| `affectsEip` | Affecte un EIP / exigence définie | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `impactedBaselines` | Références impactées (baselines) | string |  | local |  |
| `costEstimate` | Estimation de coût | currency |  | local |  |
| `scheduleImpact` | Impact planning | richtext |  | local |  |
| `effectivity` | Effectivité (tranches, numéros de série, à partir du cycle...) | string |  | local |  |
| `urgency` | Urgence | enum [`urgency`](A2_enumerations.md#urgency) |  | local |  |
| `ccbDecision` | Décision CCB | enum [`ccbDecision`](A2_enumerations.md#ccbdecision) |  | local |  |
| `ccbDate` | Date CCB | date |  | local |  |
| `ccbReference` | Référence du relevé de décision | string |  | local |  |
| `customerApprovalRequired` | Accord client requis | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `customerApprovalReference` | Référence accord client | string |  | local |  |
| `safetyReportImpact` | Impact sur le rapport de sûreté (RDS / FSAR) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `cfr5059Screening` | 10 CFR 50.59 – criblage (pack US) | enum [`cfr5059Screening`](A2_enumerations.md#cfr5059screening) |  | local |  |
| `cfr5059Outcome` | 10 CFR 50.59 – conclusion de l'évaluation | enum [`cfr5059Outcome`](A2_enumerations.md#cfr5059outcome) |  | local |  |
| `cfr5059Reference` | Référence du criblage / de l'évaluation 50.59 | string |  | local |  |

### `nonConformance` — Écart / fiche de non-conformité (FNC) / Non-conformance report (NCR)

Écart à une exigence définie, à une spécification ou à un référentiel, détecté en conception, fabrication, montage ou exploitation. Traitement proportionné aux enjeux, analyse de l'impact sur les EIP, actions CAPA.

- Workflow : [`wfNonConformance`](A4_workflows.md#wfnonconformance)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `ncOrigin` | Origine | enum [`ncOrigin`](A2_enumerations.md#ncorigin) | oui | local |  |
| `ncDetectionPhase` | Phase de détection | enum [`ncDetectionPhase`](A2_enumerations.md#ncdetectionphase) | oui | local |  |
| `ncSeverity` | Gravité | enum [`ncSeverity`](A2_enumerations.md#ncseverity) | oui | local |  |
| `affectsEip` | Affecte un EIP / exigence définie | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | local |  |
| `importantDeviation` | Écart important (au sens du référentiel) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `requirementViolated` | Exigence / référentiel non respecté | richtext |  | local |  |
| `quantityAffected` | Quantité concernée | integer |  | local |  |
| `serialNumbers` | N° de série / lots | string |  | local |  |
| `supplier` | Fournisseur | string |  | local |  |
| `containmentAction` | Action conservatoire | richtext |  | local |  |
| `ncDisposition` | Traitement proposé | enum [`ncDisposition`](A2_enumerations.md#ncdisposition) |  | local |  |
| `dispositionJustification` | Justification du traitement | richtext | `dispositionProposed` | local |  |
| `customerApprovalRequired` | Accord client requis | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `customerDecisionReference` | Référence décision client | string |  | local |  |
| `authorityNotificationRequired` | Information autorité / organisme requise | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `authorityReference` | Référence autorité / organisme | string |  | local |  |
| `significantEventType` | Événement significatif (exploitant) | enum [`significantEventType`](A2_enumerations.md#significanteventtype) |  | local |  |
| `cfsiSuspected` | Suspicion CFSI | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | local |  |
| `part21Evaluation` | Évaluation 10 CFR 21 requise (US) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `rootCauseCategory` | Cause racine | enum [`rootCauseCategory`](A2_enumerations.md#rootcausecategory) |  | local |  |
| `rootCauseDescription` | Analyse de cause | richtext |  | local |  |
| `costOfNonQuality` | Coût de non-qualité | currency |  | local |  |

### `waiver` — Dérogation / concession / Waiver / concession

Autorisation formelle de s'écarter d'une exigence (avant réalisation) ou d'accepter un produit non conforme (après).

- Workflow : [`wfWaiver`](A4_workflows.md#wfwaiver)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `waiverType` | Type | enum [`waiverType`](A2_enumerations.md#waivertype) | oui | local |  |
| `waiverJustification` | Justification technique | richtext | oui | local |  |
| `affectsEip` | Affecte un EIP / exigence définie | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | local |  |
| `effectivity` | Portée (tranches, séries, durée) | string |  | local |  |
| `expiryDate` | Date d'expiration | date |  | local |  |
| `customerApprovalReference` | Référence accord client | string |  | local |  |
| `authorityApprovalReference` | Référence accord autorité / organisme | string |  | local |  |

### `technicalIssue` — Problème technique / fortuit / Technical issue / emergent issue

Point d'entrée des affaires à cycle court (fortuit en arrêt de tranche, indication ISI, problème générique palier, question client). Workflow express mais socle non négociable conservé.

- Workflow : [`wfTechnicalIssue`](A4_workflows.md#wftechnicalissue)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `issueCategory` | Catégorie | enum [`issueCategory`](A2_enumerations.md#issuecategory) | oui | local |  |
| `urgency` | Urgence | enum [`urgency`](A2_enumerations.md#urgency) | oui | local |  |
| `site` | Site | enum [`frenchSite`](A2_enumerations.md#frenchsite) |  | local |  |
| `affectedUnit` | Tranche concernée | enum [`plantUnit`](A2_enumerations.md#plantunit) |  | local |  |
| `outageType` | Type d'arrêt | enum [`outageType`](A2_enumerations.md#outagetype) |  | local |  |
| `outageCriticalPath` | Sur le chemin critique de l'arrêt | boolean |  | local |  |
| `customerRequestReference` | Référence demande client | string |  | local |  |
| `detectedOn` | Date de détection | date |  | local |  |
| `responseDueDate` | Échéance de réponse | datetime |  | local |  |
| `solutionType` | Type de solution | enum [`solutionType`](A2_enumerations.md#solutiontype) |  | local |  |
| `safetyImpact` | Impact sûreté | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui | local |  |
| `affectsEip` | Affecte un EIP | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `espnImpact` | Concerne un ESPN | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `genericImpact` | Caractère générique (palier / flotte) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `lessonsLearnedCaptured` | REX capitalisé | boolean |  | local |  |

## Famille : Projet, livrables, revues

### `deliverable` — Livrable / document / Deliverable / document

Référence d'un document (GED = système d'archivage de référence) ou d'un document produit depuis un LiveDoc. Porte le cycle de visa client.

- Workflow : [`wfDeliverable`](A4_workflows.md#wfdeliverable)
- Jeux d'attributs hérités : `common`, `documentReference`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `documentNumber` | N° de document | string |  | documentReference |  |
| `revisionIndex` | Indice | string |  | documentReference |  |
| `customerDocumentNumber` | N° document client | string |  | documentReference |  |
| `aip` | Produit d'une AIP | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | documentReference | Activité importante pour la protection → contrôle technique indépendant obligatoire. |
| `requiredHabilitation` | Habilitation requise du vérificateur / approbateur | enum [`habilitationDomain`](A2_enumerations.md#habilitationdomain) |  | documentReference | Contrôlée par la condition qualifiedSignatory lorsque le projet a choisi la politique de signature 'habilitationBased' (model/project_setup.yaml). |
| `deliverableType` | Type | enum [`deliverableType`](A2_enumerations.md#deliverabletype) | `soumission` | local |  |
| `customerVisa` | Visa client | enum [`customerVisa`](A2_enumerations.md#customervisa) |  | local |  |
| `contractualDueDate` | Date contractuelle | date |  | local |  |
| `forecastDate` | Date prévisionnelle | date |  | local |  |
| `docAuthor` | Rédacteur | user |  | local |  |
| `docVerifier` | Vérificateur | user |  | local |  |
| `docApprover` | Approbateur | user |  | local |  |
| `language` | Langue | enum [`language`](A2_enumerations.md#language) |  | local |  |
| `liveDocPath` | LiveDoc source (chemin) | string |  | local |  |
| `sdrlReference` | Ligne SDRL / liste des documents contractuels | string |  | local |  |
| `submittalPurpose` | Objet de la transmission | enum [`submittalPurpose`](A2_enumerations.md#submittalpurpose) |  | local |  |

### `review` — Revue / jalon / Review / gate

Revue formelle (SRR, PDR, CDR, TRR, revue de sûreté...) ou jalon de décision.

- Workflow : [`wfReview`](A4_workflows.md#wfreview)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `reviewType` | Type | enum [`reviewType`](A2_enumerations.md#reviewtype) | oui | local |  |
| `reviewDate` | Date | date | oui | local |  |
| `reviewScope` | Périmètre et documents d'entrée | richtext |  | local |  |
| `entryCriteria` | Critères d'entrée | richtext |  | local |  |
| `exitCriteria` | Critères de sortie | richtext |  | local |  |
| `participants` | Participants | richtext |  | local |  |
| `reviewDecision` | Décision | enum [`reviewDecision`](A2_enumerations.md#reviewdecision) |  | local |  |
| `minutesReference` | Référence du compte rendu | string |  | local |  |

### `reviewFinding` — Remarque de revue / observation client / Review finding / customer comment

Remarque issue d'une revue ou d'une fiche d'observations client ; levée tracée.

- Workflow : [`wfReviewFinding`](A4_workflows.md#wfreviewfinding)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `findingSeverity` | Gravité | enum [`findingSeverity`](A2_enumerations.md#findingseverity) | `soumission` | local |  |
| `findingOrigin` | Émetteur | enum [`findingOrigin`](A2_enumerations.md#findingorigin) | `soumission` | local |  |
| `documentLocation` | Localisation (§, page) | string |  | local |  |
| `findingResponse` | Réponse | richtext | `answered` | local |  |
| `responseAccepted` | Réponse acceptée par l'émetteur | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |

### `action` — Action / Action

Action (conservatoire, corrective, préventive, de revue, point ouvert, surveillance, mise en œuvre).

- Workflow : [`wfAction`](A4_workflows.md#wfaction)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `actionType` | Type | enum [`actionType`](A2_enumerations.md#actiontype) | oui | local |  |
| `closureEvidence` | Preuve de réalisation | string | `done` | local |  |
| `effectivenessCheck` | Vérification d'efficacité | richtext |  | local |  |

### `workPackage` — Lot de travaux (UO réalisatrice) / Work package (performing unit)

Contrat interne entre le projet (BU, maîtrise d'ouvrage) et une UO réalisatrice (usine, centre d'ingénierie, filiale, partenaire, fournisseur). Porte le périmètre, les données d'entrée, les livrables attendus et les critères de remise. Les artefacts produits sont rattachés au lot par le lien 'inWorkPackage'. Réponse à l'organisation matricielle BU × UO sans multiplier les projets (ajout v0.3).

- Workflow : [`wfWorkPackage`](A4_workflows.md#wfworkpackage)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `workPackageType` | Nature | enum [`workPackageType`](A2_enumerations.md#workpackagetype) | oui | local |  |
| `wpManager` | Responsable de lot (UO) | user |  | local |  |
| `workPackageScope` | Périmètre et données d'entrée | richtext | `agreed` | local |  |
| `handoverCriteria` | Critères de remise / réception | richtext | `agreed` | local |  |
| `internalOrderReference` | Commande interne / OTP | string |  | local |  |
| `budgetHours` | Budget (heures) | float |  | local |  |
| `progressPercent` | Avancement (%) calculé | float | calculé | local | Part des livrables rattachés à l'état définitif / approuvé. |

## Famille : Bibliothèque

### `term` — Terme du glossaire / Glossary term

Terme / acronyme multilingue (FR / EN / DE) – référentiel terminologique commun.

- Workflow : [`wfLibraryItem`](A4_workflows.md#wflibraryitem)
- Jeux d'attributs hérités : —

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `acronym` | Acronyme | string |  | local |  |
| `termFr` | Terme (FR) | string |  | local |  |
| `termEn` | Terme (EN) | string |  | local |  |
| `termDe` | Terme (DE) | string |  | local |  |
| `definitionSource` | Source de la définition | string |  | local |  |
| `deprecatedSynonyms` | Synonymes déconseillés | string |  | local |  |
| `transitionNote` | Motif de la dernière transition | text |  | local |  |

## Famille : Modifications, écarts, fortuits

### `unitDeployment` — Déploiement par tranche / cycle (effectivité) / Unit / cycle deployment (effectivity)

Enregistrement de l'application d'une modification, d'une prescription, d'une solution générique ou d'un dossier de recharge sur UNE tranche (et un cycle / un arrêt). Les liens Polarion ne portant pas d'attributs, le statut par tranche ne peut pas être porté par le seul champ applicableUnits : un enregistrement enfant par tranche est nécessaire (palier de 20 à 32 tranches déployé sur 10 ans, 6 tranches EPR2, recharges tranche × cycle, outillage engagé sur un site).

- Workflow : [`wfUnitDeployment`](A4_workflows.md#wfunitdeployment)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `deploymentUnit` | Tranche | enum [`plantUnit`](A2_enumerations.md#plantunit) | oui | local |  |
| `deploymentSite` | Site | enum [`frenchSite`](A2_enumerations.md#frenchsite) |  | local |  |
| `cycleNumber` | Cycle (recharge) | string |  | local |  |
| `outageType` | Type d'arrêt | enum [`outageType`](A2_enumerations.md#outagetype) |  | local |  |
| `outageReference` | Référence de l'arrêt (ex. VD4 2028) | string |  | local |  |
| `plannedDate` | Date prévue | date |  | local |  |
| `actualDate` | Date de réalisation | date |  | local |  |
| `deviationsNoted` | Écarts constatés au déploiement | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `deploymentNotes` | Constats / adaptations locales | richtext |  | local |  |

## Famille : Projet, livrables, revues

### `lessonLearned` — Fiche REX (retour d'expérience) / Lesson learned (OE)

Capitalisation d'un retour d'expérience (fortuit, écart, anomalie, revue, intervention, REX externe) réutilisable entre projets et BU. Publiée dans LIB-PROCESS (requête transverse) ; la REX générique peut déclencher une évolution de bibliothèque ou de gabarit.

- Workflow : [`wfLessonLearned`](A4_workflows.md#wflessonlearned)
- Jeux d'attributs hérités : `common`

| Attribut (id) | Libellé | Type | Oblig. | Origine | Règle / définition |
|---|---|---|---|---|---|
| `discipline` | Discipline pilote | enum [`discipline`](A2_enumerations.md#discipline) | `soumission` | common |  |
| `contributingDisciplines` | Disciplines contributrices | enum [`discipline`](A2_enumerations.md#discipline) (multi) |  | common |  |
| `externalId` | Identifiant externe | string |  | common | ID dans le document source, chez le client (ReqIF) ou dans l'outil hérité (migration). |
| `sourceReference` | Référence source | string |  | common | Document / révision / paragraphe d'origine. |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  | common |  |
| `applicableUnits` | Tranches applicables | enum [`plantUnit`](A2_enumerations.md#plantunit) (multi) |  | common | Énumération surchargée au niveau projet. |
| `applicabilityCondition` | Condition d'applicabilité | text |  | common | Règle de variante en clair (ou expression du modèle de variabilité). |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  | common |  |
| `informationClassification` | Classification de l'information | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui | common |  |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui | common |  |
| `wbsCode` | Code WBS / OTP | string |  | common |  |
| `responsibleUnit` | UO responsable (pilote) | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Organisation matricielle BU × UO : unité qui porte la responsabilité de l'artefact (souvent l'UO du projet). |
| `performingUnit` | UO réalisatrice | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  | common | Unité (usine, centre d'ingénierie, filiale, partenaire) qui produit l'artefact ; alimente les tableaux de bord par UO sans créer de projet par UO. |
| `applicableTechnologies` | Filières applicables | enum [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multi) |  | common | Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) : évite de coder le vocabulaire REP dans la structure. |
| `transitionNote` | Motif de la dernière transition | text |  | common | Exigé par les transitions de retour, rejet, réouverture, annulation (l'historique conserve toutes les valeurs). |
| `lessonCategory` | Catégorie | enum [`lessonCategory`](A2_enumerations.md#lessoncategory) | oui | local |  |
| `lessonContext` | Contexte / faits | richtext |  | local |  |
| `lessonRecommendation` | Recommandation | richtext | `validated` | local |  |
| `genericImpact` | Portée générique (palier / flotte / produit) | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) |  | local |  |
| `targetAssets` | Référentiels à faire évoluer (bibliothèque, gabarit, procédure) | string |  | local |  |

