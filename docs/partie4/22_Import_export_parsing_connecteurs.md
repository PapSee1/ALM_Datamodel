# 22 — Import / export, règles d'analyse et connecteurs

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **forte** (§ 5 connecteurs ; faible pour les règles d'analyse du § 3 et les gabarits Excel du § 4, qui se transposent à tout outil) · Historique : [CHANGELOG](../../CHANGELOG.md) · Carte du dépôt : [guide de lecture](../GUIDE_DE_LECTURE.md).*
>
> **En bref**
> - **À quoi sert ce document :** spécifier comment les exigences et les données entrent dans Polarion et en sortent — échanges ReqIF avec clients et fournisseurs, import de documents Word, aller-retour Excel, connecteurs vers le PLM, les outils MBSE, les codes de calcul, la GED, l'annuaire — et comment ces échanges sont contrôlés et recettés.
> - **Qui le lit :** responsables exigences, ingénieur configuration, responsables PLM / MBSE / GED, interlocuteurs des clients et fournisseurs pour les échanges.
> - **À lire avant :** [guide de lecture](../GUIDE_DE_LECTURE.md), doc. 14 (paysage des intégrations), doc. 08 (modèle de données) ; doc. 21 § 4 pour les projets sas.
>
> Ce document répond au point « Import / Export & interopérabilité » de la demande : stratégie ReqIF, aller-retour Word / Excel, **règles de parsing** (analyse automatique d'un document pour en extraire des éléments structurés), connecteurs PLM (gestion du cycle de vie du produit : Teamcenter / 3DEXPERIENCE), MBSE (ingénierie système fondée sur les modèles : Capella / Cameo) et outils de calcul et de simulation.
>
> Il complète les fiches d'intégration du [doc. 14](../partie3/14_Integrations_et_echanges.md) (I-01..I-11) par une spécification **contrôlée contre le modèle** : `model/import_export.yaml`, vérifié par `tools/model_checks.py`, restitué dans l'[annexe A11](../generated/A11_import_export.md). Un profil qui référence un champ inexistant, une valeur d'énumération inconnue ou un champ calculé éditable fait échouer la CI (intégration continue : les contrôles automatiques rejoués à chaque modification du dépôt). Ce document est le **foyer unique** des fiches connecteurs ; le doc. 14 garde le paysage, la sécurité et le long terme.
>
> Niveaux de confiance de l'échelle du plan : **[C]** confirmé · **[P]** probable · **[H]** hypothèse de modélisation · **[NT]** non trouvé. La colonne « Confiance » des tableaux § 5 reprend les codes de `model/import_export.yaml`, alignés sur cette échelle : **C = fonctionnalité publique documentée par l'éditeur**, **P = à confirmer en maquette sur la version cible**.

## 1. Principes

1. **Une source de vérité par donnée** (ADR-07). L'échange déplace des copies identifiées (`externalId`), jamais la maîtrise de la donnée.
2. **Aucun import direct dans un projet interne** depuis l'extérieur. On reçoit dans un projet sas `EXT-*` (un projet Polarion distinct, réservé à la collaboration avec un partenaire, parce qu'un Space n'est pas une frontière de sécurité — PR-09, doc. 21 § 4), on contrôle (antivirus, conformité au profil), puis on transfère (XC-03).
3. **Tout export est filtré** par `informationClassification` et `exportControl` (XC-01). Il est journalisé dans le sas (XC-02).
4. **Les imports ne sont jamais bloqués par des champs obligatoires** (principe P6 de la politique des champs obligatoires, doc. 08 § 1) ; l'obligation se reporte sur la transition de workflow.
5. **Rien n'est supprimé** par un ré-import : un élément disparu chez le partenaire passe à l'état `superseded` (exigences d'entrée) ou `obsolete`.
6. **Les correspondances sont versionnées** dans ce dépôt et testées à chaque montée de version de Polarion (XC-04).

## 2. ReqIF

ReqIF (*Requirements Interchange Format*) est le format standard de l'OMG pour échanger des exigences entre outils. Version retenue : **OMG ReqIF 1.1 / 1.2** selon le partenaire (lecture de 1.0.1 si le partenaire utilise un outil ancien) [à vérifier sur la version cible] ; noms d'attributs standard selon le guide d'implémentation ReqIF (ProSTEP iViP). Un *profil* est la table de correspondance entre les attributs du fichier ReqIF et les champs du modèle, pour un partenaire et un sens d'échange.

### 2.1 Profils

| Profil | Sens | Type Polarion | Usage |
|---|---|---|---|
| `RIF-CUSTOMER-IN` | Import | `sourceRequirement` | Spécification client verbatim : texte verrouillé (`originalText`), `complianceStatus` = `toBeAssessed` ; attribut `onChangedReimport: reassess` (§ 2.2) |
| `RIF-CUSTOMER-COMPLIANCE-OUT` | Export | `sourceRequirement` | Retour de la matrice de conformité (`complianceStatus`, `complianceStatement`) |
| `RIF-SUPPLIER-OUT` | Export | `equipmentRequirement` | Spécification d'approvisionnement vers un fournisseur ; champs internes exclus (`informationClassification`, `exportControl`, `rationale`, `verificationStatus`) ; filtre d'export |
| `RIF-SUPPLIER-RETURN` | Import (mise à jour seule) | `equipmentRequirement` | Réponse de conformité fournisseur (`supplierComplianceStatus`, `supplierComplianceStatement`, `supplierDocumentReference`) |
| `RIF-LIBRARY-REG` | Import | `regulatoryRequirement` | Alimentation de la bibliothèque réglementaire depuis un texte structuré : `regulatoryReference`, `edition` et nature du texte `regulatoryDocType` (loi, décret, arrêté, décision, guide, norme…) ; `bindingLevel` = obligatoire |

### 2.2 Gestion des identifiants et des révisions

| Situation | Règle |
|---|---|
| Premier import | `ReqIF.ForeignID` (identifiant de l'exigence chez le partenaire) → `externalId` ; document et révision → `sourceDocument` / `sourceDocumentRevision` (champs `setByImport`, posés par l'import et non saisis) |
| Nouvelle révision du partenaire | Mise à jour par `externalId`. Un élément dont le texte a changé repasse de `accepted` à `underAnalysis` par la transition `reassess` (attribut `onChangedReimport: reassess` du profil `RIF-CUSTOMER-IN` ; script d'import à construire, étape S11 du doc. 23). Les éléments disparus passent en `superseded`. Les nouveaux sont créés. |
| Aller-retour avec un fournisseur | L'identifiant Polarion est la clé (`ReqIF.ForeignID` = `id`) ; le profil de retour est en **mise à jour seule** |
| Conflit (élément modifié des deux côtés) | Pas de fusion automatique : rapport de conflit, arbitrage par le responsable exigences |

### 2.3 Négociation avec chaque partenaire

Le profil est une **annexe du plan de management de l'interface** (le document contractuel qui fixe, avec le client ou le fournisseur, ce qui est échangé, par qui et quand) : attributs, types de données, valeurs d'énumération, sens et fréquence. Il est testé sur un fichier de référence échangé avant la première livraison réelle.

## 3. Import Word : règles de parsing

L'assistant d'import Word natif applique des règles **dans l'ordre**. Sur un document stylé, on préfère les règles fondées sur les styles aux mots-clés. Les règles sont celles de `model/import_export.yaml` (W-01..W-11, confiance H ou P selon la règle, annexe A11).

| # | Motif reconnu | Résultat |
|---|---|---|
| W-01 | Styles de titre de niveau n | `heading` (structure du LiveDoc, le document vivant Polarion) |
| W-02 | « doit », « doivent », « shall », « must » | Exigence (`bindingLevel` = `mandatory`) ; type selon le gabarit (exigence d'entrée `sourceRequirement` pour un document client, exigence système `systemRequirement` pour une spécification interne migrée) |
| W-03 | « devrait », « il est recommandé », « should » | Exigence, `bindingLevel` = `recommendation` |
| W-04 | « peut », « may » | Exigence, `bindingLevel` = `permission` (confiance P : « peut » est ambigu en français) |
| W-05 | Identifiant en tête de paragraphe | Capturé dans `externalId` |
| W-06 | « Nota », « Note », « Remarque » | Texte informatif, pas de Work Item (élément de travail Polarion) |
| W-07 | Tableau avec colonne d'identifiants | Un Work Item par ligne ; colonnes mappées sur des champs |
| W-08 | Liste à puces sous une exigence | Rattachée à l'exigence (même Work Item) |
| W-09 | Plusieurs verbes prescriptifs dans un paragraphe | Signalé « à scinder » (`transitionNote`) ; jamais scindé automatiquement (texte verbatim) |
| W-10 | Références normatives | Proposition de liens vers la bibliothèque réglementaire `LIB-REG`, validée par un humain |
| W-11 | Images, équations, tableaux non mappés | Conservés en texte riche |

**Portes qualité :**
- moins de 2 % de paragraphes prescriptifs non capturés (échantillonnage ; double lecture pour la classe A) ;
- aucun élément sans document et révision source ;
- rapport d'import archivé.

Après l'import, l'**assistant de qualité de rédaction** (`requirementPattern`, `requirementQualityScore` ; patrons de phrases EARS — *Easy Approach to Requirements Syntax* — et termes à proscrire du doc. 13 § 4) s'applique aux exigences **rédigées par Framatome**, jamais au texte client verbatim.

## 4. Aller-retour Excel

Excel Round-trip natif : export d'une requête ou d'un document vers un gabarit Excel, édition hors ligne, ré-import par identifiant.

| Gabarit | Type | Éditable | Verrouillé | Usage |
|---|---|---|---|---|
| `XL-COMPLIANCE` | `sourceRequirement` | `complianceStatus`, `complianceStatement` | `originalText`, `externalId` | Contributeur sans licence d'édition |
| `XL-CLASSIFICATION` | `physicalComponent` | `safetyClass`, `eip`, `mechanicalClass`, `electricalClass`, `seismicCategory`, `qualificationClass` | `plmItemId`, `classificationValidated` | Revue de classement en masse par la Sûreté |
| `XL-SUPPLIER` | `equipmentRequirement` | `supplierComplianceStatus`, `supplierComplianceStatement`, `supplierDocumentReference` | `description`, `acceptanceCriteria` | Fournisseur sans accès Polarion |
| `XL-FIELD-CAPTURE` | `technicalIssue` | `detectedOn` (date de détection), `affectedUnit` (tranche), `outageCriticalPath` (chemin critique de l'arrêt) | `issueCategory` | **Saisie terrain hors ligne** en arrêt de tranche (doc. 20, F-12) |

**Règles :**
- colonne ID obligatoire et verrouillée ;
- ni structure ni liens par Excel ;
- refus si l'élément a changé depuis l'export ;
- **jamais de transition ni de signature par Excel**.

## 5. Connecteurs

Les connecteurs d'un projet sont **dérivés au provisioning** : la règle D13 active `CX-MBSE-CAPELLA` ou `CX-MBSE-CAMEO` selon l'outil MBSE déclaré (Q16), la règle D14 active `CX-PLM-TC` ou `CX-PLM-3DX` selon le PLM déclaré (Q17) (doc. 21 § 2.3). Pour le pilote NUWARD : Capella et 3DEXPERIENCE (doc. 23 § 6.2).

| Connecteur | Système | Mécanisme | Sens | Confiance* | Fiche doc. 14 |
|---|---|---|---|---|---|
| `CX-PLM-TC` | Teamcenter (PLM Siemens) | Intégration Polarion – Teamcenter (Active Workspace, le client web de Teamcenter) | Bidirectionnel (liens) | C | I-03 (variante) |
| `CX-PLM-3DX` | 3DEXPERIENCE (PLM Dassault Systèmes, « 3DX ») | OSLC / REST spécifique (OSLC : standard d'interopérabilité par liens entre outils du cycle de vie ; REST : interface web programmable) | Bidirectionnel (liens) | P | I-03 |
| `CX-MBSE-CAPELLA` | Capella (outil MBSE libre, méthode Arcadia) | API REST, patron *capella2polarion* | Modèle → ALM | C | I-02 |
| `CX-MBSE-CAMEO` | CATIA Magic / Cameo (outil SysML, le langage de modélisation système de l'OMG) | OSLC RM (gestion des exigences) ou ReqIF ; passerelle à évaluer | Bidirectionnel | P | — |
| `CX-SIMULINK` | MATLAB / Simulink (modélisation et simulation de systèmes dynamiques, MathWorks) | Connecteur Polarion pour Simulink | Bidirectionnel | C | I-07 |
| `CX-CALC` | Chaînes de calcul scientifique | API REST appelée en fin de calcul | Calcul → ALM | C | — |
| `CX-TEST-BENCH` | Bancs d'essais, intégration continue | Import de résultats xUnit (format XML standard de résultats de tests) dans les Test Runs (campagnes d'exécution de cas de test) | Bancs → ALM | C | I-07 / I-08 |
| `CX-EDMS` | GED (gestion électronique de documents) | PDF/A (format PDF d'archivage) signé + manifeste (`exportToEdms`) | ALM → GED | C | I-05 |
| `CX-ERP` | ERP (progiciel de gestion intégré) | Synchronisation WBS / OTP (structure de découpage du projet) et commandes internes | ERP → ALM | P | I-06 |
| `CX-DIRECTORY` | Annuaire, référentiel RH | Groupes de rôles et d'habilitation | → ALM | C | I-09 |
| `CX-JIRA` | Jira (suivi de tickets des équipes logicielles) | Connecteur Polarion – Jira | Bidirectionnel | C | I-08 |
| `CX-DOORS-MIG` | IBM DOORS (outil de gestion d'exigences à migrer) | Connecteur DOORS ou ReqIF | → ALM (migration) | C | — |

\* Codes de `model/import_export.yaml` : C = fonctionnalité publique documentée par l'éditeur, P = à confirmer en maquette sur la version cible.

### 5.1 PLM : Teamcenter **ou** 3DEXPERIENCE

Les sources ouvertes consultées attestent un *Core Model* 3DEXPERIENCE chez Framatome (ADR-07) [C]. La seconde analyse supposait Teamcenter sans source. Le modèle n'en dépend pas :
- le PLM de référence est un **paramètre de création de projet** (Q17 ; `CX-PLM-3DX` par défaut, `CX-PLM-TC` si Teamcenter) ;
- l'objet échangé est toujours le proxy `physicalComponent` (`plmItemId`, `plmRevision`), c'est-à-dire une copie de référence du composant du PLM, jamais sa définition ;
- la règle de maîtrise est identique : la nomenclature appartient au PLM, le classement et les exigences à Polarion.

Le connecteur Teamcenter est natif côté Siemens. Pour 3DEXPERIENCE, il faut un développement OSLC / REST : c'est à chiffrer en cadrage, car il pèse dans l'équation économique de l'ADR-07.

### 5.2 MBSE : Capella maître, Cameo en option

- **Capella.** Synchronisation unidirectionnelle des fonctions, composants, interfaces et scénarios. Les champs maîtres sont en lecture seule dans Polarion ; les liens de traçabilité sont créés dans Polarion (ADR-08).
- **CATIA Magic / Cameo.** À utiliser si un client ou un partenaire l'impose (approche SysML). L'échange se fait par OSLC RM ou ReqIF ; la passerelle éditeur reste à évaluer en maquette (confiance P). L'identifiant d'élément de modèle est conservé dans `modelElementId`.

### 5.3 Outils de calcul et de simulation

Une chaîne de calcul qualifiée appelle l'API REST en fin d'exécution. Elle crée ou met à jour l'**analyse** : code, version, statut de qualification du code, empreinte du jeu de données (condensat numérique qui identifie sans ambiguïté le jeu de données utilisé), résultat. Elle alimente aussi les **paramètres de conception** : valeur calculée, incertitude, cycle.

**Le connecteur ne change jamais un statut** : le contrôle technique reste humain (`approverNotAuthor`, `qualifiedSignatory`). Une anomalie d'un code (typologie `calculationCode`) se propage par `impacts` aux analyses de tous les projets qui ont utilisé la version concernée (scénario transverse de l'annexe A9).

## 6. Migration et coexistence

| Source | Méthode | Règle |
|---|---|---|
| Documents Word existants (spécifications actives) | Import Word (§ 3) | Uniquement les référentiels **actifs** (ADR-23) ; l'historique reste en GED |
| Matrices Excel | Import Excel avec correspondance de colonnes | Identifiants d'origine dans `externalId` |
| Outils d'exigences existants (ex. DOORS) | ReqIF ou connecteur DOORS | Conservation des identifiants et des liens ; un projet migré n'est plus modifié dans l'outil source (date de gel) |

## 7. Recette des échanges

- **Jeu de référence par profil** : fichier ReqIF, document Word, classeur Excel. Il est rejoué à chaque montée de version (XC-04).
- **Cas OQ** (qualification opérationnelle : essais prouvant que l'outil configuré fait ce qui est spécifié, doc. 15 § 4) : import sans blocage, ré-import d'une révision (modification → `reassess`, suppression → `superseded`, ajout), conflit, filtre d'export (un élément `sensitiveSecurity` ne sort jamais), journal de sas.
- **Indicateurs** : part des échanges ReqIF vs ressaisie, délai d'intégration d'une révision client, taux d'anomalies d'import.
