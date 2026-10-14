# 18 — Analyse critique du plan directeur et confrontation à une seconde analyse

> Version 0.3, octobre 2026. Revue critique de la version 0.1 du plan et du modèle, confrontée à une seconde analyse produite indépendamment par un autre assistant (conversation « Prompt optimisé pour Polarion Framatome », fournie par le demandeur). Cette seconde analyse est traitée comme une **donnée d'entrée à vérifier**, pas comme une référence. Même contrainte OSINT que le reste du plan : aucune donnée interne.
>
> Format : méthode d'analyse d'écarts SE (forces, écarts 🔴 / 🟡 / 🟢, priorisation Impact × 1/Effort, mise en œuvre des 3 écarts majeurs, matrice de couverture des normes).

## Synthèse

1. **La v0.1 était solide sur le fond**, sur quatre points : les notions de l'arrêté INB, le classement multi-schémas, le socle non négociable et la configuration « as code ». **En revanche, rien ne prouvait qu'elle couvrait réellement chaque typologie de projet.**
   - Rejouée contre les scénarios de couverture introduits en v0.2, elle produit **198 erreurs** :
     - 90 lacunes de couverture : outillage 25, fortuits 10, modifications 8, etc. ;
     - 85 champs obligatoires qui auraient bloqué les imports ReqIF / Word ;
     - 12 incohérences document / profil ;
     - 3 états ambigus.
2. **La seconde analyse apporte surtout des sujets d'organisation et de périmètre :**
   - l'organisation matricielle BU × UO ;
   - des packs réglementaires multi-juridictions ;
   - l'abstraction de filière ;
   - les projets « sas » pour l'entreprise étendue ;
   - un assistant de création de projet ;
   - des signatures adossées aux habilitations ;
   - dix typologies supplémentaires.
3. **Elle contient aussi des propositions fragiles ou inexactes :**
   - un modèle réduit à 12 types, qui fusionne des cycles de vie distincts ;
   - le Test Run traité comme un Work Item ;
   - des booléens de sûreté sans valeur « à déterminer » ;
   - une sémantique de `refines` inversée ;
   - Teamcenter posé comme PLM de Framatome sans source ;
   - une feuille de route de 18 mois ;
   - des codes d'UO invérifiables.
4. **La v0.3 intègre ce qui est pertinent, corrige ce qui ne l'est pas et prouve la couverture des 32 typologies.**
   - Le validateur et les tests ont trouvé quatre défauts réels supplémentaires (§ 4) :
     - les booléens YAML `yes` / `no`, qui généraient des identifiants Polarion `True` / `False` ;
     - un champ propre à la France exigé pour tous les pays ;
     - un rôle de lien inter-projets non déclaré ;
     - un attribut absent des exigences d'entrée.

## 1. Forces de la v0.1 (conservées)

| | Force | Pourquoi c'est important |
|---|---|---|
| ✅ | **Notions de l'arrêté INB natives** (EIP, AIP, exigence définie, contrôle technique, écart) portées par des champs et des conditions bloquantes | La démonstration à l'ASNR repose sur ces notions. Elles doivent être interrogeables, pas enfouies dans du texte. |
| ✅ | **Classement multi-schémas** (`safetyClassScheme`) avec la valeur « à déterminer » par défaut (P4) | Parc, FA3, EPR2, UK, SSG-30, IEC 61226, US et KTA coexistent. Ne jamais affirmer une classe par défaut. |
| ✅ | **Socle non négociable** NN-01..08 appliqué jusqu'au fortuit express | L'approche graduée allège la méthode, jamais les exigences réglementaires. |
| ✅ | **Configuration « as code »** : validation en CI, génération FR / EN, identifiants jamais renommés | Gouvernabilité sur plus de 60 ans, revue par demande de fusion, régénération reproductible. |
| ✅ | **Convention aval → amont** compatible avec la suspicion native de Polarion | Une modification amont interpelle le bon propriétaire, sans développement. |
| ✅ | **Frontière Polarion / PLM / MBSE / GED** explicitée par nature de donnée (ADR-07, ADR-08, ADR-11) | Évite le doublon d'exigences, risque n° 1 d'un déploiement ALM à côté d'un PLM. |

## 2. Évaluation des propositions de la seconde analyse

Verdicts :
- **Retenue** : intégrée telle quelle ;
- **Adaptée** : retenue sur le fond, mise en œuvre différente ;
- **Rejetée** : erronée ou contre-productive ;
- **À vérifier** : invérifiable en source ouverte.

### 2.1 Propositions retenues ou adaptées

| Proposition | Verdict | Justification | Effet dans le modèle v0.3 |
|---|---|---|---|
| Organisation matricielle BU × UO, « co-traitance interne » par lots | **Adaptée** | Le besoin est réel (un projet RGV traverse l'ingénierie, les usines, les essais, le site). Mais des « espaces UO » synchronisés par statut créeraient des doublons. | Type `workPackage` + workflow `wfWorkPackage` (accord signé, remise, réception) ; lien `inWorkPackage` ; champs `responsibleUnit` / `performingUnit` ; règle TR-18 ; rôles `workPackageManager`, `unitManager` ; document `workPackageHandover` (ADR-24, doc. 21) |
| Packs réglementaires choisis au paramétrage du projet (France, US, Allemagne, UK, Canada, AIEA, BPF, défense) | **Retenue** | Évite un fork de configuration par pays. Le modèle global reste unique. | `model/regulatory_packs.yaml` : champs affichés / masqués, autorités, schéma de classement, bibliothèques, règles additionnelles (ADR-25) |
| Abstraction de filière (REP, REB, VVER, CANDU, MTR, Gen IV, hors réacteur) | **Retenue** | Le vocabulaire REP ne doit pas être figé dans la structure (BWR Atrium, CANDU, MTR CERCA). | Énumération `reactorTechnology`, champ `applicableTechnologies` (commun) |
| Le Space n'est pas une frontière de sécurité ; projets « sas » et Custom Sets | **Retenue (corrige la v0.1)** | Exact : les Work Items d'un projet partagent le même tracker, et la recherche ignore le rangement en Space. L'ADR-02 de la v0.1 laissait croire l'inverse. | PR-09, PR-11 ; groupe de projets `EXT-*` et gabarit `TPL-EXT` ; contrôles d'échange XC-01..04 (ADR-28) |
| Gabarits de projets par archétype et assistant de création (« provisioning wizard ») | **Adaptée** | Nécessaire pour éviter les projets artisanaux. Six archétypes plus un master, au lieu de cinq gabarits isolés. | Topologie master → 6 archétypes → 21 spécialisations ; `model/project_setup.yaml` (19 questions, 13 règles de dérivation, processus en 7 étapes) (ADR-26) |
| Signatures conditionnées aux habilitations métiers, décidées à la création du projet | **Retenue** | Demande explicite du demandeur. Cohérente avec l'exigence de compétence des intervenants des AIP (arrêté INB, ISO 19443). | Condition `qualifiedSignatory`, champ `requiredHabilitation`, énumération `habilitationDomain`, paramètre projet `signaturePolicy` (Q13, D11), PR-10 (ADR-27) |
| 10 CFR 50.59 dans la demande de modification (pack US) | **Retenue** | Obligation réglementaire américaine (Framatome Inc.). | Champs `cfr5059Screening`, `cfr5059Outcome`, `cfr5059Reference`, `safetyReportImpact` ; règle TR-19 |
| Assistant qualité de rédaction (gabarits EARS) | **Retenue** | Pratique INCOSE GtWR / ISO 29148 éprouvée. | `requirementPattern`, `requirementQualityScore` (indicatif, jamais bloquant) |
| Suivi des livrables SDRL (usine, fournisseur) | **Retenue** | Livrables contractuels attendus des UO et fournisseurs. | `sdrlReference`, `submittalPurpose` sur `deliverable` |
| ECR / ECO | **Adaptée** | La DM (ECR) est dans Polarion ; l'ordre de modification produit (ECO) reste dans le PLM (ADR-07). | Option `changeOrder` (`actionType`), lien vers le PLM |
| Dix typologies supplémentaires (isotopes, MTR, BWR / CANDU / VVER, US 50.59, configuration à la commande, laboratoire / cellule chaude, défense, atelier chaud, radioprotection…) | **Adaptée** | Valables. Plusieurs se ramènent à une typologie existante plus un pack ou une filière (BWR / CANDU / VVER → `fuelDesign` / `fuelReload` + `reactorTechnology` ; ingénierie US → `plantModification` + pack `usNrc` ; surveillance radiologique → `icApplication`). | 15 typologies ajoutées (§ 2.3), toutes prouvées par scénario (annexe A9) |
| Mendix non nécessaire au démarrage | **Retenue** | Polarion couvre le besoin. La saisie terrain hors ligne passe d'abord par l'aller-retour Excel. | `import_export.yaml` (`XL-FIELD-CAPTURE`) ; Mendix éventuel en vague 3 seulement |
| Baselines figées par jalon / fin d'arrêt (Collections) | **Adaptée** | Les baselines Polarion portent sur tout le projet. Pour les projets conteneurs, on fige plutôt une **collection de documents** par affaire. | Convention `baselineNaming` étendue (tranche × arrêt) ; doc. 21 § 6 |

### 2.2 Propositions rejetées ou à vérifier

| Proposition | Verdict | Motif |
|---|---|---|
| « 12 à 15 types de Work Items au maximum » ; fusion `risk_fmea_item` (risque projet + AMDEC + agression + menace cyber) | **Rejetée** | Le principe P1 (un type = un cycle de vie ou une règle de traçabilité distincts) est plus robuste qu'un plafond arbitraire. Un risque projet (ISO 31000), une agression (démonstration de sûreté) et une ligne d'AMDEC (IEC 60812) n'ont ni les mêmes états, ni les mêmes signataires, ni les mêmes règles de couverture. Avec la fusion, TR-09 (tout danger retenu est maîtrisé) ne peut plus être calculée sans filtre ad hoc. Les scénarios outillage et fortuit, qui chaînent `fmeaItem` —causes→ `hazard`, perdent leur sens. |
| `test_run` comme type de Work Item, lien `executed_in` | **Rejetée** | Dans Polarion, le Test Run est un objet natif (campagne, enregistrements, signatures), pas un Work Item. Le modéliser en Work Item perd la couverture native et la signature des résultats. |
| `safety_related` et `eip_status` booléens | **Rejetée** | Un booléen impose « non » par défaut, ce qui revient à affirmer une absence d'enjeu de sûreté. La v0.1 utilise `yesNoTbd` avec « à déterminer » par défaut (P4, test `test_safety_flags_default_to_tbd`). |
| `component_req refines system_req` ; `risk mitigated_by system_req` | **Rejetée** | En SysML, *refine* précise sans dériver ; la déclinaison est *deriveReqt* (`flowsDownFrom`). Le sens risque → exigence casse la convention aval → amont, donc la suspicion native. |
| Teamcenter posé comme PLM de Framatome | **À vérifier → modèle agnostique** | Les sources ouvertes consultées attestent un *Core Model* 3DEXPERIENCE (ADR-07), pas Teamcenter. La v0.3 traite le PLM comme un paramètre de création de projet (Q17). Elle prévoit les deux connecteurs : `CX-PLM-TC` (intégration native, confiance H) et `CX-PLM-3DX` (OSLC / REST spécifique, confiance P). |
| Description détaillée de la conception NUWARD (intégrée, 2 × 170 MWe) | **Rejetée comme hypothèse de conception** | EDF a annoncé à l'été 2024 la réorientation de la conception NUWARD vers des technologies éprouvées [C]. Le modèle reste neutre : la ligne de produits `PL-NUWARD` ne préjuge pas de la conception. |
| Référentiel de « 45+ UO » avec codes (CRU-F, STMA, JEU…) | **À vérifier** | Les sites sont publics, les codes internes ne le sont pas. L'énumération `operationalUnit` est une amorce marquée à remplacer en atelier (question Q-ORG-01), alimentée ensuite par l'annuaire. |
| ESPN « décret 2015 » ; classes RCC-E « C1–C3 » | **À corriger** | Le texte ESPN est l'**arrêté** du 30 décembre 2015. Les étiquettes de classes attribuées au RCC-E n'ont pas été retrouvées en source ouverte. Le modèle conserve les classes publiées pour FA3 / EPR, avec un niveau de confiance. |
| Feuille de route en 4 phases sur 18 mois, avec pilote NUWARD + RGV | **Rejetée** | Elle est incompatible avec les jalons du plan : 20 à 24 ateliers de validation OSINT, qualification de l'outil comme support d'AIP (IQ / OQ / PQ), consultation des instances représentatives du personnel (doc. 20), trois pilotes contrastés. Les 34 mois de la v0.1 sont maintenus, avec les ajouts du doc. 20. |
| « Espaces Métiers / UO / Usines » renvoyant `Verification_Status` vers l'espace du chef de projet | **Rejetée** | Elle duplique les données et synchronise des statuts. La v0.3 utilise des artefacts uniques rattachés à des lots (`inWorkPackage`), et des liens inter-projets lorsque l'UO tient son propre projet (`P-MFG-*`). |

### 2.3 Typologies : de 17 à 32, toutes prouvées

| Typologie ajoutée (v0.3) | Origine | Classe | Archétype |
|---|---|---|---|
| Augmentation de puissance | Revue critique | B | TPL-02-IB |
| Pièces de rechange / équivalence (CGD) | Seconde analyse + revue | C | TPL-05-SERIES |
| Atelier chaud | Seconde analyse (n° 34) | C | TPL-04-SERVICES |
| Démantèlement (V inversé) | Seconde analyse (n° 25) | B | TPL-02-IB |
| Services combustible sur site | Revue critique | C | TPL-04-SERVICES |
| Combustible / cibles de réacteurs de recherche | Seconde analyse (n° 27) | C | TPL-05-SERIES |
| Licensing d'usine / d'emballage (criticité, LEU+ / HALEU) | Seconde analyse (n° 28) | B | TPL-01-PRODUCT |
| Qualification de procédé / matériau | Seconde analyse (n° 18) | C | TPL-05-SERIES |
| Simulateur pleine échelle | Seconde analyse (n° 13) | B | TPL-01-PRODUCT |
| Cybersécurité d'installation (instance sensible) | Seconde analyse (n° 14) | B | TPL-02-IB |
| Code de calcul scientifique | Revue critique | B | TPL-01-PRODUCT |
| Essais de laboratoire / cellule chaude (ISO/IEC 17025) | Seconde analyse (n° 32) | C | TPL-04-SERVICES |
| Produit catalogue configuré à la commande (FCCS, PAR…) | Seconde analyse (n° 31) | C | TPL-05-SERIES |
| Production d'isotopes médicaux (nucléaire + BPF) | Seconde analyse (n° 26) | B | TPL-01-PRODUCT |
| Programme défense (principe seul, instance dédiée) | Seconde analyse (n° 33) | A | TPL-01-PRODUCT |

La matrice complète figure dans l'[annexe A9](../generated/A9_couverture_typologies.md) : 32 typologies, 261 traces de référence et 8 scénarios transverses, tous verts.

## 3. Omissions de la v0.1 par rapport à la demande complète

La demande initiale reçue était tronquée (« … gestion des »). La fin, récupérée dans la seconde conversation, ajoutait deux items à la Partie 3.

| Attendu de la demande | v0.1 | Écart | v0.3 |
|---|---|---|---|
| Stratégie ReqIF | ADR-12 + doc. 14 (narratif) | Aucun profil de correspondance exploitable | 5 profils ReqIF contrôlés (`import_export.yaml`, annexe A11, doc. 22) |
| Aller-retour Word / Excel, **règles de parsing** | Mentionné | Règles absentes | 11 règles Word (W-01..W-11), portes qualité, 4 gabarits Excel aux colonnes verrouillées |
| Connecteurs PLM (Teamcenter), MBSE (Capella / Cameo), outils de calcul / simulation | 3DX + Capella seulement | Teamcenter, Cameo, Simulink et chaînes de calcul absents | 12 connecteurs avec sens, objets, champs et confiance (annexe A11) |
| **Master Template vs Project Templates** par typologie (SMR, RGV / VD, outillage, combustible) | 13 gabarits à plat | Pas de master ni d'héritage | Master + 6 archétypes + spécialisations, héritage contrôlé (annexe A7) |
| Conduite du changement, pilote, industrialisation | Doc. 16 et 17 | Facteurs sociaux, juridiques et d'exploitation absents | Doc. 20 (facteurs de succès) |
| Applicabilité palier / tranche | Champs `applicablePlantSeries` / `applicableUnits` | Pas de statut par tranche (les liens Polarion ne portent pas d'attributs) | Type `unitDeployment` (v0.2) |
| Tableaux de bord « progrès par discipline » | Doc. 13 | Pas de vue par UO | Champ `performingUnit` + avancement de lot (`progressPercent`) |

## 4. Écarts identifiés et traitement (≤ 15)

Effort : L = faible, M = moyen, H = élevé. Impact noté de 1 à 5.

| # | Niveau | Écart | Référence normative | État v0.1 | Cible (état de l'art) | Mise en œuvre v0.2 / v0.3 | Effort | Impact |
|---|---|---|---|---|---|---|---|---|
| GAP-1 | 🔴 | Couverture des typologies non démontrée | ISO/IEC/IEEE 15288:2023 annexe A (tailoring) ; INCOSE HBK v5 (tailoring) | Profils de classe sans preuve | Chaque typologie a un scénario exécutable (types, documents, traces, attributs, valeurs) | `coverage_scenarios.yaml` + `_validate_coverage` + annexe A9 ; 198 erreurs → 0 | M | 5 |
| GAP-2 | 🔴 | Champs obligatoires bloquant les imports et synchronisations | ISO/IEC/IEEE 29148 (attributs) ; OMG ReqIF | 85 champs `required` sans valeur par défaut | Obligation portée par la transition (`requiredAt`) ; `setByImport` / `creationMode` | Principe P6 + contrôle bloquant au validateur | L | 5 |
| GAP-3 | 🔴 | Effectivité par tranche / cycle absente | ISO 10007 ; EIA-649 (effectivité) | `applicableUnits` multivalué | Un enregistrement par tranche avec son propre cycle de vie | Type `unitDeployment` + `wfUnitDeployment` | M | 5 |
| GAP-4 | 🔴 | Booléens YAML 1.1 : `yes` / `no` → `True` / `False` dans l'énumération générée | Intégrité des données (ALCOA+) | Énumération `yesNoTbd` générée avec des identifiants faux ; requêtes `eip:yes` sans résultat | Typage strict YAML 1.2 | Chargeur YAML 1.2 + contrôle « identifiant textuel » + test de non-régression | L | 5 |
| GAP-5 | 🟡 | Organisation matricielle BU × UO non modélisée | ISO 15288 § 6.3.1 (planification, WBS) | Aucune notion d'UO réalisatrice | Lots contractualisés et réceptionnés | `workPackage`, TR-18, doc. 21 | M | 4 |
| GAP-6 | 🟡 | Champs français imposés à toutes les juridictions | GSR Part 2 (approche graduée) ; 10 CFR 50.59 | `regulatoryModificationClass` exigé en CCB pour tous les projets | Packs par cadre réglementaire | `regulatory_packs.yaml` + contrôle « champ masqué exigé » | M | 4 |
| GAP-7 | 🟡 | Provisioning non outillé ; pas de master template | ISO 15288 § 6.2.1 (modèles de cycle de vie) | 13 gabarits à plat | Questionnaire, dérivation, héritage | `project_setup.yaml` + topologie à 3 niveaux | M | 4 |
| GAP-8 | 🟡 | Compétence des signataires non contrôlée | ISO 19443 § 7.2 ; arrêté INB (AIP, compétences) ; GSR Part 2 | Rôle projet seul | Habilitation nominative vérifiée à la signature (option projet) | `qualifiedSignatory` + `habilitationDomain` | M | 4 |
| GAP-9 | 🟡 | Space présenté comme cloisonnement | Sécurité de l'information (ISO/IEC 27001 A.5.15) | ADR-02 ambigu | Projets sas + permissions par requête | PR-09, `TPL-EXT`, XC-01..04 | L | 4 |
| GAP-10 | 🟡 | Import / export non spécifié de façon vérifiable | OMG ReqIF ; ISO 29148 | Narratif | Profils et règles contrôlés contre le modèle | `import_export.yaml` + `model_checks.py` | M | 4 |
| GAP-11 | 🟡 | Retour d'expérience non capitalisé | ISO 15288 § 6.2.6 (gestion des connaissances) | Champ booléen sur le fortuit | Fiche REX réutilisable, liée aux événements | `lessonLearned`, rôle `capitalizes` (v0.2) | L | 3 |
| GAP-12 | 🟢 | Qualité de rédaction non mesurée | INCOSE GtWR v3 ; EARS | — | Gabarit et score par exigence | `requirementPattern`, `requirementQualityScore` | L | 3 |
| GAP-13 | 🟢 | Obsolescence / dédicace commerciale (CGD) | 10 CFR 21 ; guides EPRI CGD (méthodes 1 à 4) | — | Caractéristiques critiques vérifiées | Champs CGD, méthodes de vérification, TR-20 | L | 3 |
| GAP-14 | 🟢 | Démantèlement : déchets non qualifiés | AIEA GSG-1 ; doctrine française (zonage déchets) | — | Catégorie de déchet par élément | `wasteClass`, `expectedWasteClass` | L | 2 |
| GAP-15 | 🟢 | Livrables contractuels (SDRL) | ISO 15288 § 6.1.1 (acquisition) | — | Ligne SDRL et objet de transmission | `sdrlReference`, `submittalPurpose` | L | 2 |

## 5. Priorisation (Impact × 1 / Effort ; L = 1, M = 2, H = 3)

| Priorité | Écart | Score | Porteur | Phase |
|---|---|---|---|---|
| 1 | GAP-2 Champs obligatoires / imports | 5,0 | Design Authority ALM | Fondations |
| 2 | GAP-4 Typage YAML | 5,0 | Équipe configuration | Fondations |
| 3 | GAP-9 Space ≠ sécurité | 4,0 | Sécurité SI + Design Authority | Cadrage |
| 4 | GAP-1 Couverture des typologies | 2,5 | SE Referents des BU | Cadrage → fondations |
| 5 | GAP-3 Effectivité par tranche | 2,5 | BU Base installée | Pilotes |
| 6 | GAP-11 REX | 3,0 | Qualité | Pilotes |
| 7 | GAP-12 / 13 / 14 / 15 | 2,0 – 3,0 | SE Referents | Industrialisation |
| 8 | GAP-5 / 6 / 7 / 8 / 10 | 2,0 | Design Authority + BU | Fondations → vague 1 |

Les écarts de score 2,0 (GAP-5 à GAP-10) sont **structurants** malgré leur score : ils conditionnent l'ouverture des vagues multi-BU et internationales. Ils sont donc planifiés en fondations (doc. 16).

## 6. Mise en œuvre des trois écarts majeurs

1. **GAP-1, couverture prouvée.** Chaque nouvelle typologie, ou chaque évolution de profil, entre dans `model/coverage_scenarios.yaml` avec cinq listes : types, documents, traces `[source, rôle, cible(, xp)]`, attributs par type et valeurs d'énumération attendues. Le validateur échoue si une trace n'est pas autorisée par les règles de liens, si un type est absent du profil effectif ou si une trace inter-projets emprunte un rôle non déclaré `crossProject`. Les SE Referents des BU **co-écrivent** ces scénarios en atelier : c'est le livrable de validation des hypothèses OSINT.
2. **GAP-2, imports non bloquants.** Est obligatoire à la création uniquement :
   - une énumération dotée d'une valeur par défaut ;
   - un champ posé par l'import (`setByImport`) ;
   - un champ d'un type créé uniquement à la main (`creationMode: manual`).

   Toute autre obligation est déplacée sur la transition (`requiredAt` → `requiredFields`). Les profils ReqIF d'import qui créent des éléments doivent alimenter tous les champs `setByImport` (contrôle `model_checks`).
3. **GAP-4, typage strict.** Le chargeur ne reconnaît comme booléens que `true` / `false` (YAML 1.2). Toute option d'énumération non textuelle est rejetée. Le test `test_yaml_yes_no_stay_strings` protège la non-régression. Sans cette correction, les conditions `eip = yes`, `definedRequirement = yes` et les règles TR-03 / TR-07 / TR-09 auraient été silencieusement inopérantes en production.

## 7. Matrice de couverture des normes

| Norme / texte | Couverture v0.3 | Où |
|---|---|---|
| ISO/IEC/IEEE 15288:2023 (processus techniques, tailoring) | ● | Doc. 07, `tailoring.yaml`, A7, A9 |
| ISO/IEC/IEEE 29148:2018 (exigences) | ● | `requirementCore`, EARS, TR-01..04 |
| ISO/IEC/IEEE 42010:2022 (architecture) | ◐ | RFLP, `designDecision` ; points de vue MBSE dans Capella |
| ISO 10007 / EIA-649 (gestion de configuration) | ● | DM / CCB, baselines, `unitDeployment` |
| IEC 60812:2018 (AMDEC) | ● | `fmeaItem`, `fmeaWorksheet` |
| IEC 61513 / 60880 / 62138 / 62566 (C-C) | ● | Typologies C-C, `softwareRequirement`, `hardwareRequirement` |
| IEC 62645 / 62443 ; 10 CFR 73.54 (cybersécurité) | ◐ | Typologie `cybersecurityCompliance`, instance sensible ; catalogue de mesures à charger |
| Arrêté INB 2012 / arrêté ESPN 2015 | ● | Socle NN, champs EIP / AIP / ESPN, pack `frAsnr` |
| 10 CFR 50 app. B, 50.59, Part 21, Part 810 | ● | Pack `usNrc`, TR-19, contrôle export |
| ISO 19443 (CFSI, ITNS, compétences) | ● | `cfsiSuspected`, `itns`, `qualifiedSignatory` |
| AIEA SSG-30 / GSR Part 2 | ● | Classement multi-schémas, approche graduée |
| EudraLex vol. 4 annexes 11 / 15 ; 21 CFR 11 | ◐ | Pack `medicalGmp` ; validation du système informatisé (doc. 20) |
| ISO/IEC 17025 | ◐ | Typologie `labTesting` ; accréditation hors outil |
| OMG ReqIF 1.1 / 1.2 | ● | Profils ReqIF (A11) |

● couvert · ◐ partiel (complément organisationnel ou hors outil nécessaire)
