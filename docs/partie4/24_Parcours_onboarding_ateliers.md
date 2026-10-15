# 24 — Parcours d'onboarding de l'équipe : ateliers progressifs

> Version 0.4. Ce parcours permet au responsable IS de **faire monter en compétence son équipe par étapes**, en ateliers internes.
>
> - L'éditeur (Siemens) et, si la charge l'exige, un intégrateur interviennent en appui.
> - **La maîtrise reste interne.** Le principe de transfert est : « je montre → on fait ensemble → tu fais ».
>
> Le parcours couvre la phase de cadrage du doc. 16 et prépare la construction décrite au doc. 23.

## 1. Les trois publics

| Public | Qui | Objectif | Parcours |
|---|---|---|---|
| **Équipe cœur** (6 à 10 personnes) | Responsable IS (animateur) ; SE Referents des BU ; 1 à 2 ingénieurs configuration ; représentants Sûreté / licensing, Qualité, DSI / sécurité ; futur chef de projet pilote | Comprendre, décider, construire, puis **enseigner** | 12 ateliers (§ 3) |
| **Équipe pilote** (NUWARD, puis pilote court) | Rédacteurs, vérificateurs, approbateurs, CCB, V&V, sûreté du lot | Utiliser l'outil dans son rôle | Cursus par rôle (doc. 16 § 7), animé par l'équipe cœur |
| **Référents des vagues suivantes** | Champions des BU / UO | Déployer dans leur périmètre | Parcours cœur condensé (blocs A et B) |

## 2. Guide de lecture par profil

L'ensemble documentaire est volumineux. Chacun lit **d'abord sa colonne**, puis le reste à la demande.

| Profil | À lire en premier (≈ 3 à 4 h) | Ensuite |
|---|---|---|
| Responsable IS | 00, 18, 19, 25, 23, 24 | Tout le reste |
| SE Referent de BU | 00, 02 (sa BU), 07, 08, 09, 25, A7, A9 (ses typologies) | 10, 12, 13, 21 |
| Ingénieur configuration | README, 08, 09, 10, 23, 25, `model/*.yaml`, `tools/` | A1–A6, A10, A11, 11, 22 |
| Sûreté / licensing | 04, 08 § 5, 09, 10, 19 § 3, A10 (packs) | 06 (ADR-10, 25), 18 |
| Qualité | 07 (socle non négociable), 10, 15, 17, 20, 21 § 3 | 19, 23 § 3 |
| DSI / sécurité | 06 (ADR-03, 16, 17, 21, 28), 11, 14, 15, 20 § 2 | 22, 23 § 4 |
| Chef de projet pilote | 00, 16, 21, 23 § 6, dossier de provisioning du pilote | 13, 12 |

## 3. Les 12 ateliers de l'équipe cœur

Format :
- demi-journée de 3 h, hebdomadaire ;
- pré-lecture d'une heure au plus ;
- au plus 10 participants ;
- un exercice pratique par atelier ;
- les décisions sont consignées dans le dépôt : statut des ADR et registre d'hypothèses.

À partir de C2, un **bac à sable** Polarion est nécessaire (doc. 23, S0).

### Vue d'ensemble

| Bloc | # | Atelier | Semaine | Décision / livrable principal |
|---|---|---|---|---|
| **A — Comprendre** | A1 | Vision, périmètre, lecture du dépôt | 1 | Charte de l'équipe cœur, rôles |
| | A2 | Le modèle de données (RFLP, types, attributs nucléaires) | 2 | Questions et hypothèses à valider |
| | A3 | Traçabilité, suspicion, couverture | 3 | Règles TR validées ou amendées |
| | A4 | Cycles de vie, signatures, socle non négociable | 4 | Workflows du pilote validés |
| **B — Décider** | B1 | Approche graduée et stratégie de modèle (50 % / 150 %) | 5 | **ADR-29**, grille de tailoring calibrée |
| | B2 | Topologie, gabarits, organisation matricielle | 6 | ADR-01 / 02 / 24 / 26 / 28 |
| | B3 | Réglementaire, sécurité, export, social | 7 | Packs du pilote ; lancement CSE / RGPD |
| | B4 | Échanges et intégrations | 8 | Connecteurs du pilote ; profil ReqIF client |
| **C — Construire et préparer** | C1 | Le modèle « as code » : YAML, validateur, CI, CCB | 9 | Chacun a livré une évolution par demande de fusion |
| | C2 | Spike de conformité sur bac à sable (avec Siemens) | 10 – 11 | Formats confirmés, corrections du générateur |
| | C3 | LiveDocs, formulaires, tableaux de bord | 12 | 1 gabarit et 1 tableau de bord construits ensemble |
| | C4 | Kit pilote NUWARD et feu vert de construction | 13 | Réponses H confirmées, plan S2–S12 engagé |

### Fiches des ateliers

#### A1 — Vision, périmètre, lecture du dépôt
- **Objectif :** savoir ce que contient le plan, pourquoi « as code », comment naviguer.
- **Pré-lecture :** 00 (§ 0 et § 1), README.
- **Déroulé :**
  - enjeux et décisions structurantes (45 min) ;
  - visite guidée du dépôt : `model/`, `generated/`, `docs/` (45 min) ;
  - exercice (60 min) ;
  - organisation de l'équipe (30 min).
- **Exercice :** chacun place 3 projets réels de sa BU sur les 32 typologies (annexe A9) et note les écarts.
- **Sorties :** charte de l'équipe cœur (rôles, rituels, temps alloué) ; premiers écarts de typologie.
- **Acquis :** chacun retrouve en moins de 2 minutes où est défini un type, un champ ou un workflow.

#### A2 — Le modèle de données
- **Objectif :** maîtriser les 36 types, les principes P1–P6 et les attributs nucléaires (EIP, AIP, exigence définie, classements multi-schémas).
- **Pré-lecture :** 08, annexe A8.
- **Exercice :** dérouler sur papier une chaîne réelle : exigence client → exigence système → fonction → composant (classement) → cas de vérification → preuve. Identifier les attributs renseignés à chaque étape.
- **Sorties :** liste des questions et hypothèses à confirmer (registre du doc. 05).
- **Acquis :** chacun sait dire pourquoi un concept est un **type** ou un **attribut** (principe P1).

#### A3 — Traçabilité, suspicion, couverture
- **Objectif :** convention aval → amont, 26 rôles de liens, règles TR-01..20, suspicion, cône d'impact.
- **Pré-lecture :** 09, annexe A3, 19 § 1–2.
- **Exercice :** sur l'exemple de A2, poser les liens et appliquer les règles TR. Puis simuler une modification amont : qui est interpellé ?
- **Sorties :** règles TR validées ou amendées (sévérité bloquante ou avertissement).
- **Acquis :** chacun sait lire une matrice de couverture et expliquer un lien suspect.

#### A4 — Cycles de vie, signatures, socle non négociable
- **Objectif :** workflows, contrôle technique indépendant, avis Sûreté conditionnel, signatures et documents R / V / A, socle NN-01..08.
- **Pré-lecture :** 10, annexe A4 (exigence, analyse, DM, document complet), 21 § 3.
- **Exercice :** jeu de rôles sur papier. Un rédacteur, un vérificateur et un ingénieur sûreté font passer une exigence définie et une note de calcul jusqu'à l'approbation, en appliquant les conditions.
- **Sorties :** workflows du pilote validés ; questions à poser à Siemens (comportement des signatures).
- **Acquis :** chacun sait quelles transitions bloquent et pourquoi.

#### B1 — Approche graduée et stratégie de modèle
- **Objectif :** décider de la stratégie cœur / extensions (doc. 25) et calibrer la grille de tailoring.
- **Pré-lecture :** 07, 25, annexe A7.
- **Exercice :** coter 5 projets réels avec la grille à 7 critères ; comparer la classe obtenue à l'intuition des participants ; ajuster les seuils si besoin.
- **Sorties :** **ADR-29 validée** ; seuils de la grille confirmés ; liste des extensions locales prévisibles.
- **Acquis :** chacun sait expliquer ce qui est du cœur et ce qui peut être local.

#### B2 — Topologie, gabarits, organisation matricielle
- **Objectif :** projets, bibliothèques, lignes de produits, master / archétypes / spécialisations, lots BU × UO, projets sas.
- **Pré-lecture :** 11, 21, ADR-01 / 02 / 24 / 26 / 28.
- **Exercice :** dessiner la topologie cible de sa BU (projets, gabarits, liens inter-projets) ; placer les UO réalisatrices d'un projet réel en lots.
- **Sorties :** ADR de topologie validées ; liste des UO réelles (remplace l'amorce OSINT, Q-ORG-01).
- **Acquis :** chacun sait pourquoi un Space ne protège pas.

#### B3 — Réglementaire, sécurité, export, social
- **Objectif :** packs réglementaires, classification, contrôle export, instances ; facteurs sociaux et juridiques.
- **Invités :** Sûreté / licensing, sécurité SI, juriste, RH.
- **Pré-lecture :** 04, annexe A10 (packs), 20 § 1–2.
- **Exercice :** dérouler le provisioning de 3 projets (dont un US et un sensible) et vérifier l'instance et les packs obtenus.
- **Sorties :** packs du pilote confirmés ; **lancement de l'information-consultation CSE / Betriebsrat et de la fiche RGPD** (facteurs F-01 et F-02, sur le chemin critique).
- **Acquis :** chacun sait dire sur quelle instance va un projet et pourquoi.

#### B4 — Échanges et intégrations
- **Objectif :** ReqIF, parsing Word, aller-retour Excel, PLM, MBSE, calcul, GED.
- **Invités :** responsables PLM, MBSE, GED ; interlocuteur du client pilote si possible.
- **Pré-lecture :** 14, 22, annexe A11.
- **Exercice :** analyser un vrai document client (ou public) avec les règles W-01..W-11 ; estimer le taux de capture et les cas litigieux.
- **Sorties :** connecteurs du périmètre pilote arbitrés (Capella dès le départ ou en second temps) ; échange de fichiers ReqIF de référence planifié avec le client.
- **Acquis :** chacun sait expliquer le cycle import → conformité → ré-import d'une révision.

#### C1 — Le modèle « as code »
- **Objectif :** que chaque membre sache faire évoluer le modèle sans casser la cohérence.
- **Pré-lecture :** README, 17 § 2, 19 § 6.
- **Exercice (sur poste) :**
  1. Chacun ajoute une valeur d'énumération, puis un champ local `x_` dans un scénario.
  2. Il lance `tools/almmodel.py`, provoque volontairement une erreur (champ inconnu, trace non autorisée), la corrige, régénère et soumet une demande de fusion.
  3. Simulation d'un CCB du modèle sur ces demandes.
- **Sorties :** circuit de demande d'évolution rodé ; règles de revue des demandes de fusion.
- **Acquis :** chacun a livré au moins une évolution validée par la CI.

#### C2 — Spike de conformité (journée entière, avec l'expert Siemens)
- **Objectif :** déposer la configuration générée sur le bac à sable et corriger le générateur ensemble (doc. 23, S1).
- **Pré-lecture :** 23 § 3–5.
- **Déroulé :** dépôt de la configuration ; chargement ; création d'un élément par type ; une transition par workflow ; consignation des écarts ; correction du générateur en binôme avec l'expert.
- **Sorties :** formats confirmés ; procédure de rechargement ; liste des corrections du générateur ; cadre commun des scripts esquissé.
- **Acquis :** l'ingénieur configuration sait déployer seul une nouvelle version du cœur.

#### C3 — LiveDocs, formulaires, tableaux de bord
- **Objectif :** savoir construire les éléments qui se font dans l'instance.
- **Pré-lecture :** 12, 13, annexe A5.
- **Exercice :** construire ensemble le gabarit STB, le formulaire `systemRequirement` et la page « couverture des exigences définies » (TR-03) ; vérifier l'indicateur sur un jeu de test.
- **Sorties :** modèles de référence pour la suite du chantier S4 / S6 / S7 ; règles de style des gabarits.
- **Acquis :** deux membres au moins savent construire un gabarit et une page sans aide.

#### C4 — Kit pilote NUWARD et feu vert de construction
- **Objectif :** confirmer les hypothèses du kit et engager la construction S2–S12.
- **Invités :** chef de projet pilote, client si possible pour le volet échanges.
- **Pré-lecture :** 23 § 6, dossier de provisioning `P-NUWARD-L1`, 20 § 8.
- **Déroulé :**
  - revue des réponses de confiance H ;
  - choix du système ou du lot pilote ;
  - critères de succès ;
  - choix du pilote court compagnon ;
  - plan, charge et répartition interne / Siemens / intégrateur.
- **Sorties :** fiche `model/pilots/P-NUWARD-L1.yaml` mise à jour et régénérée ; plan de construction engagé ; date cible du go / no-go pilote.
- **Acquis :** l'équipe sait refaire un provisioning complet pour une autre typologie.

## 4. Compétences visées en fin de parcours

| Compétence | Responsable IS | SE Referent | Ingénieur configuration | Sûreté / Qualité |
|---|---|---|---|---|
| Expliquer le modèle et ses principes | Enseigner | Enseigner | Appliquer | Appliquer |
| Coter un projet et choisir son profil | Enseigner | Enseigner | Connaître | Appliquer |
| Rédiger un scénario de couverture | Appliquer | Appliquer | Appliquer | Connaître |
| Faire évoluer le modèle (YAML, CI, demande de fusion) | Appliquer | Appliquer | Enseigner | Connaître |
| Déployer la configuration (DEV → PROD) | Connaître | — | Enseigner | — |
| Construire gabarits, formulaires, pages | Connaître | Appliquer | Enseigner | — |
| Développer un script de workflow | — | — | Appliquer (après S3) | — |
| Animer le cursus utilisateurs | Appliquer | Enseigner | Appliquer | Appliquer (son domaine) |
| Statuer en CCB du modèle | Enseigner | Appliquer | Appliquer | Appliquer |

## 5. Appui de Siemens et d'un intégrateur sans perdre la maîtrise

| Besoin | Qui | Mode | Clause de transfert |
|---|---|---|---|
| Spike de conformité, procédure de déploiement | Expert Siemens (3 à 5 j) | Atelier C2, en binôme | Corrections faites dans **notre** générateur, dans **notre** dépôt |
| Cadre de développement des scripts, API | Expert Siemens | Développement en binôme des 2 premiers scripts | Les scripts suivants sont développés en interne, revus par l'expert |
| Revue d'architecture, performances, montée de version | Siemens | Revues ponctuelles | Rapport versionné dans le dépôt |
| Pics de charge : formulaires, gabarits, pages, exécution des OQ | Intégrateur | Lots à périmètre fermé | Travail dans notre dépôt, sous notre CI et nos conventions ; aucune configuration hors dépôt ; documentation livrée ; pas de licence ou d'outil propriétaire de l'intégrateur |
| Formation des utilisateurs | Équipe cœur | — | Non sous-traitée : c'est le levier d'appropriation |

**Règle d'or :** tout ce que fait un tiers passe par le dépôt, la CI et la revue d'un membre de l'équipe cœur. Une configuration que personne en interne ne sait refaire est une dette.

## 6. Rituels pendant et après le parcours

- **Permanence hebdomadaire** (1 h) : questions, revue des demandes de fusion.
- **Registre des décisions :** statut des ADR (proposée → validée) et registre d'hypothèses du doc. 05, mis à jour à chaque atelier.
- **Tableau du chantier :** étapes S0–S13 du doc. 23, avec responsable et date.
- **Revue mensuelle** avec le sponsor : avancement, risques, facteurs de succès du doc. 20.
- **Après le pilote :** chaque membre de l'équipe cœur anime au moins un atelier pour la vague suivante. C'est le critère final de réussite du parcours.
