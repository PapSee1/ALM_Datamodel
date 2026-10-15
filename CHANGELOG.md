# Historique des versions

Toutes les versions sont établies à partir de sources ouvertes uniquement (OSINT). Les numéros de version sont ceux du plan directeur ; le modèle (`model/`) et la configuration générée évoluent avec lui.

## v0.5 — octobre 2026 — Revue de cohérence, organisation, lisibilité (en cours)

- Revue critique de cohérence de l'ensemble du dépôt (modèle, outils, tests, documents) par agents indépendants ; corrections appliquées.
- Vérification en sources ouvertes de l'organisation (BU, Business Lines, unités opérationnelles, sites, filiales) ; énumérations et doc. 01 mis à jour avec niveaux de confiance ; questions ouvertes consignées.
- Passe de lisibilité : sigles et concepts expliqués à leur première apparition, pour un ingénieur débutant.
- Nouvelle Partie 4 « Mise en œuvre et onboarding » (documents 18 à 25 déplacés depuis la Partie 3) ; tous les liens mis à jour.
- Guide de lecture et carte du dépôt (`docs/GUIDE_DE_LECTURE.md`) ; glossaire complété ; registre des sources étendu ; ce journal des versions.

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
- Modèle « as code » : 33 types, 100 énumérations, 24 rôles de liens, 21 + 3 workflows, 20 types de documents ; validateur, générateurs FR / EN, annexes A1–A8, 19 tests, CI.
