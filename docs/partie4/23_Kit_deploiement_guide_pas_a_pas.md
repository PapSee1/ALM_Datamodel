# 23 — Kit de déploiement : inventaire, reste à construire et guide pas à pas jusqu'au pilote NUWARD

> Version 0.4. Ce document répond à la question : *« avec ce dépôt, puis-je configurer Polarion et démarrer un premier projet ? »*
>
> **Réponse courte : pas encore, mais le chemin est balisé.** Le dépôt contient :
> - la **conception complète** (le « 150 % », validé) ;
> - la **configuration déclarative du cœur**, générée : types, champs, énumérations, statuts, rôles de liens, workflows, types de documents ;
> - le **kit de provisioning du pilote NUWARD**.
>
> Il ne contient pas encore ce qui se **construit dans l'instance** ou se **développe** : scripts de workflow, formulaires, gabarits de LiveDocs, tableaux de bord, permissions, gabarits de projets, contenu des bibliothèques, dossier de validation. Ce document en fait l'inventaire, chiffre le reste à faire en ordres de grandeur et donne la séquence pas à pas.

## 1. Inventaire : ce qui est prêt, ce qui reste à construire

Légende :
- ✅ prêt dans le dépôt (à vérifier une fois sur l'instance cible) ;
- 🟡 spécifié, à construire ;
- ❌ hors dépôt.

| # | Élément de configuration | État | Où dans le dépôt | Reste à faire |
|---|---|---|---|---|
| 1 | Types de Work Items, champs personnalisés, énumérations, statuts, rôles de liens et règles | ✅ | `generated/polarion/{fr,en}/.polarion/tracker/fields/` (247 fichiers par langue) | Spike de conformité sur la version cible (S1) |
| 2 | Workflows des Work Items et des documents (états, transitions, rôles, champs requis, conditions natives, signatures) | ✅ | `…/tracker/workflow/`, `…/documents/workflow/` | Idem S1 ; dépend des scripts (ligne 5) |
| 3 | Types de documents, champs de document, statuts de documents, statuts de Test Runs | ✅ | `…/documents/fields/`, `…/testing/` | S1 |
| 4 | Surcharges de configuration du projet pilote | ✅ | `generated/projects/P-NUWARD-L1/` + [dossier de provisioning](../../generated/projects/P-NUWARD-L1/provisioning-record.md) | Confirmer les réponses H (atelier C4, doc. 24) |
| 5 | **15 scripts de workflow** (`fra-*.js`) | 🟡 | Spécification : catalogue des conditions et fonctions (`model/workflows.yaml`), doc. 10 § 4, § 3 ci-dessous | Développement + tests (S3) |
| 6 | Formulaires (form layouts) par type | 🟡 | Ordre et regroupement des champs = ordre du modèle (fieldSets) | Construction (S4) ; génération possible après S1 |
| 7 | Rôles projet, permissions, champs protégés, groupes d'annuaire | 🟡 | `model/roles.yaml`, annexe A6 | Paramétrage (S2) |
| 8 | Gabarits de LiveDocs (contenu, consignes de rédaction, exemples) | 🟡 | Plans types : annexe A5, doc. 12 | Construction dans `LIB-TEMPLATES` (S6) |
| 9 | Tableaux de bord et LiveReports | 🟡 | Catalogue des indicateurs et tableaux par rôle (doc. 13), exemple Velocity | Construction (S7) |
| 10 | Requêtes des règles de traçabilité TR-01..20 | 🟡 | `model/link_roles.yaml`, annexe A3 | Écriture et validation des requêtes (S7) |
| 11 | Configuration Testing (types de Test Run, gabarits, étapes, rôle `verifies` pour la couverture) | 🟡 | Statuts générés ; ADR-19 | Paramétrage (S5) |
| 12 | Export PDF signé + manifeste + versement en GED | 🟡 | Fonction `exportToEdms`, connecteur `CX-EDMS` | Extension ou développement (après S12, export manuel au pilote) |
| 13 | Gabarits de projets (master, archétype, spécialisation, sas) | 🟡 | `model/project_topology.yaml`, doc. 21 § 2 | Construction (S8) |
| 14 | Provisioning (questionnaire, dérivation, kit projet) | ✅ / 🟡 | `model/project_setup.yaml`, `tools/generate_project.py` | Automatisation de la création par API : optionnelle (manuelle au pilote) |
| 15 | Contenu des bibliothèques (réglementaire, terminologie, cas V&V génériques) | ❌ | Structure seulement | Saisie et paraphrase (S9), licences de normes |
| 16 | Intégrations (ReqIF, Capella, PLM, GED, annuaire) | 🟡 | `model/import_export.yaml`, annexe A11, doc. 22 | Paramétrage / développement (S11) |
| 17 | Notifications, tâches planifiées (recalcul nocturne de `verificationStatus`) | 🟡 | Fonctions `notifyRoles`, `recomputeVerificationStatus` | Avec les scripts (S3) |
| 18 | Dossier de validation de l'outil (exigences utilisateur, analyse de risques, protocoles IQ / OQ / PQ) | 🟡 | Doc. 15 ; cas OQ dérivables des conditions bloquantes et des scénarios A9 | Rédaction et exécution (S12) |
| 19 | Supports de formation | 🟡 | Parcours : doc. 24 ; cursus par rôle : doc. 16 § 7 | Production (S12) |
| 20 | Infrastructure, installation, licences | ❌ | Exigences : doc. 15 | DSI + éditeur (S0) |

## 2. Effort restant jusqu'au démarrage du pilote (ordres de grandeur)

> **Hypothèses [H]** à affiner avec Siemens et l'éventuel intégrateur :
> - équipe interne formée (doc. 24) ;
> - version cible connue ;
> - périmètre = tranche du pilote NUWARD (28 types, 9 documents, 6 tableaux de bord).
>
> Unité : jour·homme.

| Étape | Lot | Effort | Porteur conseillé |
|---|---|---|---|
| S1 | Spike de conformité de la configuration générée | 10 – 15 | Interne (ingénieur configuration) + 3 à 5 j d'expert Siemens |
| S2 | Identité, rôles, permissions, groupes | 8 – 12 | Interne + DSI |
| S3 | Scripts « socle » (priorité P0, § 3) et tests | 30 – 45 | Interne, accompagné par Siemens (cadre de développement, API) |
| S4 | Formulaires des 28 types activés | 10 – 14 | Interne |
| S5 | Configuration Testing | 3 – 5 | Interne |
| S6 | 9 gabarits de LiveDocs du pilote | 18 – 27 | SE Referents + ingénieur configuration |
| S7 | Requêtes TR + 6 tableaux de bord | 20 – 30 | Interne ; intégrateur en renfort possible |
| S8 | Gabarits master, archétype, spécialisation, sas | 6 – 10 | Interne |
| S9 | Bibliothèques minimales (extraits utiles au lot, glossaire) | 15 – 25 | SE + licensing |
| S10 | Provisioning du pilote | 3 – 5 | Guichet de provisioning |
| S11 | Profil ReqIF client (test sur fichier de référence) | 5 – 10 | Interne + interlocuteur client |
| S12 | OQ du périmètre pilote + formation des utilisateurs pilotes | 35 – 55 | Qualité + interne ; intégrateur possible pour l'exécution des OQ |
| **Total socle pilote** | | **≈ 165 – 255** | |
| Options | Scripts P1 (12 – 20), synchronisation Capella (20 – 40), export GED automatisé (10 – 20) | + 42 – 80 | Siemens / intégrateur sous votre pilotage |

**Lecture :** avec une équipe cœur de 2 à 3 ETP dédiés, environ 40 à 60 j·h par mois, l'équipe doit construire environ 4 à 6 mois après la fin des ateliers. Cela correspond aux phases « fondations » et « préparation des pilotes » du doc. 16. Un intégrateur sert à **absorber les pics** (formulaires, gabarits, tableaux de bord, exécution des OQ) : la conception et les scripts du socle restent internes.

## 3. Les scripts de workflow

La configuration générée appelle 15 scripts.

> **Règle de déploiement.** Aucun workflow n'est déployé en production avant que les scripts qu'il appelle existent et soient testés. Le comportement d'une condition dont le script est absent est à vérifier au spike [P]. En bac à sable, des **bouchons journalisés** sont admis, clairement identifiés. Un bouchon « toujours vrai » est **interdit hors bac à sable** : il désactiverait le contrôle technique.

| Script | Occurrences* | Rôle | Priorité pilote | Cas de test OQ minimaux |
|---|---|---|---|---|
| `fra-independence.js` | 73 | L'utilisateur qui vérifie ou approuve n'est ni l'auteur ni le dernier rédacteur | **P0** | Auteur bloqué ; dernier modificateur bloqué ; tiers autorisé |
| `fra-field-rule.js` | 25 | Règles de valeur (`notIn`, `nonEmptyIf`, `onlyIfProjectSetting`…) | **P0** | Chaque forme de règle présente dans le modèle |
| `fra-link-cardinality.js` | 24 | Cardinalités et statuts des liens (min, exactement, référence approuvée…) | **P0** | 0 / 1 / 2 liens ; lien vers élément au mauvais statut |
| `fra-no-suspect.js` | 19 | Aucun lien suspect sur les rôles listés | **P0** | Lien suspect bloque ; levée de suspicion débloque |
| `fra-classification.js` | 11 | Pas de classification interdite sur l'instance standard | **P0** | `sensitiveSecurity` bloque sur STD |
| `fra-safety-approval.js` | 10 | Avis Sûreté présent si la condition de sûreté est vraie | **P0** | Exigence définie sans avis bloquée ; avec avis autorisée |
| `fra-request-safety-approval.js` | 9 | Ajoute un approbateur Sûreté si nécessaire | **P0** | Ajout conditionnel |
| `fra-revision-index.js` | 23 | Incrément de l'indice documentaire | **P0** | A → B ; brouillons A0 / A1 |
| `fra-baseline.js` | 23 | Baseline nommée à l'approbation | **P0** | Nom conforme à la convention |
| `fra-habilitation.js` | 22 | Signataire habilité (ADR-27) | **P0 version minimale** : neutre si `signaturePolicy = roleBased` ; complète avant tout projet `habilitationBased` | Les 5 cas du doc. 21 § 3.3 |
| `fra-export-edms.js` | 20 | Export PDF + manifeste vers la GED | P1 (export manuel tracé au pilote) | PDF/A, manifeste, référence GED retournée |
| `fra-notify.js` | 8 | Notifications ciblées | P1 | Destinataires corrects |
| `fra-verification-status.js` | 6 | Recalcul de `verificationStatus` | P1 (+ tâche nocturne) | Exigence vérifiée / partielle / non vérifiée |
| `fra-lock-fields.js` | 1 | Verrouillage du texte original après acceptation | P1 | Modification refusée après acceptation |
| `fra-sla.js` | 2 | Échéance de réponse (fortuits) | INC-2 (hors pilote NUWARD) | Calcul de l'échéance selon l'urgence |

\* Occurrences dans la configuration générée (une langue), toutes transitions confondues.

**Méthode recommandée :**
- un **cadre commun** (lecture des paramètres, messages, journalisation) développé avec l'expert Siemens ;
- puis un script par semaine, chacun avec ses cas de test.

Les scripts sont versionnés dans ce dépôt (dossier `scripts/` à créer) et déployés comme la configuration. Leur emplacement sur le serveur et leur moteur (JavaScript) sont à confirmer pour la version cible [P].

## 4. Mécanique de déploiement de la configuration

| Sujet | Règle |
|---|---|
| Stockage | Polarion conserve sa configuration dans son dépôt : configuration **globale** dans le dossier `.polarion` à la racine ; configuration **projet** dans le dossier `.polarion` du projet [P, à confirmer au spike pour la version cible] |
| Livraison | Le gestionnaire de configuration globale dépose une **version étiquetée** de ce dépôt (`generated/…`) en DEV, puis RECETTE, puis PROD. Jamais d'édition directe en production. |
| Rechargement | Certains éléments sont pris en compte à chaud, d'autres demandent un rechargement ou une réindexation. La procédure exacte est établie au spike et consignée ici. |
| Scripts | Déposés sur le serveur (chaque nœud en grappe), versionnés dans ce dépôt [P] |
| Aller-retour | Une configuration mise au point **dans l'interface d'administration en DEV** (formulaires, pages) est rapatriée dans le dépôt avant toute promotion. Le générateur fait foi pour tout ce qu'il produit : une modification manuelle d'un fichier généré serait écrasée. |
| Surcharges projet | Uniquement les fichiers listés dans `model/extension_policy.yaml` (`overridableProjectFiles`), produits par `tools/generate_project.py` |

## 5. Guide pas à pas (de l'instance vide au pilote)

Chaque étape : objectif, entrées, actions, critère de fin. Les durées sont indicatives et se recouvrent partiellement.

### S0 — Prérequis (avant les ateliers C2 / C3)

- **Entrées :** doc. 15 (infrastructure), ADR-03, ADR-18, ADR-21.
- **Actions :**
  - instance de **développement** de la version cible (et bac à sable) ;
  - licences de développement ;
  - accès administrateur au dépôt de configuration ;
  - poste d'intégration continue (Python 3, PyYAML) ;
  - désignation de l'ingénieur configuration.
- **Fin :** l'instance de développement répond ; le dépôt de configuration est accessible ; la CI de ce dépôt tourne.

### S1 — Spike de conformité (2 à 3 semaines)

- **Entrées :** `generated/polarion/en/.polarion/` (puis `fr`).
- **Actions :**
  1. Déposer la configuration globale générée en DEV.
  2. Vérifier le chargement sans erreur des types, champs, énumérations, rôles de liens, workflows et types de documents.
  3. Créer un élément de chaque type.
  4. Jouer une transition par workflow, scripts en bouchons journalisés.
  5. Créer un lien par rôle, y compris inter-projets.
  6. Noter chaque écart de format.
  7. **Corriger le générateur, pas les fichiers.**
- **Fin :** 0 erreur de chargement ; liste des formats confirmés ; générateur v1 aligné sur la version cible ; procédure de rechargement documentée (§ 4).

### S2 — Identité, rôles, permissions

- **Entrées :** `model/roles.yaml`, annexe A6, règles PR-01..PR-11.
- **Actions :**
  - créer les rôles projet ;
  - accorder les permissions par famille et par état ;
  - protéger les champs de sûreté (PR-02), l'édition des éléments approuvés (PR-03) et l'abaissement du contrôle export (PR-07) ;
  - interdire la suppression (PR-01) ;
  - relier les rôles aux groupes d'annuaire ;
  - activer l'authentification alternative pour les signatures si SSO (PR-04).
- **Fin :** jeu de comptes de test par rôle ; matrice de droits vérifiée par échantillonnage.

### S3 — Scripts du socle

- **Entrées :** § 3, `model/workflows.yaml` (catalogue des conditions et fonctions).
- **Actions :** développer le cadre commun puis les scripts P0 ; tests unitaires et cas OQ associés.
- **Fin :** scripts P0 en service en DEV ; cas OQ P0 au vert.

### S4 — Formulaires

- **Actions :**
  - un formulaire par type activé, sections par jeu d'attributs (commun, exigence, sûreté, classement…) ;
  - champs calculés en lecture seule ;
  - aide contextuelle sur les champs de sûreté.
- **Fin :** revue par deux utilisateurs pilotes.

### S5 — Configuration Testing

- **Actions :**
  - types de Test Run (campagne d'essais, revue / analyse, inspection) ;
  - gabarits de Test Run ;
  - colonnes des étapes ;
  - rôle `verifies` déclaré pour la couverture ;
  - statuts et résultats (générés).
- **Fin :** une campagne complète jouée en DEV, résultat signé.

### S6 — Gabarits de LiveDocs du pilote

- **Entrées :** annexe A5 (plans types et types autorisés), doc. 12.
- **Actions :** construire les 9 documents du pilote dans `LIB-TEMPLATES` :
  - STB, ST, SDM, note de classement, ICD ;
  - chapitre de démonstration de sûreté ;
  - matrice de conformité ;
  - plan V&V ;
  - PV de remise de lot.

  Chacun comprend les consignes de rédaction (EARS, règles de qualité du doc. 13 § 4) et un exemple par chapitre.
- **Fin :** chaque gabarit est instancié une fois et parcourt son workflow documentaire jusqu'à l'approbation.

### S7 — Requêtes et tableaux de bord

- **Entrées :** doc. 13, règles TR (annexe A3).
- **Actions :**
  - requêtes des règles TR utiles au pilote (TR-01..TR-14, TR-18) ;
  - 6 pages : chef de projet, exigences, sûreté, V&V, CCB / configuration, UO réalisatrice.
- **Fin :** chaque indicateur est vérifié sur un jeu de données de test dont le résultat est connu. Les traces du scénario `newBuildSmr` de l'annexe A9 servent de jeu de référence.

### S8 — Gabarits de projets

- **Actions :**
  - construire le master, puis l'archétype `TPL-01-PRODUCT`, puis la spécialisation `TPL-NEWBUILD` (doc. 21 § 2.2) et le gabarit sas `TPL-EXT` ;
  - y placer les gabarits de documents, les pages, les requêtes et les plans.
- **Fin :** la création d'un projet de test depuis `TPL-NEWBUILD` donne la configuration attendue.

### S9 — Bibliothèques minimales

- **Actions :**
  - pour le pack `frAsnr` + `intlIaea`, saisir **seulement** les extraits utiles au lot pilote, en références et paraphrases (ADR-14) ;
  - amorcer le glossaire ;
  - publier par le workflow de bibliothèque.
- **Fin :** les documents de bibliothèque sont publiés et une branche de test est créée dans un projet de test.

### S10 — Provisioning du pilote

- **Entrées :** `model/pilots/P-NUWARD-L1.yaml`, [dossier de provisioning](../../generated/projects/P-NUWARD-L1/provisioning-record.md).
- **Actions :**
  1. Confirmer les réponses de confiance H (atelier C4).
  2. Régénérer le kit.
  3. Créer le projet depuis `TPL-NEWBUILD`.
  4. Déposer les surcharges projet générées.
  5. Créer le projet sas `EXT-…`.
  6. Alimenter les groupes et attribuer les licences.
- **Fin :** la liste de contrôle du dossier de provisioning (§ 8) est cochée.

### S11 — Échanges

- **Actions :**
  - profil `RIF-CUSTOMER-IN` testé avec le client sur un fichier de référence, ré-import d'une révision compris ;
  - profil de retour de conformité.
  - La synchronisation Capella est activée dans un second temps, si le lot pilote dispose d'un modèle (option).
- **Fin :** les cas OQ d'échange du doc. 22 § 7 sont au vert.

### S12 — Validation et formation, go / no-go

- **Actions :**
  - exécuter les OQ du périmètre pilote (conditions bloquantes, signatures, échanges, indicateurs) ;
  - former les utilisateurs pilotes par rôle (doc. 16 § 7) ;
  - tenir la revue go / no-go.
- **Fin :** PV de go signé (Qualité, Sûreté, chef de projet pilote, responsable IS).

### S13 — Pilote en production, puis retour d'expérience

- **Actions :**
  - support rapproché les 4 premières semaines ;
  - revue à M+3 : indicateurs SC-01..SC-06 ;
  - revue des extensions locales, avec promotion ou retrait (doc. 25) ;
  - ouverture de l'incrément INC-2.

## 6. Le pilote NUWARD : avis et kit

### 6.1 NUWARD en premier pilote : oui, à trois conditions

| Pour | Contre / risque |
|---|---|
| Classe A : le pilote éprouve **tout** le cœur (exigences, RFLP, sûreté, V&V, DM, documents signés) | Cycle long : la valeur se voit tard ; un pilote qui « ne finit pas » démobilise |
| Phase de conception amont : pas d'historique à migrer | Conception réorientée en 2024 [C] : besoin client mouvant, révisions fréquentes |
| Échange client réel (ReqIF), MBSE, multi-autorités : cas d'usage exigeants et visibles | Programme multipartenaire : propriété des données et sécurité à clarifier avec le client |
| Forte visibilité : effet d'entraînement | **Risque de sur-ajuster le cœur à la classe A**, trop lourd ensuite pour les fortuits et l'outillage |

**Conditions :**
1. **Découper :** un système ou un lot du périmètre Framatome, sur 4 à 6 mois de production réelle. Pas le programme entier.
2. **Ajouter un pilote court** (fortuit ou outillage, incrément INC-2), lancé environ 2 mois après NUWARD. Il éprouve l'extrémité légère du modèle **avant** le gel du cœur.
3. **Respecter les prérequis :** pas de démarrage sans scripts P0 testés, sans gabarits des 4 documents principaux, ni sans profil ReqIF testé avec le client.

### 6.2 Contenu du kit `P-NUWARD-L1`

| Élément | Fichier |
|---|---|
| Fiche de provisioning (réponses, confiance, tranche activée, critères de succès) | `model/pilots/P-NUWARD-L1.yaml` |
| Dossier de provisioning généré | [`provisioning-record.md`](../../generated/projects/P-NUWARD-L1/provisioning-record.md) |
| Paramètres dérivés | Classe A (score 19), archétype `TPL-01-PRODUCT`, gabarit `TPL-NEWBUILD`, instance STD, packs `frAsnr` + `intlIaea`, projet sas, lots de travaux, connecteurs Capella et 3DEXPERIENCE |
| Surcharges projet générées (FR / EN) | 28 types sur 36 ; 9 types de documents ; énumérations UO, Business Line, tranches ; champs US masqués sur `changeRequest` et `nonConformance` |
| Contrôles automatiques | Socle non négociable activé ; type principal de chaque document activé ; aucune transition dépendante d'un type désactivé ; réponses conformes au questionnaire |
| Rôles à pourvoir | Liste calculée dans le dossier de provisioning (§ 6) |

### 6.3 Déroulé type des 10 premières semaines du pilote

| Semaines | Activité | Résultat attendu |
|---|---|---|
| 1 – 2 | Import ReqIF des exigences du client ; positions de conformité ; hypothèses | Matrice de conformité, critère SC-01 |
| 3 – 6 | STB / ST du lot, fonctions, classement de sûreté (note de classement), premières exigences de sûreté | STB et ST en vérification ; note de classement |
| 5 – 8 | Interfaces (ICD), lots de travaux avec les UO, plan V&V | ICD approuvé ; lots accordés |
| 7 – 10 | Premier cycle de DM en CCB ; ré-import d'une révision client ; traitement des suspicions | Critère SC-03 ; premier retour d'expérience |
