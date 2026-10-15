# Annexe A5 — Types de LiveDocs et gabarits

> Document **généré** par `tools/generate_docs.py` depuis `model/*.yaml` — ne pas éditer à la main.

## Attributs de document

| id | Libellé | Type | Obligatoire |
|---|---|---|---|
| `documentNumber` | N° de document | string | oui |
| `revisionIndex` | Indice | string | oui |
| `customerVisa` | Visa client | enum [`customerVisa`](A2_enumerations.md#customervisa) |  |
| `customerDocumentNumber` | N° document client | string |  |
| `informationClassification` | Classification | enum [`informationClassification`](A2_enumerations.md#informationclassification) | oui |
| `exportControl` | Contrôle export | enum [`exportControl`](A2_enumerations.md#exportcontrol) | oui |
| `lifecyclePhase` | Phase | enum [`lifecyclePhase`](A2_enumerations.md#lifecyclephase) |  |
| `language` | Langue | enum [`language`](A2_enumerations.md#language) |  |
| `aip` | Produit d'une AIP | enum [`yesNoTbd`](A2_enumerations.md#yesnotbd) | oui |
| `applicablePlantSeries` | Paliers applicables | enum [`plantSeries`](A2_enumerations.md#plantseries) (multi) |  |
| `docAuthor` | Rédacteur | user |  |
| `docVerifier` | Vérificateur | user |  |
| `docApprover` | Approbateur | user |  |
| `revisionSummary` | Objet de la révision | richtext |  |
| `edmsReference` | Référence GED (archive) | string |  |
| `sourceTemplate` | Gabarit d'origine (version) | string |  |
| `transitionNote` | Motif de la dernière transition | text |  |
| `requiredHabilitation` | Habilitation requise des signataires | enum [`habilitationDomain`](A2_enumerations.md#habilitationdomain) |  |
| `responsibleUnit` | UO responsable | enum [`operationalUnit`](A2_enumerations.md#operationalunit) |  |

## `stakeholderSpec` — Spécification technique de besoin (STB)

*Stakeholder requirements specification* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `stakeholderRequirement`, `sourceRequirement`, `operationalScenario`, `assumption`, `term`

Cascade document → éléments : type principal `stakeholderRequirement` ; soumis / approuvés en cascade : `stakeholderRequirement`, `operationalScenario`

Plan type :

- 1. Objet, domaine d'application, documents applicables et de référence
- 2. Contexte, parties prenantes, missions et cycle de vie du produit
- 3. Concept d'emploi (scénarios opérationnels, états d'exploitation)
- 4. Exigences de besoin par catégorie (fonctionnelles, performances, sûreté, RP, FOH, environnement, exploitabilité, maintenabilité, démantèlement)
- 5. Contraintes (réglementaires, interfaces, site, existant)
- 6. Hypothèses et données d'entrée
- 7. Critères de validation
- Annexe : glossaire, matrice de traçabilité vers les exigences d'entrée

## `systemSpec` — Spécification technique système / sous-système (ST)

*System / subsystem specification* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `systemRequirement`, `safetyRequirement`, `function`, `interface`, `designParameter`, `assumption`

Cascade document → éléments : type principal `systemRequirement` ; soumis / approuvés en cascade : `systemRequirement`, `safetyRequirement`, `function`, `designParameter` ; condition d'approbation du document : `interface` dans `agreed`, `frozen`

Plan type :

- 1. Objet, périmètre, documents applicables
- 2. Description fonctionnelle (fonctions, modes, états)
- 3. Classement de sûreté et exigences associées
- 4. Exigences fonctionnelles et de performance
- 5. Exigences de sûreté (défaillance unique, redondance, diversité, séparation, alimentations secourues)
- 6. Exigences d'interface (renvoi ICD)
- 7. Exigences d'environnement, de qualification et sismiques
- 8. Exigences de RP, FOH, cybersécurité, exploitabilité, maintenabilité, inspectabilité, testabilité
- 9. Exigences de vérification (méthodes, étapes)
- Annexes : paramètres de conception, traçabilité amont / aval

## `systemDesignManual` — Dossier de conception système (SDM)

*System design manual* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `function`, `logicalComponent`, `physicalComponent`, `interface`, `designParameter`, `designDecision`, `systemRequirement`, `safetyRequirement`, `assumption`

Cascade document → éléments : type principal `function` ; soumis / approuvés en cascade : `function`, `logicalComponent`, `physicalComponent`, `designParameter`, `systemRequirement`, `safetyRequirement` ; condition d'approbation du document : `interface` dans `agreed`, `frozen` ; `designDecision` dans `decided`

Plan type :

- 1. Rôle du système et fonctions
- 2. Bases de conception (exigences, classement, hypothèses)
- 3. Description de l'architecture (fonctionnelle, logique, physique)
- 4. Description des matériels principaux
- 5. Fonctionnement normal, incidentel, accidentel
- 6. Contrôle-commande et IHM
- 7. Interfaces
- 8. Justification du respect des exigences (renvoi analyses)
- 9. Essais (de démarrage, périodiques)
- 10. Décisions de conception et écarts acceptés

## `equipmentSpec` — Spécification technique d'équipement / d'approvisionnement (STE)

*Equipment / procurement specification* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `equipmentRequirement`, `safetyRequirement`, `regulatoryRequirement`, `interface`, `verificationCase`, `designParameter`

Cascade document → éléments : type principal `equipmentRequirement` ; soumis / approuvés en cascade : `equipmentRequirement`, `safetyRequirement`, `verificationCase`, `designParameter` ; condition d'approbation du document : `interface` dans `agreed`, `frozen`

Plan type :

- 1. Objet, périmètre de fourniture, documents applicables
- 2. Classement (sûreté, mécanique / électrique, ESPN, qualification, sismique, ITNS)
- 3. Exigences fonctionnelles et de performance
- 4. Exigences de conception (code applicable, matériaux, chimie, durée de vie)
- 5. Exigences de fabrication et de contrôle (procédés spéciaux, CND, points d'arrêt)
- 6. Exigences de qualification (programme, normes, conditions)
- 7. Exigences qualité (ISO 19443 / NQA-1, CFSI, surveillance, documentation finale)
- 8. Livrables et dossier de fin de fabrication
- Annexe : matrice de conformité à remplir par le fournisseur

## `softwareRequirementsSpec` — Spécification d'exigences logicielles (SRS)

*Software requirements specification* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `softwareRequirement`, `hardwareRequirement`, `function`, `interface`, `assumption`

Cascade document → éléments : type principal `softwareRequirement` ; soumis / approuvés en cascade : `softwareRequirement`, `hardwareRequirement`, `function` ; condition d'approbation du document : `interface` dans `agreed`, `frozen`

Plan type :

- 1. Objet, catégorie de la fonction supportée, norme applicable (IEC 60880 / 62138)
- 2. Contexte logiciel (plateforme, environnement d'ingénierie)
- 3. Exigences fonctionnelles
- 4. Exigences de performance et temps de réponse
- 5. Autosurveillance, comportement sur défaillance, robustesse
- 6. Exigences de cybersécurité
- 7. Interfaces et données
- 8. Exigences de vérification et de validation

## `interfaceControlDocument` — Document de contrôle d'interfaces (ICD)

*Interface control document* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `interface`, `systemRequirement`, `equipmentRequirement`, `designParameter`

Cascade document → éléments : type principal `interface` ; soumis / approuvés en cascade : `systemRequirement`, `equipmentRequirement`, `designParameter` ; condition d'approbation du document : `interface` dans `agreed`, `frozen`

Plan type :

- 1. Objet, entités et responsables des côtés A et B
- 2. Registre des interfaces (par type)
- 3. Données échangées (charges, débits, signaux, alimentations, encombrements)
- 4. Exigences d'interface
- 5. Statut de maturité et calendrier de gel
- 6. Points ouverts

## `safetyCase` — Dossier / chapitre de démonstration de sûreté

*Safety case / safety report chapter* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `safetyRequirement`, `safetyClaim`, `hazard`, `analysis`, `assumption`, `regulatoryRequirement`

Cascade document → éléments : type principal `safetyRequirement` ; soumis / approuvés en cascade : `safetyRequirement`, `safetyClaim`, `hazard`, `analysis`

Plan type :

- 1. Objectifs et référentiel de sûreté applicable
- 2. Arborescence des revendications (claims) et stratégies
- 3. Événements initiateurs et agressions retenus (criblage)
- 4. Exigences de sûreté et dispositions de conception
- 5. Analyses support et conclusions
- 6. Hypothèses et limites du domaine de validité
- 7. Preuves (renvois vers V&V et livrables)
- 8. Engagements et points ouverts

## `classificationList` — Note de classement / liste des EIP et exigences définies

*Classification note / EIP and defined requirements list* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `function`, `physicalComponent`, `safetyRequirement`, `systemRequirement`

Cascade document → éléments : type principal `function` ; soumis / approuvés en cascade : `function`, `physicalComponent`, `safetyRequirement`, `systemRequirement`

Plan type :

- 1. Méthode de classement et référentiel (schéma de classement du palier / projet)
- 2. Catégorisation des fonctions
- 3. Classement des SSC (sûreté, mécanique, électrique, qualification, sismique, ESPN)
- 4. Liste des EIP et exigences définies associées
- 5. Liste des AIP identifiées

## `complianceMatrix` — Matrice de conformité (client / réglementaire)

*Compliance matrix* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `sourceRequirement`, `regulatoryRequirement`

Cascade document → éléments : type principal `sourceRequirement` ; soumis / approuvés en cascade : — ; condition d'approbation du document : `sourceRequirement` dans `accepted`

Plan type :

- 1. Document source et révision traitée
- 2. Position de conformité exigence par exigence (statut, justification, renvoi)
- 3. Synthèse : non-conformités, dérogations demandées, clarifications

## `vvPlan` — Plan de vérification et validation

*Verification & validation plan* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `verificationCase`, `review`

Cascade document → éléments : type principal `verificationCase` ; soumis / approuvés en cascade : `verificationCase`

Plan type :

- 1. Stratégie V&V (niveaux, étapes, méthodes, indépendance)
- 2. Organisation et responsabilités
- 3. Moyens (bancs, maquettes, simulateurs, qualification des outils)
- 4. Cas de vérification par niveau / étape
- 5. Points d'inspection et parties convoquées
- 6. Gestion des anomalies et non-régression
- 7. Critères de fin de V&V

## `testProcedure` — Procédure d'essais

*Test procedure* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `verificationCase`

Cascade document → éléments : type principal `verificationCase` ; soumis / approuvés en cascade : `verificationCase`

Plan type :

- 1. Objet, exigences vérifiées, prérequis et configuration
- 2. Moyens, instrumentation (étalonnage), sécurité / RP
- 3. Séquence d'essai (étapes, résultats attendus, critères)
- 4. Points d'arrêt / de notification
- 5. Feuilles de relevés (via Test Run)

## `toolingSpec` — Cahier des charges fonctionnel d'outillage

*Tooling functional specification* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `stakeholderRequirement`, `systemRequirement`, `function`, `operationalScenario`, `hazard`, `fmeaItem`, `assumption`, `interface`

Cascade document → éléments : type principal `stakeholderRequirement` ; soumis / approuvés en cascade : `stakeholderRequirement`, `systemRequirement`, `function`, `operationalScenario`, `hazard`, `fmeaItem`

Plan type :

- 1. Contexte et objectif de l'intervention
- 2. Expression fonctionnelle du besoin (fonctions de service et de contrainte, critères, niveaux, flexibilité – NF EN 16271)
- 3. Séquence d'intervention et scénarios (y compris modes dégradés, récupération)
- 4. Contraintes site (accès, encombrement, RP / débit de dose, contamination, FME, manutention, alimentations)
- 5. Exigences réglementaires machine (marquage CE ; règlement (UE) 2023/1230 applicable au 20/01/2027)
- 6. Analyse de risques machine et intervention
- 7. Exigences de qualification (maquette, essais de réception)
- 8. Livrables (dossier technique, notice, formation)

## `fmeaWorksheet` — AMDEC / analyse de risques

*FMEA / risk analysis* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `fmeaItem`, `hazard`, `risk`, `action`

Cascade document → éléments : type principal `fmeaItem` ; soumis / approuvés en cascade : `fmeaItem`, `hazard`

Plan type :

- 1. Périmètre, méthode, échelles de cotation
- 2. Tableau AMDEC (éditeur tabulaire)
- 3. Actions et cotations résiduelles

## `justificationNote` — Note de justification (fortuit / écart)

*Justification note (emergent issue / deviation)* — workflow [`wfDocumentLight`](A4_workflows.md#wfdocumentlight)

Types de Work Items autorisés : `technicalIssue`, `systemRequirement`, `equipmentRequirement`, `analysis`, `verificationCase`, `assumption`, `nonConformance`

Cascade document → éléments : type principal `technicalIssue` ; soumis / approuvés en cascade : `systemRequirement`, `equipmentRequirement`, `analysis`, `verificationCase`

Plan type :

- 1. Constat (description, localisation, données d'inspection)
- 2. Exigences et critères applicables (code, spécification, RSE-M...)
- 3. Hypothèses
- 4. Analyse / justification (renvoi notes de calcul)
- 5. Conclusion, conditions et limites (durée, surveillance)
- 6. Caractère générique et REX

## `reloadSafetyReport` — Rapport de sûreté de recharge

*Reload safety evaluation report* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `designParameter`, `analysis`, `verificationCase`, `assumption`, `safetyRequirement`

Cascade document → éléments : type principal `designParameter` ; soumis / approuvés en cascade : `designParameter`, `analysis`, `verificationCase`, `safetyRequirement`

Plan type :

- 1. Données d'entrée du cycle (plan de chargement, historique)
- 2. Paramètres de sûreté de recharge vs limites des études de référence
- 3. Vérifications (neutronique, thermohydraulique, thermomécanique combustible)
- 4. Conclusion et conditions
- 5. Programme d'essais physiques de redémarrage

## `modificationFile` — Dossier de modification (base installée)

*Plant modification file* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `changeRequest`, `systemRequirement`, `equipmentRequirement`, `safetyRequirement`, `physicalComponent`, `interface`, `analysis`, `verificationCase`, `regulatoryRequirement`

Cascade document → éléments : type principal `changeRequest` ; soumis / approuvés en cascade : `systemRequirement`, `equipmentRequirement`, `safetyRequirement`, `physicalComponent`, `analysis`, `verificationCase`

Plan type :

- 1. Objet de la modification, origine, applicabilité (palier, tranches)
- 2. Exigences de la modification
- 3. Description de la solution
- 4. Analyse d'impact (sûreté, RP, environnement, exploitation, documentation)
- 5. Éléments d'appréciation pour le classement réglementaire de la modification
- 6. Programme de requalification
- 7. Mise à jour des documents d'exploitation impactés

## `managementPlan` — Plan de management (PQP, PMIS, PGC, PDL...)

*Management plan (QAP, SEMP, CMP, SDP...)* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `action`, `review`, `term`

Cascade document → éléments : type principal `action` ; soumis / approuvés en cascade : —

Plan type :

- Plan libre selon gabarit du plan concerné

## `regulatoryLibrary` — Extrait de texte réglementaire / normatif (bibliothèque)

*Regulatory / normative extract (library)* — workflow [`wfDocumentLibrary`](A4_workflows.md#wfdocumentlibrary)

Types de Work Items autorisés : `regulatoryRequirement`, `term`

Cascade document → éléments : type principal `regulatoryRequirement` ; soumis / approuvés en cascade : `regulatoryRequirement`

Plan type :

- Structure miroir du texte source (titres, articles / clauses)

## `genericProductSpec` — Spécification produit générique (ligne de produits)

*Generic product specification (product line)* — workflow [`wfDocumentLibrary`](A4_workflows.md#wfdocumentlibrary)

Types de Work Items autorisés : `stakeholderRequirement`, `systemRequirement`, `equipmentRequirement`, `safetyRequirement`, `function`, `physicalComponent`, `interface`, `designParameter`, `verificationCase`

Cascade document → éléments : type principal `stakeholderRequirement` ; soumis / approuvés en cascade : `stakeholderRequirement`, `systemRequirement`, `equipmentRequirement`, `safetyRequirement`, `function`, `physicalComponent`, `verificationCase` ; condition d'approbation du document : `interface` dans `agreed`, `frozen`

Plan type :

- Structure de la spécification maître ; conditions de variante par élément

## `glossary` — Glossaire

*Glossary* — workflow [`wfDocumentLibrary`](A4_workflows.md#wfdocumentlibrary)

Types de Work Items autorisés : `term`

Cascade document → éléments : type principal `term` ; soumis / approuvés en cascade : `term`

Plan type :

- Termes par ordre alphabétique

## `qualificationDossier` — Dossier de qualification (procédé, matériel, code de calcul, équivalence CGD)

*Qualification dossier (process, equipment, calculation code, CGD equivalency)* — workflow [`wfDocumentFull`](A4_workflows.md#wfdocumentfull)

Types de Work Items autorisés : `verificationCase`, `equipmentRequirement`, `systemRequirement`, `softwareRequirement`, `designParameter`, `analysis`, `physicalComponent`, `assumption`, `deliverable`

Cascade document → éléments : type principal `verificationCase` ; soumis / approuvés en cascade : `verificationCase`, `equipmentRequirement`, `systemRequirement`, `softwareRequirement`, `designParameter`, `analysis`, `physicalComponent`

Plan type :

- 1. Objet, domaine de qualification / d'utilisation visé, référentiel (code, norme, guide ASN n°28 pour les codes, EPRI / 10 CFR 21 pour la CGD)
- 2. Exigences et caractéristiques critiques à démontrer
- 3. Paramètres et domaine (fenêtre de procédé, domaine de validation, conditions d'environnement)
- 4. Programme : essais, analyses, inspections, méthodes CGD retenues
- 5. Résultats (renvoi aux Test Runs signés et aux notes d'analyse)
- 6. Incertitudes, limites et conditions d'emploi
- 7. Conclusion et statut de qualification ; écarts et réserves

## `workPackageHandover` — Procès-verbal de remise de lot (UO → projet)

*Work package handover record (unit → project)* — workflow [`wfDocumentLight`](A4_workflows.md#wfdocumentlight)

Types de Work Items autorisés : `workPackage`, `deliverable`, `verificationCase`, `nonConformance`, `action`

Cascade document → éléments : type principal `workPackage` ; soumis / approuvés en cascade : — ; condition d'approbation du document : `deliverable` dans `internallyApproved`, `issued`, `customerReviewed`, `final`, `superseded`

Plan type :

- 1. Lot, UO réalisatrice, commande interne, révision du périmètre accordé
- 2. Livrables remis (état, indice, référence GED)
- 3. Preuves de vérification et écarts (FNC soldées ou transférées)
- 4. Réserves et actions de levée
- 5. Décision de réception

