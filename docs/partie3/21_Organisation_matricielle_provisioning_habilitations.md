# 21 — Organisation matricielle, provisioning des projets et signatures habilitées

> Version 0.3. Ce document traite trois besoins exprimés au fil des échanges :
> 1. représenter le travail **BU × UO** (une BU pilote, plusieurs UO réalisent) ;
> 2. **créer les projets de façon reproductible** ;
> 3. permettre que les signatures électroniques soient **adossées aux habilitations métiers**, ce choix étant **une décision prise à la création du projet**.
>
> Modèle : `model/work_item_types.yaml` (`workPackage`), `model/workflows.yaml` (`wfWorkPackage`, `qualifiedSignatory`), `model/project_setup.yaml`. Annexe générée : [A10](../generated/A10_provisioning_et_packs.md).

## 1. Organisation matricielle BU × UO

### 1.1 Le besoin

Un projet (remplacement de GV, chaudière EPR2, recharge) est piloté par une BU. Il est réalisé par plusieurs UO : centres d'ingénierie, usines (forge, usinage, assemblage), centres d'essais, filiales, partenaires, fournisseurs. Les exigences descendent vers les UO et les preuves remontent. La v0.1 ne savait dire ni **qui réalise**, ni **ce qui a été confié et réceptionné**.

### 1.2 Options étudiées

| Option | Description | Avantages | Inconvénients | Verdict |
|---|---|---|---|---|
| A. Un projet par UO, avec synchronisation des statuts | Chaque UO a son projet ; les statuts V&V « remontent » | Autonomie des UO | Doublons d'exigences, synchronisation fragile, traçabilité rompue | Rejetée |
| B. Un Space par UO dans le projet | Rangement par UO | Simple | Le Space n'est pas une frontière de sécurité (PR-09) ; pas de contrat ni de réception | Admise pour la **navigation** seulement |
| C. **Lot de travaux (`workPackage`) + attribut `performingUnit`** | Le projet confie des lots signés aux UO ; les artefacts produits sont rattachés au lot | Artefacts uniques, contrat explicite, réception signée, tableau de bord par UO inter-projets | Une discipline de rattachement (TR-18) | **Retenue** (ADR-24) |
| D. Projet d'exécution d'UO + liens inter-projets | L'usine tient son projet (points d'arrêt, FNC usine) lié au projet BU | Autonomie des enregistrements qualité d'usine | Plus de projets à administrer | **Retenue en complément** quand l'UO porte ses propres enregistrements (`P-MFG-*`) |

### 1.3 Le lot de travaux

```
projet BU (P-SGR-X)                                    UO réalisatrice
  workPackage WP-12 « Forge des viroles »  ── agree (signature 'agreed') ──▶  workPackageManager
      ▲ inWorkPackage                                                         │ start
      ├── deliverable  (PV, certificats, dossier)                             │ … production …
      ├── verificationCase (points d'arrêt H / W)                             │ deliver (signature 'authored')
      └── nonConformance (FNC usine)                                          ▼
  accept (signature 'accepted', réceptionnaire ≠ responsable de lot) ◀── remise + workPackageHandover
```

- **Cycle de vie (`wfWorkPackage`)** : en préparation → accordé → en réalisation → remis → réceptionné, avec annulation possible.
  - L'accord fige le périmètre et les critères de remise ; il est signé par le chef de projet.
  - La remise exige que les livrables rattachés soient approuvés et les FNC du lot soldées ou transférées.
  - La réception est signée par le projet, avec une condition d'indépendance.
- **Champs** :
  - `workPackageType` ;
  - `performingUnit` et `responsibleUnit` (champs communs) ;
  - `workPackageScope`, `handoverCriteria` ;
  - `internalOrderReference` (commande interne), `budgetHours` ;
  - `progressPercent` (calculé).
- **Règle TR-18** : dans un projet qui comporte des lots, tout livrable en cours de vérification ou au-delà relève d'un lot.
- **Rôles** :
  - `workPackageManager` (responsable de lot côté UO) ;
  - `unitManager` (lecture transverse des artefacts dont `performingUnit` = son UO).
- **Document** : `workPackageHandover` (PV de remise de lot, workflow léger).

### 1.4 Tableaux de bord par UO

L'attribut `performingUnit` étant commun à tous les types, une requête au niveau du dépôt (`performingUnit.KEY:<UO>`) alimente un tableau de bord **par UO, tous projets confondus** : charge, lots en cours, livrables en retard, FNC ouvertes, points d'arrêt à venir. Aucun projet d'UO n'est nécessaire pour piloter une UO.

### 1.5 Énumération des UO

Les codes réels des UO ne sont pas publics. L'énumération `operationalUnit` est une **amorce** construite à partir de sites publiquement attestés. Elle est à remplacer en atelier (question Q-ORG-01), puis à alimenter depuis le référentiel organisationnel. Au niveau du projet, elle est restreinte aux UO déclarées au provisioning (règle D12).

## 2. Provisioning des projets

### 2.1 Principe

Aucun projet n'est créé à la main. Un **guichet de provisioning** (rôle global `provisioningOfficer`) instancie un gabarit à partir d'un **questionnaire** dont les réponses deviennent des **paramètres du projet**. Ces paramètres sont lisibles par les scripts de workflow et par les rapports.

### 2.2 Gabarits : master → archétypes → spécialisations

| Niveau | Contenu | Maintenu par |
|---|---|---|
| **Master** `TPL-00-MASTER` (non instanciable) | Spaces communs, paramètres obligatoires, tableaux de bord communs, requêtes des règles TR, droits par défaut | Design Authority |
| **6 archétypes** | `TPL-01-PRODUCT` (produit neuf), `TPL-02-IB` (base installée), `TPL-03-EXPRESS` (conteneur express), `TPL-04-SERVICES` (outillages, interventions, essais), `TPL-05-SERIES` (série, commande, qualification), `TPL-06-LIBRARY` | Design Authority |
| **Spécialisations** (21) | Uniquement les écarts : Spaces, documents, tableaux de bord (ex. `TPL-IB-PSR`, `TPL-CYBER`, `TPL-SOFTWARE`, `TPL-CTO`, `TPL-EXT`) | Design Authority, sur proposition des SE Referents |

Seuls le master et les archétypes sont des gabarits complets. Le validateur vérifie que toute spécialisation hérite d'un archétype, que tout archétype hérite du master, et que chaque typologie aboutit à un archétype (annexe A7).

### 2.3 Questionnaire et dérivation

Le questionnaire compte 19 questions :
- typologie ;
- BU, Business Line, UO responsable et UO réalisatrices ;
- cadres réglementaires et filières ;
- paliers, schéma de classement ;
- classification maximale, contrôle export, langue ;
- politique de signature ;
- échanges client, participants externes ;
- outil MBSE, PLM ;
- cotation de tailoring et justification.

Les **13 règles de dérivation** fixent :

| Effet | Règle |
|---|---|
| Gabarit | D01 : gabarit par défaut de la typologie |
| Classe | D02 : cotation, plancher éliminatoire, justification si écart |
| Instance | D03 défense → DEF ; D04 cybersécurité → SENS ; D05 données sensibles → SENS ; D06 export US → US ; D07 sinon STD |
| Packs réglementaires | D08 |
| Projet sas `EXT-*` | D09 : participants externes |
| Lots de travaux | D10 : plusieurs UO réalisatrices |
| Signatures habilitées | D11 |
| Énumérations projet | D12 : tranches, UO, Business Lines |
| Connecteurs MBSE | D13 |

### 2.4 Processus et délais cibles

| Étape | Délai | Contenu |
|---|---|---|
| 1 | J | Demande du chef de projet, assistée par le SE Referent de la BU |
| 2 | J+3 | Cotation de tailoring ; visa Qualité (et Sûreté si classe A ou B, ou si EIP) |
| 3 | J+5 | Criblage contrôle export et classification, puis choix de l'instance |
| 4 | J+6 | Création automatisée : gabarit, paramètres, énumérations, groupes d'annuaire, projet sas |
| 5 | J+10 | Branchement des bibliothèques et des lignes de produits ; import des données d'entrée |
| 6 | J+15 | Lancement : formation ciblée, plan de management IS |
| 7 | M+3 | Revue de démarrage ; retour d'expérience vers la Design Authority |

Un fortuit **n'est pas un projet** : il est créé en quelques minutes comme Space d'un projet conteneur déjà provisionné (`TPL-IB-FORTUIT`).

## 3. Signatures adossées aux habilitations

### 3.1 Le besoin

Dans un projet sensible, le détenteur du rôle projet `verifier` ou `approver` ne suffit pas toujours. Il faut que la personne **détienne l'habilitation nominative du domaine** : études de sûreté, ESP / code, soudage, CND, C-C de sûreté, criticité, radioprotection, études de cœur, CGD, cybersécurité, BPF. Le demandeur souhaite que ce soit **une décision de paramétrage prise à la création du projet**.

### 3.2 Mécanisme

| Élément | Rôle |
|---|---|
| Paramètre projet `signaturePolicy` (Q13) | `roleBased` (défaut) ou `habilitationBased`. Figé à la création ; son changement relève d'une modification du plan de management approuvée par la Qualité (PR-10). |
| Champ `requiredHabilitation` (énumération `habilitationDomain`) | Porté par les analyses, livrables, cas de vérification et LiveDocs. Pré-rempli selon la discipline (`habilitationDefaults` : sûreté → études de sûreté, CND → CND, C-C → C-C de sûreté…), modifiable élément par élément. |
| Groupes d'annuaire `HAB-<domaine>-<niveau>` | Alimentés depuis le référentiel RH-compétences (connecteur `CX-DIRECTORY`). Administrés par le rôle global `habilitationAdministrator`. Revue semestrielle (PR-08). |
| Condition `qualifiedSignatory` | Script de workflow (`fra-habilitation.js`) sur les transitions de vérification et d'approbation des analyses, cas de vérification, livrables et documents. **Inopérante si `signaturePolicy = roleBased`.** Sinon, bloque la transition si l'utilisateur n'appartient pas au groupe requis, avec un message explicite. |

### 3.3 Comportement attendu (cas de test OQ)

| Cas | Politique | Habilitation de l'utilisateur | Résultat |
|---|---|---|---|
| Approbation d'une note de calcul de sûreté | `roleBased` | — | Autorisée (rôle `verifier` + indépendance) |
| Idem | `habilitationBased` | `HAB-safetyAnalysis-verifier` | Autorisée |
| Idem | `habilitationBased` | Aucune | **Bloquée** : « habilitation études de sûreté requise » |
| Cas de vérification CND | `habilitationBased` | `HAB-nde-verifier` expirée (retirée du groupe) | **Bloquée** |
| Élément sans `requiredHabilitation` (`none`) | `habilitationBased` | — | Autorisée (rôle seul) |

### 3.4 Points de vigilance

- **Source de vérité des habilitations.** Sans référentiel RH à jour, la politique est inapplicable (doc. 20, F-18). Démarrer en `roleBased` puis basculer par modification tracée est préférable à un démarrage bloqué.
- **Délai de propagation.** La synchronisation d'annuaire n'est pas instantanée. Une habilitation retirée doit être répercutée avant la prochaine signature : synchronisation au minimum quotidienne, et retrait immédiat sur événement RH.
- **Traçabilité.** La signature Polarion enregistre l'utilisateur, la date et la signification. L'habilitation détenue au moment de la signature doit être **archivée** (export du groupe à la date, ou champ d'historique alimenté par le script) pour rester démontrable des années plus tard.

## 4. Projets sas et cloisonnement

Le Space n'est **pas** une frontière de sécurité pour les Work Items (PR-09) : la recherche et les requêtes ignorent le rangement. Le cloisonnement client, fournisseur ou partenaire se fait donc :

1. par **projet sas** `EXT-<partenaire>-<affaire>` (gabarit `TPL-EXT`), alimenté par branchement de documents ou par ReqIF depuis le projet interne. Ce qui n'y est pas copié n'existe pas pour l'externe ;
2. à défaut, par des **permissions fondées sur une requête** (Custom Sets) dans un projet. Ce mécanisme est plus fin, mais plus difficile à auditer. Il est réservé aux cas où le sas est disproportionné ;
3. avec, dans tous les cas, des comptes externes nominatifs à expiration (PR-11) et un journal des échanges (XC-02).

## 5. Baselines des affaires de la base installée

Une baseline Polarion porte sur **tout** un projet (révision du dépôt). Dans un projet conteneur (fortuits, modifications, recharges), une baseline par affaire n'a donc pas de sens. La pratique retenue est la suivante :

| Besoin | Mécanisme |
|---|---|
| Figer l'état documentaire d'une affaire (fortuit, modification) à sa clôture | **Collection** des LiveDocs de l'affaire à leur révision approuvée + export PDF/A signé en GED |
| Figer l'état d'une tranche après un arrêt | Collection nommée `<projet>-<tranche>-<arrêt>` (ex. `P-SGR-X-T2-VD4`), avec les `unitDeployment` requalifiés |
| Jalons d'un projet dédié (PDR, CDR, FQR) | Baseline de projet `<projet>-<jalon>-<AAAAMMJJ>` (fonction `createBaseline`) |
| Recharge (tranche × cycle) | Un rapport de sûreté de recharge par tranche × cycle ; collection par cycle |

L'inclusion des Test Runs dans les Collections dépend de la version de Polarion (confiance P). À vérifier en maquette sur la version cible.
