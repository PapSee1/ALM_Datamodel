# Annexe A11 — Import / export et interopérabilité

> Document **généré** par `tools/generate_docs.py` depuis `model/*.yaml` — ne pas éditer à la main.

## ReqIF

Norme : OMG ReqIF (1.1 / 1.2 selon le partenaire) ; noms d'attributs standard selon le guide d'implémentation ReqIF (ProSTEP iViP)

- Un profil de correspondance (mapping) par partenaire et par sens d'échange, versionné dans ce dépôt.
- L'identifiant du partenaire est toujours conservé dans externalId ; l'identifiant Polarion n'est jamais réutilisé comme clé chez le partenaire sans accord.
- Les attributs non mappés sont refusés à l'import (jamais créés à la volée) : toute évolution passe par la Design Authority.
- Ré-import d'une nouvelle révision du partenaire = mise à jour par externalId ; les éléments disparus passent à l'état 'superseded', jamais supprimés.

### `RIF-CUSTOMER-IN` — Import d'une spécification client (exigences d'entrée verbatim)

Sens : **import** ; type : `sourceRequirement` ; confiance H

| Attribut ReqIF | Champ Polarion |
|---|---|
| ReqIF.ForeignID | `externalId` |
| En-tête ReqIF (TITLE) / nom du document partenaire | `sourceDocument` |
| ReqIF.Text | `originalText` |
| ReqIF.Name | `title` |
| ReqIF.ChapterName | `heading` |
| Document / révision (attribut partenaire) | `sourceDocumentRevision` |
| Paragraphe (attribut partenaire) | `sourceParagraph` |

Valeurs posées : `requirementSourceType` = `contract`, `complianceStatus` = `toBeAssessed`

### `RIF-CUSTOMER-COMPLIANCE-OUT` — Retour de la matrice de conformité au client

Sens : **export** ; type : `sourceRequirement` ; confiance H

| Attribut ReqIF | Champ Polarion |
|---|---|
| ReqIF.ForeignID | `externalId` |
| Compliance | `complianceStatus` |
| Compliance statement | `complianceStatement` |

### `RIF-SUPPLIER-OUT` — Envoi d'une spécification d'approvisionnement à un fournisseur

Sens : **export** ; type : `equipmentRequirement` ; confiance H

| Attribut ReqIF | Champ Polarion |
|---|---|
| ReqIF.ForeignID | `id` |
| ReqIF.Name | `title` |
| ReqIF.Text | `description` |
| Acceptance criteria | `acceptanceCriteria` |
| Verification methods | `verificationMethods` |
| Safety relevant | `safetyRelevant` |
| Design code | `designCode` |

Champs jamais exportés : `informationClassification`, `exportControl`, `rationale`, `verificationStatus`

Filtre d'export : `exportControl.KEY:(notControlled euDualUse) AND NOT informationClassification.KEY:(sensitiveSecurity restricted)`

### `RIF-SUPPLIER-RETURN` — Réponse de conformité du fournisseur (aller-retour)

Sens : **import** ; type : `equipmentRequirement` ; confiance H

| Attribut ReqIF | Champ Polarion |
|---|---|
| ReqIF.ForeignID | `id` |
| Supplier compliance | `supplierComplianceStatus` |
| Supplier statement | `supplierComplianceStatement` |
| Supplier document | `supplierDocumentReference` |

### `RIF-LIBRARY-REG` — Alimentation de la bibliothèque réglementaire (texte structuré fourni en ReqIF)

Sens : **import** ; type : `regulatoryRequirement` ; confiance H

| Attribut ReqIF | Champ Polarion |
|---|---|
| ReqIF.ForeignID | `externalId` |
| ReqIF.Text | `description` |
| Reference | `regulatoryReference` |
| Edition | `edition` |

Valeurs posées : `regulatoryDocType` = `regulatorGuide`, `bindingLevel` = `mandatory`

## Règles d'analyse des imports Word

Import Word (assistant natif) : règles appliquées dans l'ordre ; une règle par style plutôt que par mot-clé chaque fois que le document source est stylé.

| # | Motif reconnu | Élément créé | Champs posés | Note | Confiance |
|---|---|---|---|---|---|
| W-01 | Style de titre de niveau n (Titre 1…9 / Heading 1…9) | `heading` | — |  | H |
| W-02 | Paragraphe contenant un verbe prescriptif ('doit', 'doivent', 'shall', 'must') | `sourceRequirement` | `bindingLevel`=mandatory | Le type cible dépend du gabarit : sourceRequirement pour un document client, systemRequirement pour une spécification interne migrée. | H |
| W-03 | Paragraphe contenant 'devrait', 'il est recommandé', 'should' | `sourceRequirement` | `bindingLevel`=recommendation |  | H |
| W-04 | Paragraphe contenant 'peut', 'may' | `sourceRequirement` | `bindingLevel`=permission |  | P |
| W-05 | Identifiant en début de paragraphe (motif [A-Z]{2,6}-[0-9]+ ou §x.y.z) | `None` | `externalId`=<capture> |  | P |
| W-06 | Paragraphe 'Nota', 'Note', 'Remarque', 'Commentaire' | `none` | — | Reste du texte informatif du LiveDoc (pas de Work Item). | H |
| W-07 | Tableau avec colonne d'identifiants | `sourceRequirement` | — | Un Work Item par ligne ; les autres colonnes sont mappées sur des champs (sinon conservées en texte). | P |
| W-08 | Liste à puces sous une exigence | `none` | — | Rattachée à l'exigence précédente (même Work Item). | P |
| W-09 | Paragraphe contenant plusieurs verbes prescriptifs | `sourceRequirement` | `transitionNote`=A scinder (qualité de rédaction) | Signalé, jamais scindé automatiquement (texte verbatim). | H |
| W-10 | Références normatives (RCC-M, IEC, 10 CFR, arrêté...) | `none` | — | Post-traitement : proposition de liens vers LIB-REG (script), validation humaine. | P |
| W-11 | Images, équations, tableaux non mappés | `none` | — | Conservés dans le texte riche ; équations en image si l'éditeur ne les supporte pas. | H |

Portes qualité de l'import :

- Taux de paragraphes prescriptifs non capturés < 2 % (contrôle par échantillonnage, double lecture sur les documents de classe A).
- Aucun Work Item créé sans sourceDocument / sourceDocumentRevision (champs setByImport).
- Rapport d'import archivé avec le document (nombre d'éléments, règles appliquées, anomalies).

## Aller-retour Excel

Excel Round-trip natif : export d'une requête / d'un document vers un gabarit Excel, édition hors ligne, ré-import par identifiant.

- Réponse de conformité par un contributeur sans licence d'édition (via projet sas).
- Mise à jour en masse d'attributs (classement, applicabilité, méthodes de vérification) par un référent.
- Saisie terrain hors connexion (relevés, constats d'arrêt) lorsque l'accès réseau est impossible.

Règles :

- Colonne ID obligatoire et verrouillée ; aucune création de structure (parents, liens) par Excel.
- Colonnes verrouillées : champs calculés et champs de sûreté approuvés (PR-02).
- Ré-import refusé si l'élément a changé dans Polarion depuis l'export (contrôle de version), sauf arbitrage.
- Les transitions de workflow et signatures ne passent jamais par Excel.

| Gabarit | Type | Colonnes éditables | Colonnes verrouillées |
|---|---|---|---|
| `XL-COMPLIANCE` | `sourceRequirement` | complianceStatus, complianceStatement | originalText, externalId |
| `XL-CLASSIFICATION` | `physicalComponent` | safetyClass, eip, mechanicalClass, electricalClass, seismicCategory, qualificationClass | plmItemId, classificationValidated |
| `XL-SUPPLIER` | `equipmentRequirement` | supplierComplianceStatus, supplierComplianceStatement, supplierDocumentReference | description, acceptanceCriteria |
| `XL-FIELD-CAPTURE` | `technicalIssue` | detectedOn, unit, outageCriticalPath | issueCategory |

## Connecteurs

| Connecteur | Système | Mécanisme | Sens | Objets (champs) | Confiance |
|---|---|---|---|---|---|
| `CX-PLM-TC` | Teamcenter (si PLM de référence de la BU) | Intégration Polarion – Teamcenter (Active Workspace) : liens de traçabilité inter-domaines, consultation croisée | bidirectional | `physicalComponent` (plmItemId, plmRevision) | H |
| `CX-PLM-3DX` | 3DEXPERIENCE (si PLM de référence de la BU ou du client) | OSLC / API REST (développement spécifique) ou échange de fichiers ; pas de connecteur natif connu | bidirectional | `physicalComponent` (plmItemId, plmRevision) | P |
| `CX-MBSE-CAPELLA` | Capella (Arcadia) | Synchronisation modèle → Polarion par l'API REST (ex. outil libre capella2polarion) ; le modèle reste maître de l'architecture | modelToAlm | `function` (modelElementId, functionLevel); `logicalComponent` (modelElementId, logicalType); `physicalComponent` (modelElementId); `interface` (interfaceType, interfaceData); `operationalScenario` (scenarioType) | H |
| `CX-MBSE-CAMEO` | CATIA Magic / Cameo (SysML) | OSLC RM ou ReqIF ; passerelle éditeur à évaluer en maquette | bidirectional | `function` (modelElementId); `logicalComponent` (modelElementId); `systemRequirement` (externalId) | P |
| `CX-SIMULINK` | MATLAB / Simulink (C-C, simulateurs) | Connecteur Polarion pour Simulink (liens bloc ↔ exigence, résultats de tests) | bidirectional | `softwareRequirement` (softwareItem); `verificationCase` (testEnvironment) | H |
| `CX-CALC` | Chaînes de calcul scientifique (codes de cœur, thermohydraulique, mécanique) | API REST Polarion appelée en fin de calcul : création / mise à jour de l'analyse (code, version, empreinte du jeu de données) ; le code ne modifie jamais le statut | toAlm | `analysis` (calculationCode, codeVersion, codeQualification, inputDataSummary, analysisResult); `designParameter` (calculatedValue, uncertainty, cycleOrConfiguration) | H |
| `CX-TEST-BENCH` | Bancs d'essais / intégration continue logicielle | Import de résultats xUnit (XML) dans les Test Runs ; signature humaine des résultats (état resultsApproved) | toAlm | `verificationCase` (evidenceReference, lastResult) | H |
| `CX-EDMS` | GED de référence (archivage, diffusion contractuelle) | Export PDF signé + manifeste de signatures à l'approbation (fonction exportToEdms) ; référence GED retournée | toEdms | `deliverable` (documentNumber, revisionIndex, customerVisa) | H |
| `CX-ERP` | ERP (structure WBS / OTP, commandes internes) | Synchronisation nocturne des codes WBS et commandes internes (énumérations projet ou champs texte contrôlés) | toAlm | `workPackage` (internalOrderReference, budgetHours, wbsCode) | P |
| `CX-DIRECTORY` | Annuaire d'entreprise et référentiel RH-compétences | Synchronisation des groupes de rôles projet et des groupes d'habilitation HAB-<domaine>-<niveau> (LDAP) | toAlm | — | H |
| `CX-JIRA` | Jira (équipes logicielles) | Connecteur Polarion – Jira (synchronisation de tickets) ; les exigences et la V&V restent dans Polarion | bidirectional | `anomaly` (fixVersion, configurationVersion) | H |
| `CX-DOORS-MIG` | IBM DOORS (migration et coexistence) | Connecteur Polarion pour DOORS ou ReqIF ; conservation des identifiants DOORS dans externalId et des liens | toAlm | `systemRequirement` (externalId, sourceReference) | H |

## Contrôles d'échange

- **XC-01** — Tout export (ReqIF, Excel, PDF) vers l'extérieur est filtré par informationClassification et exportControl (requête de filtre du profil) et validé par un exportControlOfficer pour toute valeur autre que 'non contrôlé'.
- **XC-02** — Chaque échange est consigné dans le projet sas (Space 30-Exchange log) : profil, fichier, empreinte, émetteur, date, nombre d'éléments.
- **XC-03** — Aucun import direct d'un fichier externe dans un projet interne : réception dans le sas, contrôle antivirus et de conformité au profil, puis transfert.
- **XC-04** — Les mappings ReqIF sont testés sur un jeu de référence à chaque montée de version de Polarion (non-régression d'échange).
