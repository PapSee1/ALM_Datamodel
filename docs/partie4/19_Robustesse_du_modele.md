# 19 — Robustesse du modèle de données : critères, preuves, limites

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **faible** · Historique : [CHANGELOG](../../CHANGELOG.md) · Carte du dépôt : [guide de lecture](../GUIDE_DE_LECTURE.md).*
>
> Rédigé en v0.3, complété en v0.5 (§ 3). Ce document explique **pourquoi le modèle est réputé robuste** et **comment on le prouve à chaque évolution**. Il précise aussi **ce qui ne peut pas être prouvé statiquement** et reste à démontrer sur une instance Polarion (recette, OQ : qualification opérationnelle).

> **En bref**
> - Le modèle n'est pas « robuste parce qu'on l'a relu » : neuf critères (R1 à R9) sont vérifiés automatiquement par le validateur (`tools/almmodel.py`) et par des tests qui dégradent volontairement le modèle pour s'assurer que la dégradation est détectée.
> - Lecteurs : responsable IS (ingénierie système), ingénieurs configuration, Sûreté et Qualité (§ 3 : défauts réels corrigés), toute personne qui doit faire confiance au modèle avant un atelier.
> - À lire avant : doc. 08 (modèle de données) et doc. 09 (liens et traçabilité) ; les annexes A7 (profils de tailoring) et A9 (couverture des typologies) sont les preuves générées.

## 1. Critères de robustesse

| # | Critère | Question posée | Mécanisme de preuve |
|---|---|---|---|
| R1 | Complétude par typologie | Chaque type de projet dispose-t-il des types, documents, liens, attributs et valeurs dont il a besoin, dans **son** profil de tailoring (adaptation graduée du processus aux enjeux) ? | Scénarios de couverture (`coverage_scenarios.yaml`), annexe A9 |
| R2 | Intégrité référentielle | Toute référence (type, champ, énumération, rôle, état, rôle projet, gabarit, instance, pack) existe-t-elle ? | `almmodel.validate()` + `model_checks.py` |
| R3 | Importabilité | Un import ReqIF (format standard d'échange d'exigences) / Word, une synchronisation Capella ou PLM (gestion du cycle de vie produit) peut-il créer des éléments sans être bloqué ? | Politique P6 (`required` restreint), contrôle des profils d'import |
| R4 | Multi-juridiction | Un projet US, allemand, britannique, canadien ou BPF (bonnes pratiques de fabrication pharmaceutiques) est-il exempt de champs ou de règles propres à la France qui le bloqueraient ? | Packs réglementaires ; contrôle « champ masqué exigé par une transition » |
| R5 | Invariants de sûreté | Le socle non négociable est-il présent dans toutes les classes ? Le contrôle technique est-il toujours indépendant ? Les drapeaux de sûreté valent-ils « à déterminer » par défaut ? | Contrôles dédiés + tests (`test_non_negotiable_core_in_every_class`, `test_technical_check_transitions_enforce_independence`, `test_safety_flags_default_to_tbd`) |
| R6 | Univocité sémantique | Un même identifiant d'état a-t-il la même catégorie dans tous les workflows ? Un champ partagé a-t-il le même type partout ? | Contrôles « catégories divergentes » et « définition incohérente » |
| R7 | Typage des données | Les identifiants générés sont-ils exactement ceux du modèle ? | Chargeur YAML 1.2 + contrôle « identifiant textuel » |
| R8 | Validité de la configuration générée | Les XML Polarion sont-ils bien formés et cohérents (pas de requête Lucene — le moteur de recherche de Polarion — purement négative, rôles inter-projets ouverts à `__other`, jeton qui autorise une cible dans un autre projet) ? | Tests de génération |
| R9 | Évolutivité | Le modèle peut-il évoluer sans casser les projets existants ? | Identifiants jamais renommés, ajout par extension (fieldSets, packs, spécialisations de gabarits), CI (intégration continue) qui régénère et compare |

## 2. Preuves obtenues

### 2.1 Rejeu de la version 0.1

Les contrôles de la v0.2 ont été rejoués sur une copie de la v0.1, sans modification du modèle : **198 erreurs**.

| Famille | Nb | Exemples |
|---|---|---|
| Couverture des typologies | 90 | Outillage spécial (25 : pas de `function`, `interface`, `hazard`, `fmeaItem`, `toolingSpec` dans le profil de classe C), fortuit (10), modification (8), fabrication de composant, R&D |
| Champs obligatoires bloquants | 85 | `discipline`, `reqCategory`, `stakeholder`, `verificationMethod`… obligatoires dès la création, donc imports ReqIF / Word impossibles |
| Documents incohérents avec le profil | 12 | Type principal d'un document absent du profil de la typologie (ex. `safetyCase` sans `safetyRequirement`) |
| États ambigus | 3 | Même identifiant d'état en catégorie « terminé » dans un workflow et « en cours » dans un autre (KPI — indicateurs de pilotage — faux) |
| Autres | 8 | Définitions de champ incohérentes, champs natifs redéfinis (`location`) |

### 2.2 État de la version 0.3 (et compte courant)

| Indicateur | v0.1 | v0.3 |
|---|---|---|
| Typologies de projet | 17 (non prouvées) | **32 (toutes prouvées)** |
| Traces de référence vérifiées | 0 | **261** + 8 scénarios transverses |
| Types de Work Items | 33 | 36 (`unitDeployment`, `lessonLearned`, `workPackage`) |
| Attributs distincts | 284 | 325 |
| Énumérations | 100 | 111 |
| Rôles de liens | 24 | 26 (`capitalizes`, `inWorkPackage`) |
| Workflows de Work Items + documents | 21 + 3 | 24 + 3 |
| Types de LiveDocs | 20 | 22 (`qualificationDossier`, `workPackageHandover`) |
| Règles de traçabilité | TR-01..17 | TR-01..20 |
| Rôles projet / globaux ; règles de permission | 32 / 5 ; PR-01..08 | 34 / 7 ; PR-01..11 |
| Gabarits | 13 à plat | 1 master, 6 archétypes, 21 spécialisations |
| Modèles complémentaires | — | Provisioning, packs réglementaires, import / export |
| Erreurs du validateur | 198 (rejeu) | **0** |
| Avertissements | 12 | **0** (37 informations : types optionnels volontairement masqués par l'approche graduée) |
| Tests de non-régression | 15 | 46 (v0.5) |

**Compte courant (v0.5, octobre 2026)** : 36 types, 327 attributs distincts, 112 énumérations, 26 rôles de liens, 24 + 3 workflows, 22 types de LiveDocs, 28 gabarits ; 0 erreur, 0 avertissement. Les informations du validateur (types optionnels masqués par un profil, types d'un document ni cascadés ni contrôlés à son approbation, libellés différents selon le type) sont listées par `python3 tools/almmodel.py -v` ; les comptes exacts sont régénérés dans les annexes A1 à A11.

### 2.3 Tests par mutation

Chaque contrôle est protégé par un test qui **dégrade volontairement** le modèle (c'est le sens de « mutation ») et vérifie que le validateur détecte la dégradation :

| Test | Mutation | Détection attendue |
|---|---|---|
| `test_coverage_detects_tailoring_regression` | Retrait de `physicalComponent` du profil express | Scénario fortuit en échec |
| `test_required_fields_do_not_block_imports` | `discipline` rendue obligatoire à la création | Erreur P6 |
| `test_validator_detects_unknown_enum` | Champ vers une énumération inexistante | Erreur référentielle |
| `test_validator_detects_native_field_redefinition` | Redéfinition de `status` | Erreur « champ natif » |
| `test_validator_detects_unreachable_state` | État orphelin | Erreur « inatteignable » |
| `test_pack_hidden_field_cannot_be_required` | Champ français réintroduit en obligatoire en CCB | Erreur « champ masqué exigé » |
| `test_cross_project_trace_needs_cross_project_role` | `supersedes` privé de `crossProject` | Erreur sur les traces d'obsolescence |
| `test_import_profiles_reference_model_fields` | Champ inexistant dans un profil ReqIF | Erreur sur le profil |
| `test_yaml_yes_no_stay_strings` | — (invariant) | Les options `yes` / `no` restent textuelles |

## 3. Défauts réels trouvés pendant la v0.3

Les contrôles ajoutés en v0.3 ont révélé, **dans le modèle tel qu'il était**, quatre défauts invisibles à la relecture. Chacun aurait eu un effet en production :

1. **Booléens YAML 1.1.** PyYAML (bibliothèque Python de lecture du YAML) interprète `yes` / `no` comme des booléens. L'énumération `yesNoTbd` était générée avec les identifiants Polarion `True` / `False`, alors que toutes les conditions, requêtes et règles (`eip = yes`, TR-03, TR-07, TR-09, TR-11) utilisent `yes`. **Toutes les conditions de sûreté portant sur ces drapeaux auraient été inopérantes.** Correction : chargeur YAML 1.2, contrôle d'identifiant textuel, test.
2. **Champ français imposé partout.** La transition « présenter en CCB » (comité de maîtrise des modifications) exigeait `regulatoryModificationClass` (classement des modifications au sens de la réglementation INB). Un projet US ou allemand n'aurait jamais pu présenter une DM (demande de modification) en CCB. Correction : exigence conditionnée au pack `frAsnr`.
3. **Rôle inter-projets non déclaré.** La trace d'obsolescence (article de remplacement `supersedes` l'article du référentiel parc, dans un autre projet) utilisait un rôle non ouvert aux liens inter-projets. Correction : `supersedes` déclaré `crossProject`, contrôle généralisé.
4. **Attribut manquant.** Les règles d'import Word posent la force (`bindingLevel` : doit / devrait / peut) sur les exigences d'entrée, qui ne portaient pas ce champ. Correction : champ ajouté à `sourceRequirement`.

**Revue de cohérence v0.5.** Une relecture croisée du modèle, des générateurs, des tests et des documents a conduit aux compléments suivants (détail dans le [CHANGELOG](../../CHANGELOG.md)) :
- un **état de soumission** par workflow (`submitState`) et des champs « requis à la soumission », exigés par le générateur sur les transitions qui y mènent (principe P6 (obligation portée par la transition), en-tête de `model/work_item_types.yaml`) ;
- une **cascade document → éléments** explicite par type de document (`primaryType`, `cascadeTypes`, `approvalGate` dans `model/document_types.yaml`) : à la mise en vérification d'un LiveDoc, ses éléments en brouillon sont soumis ; à son approbation, les éléments cascadés doivent être approuvés ;
- des **signatures générées systématiquement** et récapitulées dans le manifeste `generated/polarion/<lang>/SIGNATURES_ET_SCRIPTS.md`, qui liste aussi les 17 scripts de workflow appelés ; les workflows d'exigences, d'architecture, d'analyses de sûreté et de cas de vérification n'en portent pas (contrôle technique par Approvals + `approverNotAuthor`, signature portée par le LiveDoc) ;
- une **annexe D** des constructions Polarion plausibles mais non confirmées sur la version cible (PF-01..PF-14), à lever au spike S1 du doc. 23 ;
- les **seuils de classe** de tailoring lus depuis `tailoring.yaml` (score ≥ 15 → A, ≥ 9 → B, ≥ 4 → C, sinon D) au lieu d'être codés dans les outils ;
- les **énumérations d'organisation** (`businessUnit`, `businessLine`, `operationalUnit`) refondues depuis une campagne OSINT (sources ouvertes), avec un niveau de confiance par valeur (doc. 01).

## 4. Lecture de la matrice de couverture (extrait)

| Archétype | Typologies | Classe dominante | Point de vigilance |
|---|---|---|---|
| TPL-01-PRODUCT | Grand réacteur, SMR (petit réacteur modulaire), combustible, plateforme et projet C-C (contrôle-commande), R&D, simulateur, code de calcul, licensing, isotopes, défense | A / B | Synchronisation MBSE (ingénierie fondée sur les modèles), lignes de produits, argumentaire de sûreté |
| TPL-02-IB | RGV (remplacement de générateurs de vapeur), réexamen, modification, augmentation de puissance, démantèlement, cybersécurité, rénovation C-C | B / C | Effectivité par tranche (`unitDeployment`), liens vers le référentiel parc (inter-projets) |
| TPL-03-EXPRESS | Fortuit (aléa technique découvert en arrêt de tranche) | D | Socle non négociable en délai court ; REX (retour d'expérience) |
| TPL-04-SERVICES | Outillage, inspection, atelier chaud, services combustible, laboratoire | C | Exemplaires suivis par numéro de série, campagnes, essais |
| TPL-05-SERIES | Recharge, conception et fabrication de composant, équivalence CGD (dédicace d'articles commerciaux), MTR (réacteurs de recherche), qualification de procédé, configuration à la commande | B / C | Branche de la spécification maître, qualification de type réutilisée, FNC (fiches de non-conformité) usine |
| TPL-06-LIBRARY | Bibliothèques | A | Publication versionnée, droits d'auteur des normes |

Détail par typologie : [annexe A9](../generated/A9_couverture_typologies.md). Profils effectifs : [annexe A7](../generated/A7_tailoring.md).

## 5. Ce que la validation statique ne prouve pas

| Limite | Pourquoi | Comment la lever |
|---|---|---|
| Comportement des scripts de workflow (`fra-*.js` : indépendance, avis sûreté, règles de valeur, habilitation, cardinalités) | Spécifiés (doc. 10 § 4, doc. 23 § 3), non développés | Développement + tests OQ dérivés des conditions du modèle (doc. 15) |
| Requêtes Lucene et LiveReports (pages de rapport Polarion) | Syntaxe contrôlée, résultat non exécuté | Recette sur jeu de données de référence, par typologie (les scénarios A9 servent de cas de recette) |
| Performances (projets de plus de 100 000 éléments, requêtes inter-projets, suspicion en cascade) | Hors du champ du modèle | Tirs de charge en fondations (doc. 20, facteur F-17) |
| Formats XML générés et surcharge des champs par projet (packs, extensions `x_`) | Constructions plausibles, jamais chargées dans une instance (annexe D, PF-01..PF-14) | Spike S1 du doc. 23 (maquette en fondations) ; repli : permissions par champ |
| Valeurs d'énumération issues de l'OSINT (UO, Business Lines, sites : doc. 01, campagne du 15 octobre 2026) | Sources ouvertes, non internes | Ateliers (doc. 05 ; atelier B2 du doc. 24) ; alimentation par l'annuaire |
| Références réglementaires de confiance P | Sources ouvertes partielles | Vérification par le juridique et le licensing |
| Fonctionnalités Polarion de confiance P (connecteur Cameo, droits de signature de la licence REVIEWER, Collections) | Dépendent de la version et des licences [à vérifier, annexe D / spike S1, Q-TOOL-01 et Q-TOOL-03] | Maquette éditeur avant la commande des licences |

## 6. Règles pour garder le modèle robuste

1. **Aucune typologie sans scénario**, aucun scénario sans revue par un SE Referent (référent ingénierie système) de la BU.
2. **Aucun champ obligatoire à la création** hors politique P6.
3. **Aucun champ propre à une juridiction** dans une condition non conditionnée à son pack.
4. **Toute trace inter-projets** passe par un rôle `crossProject` ou un rôle système.
5. **Les informations « types optionnels masqués » sont relues** à chaque évolution de profil : une information qui devient un besoin se traduit par un `addTypes`.
6. **Chaque correction de défaut s'accompagne d'un test par mutation** (§ 2.3).
