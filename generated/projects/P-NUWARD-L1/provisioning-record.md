# Dossier de provisioning — `P-NUWARD-L1`

> Document **généré** par `tools/generate_project.py` depuis `model/pilots/P-NUWARD-L1.yaml` — ne pas éditer à la main.

**NUWARD – pilote Polarion, lot de conception n° 1 (périmètre Framatome)**

Le programme SMR NUWARD est porté par EDF (filiale dédiée) avec des partenaires industriels, dont Framatome [C]. La conception a été réorientée à l'été 2024 vers des technologies éprouvées [C] : le besoin client est en évolution, ce qui rend le pilote exigeant sur la gestion des révisions d'exigences d'entrée (ré-import ReqIF, suspicion) mais favorable à un démarrage sans historique. Framatome y est partenaire / fournisseur : les exigences du client arrivent comme exigences d'entrée, la collaboration passe par un projet sas EXT-*.

## 1. Réponses au questionnaire

| # | Paramètre | Question | Réponse | Confiance |
|---|---|---|---|---|
| Q01 | `projectType` | Typologie de projet | `newBuildSmr` |  |
| Q02 | `businessUnit` | BU maître d'ouvrage | `dti` | P |
| Q03 | `businessLine` | Business Line | `dtiNsss` | H |
| Q04 | `responsibleUnit` | UO responsable du projet | `dtiEngineering` | H |
| Q05 | `performingUnits` | UO réalisatrices (lots de travaux prévus) | `dtiEngineering`, `icEngineering` | H |
| Q06 | `regulatoryFrameworks` | Cadres réglementaires applicables (packs) | `frAsnr`, `intlIaea` | P |
| Q07 | `reactorTechnologies` | Filières / technologies concernées | `smr` |  |
| Q08 | `plantSeries` | Paliers / modèles concernés (base installée) | `nuward` |  |
| Q09 | `safetyClassScheme` | Référentiel de classement de sûreté du projet | `iaeaSsg30` | H |
| Q10 | `maxClassification` | Classification maximale des données prévues | `customerConfidential` |  |
| Q11 | `exportControl` | Contrôle export (criblage préalable) | `toBeScreened` |  |
| Q12 | `language` | Langue contractuelle | `fr` |  |
| Q13 | `signaturePolicy` | Politique de signature électronique (PR-10) | `roleBased` | P |
| Q14 | `customerExchange` | Mode d'échange avec le client | `reqif` |  |
| Q15 | `externalParticipants` | Participants externes | `customer` |  |
| Q16 | `mbseTool` | Outil MBSE | `capella` | P |
| Q17 | `plmSystem` | PLM de référence de la nomenclature | `threeDx` | P |
| Q18 | `tailoringScore` | Cotation de la grille de tailoring (7 critères, model/tailoring.yaml) | safety=3, novelty=3, size=2, disciplines=3, regulatory=3, contract=2, duration=3 |  |
| Q19 | `tailoringJustification` | Justification si la classe retenue diffère de la classe par défaut de la typologie | — |  |

*Note :* regulatoryFrameworks : revue conjointe préliminaire de NUWARD par plusieurs autorités européennes (dont ASN, STUK, SÚJB) [P] ; le pack intlIaea porte le socle commun. safetyClassScheme : à aligner sur le référentiel du client.

## 2. Paramètres dérivés (règles D01–D13)

| Paramètre | Valeur |
|---|---|
| Gabarit | `TPL-NEWBUILD` |
| Archétype | `TPL-01-PRODUCT` |
| Classe de tailoring | `classA` |
| Score de cotation | `19` |
| Instance | `STD` |
| Packs réglementaires | `frAsnr`, `intlIaea` |
| Projet sas à créer | `TPL-EXT` |
| Types activés par règle | `workPackage` |
| Documents activés par règle | `workPackageHandover` |
| Signatures habilitées | `inactive` |
| Connecteurs | `CX-MBSE-CAPELLA`, `CX-PLM-3DX` |
| Énumérations projet | `plantUnit`, `operationalUnit`, `businessLine` |
| Champs masqués (packs) | `cfr5059Outcome`, `cfr5059Reference`, `cfr5059Screening`, `part21Evaluation` |
| Incrément de déploiement du cœur | `INC-1` |

## 3. Tranche activée (sous-ensemble du modèle 150 %)

*Un système (ou sous-ensemble cohérent) du périmètre Framatome, de l'exigence client jusqu'à la V&V planifiée et au classement de sûreté, sur 4 à 6 mois de production réelle*

- **Types activés (28 / 36)** : `sourceRequirement`, `regulatoryRequirement`, `stakeholderRequirement`, `systemRequirement`, `equipmentRequirement`, `safetyRequirement`, `assumption`, `operationalScenario`, `function`, `logicalComponent`, `physicalComponent`, `interface`, `designParameter`, `designDecision`, `hazard`, `safetyClaim`, `analysis`, `regulatoryCommitment`, `verificationCase`, `changeRequest`, `waiver`, `risk`, `review`, `reviewFinding`, `action`, `deliverable`, `nonConformance`, `workPackage`
- **Types différés (8)** : `softwareRequirement`, `hardwareRequirement`, `fmeaItem`, `anomaly`, `technicalIssue`, `term`, `unitDeployment`, `lessonLearned`
- **Documents activés (9)** : `stakeholderSpec`, `systemSpec`, `systemDesignManual`, `classificationList`, `interfaceControlDocument`, `safetyCase`, `complianceMatrix`, `vvPlan`, `workPackageHandover`
- **Hors périmètre du pilote** : Ligne de produits PL-NUWARD (une seule conception à ce stade), Variants, logiciel / matériel C-C (incrément INC-3), AMDEC et effectivité par tranche (INC-2)

## 4. Fichiers de configuration projet générés

À déposer dans le dossier `.polarion/` du projet, **après** déploiement du cœur (`generated/polarion/<lang>/.polarion/`) en configuration globale. Seuls les fichiers autorisés par `model/extension_policy.yaml` (overridableProjectFiles) sont produits.

- `tracker/fields/workitem-type-enum.xml`
- `documents/fields/document-type-enum.xml`
- `tracker/fields/plantUnit-enum.xml`
- `tracker/fields/operationalUnit-enum.xml`
- `tracker/fields/businessLine-enum.xml`
- `tracker/fields/changeRequest-custom-fields.xml`
- `tracker/fields/nonConformance-custom-fields.xml`

## 5. Bibliothèques à brancher

- LIB-REG/FR/Code de l'environnement – INB
- LIB-REG/FR/Arrêté INB 2012
- LIB-REG/FR/Arrêté ESPN 2015
- LIB-REG/FR/Guides ASN-ASNR
- LIB-REG/FR/Codes AFCEN (références)
- LIB-REG/IAEA/Safety Standards
- LIB-REG/IAEA/Nuclear Security Series

## 6. Rôles projet à pourvoir (20)

Rôles intervenant dans au moins une transition des workflows activés (voir annexe A6 pour les droits et licences) :

`approver`, `ccbChair`, `configurationManager`, `customerReviewer`, `disciplineEngineer`, `documentController`, `interfaceManager`, `libraryCurator`, `licensingEngineer`, `projectManager`, `qualityEngineer`, `requirementsManager`, `reviewer`, `safetyEngineer`, `safetyLead`, `technicalLead`, `verifier`, `vvEngineer`, `vvLead`, `workPackageManager`

## 7. Critères de succès du pilote

| # | Critère | Cible |
|---|---|---|
| SC-01 | 100 % des exigences du client importées par ReqIF, positions de conformité établies | 100 % |
| SC-02 | Exigences définies vérifiées par au moins un cas approuvé (TR-03) sur la tranche pilote | ≥ 90 % en fin de pilote |
| SC-03 | Ré-import d'au moins une révision client sans ressaisie, suspicion traitée sous 10 jours | ≥ 1 cycle |
| SC-04 | Documents STB / ST / classement / ICD approuvés et signés dans l'outil, PDF versés en GED | 4 documents |
| SC-05 | Satisfaction des utilisateurs pilotes | ≥ 3,5 / 5 |
| SC-06 | Aucun contournement du socle non négociable (audit Qualité) | 0 |

## 8. Liste de contrôle de création (doc. 23 § 5)

- [ ] Réponses de confiance H confirmées en atelier (doc. 24, atelier C4)
- [ ] Cœur déployé et spike de conformité clos (doc. 23, étape S1)
- [ ] Scripts « socle » en service et testés (doc. 23, étape S3)
- [ ] Projet créé depuis le gabarit, surcharges projet ci-dessus déposées
- [ ] Projet sas créé et comptes client nominatifs ouverts (si `extProject`)
- [ ] Bibliothèques branchées, profil ReqIF client testé sur fichier de référence
- [ ] Groupes d'annuaire des rôles alimentés, licences attribuées
- [ ] Tableaux de bord du rôle opérationnels sur données de test
- [ ] Cas OQ du pilote exécutés, revue go / no-go signée
