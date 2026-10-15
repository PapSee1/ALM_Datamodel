# 22 — Import / export, règles d'analyse et connecteurs

> Version 0.3. Ce document répond au point « Import / Export & interopérabilité » de la demande : stratégie ReqIF, aller-retour Word / Excel, **règles de parsing**, connecteurs PLM (Teamcenter / 3DEXPERIENCE), MBSE (Capella / Cameo) et outils de calcul et de simulation.
>
> Il complète les fiches d'intégration du [doc. 14](../partie3/14_Integrations_et_echanges.md) (I-01..I-11) par une spécification **contrôlée contre le modèle** : `model/import_export.yaml`, vérifié par `tools/model_checks.py`, restitué dans l'[annexe A11](../generated/A11_import_export.md). Un profil qui référence un champ inexistant, une valeur d'énumération inconnue ou un champ calculé éditable fait échouer la CI.

## 1. Principes

1. **Une source de vérité par donnée** (ADR-07). L'échange déplace des copies identifiées (`externalId`), jamais la maîtrise de la donnée.
2. **Aucun import direct dans un projet interne** depuis l'extérieur. On reçoit dans un projet sas `EXT-*`, on contrôle (antivirus, conformité au profil), puis on transfère (XC-03).
3. **Tout export est filtré** par `informationClassification` et `exportControl` (XC-01). Il est journalisé dans le sas (XC-02).
4. **Les imports ne sont jamais bloqués par des champs obligatoires** (principe P6) ; l'obligation se reporte sur la transition de workflow.
5. **Rien n'est supprimé** par un ré-import : un élément disparu chez le partenaire passe à l'état `superseded` (exigences d'entrée) ou `obsolete`.
6. **Les correspondances sont versionnées** dans ce dépôt et testées à chaque montée de version de Polarion (XC-04).

## 2. ReqIF

### 2.1 Profils

| Profil | Sens | Type Polarion | Usage |
|---|---|---|---|
| `RIF-CUSTOMER-IN` | Import | `sourceRequirement` | Spécification client verbatim : texte verrouillé, `complianceStatus` = à évaluer |
| `RIF-CUSTOMER-COMPLIANCE-OUT` | Export | `sourceRequirement` | Retour de la matrice de conformité (statut + position) |
| `RIF-SUPPLIER-OUT` | Export | `equipmentRequirement` | Spécification d'approvisionnement vers un fournisseur ; champs internes exclus ; filtre d'export |
| `RIF-SUPPLIER-RETURN` | Import (mise à jour seule) | `equipmentRequirement` | Réponse de conformité fournisseur (`supplierComplianceStatus` / `Statement` / `DocumentReference`) |
| `RIF-LIBRARY-REG` | Import | `regulatoryRequirement` | Alimentation de la bibliothèque réglementaire depuis un texte structuré |

### 2.2 Gestion des identifiants et des révisions

| Situation | Règle |
|---|---|
| Premier import | `ReqIF.ForeignID` → `externalId` ; document et révision → `sourceDocument` / `sourceDocumentRevision` (champs `setByImport`) |
| Nouvelle révision du partenaire | Mise à jour par `externalId`. Les éléments modifiés repassent en analyse (script). Les éléments disparus passent en `superseded`. Les nouveaux sont créés. |
| Aller-retour avec un fournisseur | L'identifiant Polarion est la clé (`ReqIF.ForeignID` = `id`) ; le profil de retour est en **mise à jour seule** |
| Conflit (élément modifié des deux côtés) | Pas de fusion automatique : rapport de conflit, arbitrage par le responsable exigences |

### 2.3 Négociation avec chaque partenaire

Le profil est une **annexe du plan de management de l'interface** avec le client ou le fournisseur : attributs, types de données, valeurs d'énumération, sens et fréquence. Il est testé sur un fichier de référence échangé avant la première livraison réelle.

## 3. Import Word : règles de parsing

L'assistant d'import Word natif applique des règles **dans l'ordre**. Sur un document stylé, on préfère les règles fondées sur les styles aux mots-clés.

| # | Motif reconnu | Résultat |
|---|---|---|
| W-01 | Styles de titre de niveau n | `heading` (structure du LiveDoc) |
| W-02 | « doit », « doivent », « shall », « must » | Exigence (`bindingLevel` = obligatoire) ; type selon le gabarit (exigence d'entrée pour un document client, exigence système pour une spécification interne migrée) |
| W-03 | « devrait », « il est recommandé », « should » | Exigence, `bindingLevel` = recommandation |
| W-04 | « peut », « may » | Exigence, `bindingLevel` = permission (confiance P : « peut » est ambigu en français) |
| W-05 | Identifiant en tête de paragraphe | Capturé dans `externalId` |
| W-06 | « Nota », « Note », « Remarque » | Texte informatif, pas de Work Item |
| W-07 | Tableau avec colonne d'identifiants | Un Work Item par ligne ; colonnes mappées sur des champs |
| W-08 | Liste à puces sous une exigence | Rattachée à l'exigence (même Work Item) |
| W-09 | Plusieurs verbes prescriptifs dans un paragraphe | Signalé « à scinder » ; jamais scindé automatiquement (texte verbatim) |
| W-10 | Références normatives | Proposition de liens vers la bibliothèque réglementaire, validée par un humain |
| W-11 | Images, équations, tableaux non mappés | Conservés en texte riche |

**Portes qualité :**
- moins de 2 % de paragraphes prescriptifs non capturés (échantillonnage ; double lecture pour la classe A) ;
- aucun élément sans document et révision source ;
- rapport d'import archivé.

Après l'import, l'**assistant de qualité de rédaction** (`requirementPattern`, `requirementQualityScore`) s'applique aux exigences **rédigées par Framatome**, jamais au texte client verbatim.

## 4. Aller-retour Excel

| Gabarit | Type | Éditable | Verrouillé | Usage |
|---|---|---|---|---|
| `XL-COMPLIANCE` | `sourceRequirement` | Statut et position de conformité | Texte original, ID externe | Contributeur sans licence d'édition |
| `XL-CLASSIFICATION` | `physicalComponent` | Classes de sûreté, mécanique, électrique, sismique, qualification ; EIP | ID PLM, validation Sûreté | Revue de classement en masse par la Sûreté |
| `XL-SUPPLIER` | `equipmentRequirement` | Réponse fournisseur | Texte, critères d'acceptation | Fournisseur sans accès Polarion |
| `XL-FIELD-CAPTURE` | `technicalIssue` | Date de détection, tranche, chemin critique | Catégorie | **Saisie terrain hors ligne** en arrêt de tranche (doc. 20, F-12) |

**Règles :**
- colonne ID obligatoire et verrouillée ;
- ni structure ni liens par Excel ;
- refus si l'élément a changé depuis l'export ;
- **jamais de transition ni de signature par Excel**.

## 5. Connecteurs

| Connecteur | Système | Mécanisme | Sens | Confiance | Fiche doc. 14 |
|---|---|---|---|---|---|
| `CX-PLM-TC` | Teamcenter | Intégration Polarion – Teamcenter (Active Workspace) | Bidirectionnel (liens) | H | I-03 (variante) |
| `CX-PLM-3DX` | 3DEXPERIENCE | OSLC / REST spécifique | Bidirectionnel (liens) | P | I-03 |
| `CX-MBSE-CAPELLA` | Capella | API REST, patron *capella2polarion* | Modèle → ALM | H | I-02 |
| `CX-MBSE-CAMEO` | CATIA Magic / Cameo | OSLC RM ou ReqIF ; passerelle à évaluer | Bidirectionnel | P | — |
| `CX-SIMULINK` | MATLAB / Simulink | Connecteur Polarion pour Simulink | Bidirectionnel | H | I-07 |
| `CX-CALC` | Chaînes de calcul scientifique | API REST appelée en fin de calcul | Calcul → ALM | H | — |
| `CX-TEST-BENCH` | Bancs, intégration continue | Import de résultats xUnit dans les Test Runs | Bancs → ALM | H | I-07 / I-08 |
| `CX-EDMS` | GED | PDF/A signé + manifeste (`exportToEdms`) | ALM → GED | H | I-05 |
| `CX-ERP` | ERP | Synchronisation WBS / commandes internes | ERP → ALM | P | I-06 |
| `CX-DIRECTORY` | Annuaire, référentiel RH | Groupes de rôles et d'habilitation | → ALM | H | I-09 |
| `CX-JIRA` | Jira | Connecteur Polarion – Jira | Bidirectionnel | H | I-08 |
| `CX-DOORS-MIG` | IBM DOORS | Connecteur DOORS ou ReqIF | → ALM (migration) | H | — |

### 5.1 PLM : Teamcenter **ou** 3DEXPERIENCE

Les sources ouvertes consultées attestent un *Core Model* 3DEXPERIENCE chez Framatome (ADR-07). La seconde analyse supposait Teamcenter sans source. Le modèle n'en dépend pas :
- le PLM de référence est un **paramètre de création de projet** (Q17) ;
- l'objet échangé est toujours le proxy `physicalComponent` (`plmItemId`, `plmRevision`) ;
- la règle de maîtrise est identique : la nomenclature appartient au PLM, le classement et les exigences à Polarion.

Le connecteur Teamcenter est natif côté Siemens. Pour 3DEXPERIENCE, il faut un développement OSLC / REST : c'est à chiffrer en cadrage, car il pèse dans l'équation économique de l'ADR-07.

### 5.2 MBSE : Capella maître, Cameo en option

- **Capella.** Synchronisation unidirectionnelle des fonctions, composants, interfaces et scénarios. Les champs maîtres sont en lecture seule dans Polarion ; les liens de traçabilité sont créés dans Polarion (ADR-08).
- **CATIA Magic / Cameo.** À utiliser si un client ou un partenaire l'impose (approche SysML). L'échange se fait par OSLC RM ou ReqIF ; la passerelle éditeur reste à évaluer en maquette (confiance P). L'identifiant d'élément de modèle est conservé dans `modelElementId`.

### 5.3 Outils de calcul et de simulation

Une chaîne de calcul qualifiée appelle l'API REST en fin d'exécution. Elle crée ou met à jour l'**analyse** : code, version, statut de qualification du code, empreinte du jeu de données, résultat. Elle alimente aussi les **paramètres de conception** : valeur calculée, incertitude, cycle.

**Le connecteur ne change jamais un statut** : le contrôle technique reste humain (`approverNotAuthor`, `qualifiedSignatory`). Une anomalie d'un code (typologie `calculationCode`) se propage par `impacts` aux analyses de tous les projets qui ont utilisé la version concernée (scénario transverse A9).

## 6. Migration et coexistence

| Source | Méthode | Règle |
|---|---|---|
| Documents Word existants (spécifications actives) | Import Word (§ 3) | Uniquement les référentiels **actifs** (ADR-23) ; l'historique reste en GED |
| Matrices Excel | Import Excel avec correspondance de colonnes | Identifiants d'origine dans `externalId` |
| Outils d'exigences existants (ex. DOORS) | ReqIF ou connecteur DOORS | Conservation des identifiants et des liens ; un projet migré n'est plus modifié dans l'outil source (date de gel) |

## 7. Recette des échanges

- **Jeu de référence par profil** : fichier ReqIF, document Word, classeur Excel. Il est rejoué à chaque montée de version (XC-04).
- **Cas OQ** : import sans blocage, ré-import d'une révision (modification, suppression, ajout), conflit, filtre d'export (un élément `sensitiveSecurity` ne sort jamais), journal de sas.
- **Indicateurs** : part des échanges ReqIF vs ressaisie, délai d'intégration d'une révision client, taux d'anomalies d'import.
