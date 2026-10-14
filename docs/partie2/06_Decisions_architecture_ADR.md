# Partie 2.2 — Questions d'architecture à trancher (Architecture Decision Records)

> **Statut de toutes les ADR : PROPOSÉE.** Chaque ADR présente le contexte, les options, les critères, la recommandation et les conséquences. Elle doit être validée par la Design Authority ALM après les ateliers internes (document 05).
>
> Critères transverses de décision :
> - **SÛR** : conformité au socle réglementaire ;
> - **RÉU** : réutilisation ;
> - **PERF** : performance et volumétrie ;
> - **SIMP** : simplicité d'usage ;
> - **GOUV** : gouvernabilité ;
> - **COÛT** ;
> - **RISQ** : risque de mise en œuvre.

## Index

| ADR | Sujet | Recommandation résumée |
|---|---|---|
| ADR-01 | Topologie des projets | Fédération « hub & spoke » : configuration globale, bibliothèques, lignes de produits, projets de réalisation |
| ADR-02 | Granularité des projets | Un projet par contrat ou périmètre majeur ; projets conteneurs pour les affaires courtes |
| ADR-03 | Instances et hébergement | Sur site (on-premise) ; instance standard UE + instance sensible + instance US (à confirmer) |
| ADR-04 | Gestion de la configuration de l'outil | Configuration globale héritée, gabarits de projets, configuration « as code » (ce dépôt) |
| ADR-05 | Variantes et paliers | Combinaison graduée : attributs d'applicabilité → branches → module Variants |
| ADR-06 | Réutilisation des bibliothèques | Branche de document (copie liée et fusionnable) par défaut ; référence figée pour consultation |
| ADR-07 | Périmètre Polarion vs 3DEXPERIENCE Core Model / MES | Polarion = exigences, V&V, démonstration, écarts d'ingénierie ; 3DX = produit, nomenclature, CAO, fabrication |
| ADR-08 | MBSE | Capella maître de l'architecture ; synchronisation vers Polarion |
| ADR-09 | Granularité des types de Work Items | 36 types (v0.3) fondés sur un cycle de vie ou une règle de traçabilité distincts |
| ADR-10 | Classement de sûreté | Multi-schémas tracés (`safetyClassScheme`) + tables de correspondance |
| ADR-11 | Signatures et document de référence | Signatures Polarion + PDF signé archivé en GED (archive de référence) |
| ADR-12 | Collaboration avec l'architecte-ensemblier / client | ReqIF aller-retour + espaces de collaboration ; propriété explicite des exigences |
| ADR-13 | Écarts / CAPA | Écarts d'ingénierie dans Polarion ; écarts de fabrication dans MES / QMS avec lien |
| ADR-14 | Bibliothèque normative et droits d'auteur | Références + paraphrases ; texte intégral seulement sous licence |
| ADR-15 | Langue | Identifiants anglais ; libellés FR ou EN par instance ; documents dans la langue du contrat |
| ADR-16 | Personnalisation | Configuration > scripts > extensions qualifiées ; jamais de modification du cœur |
| ADR-17 | IA générative (Polarion Copilot) | Désactivée par défaut ; ouverture encadrée, LLM sur site uniquement |
| ADR-18 | Licences | Mixte nommées / concurrentes ; REVIEWER pour vérificateurs, approbateurs et clients |
| ADR-19 | Gestion des essais | Test Runs Polarion pour toutes les méthodes V&V ; outils spécialisés reliés |
| ADR-20 | Suspicion | Auto-suspect natif + filtrage par champ via hook (phase 2) |
| ADR-21 | Version et montées de version | Dernière version stable (2606) ; N-1 en production, 1 montée par an minimum |
| ADR-22 | Identification | Préfixes projet courts ; ID externe dans `externalId` |
| ADR-23 | Reprise de l'existant | Greenfield + import ciblé des référentiels actifs uniquement |
| ADR-24 | Organisation matricielle BU × UO (v0.3) | Lots de travaux (`workPackage`) + `performingUnit` ; projet d'exécution d'UO seulement si l'UO porte ses propres enregistrements |
| ADR-25 | Multi-juridiction (v0.3) | Packs réglementaires sur un modèle unique (champs affichés / masqués, règles, bibliothèques) ; abstraction de filière |
| ADR-26 | Gabarits et provisioning (v0.3) | Master non instanciable → 6 archétypes → spécialisations ; création par questionnaire et règles de dérivation |
| ADR-27 | Signatures et habilitations (v0.3) | Politique choisie à la création du projet : rôle seul (défaut) ou rôle + habilitation nominative |
| ADR-28 | Collaboration externe (v0.3, précise ADR-02 et ADR-12) | Projets sas `EXT-*` ; le Space n'est pas une frontière de sécurité |

---

### ADR-01 — Topologie : projet monolithique, projets fédérés ou hybride

- **Contexte.** Le déploiement est multi-BU, avec des typologies très hétérogènes (fortuit de 48 h jusqu'à l'EPR2 sur 15 ans), une forte réutilisation (paliers, produits génériques) et des exigences de cloisonnement (clients, export).
- **Options.**
  - (a) **Monolithe** : un projet unique par BU. Simple pour les requêtes, mais permissions ingérables, performances dégradées, aucune isolation contractuelle.
  - (b) **Fédération stricte** : un projet par affaire, sans partage. Isolation maximale, mais réutilisation nulle, configuration divergente et gouvernance impossible.
  - (c) **Hybride « hub & spoke »** :
    - configuration globale unique héritée ;
    - projets bibliothèques (`LIB-*`) ;
    - projets lignes de produits (`PL-*`) ;
    - projets de réalisation (`P-*`) qui réutilisent par branchement de documents ;
    - liens inter-projets explicites (règles `__other`).
- **Recommandation : (c).** Polarion supporte nativement l'héritage de configuration, les gabarits de projets, les liens inter-projets, les requêtes au niveau du dépôt et le branchement de documents avec fusion 3-way (2404+).
- **Conséquences.**
  - Rapports de portefeuille au niveau du dépôt.
  - Discipline de gouvernance : aucune configuration locale divergente sans dérogation de la Design Authority.
  - Les liens inter-projets doivent être autorisés par les règles de rôles (`__other`), ce que fait le générateur.

### ADR-02 — Granularité des projets

- **Options.** Un projet par affaire (y compris les fortuits), par contrat, par client, ou par BU.
- **Recommandation.**
  - **Un projet par contrat ou périmètre majeur** pour les classes A et B (ex. `P-EPR2-NSSS`).
  - **Un projet conteneur par client ou parc** pour les affaires courtes et nombreuses (fortuits, modifications, recharges, outillages), avec **un Space par affaire**.
- **Justification.**
  - Créer un projet coûte cher en administration (droits, gabarit, plans).
  - Des milliers de fortuits en projets séparés rendraient le portefeuille illisible.
  - Le Space permet l'**organisation** documentaire. Les permissions hiérarchiques par Space sont disponibles depuis 2310.
- **Conséquences.** Volumétrie des projets conteneurs à surveiller (archivage annuel par Space, voir document 15).
- **Correction v0.3.** Le Space n'est **pas** une frontière de sécurité pour les Work Items : tous les Work Items d'un projet partagent le même tracker, et la recherche ou les requêtes ignorent le rangement. Un conteneur ne doit donc jamais mélanger des affaires de clients concurrents ou des données d'export control différentes. Le cloisonnement passe par un projet distinct (ADR-28, PR-09).

### ADR-03 — Instances et hébergement

- **Contexte.** Plusieurs contraintes cohabitent :
  - informations sensibles (sécurité nucléaire, défense, Diffusion Restreinte) ;
  - réglementations US (10 CFR 810, NQA-1) ;
  - contrôle export UE / FR / DE ;
  - souveraineté.
  - Polarion X (SaaS) est hébergé sur AWS.
- **Options.**
  - (a) instance unique en SaaS ;
  - (b) instance unique sur site ;
  - (c) multi-instance sur site : STD (UE), SENS (réseau isolé homologué), US.
- **Recommandation : (c), avec décision formelle par instance.**
  - **STD** : obligatoire.
  - **SENS** : uniquement si des besoins d'ingénierie sur données protégées sont confirmés ; sinon, interdiction de ces données dans l'ALM.
  - **US** : selon l'analyse juridique export.
  - Le SaaS est écarté pour les données d'ingénierie nucléaire, sauf décision contraire de la sécurité (SecNumCloud le cas échéant).
- **Conséquences.**
  - Pas de lien automatique entre instances : échanges ReqIF contrôlés et revus par le contrôle export.
  - Configuration identique déployée partout depuis ce dépôt.

### ADR-04 — Gestion de la configuration de l'outil

- **Recommandation.**
  - **Configuration globale** (types, champs, énumérations, rôles de liens, workflows) héritée par tous les projets. Surcharges projet limitées à `plantUnit`, `businessLine`, requêtes et tableaux de bord.
  - **Gabarits de projets** par typologie (`TPL-*`).
  - **Configuration « as code »** : ce dépôt est la source ; génération des XML (`tools/generate_polarion.py`), revue par demande de fusion (pull request), déploiement DEV → recette → PROD.
- **Conséquences.**
  - Aucune modification manuelle en production dans l'interface d'administration.
  - Toute dérive est détectée par comparaison du dépôt SVN avec les fichiers générés (document 15).

### ADR-05 — Gestion des variantes (paliers 900 / 1300 / N4 / EPR / EPR2 / SMR, tranches, cycles)

- **Options.**
  - (a) **Attributs d'applicabilité** (`applicablePlantSeries`, `applicableUnits`, `applicabilityCondition`) : simple, requêtable, sans licence.
  - (b) **Branches de documents** par variante, avec fusion 3-way : isolation forte, divergences tracées.
  - (c) **Module Polarion Variants** : *feature model*, spécification maître, conditions pvSCL, génération de documents de variante ; licence additionnelle, maturité organisationnelle requise.
- **Recommandation : graduée.**

| Contexte | Mécanisme |
|---|---|
| Parc existant (applicabilité palier / tranche des modifications, réexamens) | (a) |
| Projets de réalisation dérivés d'une référence (paires EPR2, tranches HPC / SZC) | (b) |
| Produits génériques configurables (NUWARD, plateformes C-C, gammes combustibles, catalogue d'outillages) | (c), à évaluer en pilote (phase 3) |
| Recharges (tranche × cycle) | (a) + documents par cycle |

- **Conséquences.** Licence Variants à budgéter pour PL-NUWARD / PL-ICPLATFORM en cas de pilote concluant.

### ADR-06 — Réutilisation des bibliothèques et produits génériques

- **Mécanismes disponibles** :
  - référence d'élément **vivante** (live) ou **figée à une révision** (frozen) ;
  - **document dérivé** (rôle système `derived_from`) : lecture seule hors champs autorisés, mise à jour depuis la source ;
  - **branche** (`branched_from`) : copie modifiable, fusion 3-way.
- **Recommandation.**
  - **Exigences réglementaires et normatives** → **branche**. Le projet doit porter ses champs de conformité (`complianceStatus`, `complianceStatement`) ; la bibliothèque reste neutre.
  - **Gabarits** → copie.
  - **Spécification générique de produit** → branche, ou document dérivé si aucune adaptation locale n'est permise.
  - **Consultation sans engagement** → référence figée.
- **Conséquences.** Les évolutions de la bibliothèque rendent suspects les liens `branched_from`. Le tableau de bord « projets à resynchroniser » est obligatoire.

### ADR-07 — Périmètre Polarion vs 3DEXPERIENCE (Core Model SE / PLM) vs MES / ERP

- **Contexte OSINT [C].** Framatome déploie un *Core Model* SE et PLM sur 3DEXPERIENCE (interfaces MES / ERP). EDF utilise 3DEXPERIENCE (SWITCH). Le risque principal est **le doublon des exigences** dans deux outils.
- **Recommandation : partage par nature de donnée et par source unique.**

| Donnée | Système maître | Copie / proxy |
|---|---|---|
| Exigences (entrée, besoin, système, équipement, logiciel, sûreté), conformité | **Polarion** | Proxy ou lien OSLC dans 3DX si nécessaire |
| Architecture fonctionnelle et logique | **Capella** (ADR-08) | Polarion (`function`, `logicalComponent` synchronisés) |
| Architecture physique, nomenclature, CAO, implantation | **3DEXPERIENCE** (et AVEVA côté EDF) | Polarion (`physicalComponent` proxy avec `plmItemId`) |
| V&V (cas, campagnes, résultats), démonstration de sûreté, hypothèses | **Polarion** | — |
| Modifications d'ingénierie (DM) | **Polarion** pour les exigences et documents ; **3DX** pour les modifications produit (ECO) | Liens croisés |
| Fabrication (gammes, ordres, relevés, preuves de fabrication) | **MES / 3DX** | Polarion référence les preuves (`evidenceReference`) |
| Écarts | Ingénierie → Polarion ; fabrication → MES / QMS (ADR-13) | Lien |
| Documents officiels | **GED** (archive de référence) | Polarion (LiveDocs sources + `edmsReference`) |

- **Alternative à examiner en atelier.** Si le Core Model 3DX porte déjà les exigences pour certaines BU (ex. Le Creusot), Polarion peut se limiter à ces BU pour le haut du V et la démonstration. Une seule source par niveau d'exigence reste obligatoire.
- **Conséquences.** Intégration OSLC / REST Polarion ↔ 3DEXPERIENCE à spécifier (document 14). Gouvernance commune des identifiants pivots.
- **Note v0.3.** Une seconde analyse suppose Teamcenter comme PLM de Framatome, sans source ouverte à l'appui. Le modèle est rendu **agnostique** :
  - le PLM est un paramètre de création de projet (Q17) ;
  - les deux connecteurs sont décrits : `CX-PLM-TC` (natif, confiance H) et `CX-PLM-3DX` (spécifique, confiance P) ;
  - l'objet échangé reste le proxy `physicalComponent` (doc. 22 § 5.1).

  Le coût du connecteur 3DEXPERIENCE pèse dans cette ADR.

### ADR-08 — MBSE : Capella maître ou Polarion maître

- **Contexte.** Capella / Arcadia est utilisé sur les grands projets [C]. Le patron open source *capella2polarion* synchronise un modèle Capella vers des Work Items (client REST), en mode autorité complète ou mixte sur les LiveDocs.
- **Recommandation.**
  - **Capella maître** des éléments d'architecture (fonctions, composants logiques et physiques, échanges et interfaces).
  - **Polarion maître** des exigences, de la V&V et de la démonstration.
  - **Synchronisation unidirectionnelle** Capella → Polarion des éléments d'architecture (`modelElementId`).
  - Liens de traçabilité (`satisfies`, `realizes`) créés **dans Polarion**.
- **Conséquences.**
  - Les éléments synchronisés sont en lecture seule dans Polarion (champs maîtres).
  - Le cycle de vie de ces éléments est porté par le modèle (revue du modèle Capella), Polarion reflétant l'état.
  - Choix d'outil à confirmer : Capella, Siemens System Modeling Workbench, Cameo / SysML v2.

### ADR-09 — Granularité des types de Work Items

- **Options.**
  - (a) peu de types génériques (Requirement, Test, Issue) avec beaucoup d'attributs ;
  - (b) un type par concept métier.
- **Recommandation : (b) bornée par deux règles.** Un nouveau type est créé **seulement si** son cycle de vie diffère, **ou si** sa règle de traçabilité diffère (les règles de rôles de liens Polarion portent sur les types, pas sur les valeurs de champs). D'où 33 types en v0.1, 36 en v0.3 (`unitDeployment`, `lessonLearned`, `workPackage`), discriminés par attributs à l'intérieur de chaque type (`reqLevel`, `analysisType`...).
- **Conséquences.**
  - Le tailoring masque les types inutiles par classe de projet.
  - Le coût de formation est atténué par des menus de création contextuels (formulaires par type).

### ADR-10 — Schéma de classement de sûreté

- **Constat [C].** Plusieurs schémas coexistent :
  - parc (IPS / EIP, K1-K3) ;
  - FA3 (F1A / F1B / F2, M1-3, EE1-2, E1A / E1B / E2, SC1 / SC2) ;
  - EPR2 (catégories 1-3, S1-S3) ;
  - UK EPR ;
  - SSG-30 ;
  - IEC 61226 (A / B / C, classes 1-3) ;
  - US (*safety-related*, 1E).
- **Recommandation.**
  - Ne **pas** forcer un schéma harmonisé.
  - Tracer le schéma utilisé (`safetyClassScheme`), avec des énumérations qui couvrent tous les schémas.
  - Fournir des **tables de correspondance** (indicatives, pour le reporting transverse uniquement).
  - Le champ `eip` (arrêté INB) reste transverse et obligatoire.
- **Conséquences.** Les rapports de portefeuille par « niveau d'enjeu » utilisent une projection (ex. *haut* = F1A / cat. 1 / A / classe 1 / M1 / N1).

### ADR-11 — Signatures électroniques et document de référence

- **Constat.** Polarion offre des signatures de documents et de transitions de Work Items avec ré-authentification, conçues selon le 21 CFR Part 11 et l'Annexe 11 (réponse de conformité Siemens). La conformité reste à la charge de l'utilisateur. En SSO, l'authentification alternative LDAP doit être autorisée pour les signatures.
- **Recommandation.**
  - Signatures Polarion pour le contrôle technique et l'approbation (R / V / A).
  - **Export PDF signé, avec manifeste des signatures, versé à la GED**, qui reste le **système d'archivage de référence** (durée de vie des installations supérieure à 60 ans, formats pérennes PDF/A + ReqIF / XML).
  - Valeur probante définie par procédure qualité (signature électronique simple au sens d'eIDAS, adossée à l'authentification forte). Signature qualifiée seulement si le client l'exige contractuellement (dans la GED).
- **Conséquences.**
  - Validation de l'outil (document 15) couvrant l'intégrité des signatures.
  - Conservation des journaux d'authentification.

### ADR-12 — Collaboration avec l'architecte-ensemblier et les clients

- **Options.**
  - (a) accès direct des clients à l'instance Framatome ;
  - (b) échanges ReqIF aller-retour ;
  - (c) espace de collaboration dédié (projet ou Space) avec licences REVIEWER ;
  - (d) PDF uniquement.
- **Recommandation : (b) + (c)**, selon le contrat.
  - **Propriété explicite** : les exigences du client sont importées en `sourceRequirement` (texte verbatim verrouillé). Les exigences Framatome sont rédigées en aval et liées par `flowsDownFrom`.
  - Aucune modification des exigences du client dans l'outil Framatome : on porte une position de conformité.
- **Conséquences.**
  - Gabarits de correspondance ReqIF par client (`.polarion/reqif/templates`), spécifiés dans `model/import_export.yaml` (doc. 22).
  - Contrôle export avant tout export.
  - **Précision v0.3** : l'« espace de collaboration » de l'option (c) est un **projet** sas `EXT-*`, jamais un Space du projet interne (ADR-28).

### ADR-13 — Écarts et CAPA

- **Recommandation.**
  - Les **écarts d'ingénierie** (conception, documentation, logiciel, essais, constats d'ingénierie sur site) sont gérés dans Polarion (`nonConformance`), car ils doivent être liés aux exigences et aux EIP.
  - Les **écarts de fabrication** sont gérés dans le MES ou le QMS (proximité de l'atelier), avec un **lien obligatoire** vers Polarion lorsqu'ils affectent une exigence définie ou nécessitent une décision d'ingénierie (proxy `nonConformance` avec `externalId`).
- **Conséquences.** Un seul tableau de bord transverse des écarts EIP (consolidation par requête et intégration).

### ADR-14 — Bibliothèque normative et droits d'auteur

- **Recommandation.**
  - Stocker la référence, l'édition, la clause et une paraphrase (`copyrightRestricted`).
  - Négocier avec l'AFCEN et l'IEC des licences d'intégration, notamment pour le **RCC-E 2025 au format « Requirement Engineering »**, qui se prête à un import structuré.
  - Les textes réglementaires publics (Légifrance, ASNR) peuvent être chargés intégralement.
- **Conséquences.** Budget de licences ; procédure de mise à jour par édition (document 04 §10).

### ADR-15 — Langue

- **Recommandation.**
  - Identifiants techniques en anglais (stables).
  - Libellés générés en FR ou en EN par instance ou par projet (`--lang`). Polarion n'offre pas de libellés multilingues pour un même champ personnalisé ; l'interface multilingue (2606) ne couvre que l'interface standard.
  - Glossaire FR / EN / DE (`term`).
  - Documents dans la langue contractuelle (`language`).
- **Conséquences.** L'instance STD franco-allemande utilise les libellés EN ou FR selon le choix de la Design Authority (EN recommandé pour l'instance groupe).

### ADR-16 — Stratégie de personnalisation

- **Ordre de préférence** :
  1. configuration native ;
  2. conditions et fonctions natives de workflow ;
  3. scripts de workflow et de sauvegarde (JavaScript, Polarion Scripting 2410+) ;
  4. extensions open source qualifiées (ex. export PDF, intercepteurs) ;
  5. développements Java spécifiques.
- **Interdits** : modification du cœur ; extensions non maintenues ; logique métier critique non testée.
- **Conséquences.** Chaque script est versionné ici, testé en recette et revu au titre de la validation de l'outil.

### ADR-17 — IA générative (Polarion Copilot, 2512 / 2606)

- **Constat.** Copilot est un module payant reposant sur un LLM (OpenAI via Azure, hébergé par le client). La version 2606 permet des connecteurs LLM personnalisés sur site et une API Copilot.
- **Recommandation.**
  - **Désactivé par défaut** (`com.siemens.polarion.copilot.enabled=false`).
  - Ouverture par cas d'usage validé (aide à la rédaction d'exigences INCOSE, détection d'ambiguïtés, synthèse d'impacts), **uniquement avec un LLM hébergé sur site**.
  - Jamais sur des données sensibles ou soumises au contrôle export.
  - Revue humaine obligatoire et traçabilité de l'usage.
- **Conséquences.** Politique RSSI et juridique ; évaluation de l'impact AIP (un contenu généré reste soumis au contrôle technique).

### ADR-18 — Licences

- **Recommandation.**
  - **ALM** ou **REQUIREMENTS** nommées pour les contributeurs réguliers.
  - **Concurrentes** pour les contributeurs occasionnels.
  - **REVIEWER** pour les vérificateurs, approbateurs, présidents de CCB, relecteurs internes et clients. REVIEWER permet de lire, commenter et approuver des Work Items ; la signature de documents est à confirmer sur la version cible.
  - **QA** pour les équipes V&V.
  - **Variants** selon ADR-05.
- **Conséquences.** Le modèle de rôles (Annexe A6) indique la licence cible de chaque rôle et sert de base au chiffrage.

### ADR-19 — Gestion des essais et de la V&V

- **Recommandation.**
  - Un cas de vérification unique (`verificationCase`) pour toutes les méthodes.
  - **Test Runs** Polarion comme campagnes d'enregistrement : essais usine, essais sur site, revues d'analyses, inspections. Les résultats sont signés (statut `resultsApproved`).
  - Les outils spécialisés (bancs C-C, SIVAT, simulateurs) restent maîtres de l'exécution ; leurs résultats sont importés ou référencés (`evidenceReference`).
- **Conséquences.** Statut de vérification des exigences calculé à partir des derniers enregistrements (script `recomputeVerificationStatus`).

### ADR-20 — Suspicion

- **Constat [C].**
  - L'auto-suspect natif marque les liens des éléments aval à tout enregistrement de l'élément amont, sans filtre par champ ni par rôle.
  - Il ne s'applique pas aux liens parent.
  - Il n'existe pas de propagation transitive, ni de condition native de blocage.
- **Recommandation.**
  - **Phase 1** : auto-suspect natif activé ; levée rapide par le propriétaire aval ; condition de blocage `noSuspectLinks` par script aux approbations et aux clôtures.
  - **Phase 2** : hook de sauvegarde filtrant par champ (`suspectTriggerFields`) et rapport de propagation transitive (N niveaux) pour l'analyse d'impact.
- **Conséquences.** Risque de « bruit » de suspicion en phase 1, à mesurer (indicateur : taux de suspects levés sans modification).

### ADR-21 — Version cible et politique de montée de version

- **Constat [C].** Versions semestrielles : 2404, 2410, 2506, 2512, 2606 (mai 2026). Une version est en fin de vie environ deux ans après sa sortie (ex. 2404).
- **Recommandation.**
  - Démarrer en **2606** (ou dernière version stable au lancement).
  - Politique **N-1** en production ; au moins une montée de version par an.
  - Recette de non-régression automatisée de la configuration (validateur + jeux d'essais).

### ADR-22 — Identification

- **Recommandation.**
  - Préfixe d'ID Polarion = identifiant court du projet.
  - Identifiants externes (client, ReqIF, numéro de document, DOORS) dans `externalId` / `documentNumber`.
  - Pas de sémantique dans les ID (pas de BU, pas de discipline).
  - Les références croisées dans les documents utilisent l'ID Polarion **et** l'ID externe.

### ADR-23 — Reprise de l'existant

- **Contexte.** Le projet est greenfield, mais des référentiels existent (spécifications Word, matrices Excel, éventuels outils d'exigences).
- **Recommandation.**
  - Ne pas migrer l'historique.
  - **Importer seulement les référentiels vivants** : exigences client des contrats en cours, bibliothèques réglementaires, catalogues de produits.
  - Formats : import Word / Excel ou ReqIF, avec contrôles de qualité à l'import (attributs obligatoires, liens).
  - Projets en cours : bascule à un jalon (baseline de départ), jamais en cours de phase.

---

## ADR ajoutées en v0.3 (revue critique, doc. 18)

### ADR-24 — Organisation matricielle BU × UO

- **Contexte.** Un projet piloté par une BU est réalisé par plusieurs UO : ingénierie, usines, essais, filiales, partenaires. La v0.1 ne représentait ni l'UO réalisatrice, ni le contrat interne, ni la réception.
- **Options.**
  - (a) un projet par UO avec synchronisation des statuts ;
  - (b) un Space par UO ;
  - (c) lot de travaux + attribut d'UO ;
  - (d) projet d'exécution d'UO lié au projet BU.
- **Recommandation : (c), complété par (d)** quand l'UO tient ses propres enregistrements qualité (points d'arrêt, FNC usine).
- **Conséquences.**
  - Type `workPackage` + `wfWorkPackage`, lien `inWorkPackage`, TR-18 ;
  - rôles `workPackageManager` et `unitManager` ; document `workPackageHandover` ;
  - tableau de bord par UO au niveau du dépôt (doc. 21).

### ADR-25 — Multi-juridiction : packs réglementaires

- **Contexte.** Activités en France, aux États-Unis, en Allemagne, au Royaume-Uni et au Canada, à l'export, en santé (BPF) et en défense. En v0.1, des champs et règles français s'appliquaient à tous les projets (ex. classement réglementaire de la modification exigé en CCB).
- **Options.**
  - (a) une configuration par pays (fork) ;
  - (b) un modèle unique avec tous les champs visibles ;
  - (c) un modèle unique + packs (champs affichés / masqués par surcharge projet, règles additionnelles, bibliothèques, schéma de classement).
- **Recommandation : (c).**
- **Conséquences.**
  - `model/regulatory_packs.yaml` ; contrôle « champ masqué exigé par une transition » ;
  - énumération `reactorTechnology` pour ne pas figer le vocabulaire REP ;
  - à confirmer en maquette : surcharge des champs par projet sur la version cible (repli : permissions par champ).

### ADR-26 — Gabarits et provisioning

- **Contexte.** La demande distingue un Master Template et des gabarits par typologie. La v0.1 proposait 13 gabarits à plat, et la création de projets n'était pas outillée.
- **Recommandation.**
  - Master non instanciable → 6 archétypes → spécialisations limitées à leurs écarts (`extends`).
  - Création exclusivement par le guichet de provisioning : questionnaire de 19 questions et 13 règles de dérivation.
- **Conséquences.**
  - `model/project_setup.yaml` ;
  - héritage contrôlé par le validateur ;
  - rôle global `provisioningOfficer` ;
  - délai cible de 15 jours ouvrés pour un projet, quelques minutes pour un fortuit (Space d'un conteneur).

### ADR-27 — Signatures et habilitations

- **Contexte.** Le demandeur souhaite que les signatures puissent être conditionnées aux habilitations métiers, par décision prise à la création du projet.
- **Options.**
  - (a) rôle projet seul ;
  - (b) habilitation obligatoire partout ;
  - (c) choix par projet.
- **Recommandation : (c)**, `roleBased` par défaut ; bascule tracée (PR-10).
- **Conséquences.**
  - Condition `qualifiedSignatory`, champ `requiredHabilitation`, groupes `HAB-<domaine>-<niveau>` synchronisés depuis le référentiel RH ;
  - archivage de l'habilitation détenue à la date de signature ;
  - prérequis : référentiel des habilitations (doc. 20, F-18).

### ADR-28 — Collaboration externe : projets sas

- **Contexte.** L'ADR-02 de la v0.1 laissait entendre qu'un Space cloisonne. C'est faux pour les Work Items.
- **Recommandation.**
  - Un projet sas `EXT-<partenaire>-<affaire>` par collaboration, alimenté par branchement de documents ou ReqIF.
  - Permissions fondées sur une requête (Custom Sets) uniquement quand un sas est disproportionné.
  - Comptes externes nominatifs à expiration.
- **Conséquences.**
  - Gabarit `TPL-EXT` ; règles PR-09 et PR-11 ;
  - contrôles d'échange XC-01 à XC-04 ;
  - règle de provisioning D09.
