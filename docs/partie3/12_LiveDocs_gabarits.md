# Partie 3.6 — Architecture documentaire : LiveDocs, gabarits et échanges documentaires

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **faible** (§ 3 et § 6–8 spécifiques à Polarion : gabarits de LiveDocs, relecture, exports, conditions documentaires) · Historique : [CHANGELOG](../../CHANGELOG.md) · Carte du dépôt : [guide de lecture](../GUIDE_DE_LECTURE.md).*
>
> Catalogue des **22 types de documents**, plans types et types de Work Items autorisés : [Annexe A5](../generated/A5_documents.md) (générée). Source : `model/document_types.yaml` ; workflows documentaires : `model/workflows.yaml` (`wfDocumentFull`, `wfDocumentLight`, `wfDocumentLibrary`). « [à vérifier] » signale une capacité Polarion dépendante de la version cible (annexe D, spike S1 du doc. 23).

> **En bref**
> - Ce document fixe **la place du document dans l'outil** : ce que porte un LiveDoc (document vivant de Polarion), ce que porte chaque élément qu'il contient (Work Item) et ce qui reste dans la GED (gestion électronique des documents, archive de référence). Il décrit les 22 types de LiveDocs, l'anatomie d'un gabarit, les indices et visas, la relecture, les exports et les règles de qualité contrôlées automatiquement.
> - Lecteurs : rédacteurs et vérificateurs de spécifications, responsables de documentation (*document controllers*), SE Referents (référents ingénierie système des BU) qui construisent les gabarits, Qualité.
> - À lire avant : doc. 08 (types de Work Items), doc. 10 (workflows et signatures). Pour les plans types détaillés : annexe A5 ; pour les échanges Word / Excel / ReqIF : [doc. 22](../partie4/22_Import_export_parsing_connecteurs.md).

## 1. Positionnement : centré document ou centré élément ?

La culture d'ingénierie nucléaire française est **documentaire** : « le document fait foi », avec un visa client par indice (version diffusée) et un archivage en GED. Polarion permet une approche **hybride**, retenue ici :

| Aspect | Porté par | Raison |
|---|---|---|
| Rédaction, relecture, structure, contexte | **LiveDoc** (document Polarion composé de texte libre et de Work Items) | Ergonomie proche de Word, lecture continue, signatures R / V / A (rédigé / vérifié / approuvé) |
| Granularité de traçabilité, statuts, attributs | **Work Item** (élément unitaire — exigence, cas de vérification, fonction… — placé dans le LiveDoc) | Liens, couverture, suspicion, requêtes |
| Référence contractuelle et archive | **PDF signé en GED** | Pérennité (plus de 60 ans), valeur probante, visas client |
| Livrables non produits dans Polarion (plans, notes de calcul, PV externes) | Work Item `deliverable` (*proxy* GED : fiche Polarion qui représente le document archivé ailleurs, avec son numéro, son indice et son visa) | Traçabilité sans duplication |

## 2. Catalogue des LiveDocs (synthèse)

Trois workflows documentaires existent (doc. 10 § 5.2) : `wfDocumentFull` (rédaction → relecture → vérification → approbation, trois signatures), `wfDocumentLight` (classe D : rédaction → vérification-approbation en une étape, deux signatures) et `wfDocumentLibrary` (bibliothèques : préparation → approbation → publication versionnée).

| Famille | Types de documents | Workflow |
|---|---|---|
| Spécifications | STB (`stakeholderSpec`, spécification technique de besoin), ST (`systemSpec`, spécification technique système), STE (`equipmentSpec`, spécification technique d'équipement / d'approvisionnement), SRS (`softwareRequirementsSpec`, spécification d'exigences logicielles), CdC outillage (`toolingSpec`, cahier des charges fonctionnel) | `wfDocumentFull` |
| Conception | Dossier de conception système (`systemDesignManual`, SDM), ICD (`interfaceControlDocument`, document de contrôle d'interfaces) | `wfDocumentFull` |
| Sûreté | Dossier de démonstration (`safetyCase`), note de classement / liste des EIP (`classificationList` ; EIP = élément important pour la protection des intérêts, arrêté INB), AMDEC (`fmeaWorksheet`, analyse des modes de défaillance), rapport de sûreté de recharge (`reloadSafetyReport`) | `wfDocumentFull` |
| Conformité | Matrice de conformité (`complianceMatrix`) | `wfDocumentFull` |
| V&V | Plan V&V (`vvPlan`, vérification et validation), procédure d'essais (`testProcedure`) | `wfDocumentFull` |
| Base installée | Dossier de modification (`modificationFile`), note de justification (`justificationNote`) | Full / **Light** |
| Qualification et lots (v0.3) | Dossier de qualification (`qualificationDossier` : procédé, matériel, code de calcul, équivalence), procès-verbal de remise de lot UO → projet (`workPackageHandover`, ADR-24) | Full / **Light** |
| Management | Plans (PQP, PMIS, PGC, PDL… : plan qualité projet, plan de management de l'ingénierie système, plan de gestion de configuration, plan de développement logiciel) (`managementPlan`) | `wfDocumentFull` |
| Bibliothèques | Extrait réglementaire (`regulatoryLibrary`), spécification produit générique (`genericProductSpec`), glossaire (`glossary`) | `wfDocumentLibrary` |

Chaque type déclare dans `model/document_types.yaml` ses types de Work Items autorisés (`allowedTypes`) et son **type principal** (`primaryType`, obligatoirement actif dans toute typologie qui utilise le document). Il déclare aussi les types que le document **pilote en cascade** (`cascadeTypes`) et, le cas échéant, les statuts admis d'autres types à l'approbation (`approvalGate`) — voir § 8.

## 3. Anatomie d'un gabarit

Chaque gabarit (document modèle rangé dans le projet `LIB-TEMPLATES`, copié à l'initialisation de chaque projet) contient :
1. **Page de garde** (champs de document, `documentCustomFields`) : n° de document, indice, titre, classification, contrôle export, phase, langue, AIP (activité importante pour la protection, arrêté INB), paliers applicables, n° de document client, habilitation requise des signataires (`requiredHabilitation`, doc. 21 § 3), UO responsable (`responsibleUnit`).
2. **Cartouche de signatures** : rédacteur / vérificateur / approbateur (`docAuthor`, `docVerifier`, `docApprover`), alimenté par les signatures électroniques du workflow (date, signification). Les signataires sont désignés manuellement ou par le mécanisme d'approbations (*Approvals*) de Polarion.
3. **Historique des révisions** : indice, date, objet de la révision (`revisionSummary`).
4. **Sommaire** et **plan type** (annexe A5), avec des titres (Work Items `heading`) pré-créés.
5. **Blocs d'aide à la rédaction**, en texte non Work Item, masqués à l'export.
6. **Tableaux de traçabilité intégrés** (macros ou *widgets*) : couverture amont, aval et vérification de la section.
7. **Configuration des types autorisés** et formulaires de création restreints au profil de tailoring (doc. 07 § 4).

## 4. Plans types des gabarits principaux

> **Référence unique : [annexe A5](../generated/A5_documents.md)** (générée depuis `outline` de `model/document_types.yaml`, pour les 22 types). Les plans types ne sont plus recopiés ici ; seules les particularités à connaître sont rappelées.

- **STE / spécification d'approvisionnement** : chapitre 2 « classement complet » (sûreté, mécanique / électrique, ESPN — équipement sous pression nucléaire —, K — conditions de qualification —, sismique, ITNS — important pour la sûreté nucléaire, ISO 19443) ; chapitre 5 fabrication et contrôles avec procédés spéciaux, CND (contrôles non destructifs) et **points d'arrêt** (étapes où le fabricant ne peut continuer sans l'accord du client ou de l'inspecteur) ; chapitre 7 qualité avec **CFSI** (articles contrefaits, frauduleux ou suspects) ; annexe = matrice de conformité à remplir par le fournisseur.
- **Cahier des charges fonctionnel d'outillage** : expression fonctionnelle du besoin selon **NF EN 16271** (fonctions de service et de contrainte, critères, niveaux, flexibilité) ; contraintes de site (RP — radioprotection —, contamination, FME — exclusion des corps étrangers —) ; exigences machines (marquage CE ; règlement (UE) 2023/1230 applicable au 20/01/2027 [P\*, doc. 04]).
- **Procédure d'essais** : la séquence (étapes, résultats attendus, critères) est portée par le champ structuré `testSteps` du cas de vérification ; les feuilles de relevés sont les *Test Runs* (campagnes d'exécution natives de Polarion, doc. 10).
- **Note de justification (fortuit)** : critères du code et du RSE-M (code AFCEN de surveillance en exploitation) ; chapitre final « caractère générique et REX » (retour d'expérience), lié au REX capitalisé (`lessonsLearnedCaptured`).
- **Dossier de sûreté** : arborescence des revendications (*claims*), criblage des initiateurs et agressions (`hazard`, `screening`), preuves par renvoi vers la V&V.
- **Plan de management** : plan libre selon le gabarit du plan concerné (PQP, PMIS, PGC, PDL).

## 5. Numérotation, indices et états documentaires

| Élément | Règle |
|---|---|
| N° de document | Attribué par la GED (`documentNumber`) ; **jamais** dérivé de l'ID Polarion (ADR-22) |
| Indice (version diffusée) | Brouillons : A0, A1… Diffusions : A, B, C… (fonction `incrementRevisionIndex`, script `fra-revision-index.js`). Chaque diffusion = baseline (photographie figée du projet) + PDF en GED |
| Visa client | VSO / VSO-SR / VAO / VAOB / REF / pour information (`customerVisa` : vu sans observation / sous réserve / avec observations / avec observations bloquantes / refusé ; codes à confirmer par client) ; VAOB ou REF → nouvel indice (transition `newRevision` du livrable) |
| État documentaire | Workflow du LiveDoc (`wfDocumentFull` : En rédaction, En relecture, En vérification, En approbation, Approuvé, Remplacé) ; « Définitif » (`final`) porté par le `deliverable` associé après visa |

## 6. Relecture et commentaires

- **Relecture interne** : état `inReview`. Commentaires Polarion (fils de discussion ; mentions d'utilisateurs [à vérifier, Q-TOOL-01 : annoncées en 2512]) et approbations des relecteurs désignés (licence REVIEWER : lecture, commentaire et approbation, capacités de signature à confirmer, Q-TOOL-03).
- **Remarques formelles** (revues, client) : Work Items `reviewFinding` liés (rôle `raisedIn`) au livrable ou à la revue. Gravité (`findingSeverity`) alignée sur le visa (bloquante ↔ VAOB). Levée tracée (état `accepted`).
- **Clôture de revue** : aucune remarque bloquante hors états `accepted` / `closed` (condition de `wfReview.close`).

## 7. Exports et échanges documentaires

> Les échanges structurés sont spécifiés au [doc. 22](../partie4/22_Import_export_parsing_connecteurs.md) (ReqIF § 2, import Word § 3, aller-retour Excel § 4) et contrôlés contre le modèle (`model/import_export.yaml`, annexe A11). Ce paragraphe ne garde que ce qui est propre au document.

| Besoin | Mécanisme | Remarques |
|---|---|---|
| PDF officiel signé | Extension d'export PDF (ex. *pdf-exporter* open source [à vérifier, spike S1 : compatibilité avec la version cible]) + gabarit d'entreprise + manifeste de signatures | Versé en GED à l'approbation (fonction `exportToEdms`, connecteur `CX-EDMS`) |
| Word aller-retour | Export / réimport Word natif | Pour les contributeurs externes sans accès ; à limiter (risque de perte de liens). Règles d'analyse W-01..W-11 : doc. 22 § 3 |
| Excel aller-retour | Export / import Excel (tables) | Matrices de conformité fournisseurs (gabarits `XL-*`, doc. 22 § 4) |
| ReqIF | Import / export OMG ReqIF 1.1 / 1.2 (lecture de 1.0.1 si partenaire ancien) [à vérifier sur la version cible], avec gabarits de correspondance (`.polarion/reqif/templates`) | Profils `RIF-*` (doc. 22 § 2) ; échanges avec le client et l'architecte-ensemblier (maître d'œuvre d'ensemble de l'installation, ADR-12) ; réimport mettant à jour le même document |
| Comparaison | Comparaison de révisions / baselines de documents ; fusion à trois sources (*3-way*) [à vérifier, spike S1 / Q-TOOL-01 : annoncée 2404+] | Revues de modifications, branches (doc. 11 § 5) |

## 8. Règles de qualité documentaire (contrôlées)

1. **Cascade document → éléments** (mécanique `primaryType` / `cascadeTypes` / `approvalGate` de `model/document_types.yaml`, conditions de `model/workflows.yaml`) :
   - au passage **en vérification** (`submitVerification`, ou `submit` pour Light / Library), le document soumet en cascade (`invokeOnDocItems`, Polarion `InvokeAction` — annexe D PF-07) les Work Items de ses `cascadeTypes` encore en brouillon ;
   - à **l'approbation**, la condition `cascadedItemsApproved` exige que tous les Work Items des `cascadeTypes` soient approuvés et que les types sous `approvalGate` soient dans les statuts admis (ex. `interface` en `agreed` ou `frozen` dans une ST) — implémentée par `ContainsNoMatchingWorkItems` ; l'approbation du document approuve alors en cascade les éléments concernés.
   - Conséquence : un Work Item approuvé dans un LiveDoc ne porte pas de signature propre ; la **signature électronique est portée par le document** (R / V / A), décision explicitée au doc. 10 § 5.
2. Aucun lien suspect dans le document à la vérification (`noSuspectLinks` sur les éléments du document ; Polarion `ContainsNoMatchingWorkItems(suspect:true)`).
3. Classification du document ≥ classification maximale de ses éléments (rapport) ; aucune classification interdite sur l'instance standard (`noForbiddenClassification`).
4. Types de Work Items conformes au type de document (`allowedTypes`, configuration).
5. Champs de garde complets (`documentNumber`, `revisionIndex`, `aip`, `informationClassification`, `exportControl` : champs requis du document).
