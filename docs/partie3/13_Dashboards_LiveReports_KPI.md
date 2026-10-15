# Partie 3.7 — Tableaux de bord, LiveReports et indicateurs de pilotage

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **faible** (§ 5–6 spécifiques à Polarion : requêtes Lucene / SQL et widget Velocity ; les indicateurs K-xxx sont indépendants de l'outil) · Historique : [CHANGELOG](../../CHANGELOG.md) · Carte du dépôt : [guide de lecture](../GUIDE_DE_LECTURE.md).*
>
> **Syntaxe de requête** (langage de recherche Lucene de Polarion, annexe D PF-08 [à vérifier au spike S1]). Les opérateurs `AND` / `OR` / `NOT` s'écrivent en majuscules ; un espace vaut OR ; énumération personnalisée : `champ.KEY:valeur` ; champ vide : `NOT HAS_VALUE:champ` ; liens : `linkedWorkItems:rôle=ID` (éléments qui lient vers ID) et `backlinkedWorkItems:rôle=ID` (cibles des liens de ID) ; suspects : `suspect:true` ; dates relatives : `$today$`, `$today-2w$`. L'absence de lien d'un rôle donné nécessite une requête `SQL:(…)` (§ 5).
> Les requêtes marquées ⚠ sont à valider sur l'instance de recette (version cible). Tous les identifiants d'états et de champs cités ont été vérifiés contre `model/workflows.yaml` et `model/work_item_types.yaml` (v0.5).

> **En bref**
> - Ce document est le **catalogue des indicateurs** (K-xxx : définition, requête de référence, seuil de départ, public) et des **tableaux de bord par rôle** ; il donne aussi la liste des termes vagues à proscrire dans les exigences et deux exemples techniques (requête SQL de couverture, widget Velocity).
> - Un *LiveReport* est une page de rapport Polarion construite à partir de requêtes ; un *KPI* (indicateur clé de performance) est ici toujours calculé depuis les données, jamais saisi.
> - Lecteurs : chefs de projet, responsables techniques et des exigences, Sûreté, Qualité, V&V, CCB, Design Authority ALM, DSI ; les § 5–6 s'adressent à l'intégrateur Polarion.
> - À lire avant : doc. 09 § 6 (définitions normalisées des couvertures), doc. 10 (états des workflows).

## 1. Principes

1. **Un indicateur = une définition normalisée** (document 09 § 6), une requête de référence, un seuil, un propriétaire, une fréquence.
2. **Pas de saisie manuelle d'indicateurs** : tout est calculé depuis les Work Items, les liens, les Test Runs (campagnes d'exécution des cas de vérification) et l'historique.
3. Tableaux de bord **par rôle** (pages LiveReport dans les gabarits de projets) et **de portefeuille** (requêtes au niveau du dépôt, tous projets).
4. Les seuils sont des **valeurs de départ** à calibrer après les pilotes.

## 2. Catalogue des indicateurs

**Légende de la colonne « Public »** (rôles projet de `model/roles.yaml`, annexe A6) : **CP** = chef de projet (`projectManager`) · **RE** = responsable des exigences (`requirementsManager`) · **RT** = responsable technique (`technicalLead`) · **GI** = gestionnaire d'interfaces (`interfaceManager`) · **V&V** = responsable et ingénieurs vérification-validation (`vvLead`, `vvEngineer`) · **Sûreté** = `safetyEngineer`, `safetyLead` · **Qualité** = `qualityEngineer` · **CCB** = comité de maîtrise des modifications (`ccbChair`, `ccbMember`) · **Gest. configuration** = `configurationManager` · **Licensing** = `licensingEngineer` · **BI** = BU Base installée (chef de projet d'arrêt, cellule fortuits ; à ne pas confondre avec l'informatique décisionnelle du § 7) · **DA ALM** = Design Authority ALM (propriétaire du modèle, doc. 17) · **DSI** = direction des systèmes d'information (exploitant de la plateforme) · **RSSI** = responsable de la sécurité des systèmes d'information · **Direction** = direction de BU ou de portefeuille · **client** = relecteur client (`customerReviewer`, via projet sas).

### 2.1 Exigences et traçabilité

| ID | Indicateur | Définition / formule | Requête de référence | Seuil indicatif | Public |
|---|---|---|---|---|---|
| K-REQ-01 | Volume d'exigences par niveau et état | Comptage par `type` × `status` | `type:(stakeholderRequirement systemRequirement equipmentRequirement softwareRequirement hardwareRequirement safetyRequirement)` | — | CP, RE |
| K-REQ-02 | Maturité | % d'exigences `maturity` ∈ {tbd, tbc} (à définir, à confirmer) | `type:systemRequirement AND maturity.KEY:(tbd tbc)` | < 5 % à la CDR (revue de conception détaillée) | RT |
| K-REQ-03 | Exigences d'entrée non évaluées | `sourceRequirement` avec `complianceStatus = toBeAssessed` | `type:sourceRequirement AND complianceStatus.KEY:toBeAssessed` | 0 à la revue d'exigences | RE |
| K-REQ-04 | Non-conformités et dérogations demandées | `complianceStatus` ∈ {nonCompliant, deviationRequested} | `type:sourceRequirement AND complianceStatus.KEY:(nonCompliant deviationRequested)` | Suivi nominatif | CP, client |
| K-REQ-05 | Couverture de déclinaison | Voir document 09 § 6 | SQL ⚠ (§ 5) | > 95 % à la CDR | RE |
| K-REQ-06 | Couverture d'allocation | % d'exigences avec `satisfies` entrant | SQL ⚠ | > 95 % à la CDR | RT |
| K-REQ-07 | Exigences sans méthode de vérification | Exigences approuvées | `type:systemRequirement AND status:approved AND NOT HAS_VALUE:verificationMethods` | 0 | RE |
| K-REQ-08 | Qualité rédactionnelle | Exigences contenant des termes ambigus (§ 4) | `type:systemRequirement AND description:(adéquat suffisant "si possible" approprié minimiser maximiser environ "et/ou")` ⚠ | Tendance à la baisse | RE |
| K-REQ-09 | Orphelins | Éléments sans lien qualifié | SQL ⚠ | 0 sur les éléments approuvés | RE |
| K-REQ-10 | Exigences d'interface non liées à une interface | Catégorie interface sans `satisfies` depuis une `interface` | SQL ⚠ | 0 | GI |

### 2.2 V&V

| ID | Indicateur | Définition | Requête | Seuil | Public |
|---|---|---|---|---|---|
| K-VV-01 | Couverture planifiée | % d'exigences avec au moins un `verifies` / `validates` entrant depuis un cas approuvé | SQL ⚠ | > 90 % à la TRR (revue de préparation des essais) | V&V |
| K-VV-02 | **Couverture des exigences définies** | Idem pour `definedRequirement = yes` (exigence assignée à un EIP, arrêté INB) | `definedRequirement.KEY:yes AND NOT verificationStatus.KEY:(passed passedWithReserves)` (reste à faire) | **100 % à la clôture** (≥ 90 % en fin de pilote, SC-02) | Sûreté, Qualité |
| K-VV-03 | Avancement V&V (*burn-up* : courbe cumulée du réalisé face au total planifié) | Cumul des résultats `passed` dans le temps, par étape (`vvStage`) | Test Runs : statistiques par campagne | Selon le plan | V&V, CP |
| K-VV-04 | Taux de premier passage | Résultats `passed` au premier enregistrement / total | Test Records (enregistrements d'exécution d'un cas dans un Test Run) | > 85 % | V&V |
| K-VV-05 | Anomalies ouvertes par gravité et âge | `anomaly` non closes | `type:anomaly AND NOT status:(closed rejected waived)` | Âge médian < 30 j | V&V, RT |
| K-VV-06 | Anomalies à impact sûreté | `safetyImpact = yes` ouvertes | `type:anomaly AND safetyImpact.KEY:yes AND NOT status:(closed rejected)` | Suivi nominatif | Sûreté |
| K-VV-07 | Points d'arrêt à venir | Cas avec `inspectionPoint = hold` (point d'arrêt : l'activité ne continue pas sans l'accord du client ou de l'inspecteur) planifiés dans les 30 jours | `type:verificationCase AND inspectionPoint.KEY:hold` + plan | — | Qualité, client |
| K-VV-08 | Réserves non levées | Résultats `passedWithReserves` sans action close | Rapport | 0 à la réception | V&V |

### 2.3 Sûreté et démonstration

| ID | Indicateur | Définition | Requête | Seuil | Public |
|---|---|---|---|---|---|
| K-SAF-01 | Agressions retenues non maîtrisées | `hazard` `screening = retained` sans `mitigates` entrant | SQL ⚠ | 0 à la revue de sûreté | Sûreté |
| K-SAF-02 | Classement non validé | `physicalComponent` EIP avec `classificationValidated = false` | `type:physicalComponent AND eip.KEY:yes AND NOT classificationValidated:true` ⚠ | 0 à la CDR | Sûreté |
| K-SAF-03 | EIP / exigences « À déterminer » | `eip` ou `definedRequirement` = tbd sur des éléments approuvés | `eip.KEY:tbd OR definedRequirement.KEY:tbd` | 0 sur les approuvés (socle NN-01) | Sûreté |
| K-SAF-04 | Couverture de l'argumentaire | % de revendications (*goal* / *strategy*) étayées | SQL ⚠ | 100 % au dépôt du dossier | Sûreté, Licensing |
| K-SAF-05 | Hypothèses ouvertes | `assumption` `open`, par échéance | `type:assumption AND status:open` | 0 hypothèse de sûreté ouverte à la clôture | RT, Sûreté |
| K-SAF-06 | Marges | `designParameter` avec marge < seuil | Rapport (champ calculé `margin`) | Alerte si marge < X % | Disciplines |
| K-SAF-07 | Engagements envers l'autorité | `regulatoryCommitment` par échéance ; en retard | `type:regulatoryCommitment AND NOT status:(closed cancelled) AND commitmentDueDate:[19700101 TO $today$]` ⚠ | 0 en retard | Licensing, Direction |

### 2.4 Configuration, modifications, écarts

| ID | Indicateur | Définition | Requête | Seuil | Public |
|---|---|---|---|---|---|
| K-CHG-01 | Demandes de modification (DM) par état et classe | `changeRequest` × `status` × `changeClass` | `type:changeRequest` | — | CCB |
| K-CHG-02 | Délai de cycle des demandes | Médiane (émission → clôture), par classe | Historique | Classe II < 30 j | CCB |
| K-CHG-03 | Demandes en attente de CCB | `status:ccbReview` âgées de plus de 15 j | `type:changeRequest AND status:ccbReview` | 0 | CCB |
| K-CHG-04 | **Suspects** | Éléments avec liens suspects (liens marqués « à revoir » après modification de l'amont, doc. 09 § 5), par propriétaire et âge | `suspect:true` | Âge < 10 j | Tous |
| K-CHG-05 | Bruit de suspicion | % de suspects levés sans modification de l'élément aval | Historique ⚠ | Mesure (ADR-20) | DA ALM |
| K-CHG-06 | Modifications hors demande de modification | Éléments approuvés modifiés après baseline sans DM liée | Rapport d'audit (doc. 11 § 7) | 0 | Gest. configuration |
| K-NC-01 | FNC (fiches de non-conformité) ouvertes par gravité, origine, âge | `nonConformance` non soldées | `type:nonConformance AND NOT status:(closed cancelled)` | Âge médian < 60 j | Qualité |
| K-NC-02 | **FNC affectant un EIP** | `affectsEip = yes` ouvertes | `type:nonConformance AND affectsEip.KEY:yes AND NOT status:(closed cancelled)` | Suivi nominatif | Sûreté, Qualité, Direction |
| K-NC-03 | FNC non caractérisées dans le délai | `status:open` au-delà de l'échéance `dueDate` posée à la caractérisation (script `fra-sla.js`, 5 jours indicatifs ; arrêté INB art. 2.6.2 « examen sans délai ») | `type:nonConformance AND status:open AND dueDate:[19700101 TO $today$]` ⚠ | 0 | Qualité |
| K-NC-04 | Suspicions CFSI (articles contrefaits, frauduleux ou suspects) | `cfsiSuspected = yes` | `type:nonConformance AND cfsiSuspected.KEY:yes` | Suivi nominatif | Qualité, Direction |
| K-NC-05 | Pareto des causes (classement des causes par fréquence décroissante) | Par `rootCauseCategory` | Graphique | — | Qualité |
| K-NC-06 | Revue périodique des écarts (arrêté INB art. 2.7.1 [à vérifier ; coté P au doc. 04 § 2.2]) | Cumul par EIP, récurrence | Rapport | Trimestriel | Qualité |
| K-WV-01 | Dérogations actives et expirant dans les 30 jours | `waiver` approuvées avec `expiryDate` | `type:waiver AND status:approved` | — | Gest. configuration |

### 2.5 Fortuits (base installée)

Un *fortuit* est un aléa technique découvert pendant un arrêt de tranche, qui appelle une réponse rapide ; il est porté par le Work Item `technicalIssue`.

| ID | Indicateur | Définition | Seuil | Public |
|---|---|---|---|---|
| K-FOR-01 | Respect des SLA (délais de réponse engagés) | % de fortuits avec solution proposée avant `responseDueDate` (échéance posée au triage selon l'urgence, script `fra-sla.js`) | > 95 % | BI, client |
| K-FOR-02 | Fortuits sur chemin critique | `outageCriticalPath = true` ouverts | Suivi temps réel | CP arrêt |
| K-FOR-03 | Délai de traitement | Médiane triage → solution acceptée, par urgence | Tendance | BI |
| K-FOR-04 | Problèmes génériques | `genericImpact = yes` (palier, flotte) | Suivi | Sûreté, client |
| K-FOR-05 | REX capitalisé (retour d'expérience) | % de fortuits clos avec `lessonsLearnedCaptured = true` | 100 % | Qualité |

### 2.6 Interfaces, livrables, revues, risques

| ID | Indicateur | Définition | Seuil | Public |
|---|---|---|---|---|
| K-ITF-01 | Maturité des interfaces | % d'interfaces `frozen` (gelées) par partenaire | Selon le jalon | GI, CP |
| K-ITF-02 | Interfaces en retard de gel | `freezeDate` dépassée sans état `frozen` | 0 | GI |
| K-DLV-01 | Avancement des livrables | Planifiés vs diffusés vs définitifs (courbe) | Selon le plan | CP |
| K-DLV-02 | Taux de bon du premier coup | % de livrables VSO / VSO-SR (visa client « vu sans observation », éventuellement sous réserve) au premier indice diffusé | > 70 % | CP, Qualité |
| K-DLV-03 | Visas bloquants | Livrables VAOB / REF (observations bloquantes / refusé) ouverts | Suivi | CP |
| K-REV-01 | Remarques bloquantes non levées | `reviewFinding` avec `findingSeverity = blocking` hors états `accepted` / `closed` (condition de `wfReview.close`) | 0 au prononcé de la revue | RT |
| K-RSK-01 | Carte des risques | Matrice probabilité × impact, 10 premiers risques | — | CP, Direction |
| K-RSK-02 | Risques sans traitement | Criticité élevée sans `mitigates` | 0 | CP |

### 2.7 Adoption et santé de l'outil

| ID | Indicateur | Seuil | Public |
|---|---|---|---|
| K-ADO-01 | Utilisateurs actifs par BU / licence | Cible du plan de déploiement | DA ALM |
| K-ADO-02 | Projets conformes au profil de tailoring | 100 % | DA ALM |
| K-ADO-03 | Données interdites détectées (classification) | 0 | RSSI |
| K-OPS-01 | Temps de réponse (ouverture de document, requête) | < 3 s au 95e centile (95 % des mesures sous ce seuil) | DSI |
| K-OPS-02 | Volumétrie par projet / document (éléments) | Alerte au-delà des seuils de référence (Q-TOOL-04) | DSI |
| K-OPS-03 | Licences : taux d'utilisation et refus (concurrentes) | < 2 % de refus | DSI |

## 3. Tableaux de bord par rôle

| Tableau de bord | Indicateurs | Gabarit |
|---|---|---|
| **Direction / portefeuille BU** (niveau dépôt) | K-NC-02, K-NC-04, K-SAF-07, K-RSK-01, K-DLV-02, K-FOR-01, K-ADO-01 | Page globale |
| **Chef de projet** | K-REQ-01, K-DLV-01/03, K-CHG-01/03, K-RSK-01/02, K-VV-03, K-ITF-01 | Tous gabarits |
| **Responsable technique / exigences** | K-REQ-02 à 10, K-CHG-04, K-SAF-05 | Classes A / B / C |
| **Sûreté** | K-SAF-01 à 07, K-VV-02/06, K-NC-02 | Classes A / B |
| **Qualité** | K-NC-01 à 06, K-VV-07, K-CHG-06, K-FOR-05 | Tous |
| **V&V** | K-VV-01 à 08 | Classes A / B / C |
| **CCB / configuration** | K-CHG-01 à 06, K-WV-01 | Tous |
| **Fortuits (cellule d'arrêt)** | K-FOR-01 à 05 | TPL-IB-FORTUIT |
| **Interfaces** | K-ITF-01/02, K-REQ-10 | Classes A / B |
| **Design Authority ALM** | K-CHG-05, K-ADO-01/02/03, K-OPS-01 à 03 | Page d'administration |
| **UO réalisatrice** (v0.3, niveau dépôt) | Lots par état, avancement (`progressPercent`), livrables en retard, FNC et points d'arrêt à venir, filtrés par `performingUnit` | Page globale (doc. 21 § 1.4) |
| **Déploiement par tranche** (v0.3) | `unitDeployment` par état, par tranche et par arrêt ; écarts constatés au déploiement | TPL-02-IB |

## 4. Contrôle qualité des exigences : termes à proscrire

| Langue | Termes signalés (liste initiale, à enrichir) |
|---|---|
| FR | adéquat, approprié, suffisant, si possible, si nécessaire, le cas échéant, minimiser, maximiser, optimiser, rapide, facile, convivial, robuste, environ, notamment, etc., et/ou, au moins (sans valeur), pas limité à, tout, toujours, jamais, compatible (sans référence), TBD, TBC, à définir |
| EN | adequate, appropriate, sufficient, as possible, if necessary, as applicable, minimize, maximize, optimize, fast, easy, user-friendly, robust, about, approximately, including, etc., and/or, at least (no value), not limited to, all, always, never, TBD, TBC |

Contrôles complémentaires (script de rendu ou script planifié) :
- plusieurs verbes prescriptifs (« doit » / *shall*) dans un même énoncé ;
- nombres sans unité ;
- absence de critère d'acceptation ;
- longueur supérieure à 400 caractères ;
- forme passive sans sujet.

## 5. Requêtes SQL de couverture (gabarits ⚠ à valider)

Polarion expose sa base PostgreSQL en lecture pour les requêtes que Lucene ne sait pas exprimer (ici : l'absence de lien d'un rôle donné). Les noms de tables et de colonnes `POLARION.*` ci-dessous sont ceux observés dans des exemples publiés ; ils sont **[à vérifier, spike S1 / Q-TOOL-04]** sur la version cible.

Exigences d'un projet **sans cas de vérification** (lien `verifies` entrant) :

```
SQL:(SELECT item.* FROM POLARION.WORKITEM item
 INNER JOIN POLARION.PROJECT p ON item.FK_URI_PROJECT = p.C_URI
 WHERE p.C_ID = 'P-EPR2-NSSS'
   AND item.C_TYPE IN ('systemRequirement','equipmentRequirement','safetyRequirement')
   AND item.C_STATUS = 'approved'
   AND NOT EXISTS (
     SELECT 1 FROM POLARION.STRUCT_WORKITEM_LINKEDWORKITEMS l
     WHERE l.FK_URI_WORKITEM = item.C_URI AND l.C_ROLE IN ('verifies','validates')))
```

Le même gabarit sert pour :
- les agressions non maîtrisées (`C_TYPE = 'hazard'`, rôle `mitigates`) ;
- les exigences de sûreté non satisfaites (`satisfies`) ;
- les fonctions catégorisées non réalisées (`realizes`) ;
- les orphelins (aucun rôle hors `relates_to`, ni en entrée ni en sortie ; TR-17).

## 6. Exemple de widget LiveReport (Velocity, API de rendu)

Velocity est le langage de gabarit (*template*) utilisé par les pages de rapport Polarion : il mélange du texte et des appels à l'API Java de l'outil.

Indicateur K-VV-02 (exigences définies restant à vérifier), par discipline :

```velocity
#set($q = "project.id:$projectId AND definedRequirement.KEY:yes AND NOT status:(obsolete rejected)")
#set($items = $transaction.workItems().search().query($q).sort("id"))
#set($byDisc = {})
#foreach($wi in $items)
  #set($d = $wi.fields().get("discipline").render().htmlFor().forFrame())  ## ⚠ API à valider
  #set($st = $wi.fields().get("verificationStatus").render().htmlFor().forFrame())
  ## agrégation par discipline et statut (passed / autres)
#end
## rendu tableau HTML + jauge de couverture
```

> Le code ci-dessus montre le principe (variables `$transaction`, `$projectId`, recherche Lucene). Les accesseurs exacts des champs personnalisés sont à valider sur le SDK (kit de développement) de la version cible [à vérifier, spike S1]. Pour les volumétries importantes, un **script planifié** (exécution nocturne côté serveur [à vérifier, Q-TOOL-01 : annoncé 2506+]) pré-calcule les indicateurs dans un élément « tableau de bord » ou dans un export vers l'entrepôt de données.

## 7. Export vers l'informatique décisionnelle

- Extraction nocturne (API REST de Polarion, version v1 [à vérifier, Q-TOOL-01], jeton de service en lecture seule) vers l'entrepôt de données de l'entreprise : Work Items (champs indexés), liens, Test Records, historique des statuts.
- Usages : consolidation multi-instances (hors SENS) ; indicateurs de portefeuille croisés avec l'ERP (progiciel de gestion : commandes, WBS) et le planning ; tendances longues.
- La classification et le contrôle export sont **propagés** dans l'entrepôt de données (filtrage par habilitation).
