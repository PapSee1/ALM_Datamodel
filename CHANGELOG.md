# Historique des versions

Toutes les versions sont établies à partir de sources ouvertes uniquement (OSINT). Les numéros de version sont ceux du plan directeur ; le modèle (`model/`) et la configuration générée évoluent avec lui.

## v0.5 — octobre 2026 — Revue de cohérence, organisation OSINT, lisibilité

**Revue.** Revue critique de cohérence de l'ensemble du dépôt (modèle, générateurs, tests, 25 documents, annexes) par quatre revues indépendantes : 46 constats techniques, 76 constats documentaires, tous traités ou consignés « à vérifier ».

**Organisation (OSINT).** Campagne de recherche en sources ouvertes sur les BU, Business Lines, unités opérationnelles, sites et filiales de Framatome : doc. 01 réécrit (identité, BU et réorganisations, BL et UO par BU avec codes et sources S-n, sites, filiales, écosystème, questions ouvertes) ; énumérations `businessUnit` (9), `businessLine` (28) et `operationalUnit` (43) refondues avec niveau de confiance par valeur ; questions Q-ORG-05 à Q-ORG-13 ; registre des sources (annexe C § 1 bis).

**Modèle.** État de soumission par workflow (`submitState`) et champs requis « à la soumission » (principe P10 : obligation portée par la transition) ; catégories d'états et familles de types déclarées ; cascade document → éléments explicite par type de document (`primaryType`, `cascadeTypes`, `approvalGate`) et décision ADR-30 (signature portée par le LiveDoc pour les exigences, architecture, analyses de sûreté, cas de vérification) ; transition `approveClassII` (CCB allégé) ; état `waived` des anomalies ; conditions NN-01 (`tbd` interdit à l'approbation des champs de sûreté) ; seuils de classe de tailoring dans `tailoring.yaml` ; règles D06bis (PPST → SENS), D13 / D14 (connecteurs MBSE / PLM) ; convention `collectionNaming` ; pseudo-rôles identifiés ; `libraryDesignAuthority` ; champs déclencheurs de suspicion par type ; énumérations `assumptionType`, `testResult`, `region` complétée ; champs de document `customerVisa`, `requiredHabilitation`, `responsibleUnit` ; champs locaux `x_` et valeurs d'énumération projet dans les fiches pilotes.

**Générateur et validateur.** Générateur réécrit : signatures émises systématiquement, conditions sur les liés par type / champ, valeur par défaut à la transition, filtrage par type des workflows partagés, groupes de cascade `InvokeAction`, pseudo-rôles traduits en scripts, configuration anglaise sans libellé français ; manifeste `SIGNATURES_ET_SCRIPTS.md` (scripts, signatures, constructions à confirmer) ; 249 fichiers XML par langue ; 17 scripts (`fra-document-owner.js`, `fra-set-if-empty.js`, `fra-link-status.js` ajoutés ; `fra-lock-fields.js` retiré). Validateur : une trentaine de contrôles ajoutés (états de soumission, `requiredAt`, familles, champs des conditions, cascade, rôles, seuils, formats d'identifiants), code de retour non nul en cas d'erreur. 14 tests ajoutés (46 au total). `requirements.txt` et CI simplifiée.

**Documentation.** Nouvelle Partie 4 « Revue, mise en œuvre et onboarding » (documents 18 à 25 déplacés, numéros conservés, liens mis à jour) ; guide de lecture et carte du dépôt (`docs/GUIDE_DE_LECTURE.md`) ; annexe D (constructions Polarion à confirmer, PF-01..PF-14) ; en-tête uniforme (version, dépendance à l'outil, historique, carte) ; passe de lisibilité pour un ingénieur débutant (sigles et concepts expliqués à leur première apparition, encadrés « En bref ») ; doublons réduits à un foyer unique ; glossaire complété ; ce journal des versions.

## v0.4 — octobre 2026 — Kit de déploiement, pilote NUWARD, onboarding, stratégie de modèle

- Doc. 23 : inventaire de ce qui est prêt et de ce qui reste à construire (scripts, formulaires, gabarits, tableaux de bord, permissions, validation), effort estimé, guide pas à pas S0–S13.
- Doc. 24 : parcours d'onboarding en 12 ateliers ; lecture par profil ; appui éditeur / intégrateur sans perte de maîtrise.
- Doc. 25 et ADR-29 : arbitrage cœur 50 % / modèle 150 % → 150 % conçu, cœur gouverné, exposé par incréments, extensions locales `x_`, promotion par le CCB.
- `model/extension_policy.yaml`, `model/pilots/P-NUWARD-L1.yaml`, `tools/generate_project.py` ; kit projet généré ; 6 tests ajoutés (32 au total).

## v0.3 — octobre 2026 — Analyse critique, robustesse, organisation matricielle, échanges

- Doc. 18 : analyse critique du plan et d'une seconde analyse indépendante ; 15 écarts classés et traités.
- Doc. 19 : critères de robustesse, rejeu de la v0.1 (198 erreurs → 0), tests par mutation, 4 défauts réels corrigés (dont les identifiants `yes` / `no` générés en `True` / `False`).
- Doc. 20 : 26 facteurs de succès non couverts (instances du personnel, RGPD, PPST, validation, arrêts, réversibilité, habilitations…).
- Doc. 21 : lots de travaux BU × UO, provisioning par questionnaire, gabarits master → archétypes, signatures habilitées, projets sas.
- Doc. 22 : profils ReqIF, règles d'analyse Word, aller-retour Excel, connecteurs.
- Modèle : 15 typologies ajoutées (32 au total), type `workPackage`, packs réglementaires, `project_setup.yaml`, `import_export.yaml`, ADR-24 à ADR-28, règles TR-18 à TR-20, PR-09 à PR-11.

## v0.2 — octobre 2026 — Couverture prouvée

- `model/coverage_scenarios.yaml` et annexe A9 : chaque typologie est prouvée par un scénario vérifié en CI.
- Types `unitDeployment` (effectivité par tranche) et `lessonLearned` (REX) ; rôle `capitalizes`.
- Politique des champs obligatoires (P6) pour ne plus bloquer les imports ; états ambigus corrigés ; profils de classes complétés.

## v0.1 — octobre 2026 — Plan directeur initial

- Parties 1 à 3 : contexte, recherche OSINT et ADR-01 à ADR-23, méthodologie, modèle de données, traçabilité, workflows, topologie, LiveDocs, tableaux de bord, intégrations, infrastructure, feuille de route, gouvernance.
- Modèle « as code » : 33 types, 100 énumérations, 24 rôles de liens, 21 + 3 workflows, 20 types de documents ; validateur, générateurs FR / EN, annexes A1–A8, 15 tests, CI.
