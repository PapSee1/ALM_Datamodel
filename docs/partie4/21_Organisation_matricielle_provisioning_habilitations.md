# 21 — Organisation matricielle, provisioning des projets et signatures habilitées

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **moyenne** (§ 2.2 gabarits, § 4 projets sas et § 5 Collections spécifiques à Polarion) · Historique : [CHANGELOG](../../CHANGELOG.md) · Carte du dépôt : [guide de lecture](../GUIDE_DE_LECTURE.md).*
>
> **En bref**
> - **À quoi sert ce document :** dire comment un projet confie du travail à plusieurs unités (lots de travaux), comment un projet Polarion est créé de façon reproductible (questionnaire et règles de dérivation), comment les signatures peuvent exiger une habilitation nominative, et pourquoi le cloisonnement se fait par projet « sas » et non par Space.
> - **Qui le lit :** SE Referents, guichet de provisioning, Qualité, responsables sécurité de l'information, ingénieur configuration.
> - **À lire avant :** [guide de lecture](../GUIDE_DE_LECTURE.md), doc. 01 (organisation BU / BL / UO), doc. 11 (topologie des projets), doc. 10 (workflows et rôles).
> - **Foyer unique :** ce document est la référence du dépôt pour « le Space n'est pas une frontière de sécurité / projets sas » (§ 4) et pour les « signatures habilitées » (§ 3) ; les autres documents y renvoient.
>
> Ce document traite trois besoins exprimés au fil des échanges :
> 1. représenter le travail **BU × UO** (une *Business Unit*, division de premier niveau, pilote ; plusieurs *unités opérationnelles* — sites, centres d'ingénierie, filiales — réalisent) ;
> 2. **créer les projets de façon reproductible** ;
> 3. permettre que les signatures électroniques soient **adossées aux habilitations métiers**, ce choix étant **une décision prise à la création du projet**.
>
> Modèle : `model/work_item_types.yaml` (`workPackage`), `model/workflows.yaml` (`wfWorkPackage`, `qualifiedSignatory`), `model/project_setup.yaml` (questionnaire, règles de dérivation), `model/project_topology.yaml` (gabarits, conventions de nommage), `model/roles.yaml` (rôles, règles PR-xx). Annexes générées : [A10](../generated/A10_provisioning_et_packs.md) (provisioning et packs), [A6](../generated/A6_roles_permissions.md) (rôles), [A7](../generated/A7_tailoring.md) (héritage des gabarits).
>
> Niveaux de confiance utilisés ici : **[C]** confirmé par une source publique · **[P]** probable · **[H]** hypothèse de modélisation · **[NT]** non trouvé en source ouverte (échelle complète : doc. 05 § 3).

## 1. Organisation matricielle BU × UO

### 1.1 Le besoin

Un projet (remplacement de GV — générateurs de vapeur —, chaudière EPR2 — le nouveau réacteur d'EDF —, recharge de combustible) est piloté par une BU. Il est réalisé par plusieurs UO : centres d'ingénierie, usines (forge, usinage, assemblage), centres d'essais, filiales, partenaires, fournisseurs. Les exigences descendent vers les UO et les preuves remontent. La v0.1 ne savait dire ni **qui réalise**, ni **ce qui a été confié et réceptionné**.

### 1.2 Options étudiées

| Option | Description | Avantages | Inconvénients | Verdict |
|---|---|---|---|---|
| A. Un projet par UO, avec synchronisation des statuts | Chaque UO a son projet ; les statuts V&V (vérification et validation) « remontent » | Autonomie des UO | Doublons d'exigences, synchronisation fragile, traçabilité rompue | Rejetée |
| B. Un Space par UO dans le projet | Rangement par UO (un *Space* est un dossier de rangement des documents et pages d'un projet Polarion) | Simple | Le Space n'est pas une frontière de sécurité (PR-09, § 4) ; pas de contrat ni de réception | Admise pour la **navigation** seulement |
| C. **Lot de travaux (`workPackage`) + attribut `performingUnit`** | Le projet confie des lots signés aux UO ; les artefacts produits sont rattachés au lot | Artefacts uniques, contrat explicite, réception signée, tableau de bord par UO inter-projets | Une discipline de rattachement (TR-18) | **Retenue** (ADR-24) |
| D. Projet d'exécution d'UO + liens inter-projets | L'usine tient son projet (points d'arrêt, FNC usine) lié au projet BU | Autonomie des enregistrements qualité d'usine | Plus de projets à administrer | **Retenue en complément** quand l'UO porte ses propres enregistrements (`P-MFG-*`) |

### 1.3 Le lot de travaux

Le lot de travaux est un *Work Item* (élément de travail unitaire de Polarion, au même titre qu'une exigence ou un cas de vérification) de type `workPackage`. Il matérialise le contrat interne entre le projet et l'UO réalisatrice.

```
projet BU (P-SGR-X)                                    UO réalisatrice
  workPackage WP-12 « Forge des viroles »  ── agree (signature 'agreed') ──▶  workPackageManager
      ▲ inWorkPackage                                                         │ start
      ├── deliverable  (PV, certificats, dossier)                             │ … production …
      ├── verificationCase (points d'arrêt H / W)                             │ deliver (signature 'authored')
      └── nonConformance (FNC usine)                                          ▼
  accept (signature 'accepted', réceptionnaire ≠ responsable de lot) ◀── remise + workPackageHandover
```

Lecture du schéma : PV = procès-verbal ; FNC = fiche de non-conformité ; points H / W = points d'arrêt (*Hold*, l'activité ne peut pas continuer sans l'inspecteur) et points de convocation (*Witness*, l'inspecteur est convoqué mais l'activité peut continuer s'il ne se présente pas).

- **Cycle de vie (`wfWorkPackage`)** : en préparation → accordé → en réalisation → remis → réceptionné, avec annulation possible.
  - L'accord fige le périmètre et les critères de remise ; il est signé par le chef de projet (`projectManager`, signature `agreed`).
  - La remise (signature `authored` du responsable de lot) exige que les livrables rattachés soient approuvés et les FNC du lot soldées ou transférées au projet avec accord tracé.
  - La réception est signée par le projet (signature `accepted`), avec une condition d'indépendance (`approverNotAuthor` : le réceptionnaire n'est pas celui qui a remis).
- **Champs** :
  - `workPackageType` (ingénierie, études de sûreté, fabrication, approvisionnement, essais, travaux sur site, outillage, logiciel, documentation) ;
  - `performingUnit` et `responsibleUnit` (champs communs à tous les types) ;
  - `workPackageScope`, `handoverCriteria` ;
  - `wpManager` (responsable de lot) ;
  - `internalOrderReference` (commande interne, c'est-à-dire l'ordre de travail de l'ERP — progiciel de gestion intégré — qui porte le budget), `budgetHours` ;
  - `progressPercent` (calculé).
- **Règle TR-18** : dans un projet qui comporte des lots, tout livrable en cours de vérification ou au-delà relève d'un lot.
- **Rôles** :
  - `workPackageManager` (responsable de lot côté UO) ;
  - `unitManager` (lecture transverse des artefacts dont `performingUnit` = son UO).
- **Document** : `workPackageHandover` (PV de remise de lot, workflow documentaire léger).

### 1.4 Tableaux de bord par UO

L'attribut `performingUnit` étant commun à tous les types, une requête au niveau du dépôt (`performingUnit.KEY:<UO>`) alimente un tableau de bord **par UO, tous projets confondus** : charge, lots en cours, livrables en retard, FNC ouvertes, points d'arrêt à venir. Aucun projet d'UO n'est nécessaire pour piloter une UO.

### 1.5 Énumération des UO

Les codes réels des UO ne sont pas publics. L'énumération `operationalUnit` est une **amorce** construite à partir de sites publiquement attestés (doc. 01, campagne OSINT — renseignement de sources ouvertes — d'octobre 2026). Elle est à remplacer en atelier (question Q-ORG-01), puis à alimenter depuis le référentiel organisationnel. Au niveau du projet, elle est restreinte aux UO déclarées au provisioning (règle D12). Les Business Lines sont dans l'énumération `businessLine`, les UO dans `operationalUnit`, jamais l'inverse.

## 2. Provisioning des projets

### 2.1 Principe

Aucun projet n'est créé à la main. Un **guichet de provisioning** (rôle global `provisioningOfficer`) instancie un gabarit à partir d'un **questionnaire** dont les réponses deviennent des **paramètres du projet**. Ces paramètres sont lisibles par les scripts de workflow et par les rapports.

Les rôles mis en jeu sont définis dans `model/roles.yaml` (annexe A6) : **7 rôles globaux** (dont `provisioningOfficer`, `habilitationAdministrator`, `designAuthority`) et **34 rôles projet**, dont `libraryDesignAuthority` (autorité de conception d'une bibliothèque ou d'un produit générique, distincte de la Design Authority du modèle) et quatre **pseudo-rôles** qui ne sont pas des rôles Polarion à attribuer : `anyProjectMember`, `documentOwner` (auteur du LiveDoc, réalisé par le script `fra-document-owner.js`), `workitem.assignee` et `workitem.author` (rôles spéciaux Polarion, à confirmer : annexe D, PF-11). Le dossier de provisioning généré liste les rôles projet à pourvoir, c'est-à-dire ceux qui interviennent dans au moins une transition des workflows activés (20 pour le pilote NUWARD).

### 2.2 Gabarits : master → archétypes → spécialisations

| Niveau | Contenu | Maintenu par |
|---|---|---|
| **Master** `TPL-00-MASTER` (non instanciable) | Spaces communs, paramètres obligatoires, tableaux de bord communs, requêtes des règles TR, droits par défaut | Design Authority (autorité de conception du modèle, doc. 17) |
| **6 archétypes** | `TPL-01-PRODUCT` (produit neuf), `TPL-02-IB` (base installée), `TPL-03-EXPRESS` (conteneur express), `TPL-04-SERVICES` (outillages, interventions, essais), `TPL-05-SERIES` (série, commande, qualification), `TPL-06-LIBRARY` (bibliothèque) | Design Authority |
| **Spécialisations** (21) | Uniquement les écarts : Spaces, documents, tableaux de bord (ex. `TPL-IB-PSR`, `TPL-CYBER`, `TPL-SOFTWARE`, `TPL-CTO`, `TPL-EXT`) | Design Authority, sur proposition des SE Referents (référents ingénierie système des BU) |

Seuls le master et les archétypes sont des gabarits complets (28 gabarits au total). Le validateur vérifie que toute spécialisation hérite d'un archétype, que tout archétype hérite du master, et que chaque typologie aboutit à un archétype (annexe A7).

### 2.3 Questionnaire et dérivation

Le questionnaire compte 19 questions (Q01–Q19) :
- typologie (Q01) ;
- BU, Business Line, UO responsable et UO réalisatrices (Q02–Q05) ;
- cadres réglementaires et filières (Q06–Q07) ;
- paliers, schéma de classement de sûreté (Q08–Q09) ;
- classification maximale de l'information, contrôle export, langue (Q10–Q12) ;
- politique de signature (Q13) ;
- échanges client, participants externes (Q14–Q15) ;
- outil MBSE (ingénierie système fondée sur les modèles) et PLM (gestion du cycle de vie du produit, c'est-à-dire la nomenclature) (Q16–Q17) ;
- cotation de tailoring et justification (Q18–Q19).

Les **15 règles de dérivation** (D01–D14 et D06bis), évaluées dans l'ordre — la première règle qui fixe un paramètre l'emporte —, fixent :

| Effet | Règle |
|---|---|
| Gabarit | D01 : gabarit par défaut de la typologie |
| Classe | D02 : cotation, plancher éliminatoire, justification si écart |
| Instance | D03 défense → DEF ; D04 cybersécurité → SENS ; D05 données sensibles → SENS ; D06 export US → US ; **D06bis** potentiel scientifique et technique (PPST / ZRR, `exportControl = frPpst`) → SENS ; D07 sinon STD |
| Packs réglementaires | D08 |
| Projet sas `EXT-*` | D09 : participants externes |
| Lots de travaux | D10 : plusieurs UO réalisatrices |
| Signatures habilitées | D11 |
| Énumérations projet | D12 : tranches, UO, Business Lines |
| Connecteurs | D13 : outil MBSE déclaré (Q16) → `CX-MBSE-CAPELLA` ou `CX-MBSE-CAMEO` ; D14 : PLM déclaré (Q17) → `CX-PLM-TC` ou `CX-PLM-3DX` (fiches au doc. 22 § 5) |

### 2.4 Processus et délais cibles

| Étape | Délai | Contenu |
|---|---|---|
| 1 | J | Demande du chef de projet, assistée par le SE Referent de la BU |
| 2 | J+3 | Cotation de tailoring ; visa Qualité (et Sûreté si classe A ou B, ou si EIP — élément important pour la protection, arrêté INB) |
| 3 | J+5 | Criblage contrôle export et classification, puis choix de l'instance |
| 4 | J+6 | Création automatisée : gabarit, paramètres, énumérations, groupes d'annuaire, projet sas |
| 5 | J+10 | Branchement des bibliothèques et des lignes de produits ; import des données d'entrée |
| 6 | J+15 | Lancement : formation ciblée, plan de management IS (ingénierie système) |
| 7 | M+3 | Revue de démarrage ; retour d'expérience vers la Design Authority |

Un fortuit **n'est pas un projet** : il est créé en quelques minutes comme Space d'un projet conteneur déjà provisionné (`TPL-IB-FORTUIT`).

## 3. Signatures adossées aux habilitations

### 3.1 Le besoin

Dans un projet sensible, le détenteur du rôle projet `verifier` ou `approver` ne suffit pas toujours. Il faut que la personne **détienne l'habilitation nominative du domaine** : études de sûreté, ESP (équipements sous pression) / code de construction, soudage, CND (contrôles non destructifs), C-C (contrôle-commande) de sûreté, criticité, radioprotection, études de cœur, CGD (dédicace d'articles commerciaux : qualification d'un composant du commerce pour un usage de sûreté), cybersécurité, BPF (bonnes pratiques de fabrication, isotopes médicaux). Le demandeur souhaite que ce soit **une décision de paramétrage prise à la création du projet** (ADR-27).

### 3.2 Mécanisme

| Élément | Rôle |
|---|---|
| Paramètre projet `signaturePolicy` (Q13) | `roleBased` (défaut) ou `habilitationBased`. Figé à la création ; son changement relève d'une modification du plan de management approuvée par la Qualité (PR-10). La règle D11 active la condition ci-dessous. |
| Champ `requiredHabilitation` (énumération `habilitationDomain`) | Porté par les analyses, les livrables, les cas de vérification et les LiveDocs (documents vivants Polarion). Pré-rempli selon la discipline (`habilitationDefaults` : sûreté → études de sûreté, CND → CND, C-C → C-C de sûreté…) par le script `fra-habilitation.js` en mode `prefill`, modifiable élément par élément. |
| Groupes d'annuaire `HAB-<domaine>-<niveau>` | Alimentés depuis le référentiel RH-compétences (connecteur `CX-DIRECTORY`). Niveau = `verifier` ou `approver`. Administrés par le rôle global `habilitationAdministrator`. Revue semestrielle (PR-08). |
| Condition `qualifiedSignatory` | Script de workflow (`fra-habilitation.js`) sur les transitions de vérification et d'approbation des analyses, cas de vérification, livrables et documents. **Inopérante si `signaturePolicy = roleBased`.** Sinon, bloque la transition si l'utilisateur n'appartient pas au groupe requis, avec un message explicite. |

Nota : sur les Work Items d'exigence, d'architecture, d'analyse de sûreté et de cas de vérification, il n'y a pas de signature électronique propre ; le contrôle technique y est tracé par les approbations (Approvals) et la signature est portée par le LiveDoc (doc. 10 § 5). La condition `qualifiedSignatory` s'applique donc à l'approbation de l'élément, qu'elle soit signée ou non.

### 3.3 Comportement attendu (cas de test OQ)

OQ = qualification opérationnelle : jeu d'essais prouvant que l'outil configuré se comporte comme spécifié (doc. 15 § 4).

| Cas | Politique | Habilitation de l'utilisateur | Résultat |
|---|---|---|---|
| Approbation d'une note de calcul de sûreté | `roleBased` | — | Autorisée (rôle `verifier` + indépendance) |
| Idem | `habilitationBased` | `HAB-safetyAnalysis-verifier` | Autorisée |
| Idem | `habilitationBased` | Aucune | **Bloquée** : « habilitation études de sûreté requise » |
| Cas de vérification CND | `habilitationBased` | `HAB-nde-verifier` expirée (retirée du groupe) | **Bloquée** |
| Élément sans `requiredHabilitation` (`none`) | `habilitationBased` | — | Autorisée (rôle seul) |

### 3.4 Points de vigilance

- **Source de vérité des habilitations.** Sans référentiel RH à jour, la politique est inapplicable (doc. 20, F-18). Démarrer en `roleBased` puis basculer par modification tracée est préférable à un démarrage bloqué. C'est le choix du pilote NUWARD (`signaturePolicy = roleBased`, doc. 23 § 6.2).
- **Délai de propagation.** La synchronisation d'annuaire n'est pas instantanée. Une habilitation retirée doit être répercutée avant la prochaine signature : synchronisation au minimum quotidienne, et retrait immédiat sur événement RH.
- **Traçabilité.** La signature Polarion enregistre l'utilisateur, la date et la signification. L'habilitation détenue au moment de la signature doit être **archivée** (export du groupe à la date, ou champ d'historique alimenté par le script) pour rester démontrable des années plus tard.

## 4. Projets sas et cloisonnement

Le Space n'est **pas** une frontière de sécurité pour les Work Items (PR-09, ADR-28) : tous les Work Items d'un projet partagent le même tracker, et la recherche et les requêtes ignorent le rangement en Space. Un conteneur ne doit donc jamais mélanger des affaires de clients concurrents ni des données de contrôle export différentes. Le cloisonnement client, fournisseur ou partenaire se fait :

1. par **projet sas** `EXT-<partenaire>-<affaire>` (gabarit `TPL-EXT`, un projet par partenaire et par affaire, créé par la règle D09 dès que le questionnaire déclare des participants externes ou un échange « sas », Q14–Q15). Le sas est alimenté par branchement de documents ou par ReqIF (format d'échange d'exigences, doc. 22 § 2) depuis le projet interne ; jamais par un lien direct qui exposerait le projet interne. Ce qui n'y est pas copié n'existe pas pour l'externe. Ses Spaces : `10-Inbound (shared by Framatome)`, `20-Partner contributions`, `30-Exchange log (ReqIF)` ;
2. à défaut, par des **permissions fondées sur une requête** (*Custom Sets* : un ensemble d'éléments défini par une requête auquel on attache des droits) dans un projet [à vérifier, spike S1]. Ce mécanisme est plus fin, mais plus difficile à auditer. Il est réservé aux cas où le sas est disproportionné ;
3. avec, dans tous les cas, des comptes externes nominatifs à expiration, revus chaque trimestre, sans licence nommée partagée (PR-11), qui n'ont accès qu'aux projets sas et jamais aux requêtes inter-projets (PR-06) ;
4. et des **contrôles d'échange** : tout export est filtré par classification et contrôle export (XC-01), chaque échange est consigné dans le sas (XC-02), aucun fichier externe n'entre directement dans un projet interne (XC-03), les correspondances sont rejouées à chaque montée de version (XC-04) — détail au doc. 22 § 1.

Les rôles externes (`customerReviewer`, `supplierContributor`) n'existent que dans un sas. La formulation « espace fournisseur » ou « espace de collaboration » d'anciens documents désigne toujours un projet sas, jamais un Space.

## 5. Baselines et Collections des affaires de la base installée

Une *baseline* Polarion (révision figée servant de référence de configuration) porte sur **tout** un projet (révision du dépôt) : convention `baselineNaming` = `<projet>-<jalon>-<AAAAMMJJ>`. Dans un projet conteneur (fortuits, modifications, recharges), une baseline par affaire n'a donc pas de sens. On utilise alors une *Collection* (ensemble de documents Polarion pris chacun à une révision donnée) : convention `collectionNaming`, distincte de `baselineNaming` dans `model/project_topology.yaml`. La pratique retenue :

| Besoin | Mécanisme |
|---|---|
| Figer l'état documentaire d'une affaire (fortuit, modification) à sa clôture | **Collection** des LiveDocs de l'affaire à leur révision approuvée, nommée `<projet>-<affaire>-<AAAAMMJJ>` + export PDF/A (format PDF d'archivage, ISO 19005) signé en GED (gestion électronique de documents) |
| Figer l'état d'une tranche après un arrêt | Collection nommée `<projet>-<tranche>-<arrêt>` (ex. `P-SGR-X-T2-VD4`, VD4 = quatrième visite décennale), avec les `unitDeployment` requalifiés |
| Jalons d'un projet dédié (PDR, CDR, FQR : revues de conception préliminaire, critique, et revue formelle de qualification) | Baseline de projet `<projet>-<jalon>-<AAAAMMJJ>` (fonction `createBaseline`) |
| Recharge (tranche × cycle) | Un rapport de sûreté de recharge par tranche × cycle ; Collection par cycle |

L'inclusion des *Test Runs* (campagnes d'exécution de cas de test) dans les Collections dépend de la version de Polarion (confiance P) [à vérifier, spike S1 / Q-TOOL-01].
