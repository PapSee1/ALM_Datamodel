# 23 — Kit de déploiement : inventaire, reste à construire et guide pas à pas jusqu'au pilote NUWARD

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **forte** · Historique : [CHANGELOG](../../CHANGELOG.md) · Carte du dépôt : [guide de lecture](../GUIDE_DE_LECTURE.md).*
>
> **En bref**
> - **À quoi sert ce document :** dire ce que le dépôt fournit déjà pour configurer Polarion, ce qu'il reste à construire dans l'instance (scripts, formulaires, gabarits, tableaux de bord, permissions, validation), combien cela coûte en ordre de grandeur, et dans quel ordre le faire (étapes S0–S13) jusqu'au premier projet pilote.
> - **Qui le lit :** responsable IS (ingénierie système), ingénieur configuration, Qualité (validation de l'outil), DSI (direction des systèmes d'information), chef de projet pilote.
> - **À lire avant :** [guide de lecture](../GUIDE_DE_LECTURE.md), README (commandes), doc. 10 (workflows et scripts), doc. 21 (provisioning), doc. 24 (ateliers qui précèdent la construction), doc. 25 (stratégie d'exposition par incréments).
>
> Ce document répond à la question : *« avec ce dépôt, puis-je configurer Polarion et démarrer un premier projet ? »*
>
> **Réponse courte : pas encore, mais le chemin est balisé.** Le dépôt contient :
> - la **conception complète** (le « 150 % », validé) ;
> - la **configuration déclarative du cœur**, générée : types, champs, énumérations, statuts, rôles de liens, workflows, types de documents, accompagnée du manifeste `generated/polarion/<lang>/SIGNATURES_ET_SCRIPTS.md` (scripts attendus, points de signature, constructions à confirmer) ;
> - la liste fermée des **constructions Polarion non confirmées** sur la version cible : [annexe D](../annexes/D_Formats_Polarion_a_verifier.md), PF-01..PF-14 ;
> - le **kit de provisioning du pilote NUWARD** (NUWARD : projet de petit réacteur modulaire — SMR — porté par EDF, dont Framatome est partenaire [C]).
>
> Il ne contient pas encore ce qui se **construit dans l'instance** ou se **développe** : scripts de workflow, formulaires, gabarits de LiveDocs (documents vivants Polarion), tableaux de bord, permissions, gabarits de projets, contenu des bibliothèques, dossier de validation. Ce document en fait l'inventaire, chiffre le reste à faire en ordres de grandeur et donne la séquence pas à pas.
>
> Niveaux de confiance utilisés ici : **[C]** confirmé par une source publique · **[P]** probable · **[H]** hypothèse de modélisation · **[NT]** non trouvé (échelle complète : doc. 05 § 3).

## 1. Inventaire : ce qui est prêt, ce qui reste à construire

Légende :
- ✅ prêt dans le dépôt (à vérifier une fois sur l'instance cible) ;
- 🟡 spécifié, à construire ;
- ❌ hors dépôt.

| # | Élément de configuration | État | Où dans le dépôt | Reste à faire |
|---|---|---|---|---|
| 1 | Types de Work Items (éléments de travail), champs personnalisés, énumérations, statuts, rôles de liens et règles | ✅ | `generated/polarion/{fr,en}/.polarion/` : 249 fichiers XML par langue, dont 186 sous `tracker/fields/` (36 sous `tracker/workflow/`, 25 sous `documents/`, 2 sous `testing/`) ; manifeste `SIGNATURES_ET_SCRIPTS.md` | Spike de conformité sur la version cible (S1) : confirmer les constructions PF-01..PF-14 de l'annexe D |
| 2 | Workflows des Work Items et des documents (états, transitions, rôles, champs requis, conditions natives, signatures) | ✅ | `…/tracker/workflow/`, `…/documents/workflow/` | Idem S1 ; dépend des scripts (ligne 5) |
| 3 | Types de documents, champs de document, statuts de documents, statuts de Test Runs (campagnes d'exécution de cas de test) | ✅ | `…/documents/fields/`, `…/testing/` | S1 |
| 4 | Surcharges de configuration du projet pilote (fichiers projet qui remplacent, pour ce projet, l'élément global correspondant) | ✅ | `generated/projects/P-NUWARD-L1/` + [dossier de provisioning](../../generated/projects/P-NUWARD-L1/provisioning-record.md) | Confirmer les réponses H (atelier C4, doc. 24) |
| 5 | **17 scripts de workflow** (`fra-*.js`) | 🟡 | Spécification : catalogue des conditions et fonctions (`model/workflows.yaml`), doc. 10 § 4, § 3 ci-dessous ; occurrences dans le manifeste | Développement + tests (S3) |
| 6 | Formulaires (*form layouts* : disposition des champs à l'écran) par type | 🟡 | Ordre et regroupement des champs = ordre du modèle (fieldSets) | Construction (S4) ; génération possible après S1 |
| 7 | Rôles projet, permissions, champs protégés, groupes d'annuaire | 🟡 | `model/roles.yaml`, annexe A6 | Paramétrage (S2) |
| 8 | Gabarits de LiveDocs (contenu, consignes de rédaction, exemples) | 🟡 | Plans types : annexe A5, doc. 12 | Construction dans `LIB-TEMPLATES` (S6) |
| 9 | Tableaux de bord et LiveReports (pages de rapport Polarion) | 🟡 | Catalogue des indicateurs et tableaux par rôle (doc. 13), exemple Velocity | Construction (S7) |
| 10 | Requêtes des règles de traçabilité TR-01..20 | 🟡 | `model/link_roles.yaml`, annexe A3 | Écriture et validation des requêtes (S7) |
| 11 | Configuration Testing (types de Test Run, gabarits, étapes, rôle `verifies` pour la couverture) | 🟡 | Statuts générés ; ADR-19 ; annexe D, PF-10 | Paramétrage (S5) |
| 12 | Export PDF signé + manifeste + versement en GED (gestion électronique de documents) | 🟡 | Fonction `exportToEdms`, connecteur `CX-EDMS` | Extension ou développement (après S12, export manuel au pilote) |
| 13 | Gabarits de projets (master, archétype, spécialisation, sas) | 🟡 | `model/project_topology.yaml`, doc. 21 § 2 | Construction (S8) |
| 14 | Provisioning (questionnaire, dérivation, kit projet) | ✅ / 🟡 | `model/project_setup.yaml`, `tools/generate_project.py` | Automatisation de la création par API : optionnelle (manuelle au pilote) |
| 15 | Contenu des bibliothèques (réglementaire, terminologie, cas V&V génériques) | ❌ | Structure seulement | Saisie et paraphrase (S9), licences de normes |
| 16 | Intégrations (ReqIF, Capella, PLM, GED, annuaire) | 🟡 | `model/import_export.yaml`, annexe A11, doc. 22 | Paramétrage / développement (S11) |
| 17 | Notifications, tâches planifiées (recalcul nocturne de `verificationStatus`) | 🟡 | Fonctions `notifyRoles`, `recomputeVerificationStatus` | Avec les scripts (S3) |
| 18 | Dossier de validation de l'outil (exigences utilisateur, analyse de risques, protocoles IQ / OQ / PQ) | 🟡 | Doc. 15 § 4 ; cas OQ dérivables des conditions bloquantes et des scénarios A9 | Rédaction et exécution (S12) |
| 19 | Supports de formation | 🟡 | Parcours : doc. 24 ; cursus par rôle : doc. 16 § 7 | Production (S12) |
| 20 | Infrastructure, installation, licences | ❌ | Exigences : doc. 15 | DSI + éditeur (S0) |

IQ / OQ / PQ (ligne 18) : qualification d'installation (l'outil est installé comme prévu), qualification opérationnelle (l'outil configuré fait ce qui est spécifié : jeux d'essais des fonctions critiques) et qualification de performance (l'outil tient en conditions réelles) ; détail au doc. 15 § 4.

## 2. Effort restant jusqu'au démarrage du pilote (ordres de grandeur)

> **Hypothèses [H]** à affiner avec Siemens et l'éventuel intégrateur (prestataire qui configure et développe pour le compte de Framatome) :
> - équipe interne formée (doc. 24) ;
> - version cible connue ;
> - périmètre = tranche du pilote NUWARD (28 types, 9 documents, 6 tableaux de bord).
>
> Unité : jour·homme (j·h, une personne pendant une journée).

| Étape | Lot | Effort | Porteur conseillé |
|---|---|---|---|
| S1 | Spike de conformité de la configuration générée (annexe D, PF-01..PF-14 ; manifeste) | 10 – 15 | Interne (ingénieur configuration) + 3 à 5 j d'expert Siemens |
| S2 | Identité, rôles, permissions, groupes | 8 – 12 | Interne + DSI |
| S3 | Scripts « socle » (priorité P0, § 3) et tests | 30 – 45 | Interne, accompagné par Siemens (cadre de développement, API) |
| S4 | Formulaires des 28 types activés | 10 – 14 | Interne |
| S5 | Configuration Testing | 3 – 5 | Interne |
| S6 | 9 gabarits de LiveDocs du pilote | 18 – 27 | SE Referents (référents ingénierie système des BU) + ingénieur configuration |
| S7 | Requêtes TR + 6 tableaux de bord | 20 – 30 | Interne ; intégrateur en renfort possible |
| S8 | Gabarits master, archétype, spécialisation, sas | 6 – 10 | Interne |
| S9 | Bibliothèques minimales (extraits utiles au lot, glossaire) | 15 – 25 | SE + licensing |
| S10 | Provisioning du pilote | 3 – 5 | Guichet de provisioning |
| S11 | Profil ReqIF client (test sur fichier de référence) | 5 – 10 | Interne + interlocuteur client |
| S12 | OQ du périmètre pilote + formation des utilisateurs pilotes | 35 – 55 | Qualité + interne ; intégrateur possible pour l'exécution des OQ |
| **Total socle pilote** | | **≈ 165 – 255** | |
| Options | Scripts P1 (12 – 20), synchronisation Capella (20 – 40), export GED automatisé (10 – 20) | + 42 – 80 | Siemens / intégrateur sous votre pilotage |

**Lecture :** avec une équipe cœur de 2 à 3 ETP (équivalents temps plein) dédiés, environ 40 à 60 j·h par mois, l'équipe doit construire environ 4 à 6 mois après la fin des ateliers. Cela correspond à la phase 1 (fondations) et au début de la phase 2 (pilotes) du doc. 16. Un intégrateur sert à **absorber les pics** (formulaires, gabarits, tableaux de bord, exécution des OQ) : la conception et les scripts du socle restent internes.

## 3. Les scripts de workflow

La configuration générée appelle 17 scripts (liste et occurrences tenues à jour dans le manifeste `generated/polarion/<lang>/SIGNATURES_ET_SCRIPTS.md`). Un script de workflow est un petit programme JavaScript que Polarion exécute au moment d'une transition, soit pour l'autoriser ou la bloquer (*condition*), soit pour agir (*fonction* : poser une valeur, créer une baseline, notifier).

> **Règle de déploiement.** Aucun workflow n'est déployé en production avant que les scripts qu'il appelle existent et soient testés. Le comportement d'une condition dont le script est absent est à vérifier au spike [P]. En bac à sable (instance d'essai sans donnée réelle), des **bouchons journalisés** (versions provisoires qui ne font que tracer leur appel) sont admis, clairement identifiés. Un bouchon « toujours vrai » est **interdit hors bac à sable** : il désactiverait le contrôle technique.

Priorités : **P0** = indispensable au démarrage du pilote NUWARD ; **P1** = après le démarrage, avec une solution manuelle tracée entre-temps ; **INC-2** = porté par l'incrément suivant (doc. 25 § 4).

| Script | Occurrences* | Rôle | Priorité pilote | Cas de test OQ minimaux |
|---|---|---|---|---|
| `fra-document-owner.js` | 74 | Condition : l'utilisateur est l'auteur du LiveDoc (pseudo-rôle `documentOwner`, pour lequel Polarion n'a pas de rôle spécial connu) sur les transitions documentaires (lancer la relecture, soumettre, retour en rédaction, nouvelle révision). Quand la transition admet aussi d'autres rôles, le cumul avec la condition de rôle native est à confirmer au spike (annexe D, PF-11) | **P0** (les 9 documents du pilote) | Auteur autorisé ; non-auteur bloqué ; autre rôle admis par la transition autorisé |
| `fra-independence.js` | 73 | Condition : l'utilisateur qui vérifie ou approuve n'est ni l'auteur ni le dernier rédacteur | **P0** | Auteur bloqué ; dernier modificateur bloqué ; tiers autorisé |
| `fra-field-rule.js` | 45 | Condition : règles de valeur (`notIn`, `nonEmptyIf`, `onlyIfProjectSetting`…) | **P0** | Chaque forme de règle présente dans le modèle |
| `fra-habilitation.js` | 39 | Condition : signataire habilité (ADR-27) ; mode `prefill` à la création | **P0 version minimale** : neutre si `signaturePolicy = roleBased` ; complète avant tout projet `habilitationBased` | Les 5 cas du doc. 21 § 3.3 |
| `fra-link-cardinality.js` | 25 | Condition : cardinalités et statuts des liens (min, exactement, référence approuvée…) | **P0** | 0 / 1 / 2 liens ; lien vers élément au mauvais statut |
| `fra-revision-index.js` | 23 | Fonction : incrément de l'indice documentaire | **P0** | A → B ; brouillons A0 / A1 |
| `fra-baseline.js` | 23 | Fonction : baseline (révision figée de référence) nommée à l'approbation | **P0** | Nom conforme à la convention `baselineNaming` |
| `fra-export-edms.js` | 20 | Fonction : export PDF + manifeste vers la GED | P1 (export manuel tracé au pilote) | PDF/A, manifeste, référence GED retournée |
| `fra-no-suspect.js` | 17 | Condition : aucun lien suspect sur les rôles listés | **P0** | Lien suspect bloque ; levée de suspicion débloque |
| `fra-classification.js` | 11 | Condition : pas de classification interdite sur l'instance standard | **P0** | `sensitiveSecurity` bloque sur STD |
| `fra-safety-approval.js` | 10 | Condition : avis Sûreté présent si la condition de sûreté est vraie | **P0** | Exigence définie sans avis bloquée ; avec avis autorisée |
| `fra-request-safety-approval.js` | 9 | Fonction : ajoute un approbateur Sûreté si nécessaire | **P0** | Ajout conditionnel |
| `fra-notify.js` | 8 | Fonction : notifications ciblées | P1 | Destinataires corrects |
| `fra-verification-status.js` | 6 | Fonction : recalcul de `verificationStatus` | P1 (+ tâche nocturne) | Exigence vérifiée / partielle / non vérifiée |
| `fra-set-if-empty.js` | 6 | Fonction : positionne un champ seulement s'il est vide (`setFieldValue.valueIfEmpty`, ex. `maturity` = `consolidated` à l'approbation d'une exigence, la fonction native `ChangeField` étant inconditionnelle) | **P0** (appelée par `wfRequirement`, six types du pilote) | Champ vide → valeur posée ; champ déjà renseigné → inchangé |
| `fra-link-status.js` | 5 | Condition : statut des éléments liés filtré par type ou par champ (`linkedItemsStatus` avec `type` / `field`, que la condition native ne sait pas faire ; ex. remise d'un lot : livrables approuvés et FNC soldées) | **P0** (`changeRequest`, `nonConformance`, `review`, `workPackage` du pilote) | Lié du type visé au mauvais statut bloque ; lié d'un autre type ignoré |
| `fra-sla.js` | 2 | Fonction : calcul d'une échéance (SLA, délai de service engagé) | **P0** : FNC (fiche de non-conformité) du pilote, échéance de caractérisation à 5 jours (`wfNonConformance.characterise`) ; branche fortuits (`responseDueDate` selon l'urgence) en INC-2 | Échéance à J+5 posée à la caractérisation ; (INC-2) échéance selon l'urgence |

\* Occurrences dans la configuration générée en français (`generated/polarion/fr`, fichiers XML), toutes transitions confondues.

Le verrouillage du texte original d'une exigence d'entrée après acceptation ne passe plus par un script (`fra-lock-fields.js` a été retiré) : il relève des permissions par état (PR-03, étape S2).

**Méthode recommandée :**
- un **cadre commun** (lecture des paramètres, messages, journalisation) développé avec l'expert Siemens ;
- puis un script par semaine, chacun avec ses cas de test.

Les scripts sont versionnés dans ce dépôt (dossier `scripts/` à créer) et déployés comme la configuration. Leur emplacement sur le serveur et leur moteur (JavaScript) sont à confirmer pour la version cible [P] (annexe D, PF-06).

## 4. Mécanique de déploiement de la configuration

| Sujet | Règle |
|---|---|
| Stockage | Polarion conserve sa configuration dans son dépôt : configuration **globale** dans le dossier `.polarion` à la racine ; configuration **projet** dans le dossier `.polarion` du projet [P, à confirmer au spike pour la version cible] |
| Livraison | Le gestionnaire de configuration globale dépose une **version étiquetée** de ce dépôt (`generated/…`) en DEV (développement), puis RECETTE, puis PROD (production). Jamais d'édition directe en production. |
| Rechargement | Certains éléments sont pris en compte à chaud, d'autres demandent un rechargement ou une réindexation. La procédure exacte est établie au spike (annexe D, PF-14) et consignée ici. |
| Scripts | Déposés sur le serveur (chaque nœud en grappe — *cluster*, groupe de serveurs qui se partagent la charge), versionnés dans ce dépôt [P] |
| Aller-retour | Une configuration mise au point **dans l'interface d'administration en DEV** (formulaires, pages) est rapatriée dans le dépôt avant toute promotion. Le générateur fait foi pour tout ce qu'il produit : une modification manuelle d'un fichier généré serait écrasée. |
| Surcharges projet | Uniquement les fichiers listés dans `model/extension_policy.yaml` (`overridableProjectFiles`), produits par `tools/generate_project.py` (annexe D, PF-12) |

## 5. Guide pas à pas (de l'instance vide au pilote)

Chaque étape : objectif, entrées, actions, critère de fin. Les durées sont indicatives et se recouvrent partiellement. Le dossier de provisioning généré du pilote renvoie à cette section pour sa liste de contrôle.

### S0 — Prérequis (avant les ateliers C2 / C3)

- **Entrées :** doc. 15 (infrastructure), ADR-03, ADR-18, ADR-21.
- **Actions :**
  - instance de **développement** de la version cible (et bac à sable) ;
  - licences de développement ;
  - accès administrateur au dépôt de configuration ;
  - poste d'intégration continue (CI : exécution automatique du validateur, des tests et des générateurs ; Python 3, PyYAML — la bibliothèque Python qui lit les fichiers YAML du modèle) ;
  - désignation de l'ingénieur configuration.
- **Fin :** l'instance de développement répond ; le dépôt de configuration est accessible ; la CI de ce dépôt tourne.

### S1 — Spike de conformité (2 à 3 semaines)

Un *spike* est une expérimentation courte et bornée qui lève un doute technique avant d'engager la construction.

- **Entrées :** `generated/polarion/en/.polarion/` (puis `fr`) ; le manifeste `generated/polarion/<lang>/SIGNATURES_ET_SCRIPTS.md` ; la liste fermée des constructions à confirmer de l'[annexe D](../annexes/D_Formats_Polarion_a_verifier.md) (PF-01..PF-14 : règles de liens, bloc de signatures, types de champs, conditions et scripts, `InvokeAction`, requêtes Lucene, fichiers de documents et de Testing, rôles spéciaux, surcharges projet, champs requis, rechargement).
- **Actions :**
  1. Déposer la configuration globale générée en DEV.
  2. Vérifier le chargement sans erreur des types, champs, énumérations, rôles de liens, workflows et types de documents.
  3. Créer un élément de chaque type.
  4. Jouer une transition par workflow, scripts en bouchons journalisés.
  5. Créer un lien par rôle, y compris inter-projets.
  6. Statuer sur chaque ligne PF-01..PF-14 de l'annexe D (✅ confirmée, ❌ infirmée → repli) et noter tout autre écart de format.
  7. **Corriger le générateur, pas les fichiers.**
- **Fin :** 0 erreur de chargement ; annexe D renseignée (date, version, personne) sans ligne 🔲 ; générateur v1 aligné sur la version cible ; procédure de rechargement documentée (§ 4).

### S2 — Identité, rôles, permissions

- **Entrées :** `model/roles.yaml`, annexe A6, règles PR-01..PR-11.
- **Actions :**
  - créer les rôles projet ;
  - accorder les permissions par famille et par état ;
  - protéger les champs de sûreté (PR-02), l'édition des éléments approuvés et du texte original des exigences d'entrée acceptées (PR-03) et l'abaissement du contrôle export (PR-07) ;
  - interdire la suppression (PR-01) ;
  - relier les rôles aux groupes d'annuaire ;
  - activer l'authentification alternative pour les signatures si SSO (authentification unique, PR-04).
- **Fin :** jeu de comptes de test par rôle ; matrice de droits vérifiée par échantillonnage.

### S3 — Scripts du socle

- **Entrées :** § 3, `model/workflows.yaml` (catalogue des conditions et fonctions), manifeste généré.
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
  - statuts et résultats (générés ; annexe D, PF-10).
- **Fin :** une campagne complète jouée en DEV, résultat signé.

### S6 — Gabarits de LiveDocs du pilote

- **Entrées :** annexe A5 (plans types et types autorisés), doc. 12.
- **Actions :** construire les 9 documents du pilote dans `LIB-TEMPLATES` :
  - STB (spécification technique du besoin), ST (spécification technique du système), SDM (dossier de conception système), note de classement, ICD (document de contrôle d'interface) ;
  - chapitre de démonstration de sûreté ;
  - matrice de conformité ;
  - plan V&V (vérification et validation) ;
  - PV (procès-verbal) de remise de lot.

  Chacun comprend les consignes de rédaction (patrons de phrases EARS — *Easy Approach to Requirements Syntax* —, règles de qualité du doc. 13 § 4) et un exemple par chapitre.
- **Fin :** chaque gabarit est instancié une fois et parcourt son workflow documentaire jusqu'à l'approbation.

### S7 — Requêtes et tableaux de bord

- **Entrées :** doc. 13, règles TR (annexe A3).
- **Actions :**
  - requêtes des règles TR utiles au pilote (TR-01..TR-14, TR-18) ;
  - 6 pages : chef de projet, exigences, sûreté, V&V, CCB (comité de maîtrise des modifications) / configuration, UO (unité opérationnelle) réalisatrice.
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
- **Fin :** la liste de contrôle du dossier de provisioning (§ 8 de ce dossier) est cochée.

### S11 — Échanges

- **Actions :**
  - profil `RIF-CUSTOMER-IN` (ReqIF, format d'échange d'exigences) testé avec le client sur un fichier de référence, ré-import d'une révision compris (script d'import `onChangedReimport: reassess`, doc. 22 § 2.2) ;
  - profil de retour de conformité.
  - La synchronisation Capella (outil MBSE — ingénierie système fondée sur les modèles) est activée dans un second temps, si le lot pilote dispose d'un modèle (option).
- **Fin :** les cas OQ d'échange du doc. 22 § 7 sont au vert.

### S12 — Validation et formation, go / no-go

- **Actions :**
  - exécuter les OQ du périmètre pilote (conditions bloquantes, signatures, échanges, indicateurs) ;
  - former les utilisateurs pilotes par rôle (doc. 16 § 7) ;
  - tenir la revue go / no-go (décision formelle de lancer ou non le pilote).
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
| Classe A : le pilote éprouve **tout** le cœur (exigences, RFLP — vues exigences / fonctionnelle / logique / physique de l'architecture —, sûreté, V&V, DM — demandes de modification —, documents signés) | Cycle long : la valeur se voit tard ; un pilote qui « ne finit pas » démobilise |
| Phase de conception amont : pas d'historique à migrer | Conception réorientée en 2024 [C] : besoin client mouvant, révisions fréquentes |
| Échange client réel (ReqIF), MBSE, multi-autorités : cas d'usage exigeants et visibles | Programme multipartenaire : propriété des données et sécurité à clarifier avec le client |
| Forte visibilité : effet d'entraînement | **Risque de sur-ajuster le cœur à la classe A**, trop lourd ensuite pour les fortuits et l'outillage |

**Conditions :**
1. **Découper :** un système ou un lot du périmètre Framatome, sur 4 à 6 mois de production réelle. Pas le programme entier.
2. **Ajouter un pilote court** (fortuit ou outillage, incrément INC-2), lancé environ 2 mois après NUWARD. Il éprouve l'extrémité légère du modèle **avant** le gel du cœur. (v0.4 : les « trois pilotes contrastés » de la v0.1 sont ramenés à NUWARD + ce pilote court.)
3. **Respecter les prérequis :** pas de démarrage sans scripts P0 testés, sans gabarits des 4 documents principaux, ni sans profil ReqIF testé avec le client.

### 6.2 Contenu du kit `P-NUWARD-L1`

| Élément | Fichier |
|---|---|
| Fiche de provisioning (réponses, confiance, tranche activée, critères de succès, extensions locales `localFields` / `projectEnumValues` — vides au démarrage) | `model/pilots/P-NUWARD-L1.yaml` |
| Dossier de provisioning généré | [`provisioning-record.md`](../../generated/projects/P-NUWARD-L1/provisioning-record.md) |
| Paramètres dérivés | Classe A (score 19), archétype `TPL-01-PRODUCT`, gabarit `TPL-NEWBUILD`, instance STD, packs `frAsnr` + `intlIaea`, projet sas, lots de travaux, politique de signature `roleBased`, connecteurs Capella (`CX-MBSE-CAPELLA`) et 3DEXPERIENCE (`CX-PLM-3DX`, PLM — gestion du cycle de vie du produit) |
| Surcharges projet générées (FR / EN) | 28 types sur 36 ; 9 types de documents ; énumérations UO, Business Line, tranches ; champs US masqués sur `changeRequest` et `nonConformance` |
| Contrôles automatiques | Socle non négociable activé ; type principal de chaque document activé ; aucune transition dépendante d'un type désactivé ; réponses conformes au questionnaire |
| Rôles à pourvoir | Liste calculée dans le dossier de provisioning (§ 6 de ce dossier : 20 rôles) |

### 6.3 Déroulé type des 10 premières semaines du pilote

| Semaines | Activité | Résultat attendu |
|---|---|---|
| 1 – 2 | Import ReqIF des exigences du client ; positions de conformité ; hypothèses | Matrice de conformité, critère SC-01 |
| 3 – 6 | STB / ST du lot, fonctions, classement de sûreté (note de classement), premières exigences de sûreté | STB et ST en vérification ; note de classement |
| 5 – 8 | Interfaces (ICD), lots de travaux avec les UO, plan V&V | ICD approuvé ; lots accordés |
| 7 – 10 | Premier cycle de DM en CCB ; ré-import d'une révision client ; traitement des suspicions | Critère SC-03 ; premier retour d'expérience |
