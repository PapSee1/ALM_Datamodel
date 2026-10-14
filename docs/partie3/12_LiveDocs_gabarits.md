# Partie 3.6 — Architecture documentaire : LiveDocs, gabarits et échanges documentaires

> Catalogue des 20 types de documents, plans types et types de Work Items autorisés : [Annexe A5](../generated/A5_documents.md). Source : `model/document_types.yaml`.

## 1. Positionnement : centré document ou centré élément ?

La culture d'ingénierie nucléaire française est **documentaire** : « le document fait foi », avec un visa client par indice et un archivage en GED. Polarion permet une approche **hybride**, retenue ici :

| Aspect | Porté par | Raison |
|---|---|---|
| Rédaction, relecture, structure, contexte | **LiveDoc** | Ergonomie Word-like, lecture continue, signatures R / V / A |
| Granularité de traçabilité, statuts, attributs | **Work Item** (dans le LiveDoc) | Liens, couverture, suspicion, requêtes |
| Référence contractuelle et archive | **PDF signé en GED** | Pérennité (plus de 60 ans), valeur probante, visas client |
| Livrables non produits dans Polarion (plans, notes de calcul, PV externes) | Work Item `deliverable` (proxy GED) | Traçabilité sans duplication |

## 2. Catalogue des LiveDocs (synthèse)

| Famille | Types de documents | Workflow |
|---|---|---|
| Spécifications | STB (`stakeholderSpec`), ST (`systemSpec`), STE (`equipmentSpec`), SRS (`softwareRequirementsSpec`), CdC outillage (`toolingSpec`) | `wfDocumentFull` |
| Conception | Dossier de conception système (`systemDesignManual`), ICD (`interfaceControlDocument`) | `wfDocumentFull` |
| Sûreté | Dossier de démonstration (`safetyCase`), note de classement / liste des EIP (`classificationList`), AMDEC (`fmeaWorksheet`), rapport de sûreté de recharge (`reloadSafetyReport`) | `wfDocumentFull` |
| Conformité | Matrice de conformité (`complianceMatrix`) | `wfDocumentFull` |
| V&V | Plan V&V (`vvPlan`), procédure d'essais (`testProcedure`) | `wfDocumentFull` |
| Base installée | Dossier de modification (`modificationFile`), note de justification (`justificationNote`) | Full / **Light** |
| Management | Plans (PQP, PMIS, PGC, PDL…) (`managementPlan`) | `wfDocumentFull` |
| Bibliothèques | Extrait réglementaire (`regulatoryLibrary`), spécification produit générique (`genericProductSpec`), glossaire (`glossary`) | `wfDocumentLibrary` |

## 3. Anatomie d'un gabarit

Chaque gabarit (projet `LIB-TEMPLATES`) contient :
1. **Page de garde** (champs de document) : n° de document, indice, titre, classification, contrôle export, phase, langue, AIP, applicabilité, n° client.
2. **Cartouche de signatures** : rédacteur / vérificateur / approbateur, alimenté par les signatures du workflow (date, signification).
3. **Historique des révisions** : indice, date, objet de la révision (`revisionSummary`).
4. **Sommaire** et **plan type** (Annexe A5), avec des titres (`heading`) pré-créés.
5. **Blocs d'aide à la rédaction**, en texte non Work Item, masqués à l'export.
6. **Tableaux de traçabilité intégrés** (macros ou widgets) : couverture amont, aval et vérification de la section.
7. **Configuration des types autorisés** et formulaires de création restreints au profil.

## 4. Plans types des gabarits principaux (extrait)

**STB** :
1. Objet et documents applicables
2. Contexte, parties prenantes, missions
3. Concept d'emploi (scénarios, états)
4. Exigences de besoin par catégorie
5. Contraintes
6. Hypothèses
7. Critères de validation

Annexes : glossaire et traçabilité vers les exigences d'entrée.

**ST système** :
1. Objet
2. Description fonctionnelle
3. Classement de sûreté
4. Exigences fonctionnelles et de performance
5. Exigences de sûreté (défaillance unique, redondance, diversité, séparation, alimentations secourues)
6. Interfaces (renvoi ICD)
7. Environnement, qualification et séisme
8. RP, FOH, cybersécurité, exploitabilité, maintenabilité, inspectabilité, testabilité
9. Exigences de vérification

**STE / spécification d'approvisionnement** :
1. Périmètre de fourniture
2. **Classement complet** (sûreté, M / E, ESPN, K, SC, ITNS)
3. Fonctions et performances
4. Conception (code, matériaux, chimie, durée de vie)
5. Fabrication et contrôles (procédés spéciaux, CND, **points d'arrêt**)
6. Qualification
7. Qualité (ISO 19443 / NQA-1, **CFSI**, surveillance, documentation finale)
8. Livrables et dossier de fin de fabrication

Annexe : matrice de conformité fournisseur.

**Cahier des charges fonctionnel d'outillage (NF EN 16271)** :
1. Contexte et objectif de l'intervention
2. Fonctions de service et de contrainte (critère, niveau, flexibilité)
3. Séquence d'intervention, modes dégradés, récupération
4. Contraintes du site (accès, RP, contamination, FME, manutention, alimentations)
5. Exigences machines (marquage CE ; règlement (UE) 2023/1230 au 20/01/2027)
6. Analyse de risques
7. Qualification (maquette, réception)
8. Livrables

**Procédure d'essais** :
1. Objet, exigences vérifiées, prérequis, configuration
2. Moyens et instrumentation (étalonnage), sécurité et RP
3. Séquence (étapes, résultats attendus, critères) : `testSteps`
4. Points d'arrêt et de notification
5. Feuilles de relevés via Test Run

**Dossier de sûreté** :
1. Objectifs et référentiel
2. Arborescence des revendications
3. Initiateurs et agressions (criblage)
4. Exigences et dispositions
5. Analyses et conclusions
6. Hypothèses et domaine de validité
7. Preuves
8. Engagements et points ouverts

**Note de justification (fortuit)** :
1. Constat
2. Exigences et critères (code, RSE-M)
3. Hypothèses
4. Analyse / justification
5. Conclusion, conditions, limites (durée, surveillance)
6. Caractère générique et REX

## 5. Numérotation, indices et états documentaires

| Élément | Règle |
|---|---|
| N° de document | Attribué par la GED (`documentNumber`) ; **jamais** dérivé de l'ID Polarion |
| Indice | Brouillons : A0, A1… Diffusions : A, B, C… (`fra-revision-index.js`). Chaque diffusion = baseline + PDF en GED |
| Visa client | VSO / VSO-SR / VAO / VAOB / REF / pour information (`customerVisa`, à confirmer par client) ; VAOB ou REF → nouvel indice |
| État documentaire | Workflow du LiveDoc (Rédaction, Relecture, Vérification, Approbation, Approuvé, Remplacé) ; « Définitif » porté par le `deliverable` associé |

## 6. Relecture et commentaires

- **Relecture interne** : état `inReview`. Commentaires Polarion (fils de discussion, mentions depuis 2512) et approbations des relecteurs désignés (licence REVIEWER).
- **Remarques formelles** (revues, client) : Work Items `reviewFinding` liés (`raisedIn`) au livrable ou à la revue. Gravité alignée sur le visa (bloquante ↔ VAOB). Levée tracée.
- **Clôture de revue** : aucune remarque bloquante ouverte (condition de `wfReview.close`).

## 7. Exports et échanges documentaires

| Besoin | Mécanisme | Remarques |
|---|---|---|
| PDF officiel signé | Extension d'export PDF (ex. pdf-exporter open source, compatible 2606) + gabarit d'entreprise + manifeste de signatures | Versé en GED à l'approbation (`exportToEdms`) |
| Word aller-retour | Export / réimport Word natif | Pour les contributeurs externes sans accès ; à limiter (risque de perte de liens) |
| Excel aller-retour | Export / import Excel (tables) | Matrices de conformité fournisseurs |
| ReqIF | Import / export ReqIF 1.0.1 / 1.1 avec gabarits de correspondance (`.polarion/reqif/templates`) | Échanges structurés client et architecte-ensemblier (ADR-12) ; réimport mettant à jour le même document |
| Comparaison | Comparaison de révisions / baselines de documents ; fusion 3-way (2404+) | Revues de modifications, branches |

## 8. Règles de qualité documentaire (contrôlées)

1. Aucun Work Item du document dans un état antérieur à `inReview` au passage en vérification ; tous approuvés à l'approbation (`ContainsNoMatchingWorkItems`).
2. Aucun lien suspect dans le document à la vérification (`ContainsNoMatchingWorkItems(suspect:true)`).
3. Classification du document ≥ classification maximale de ses éléments (rapport).
4. Types de Work Items conformes au type de document (configuration).
5. Champs de garde complets (`documentNumber`, `revisionIndex`, `aip`, classification, export).
