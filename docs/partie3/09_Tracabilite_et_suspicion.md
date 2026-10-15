# Partie 3.3 — Modèle de liens, traçabilité et propagation de la suspicion

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **faible** (§ 5.1–5.2 spécifiques à Polarion) · Historique : [CHANGELOG](../../CHANGELOG.md) · Carte du dépôt : [guide de lecture](../GUIDE_DE_LECTURE.md).*
>
> **En bref**
> - Ce document fixe le modèle de liens entre Work Items : convention de sens (aval → amont), les 26 rôles de liens, les règles d'autorisation type × type, les règles de complétude TR-01..TR-20, la politique de **suspicion** (un lien devient « suspect » quand l'élément amont change et doit être revu), l'analyse d'impact et les indicateurs de couverture.
> - Lecteurs : SE Referents, responsables exigences, V&V, Sûreté ; ingénieurs configuration (§ 3 et § 5).
> - À lire avant : doc. 08 (modèle de données). Catalogue exhaustif des rôles, règles d'autorisation et matrice type × type : [Annexe A3](../generated/A3_liens_et_tracabilite.md). Source : `model/link_roles.yaml`.

## 1. Convention fondamentale : aval → amont

Un lien est **toujours créé depuis l'artefact aval (source) vers l'artefact amont (cible)**. L'amont est ce qui vient en premier dans le cycle en V (besoin, exigence de niveau supérieur, hypothèse, preuve) ; l'aval en dépend (exigence déclinée, élément de conception, cas de vérification, revendication étayée, livrable).

**Pourquoi.** En natif, Polarion marque **suspects les liens entrants des éléments aval** lorsqu'on enregistre l'élément amont (cible) [C, aide Polarion]. La convention garantit que :
- toute évolution d'une exigence amont interpelle le propriétaire de l'exigence déclinée, du cas de vérification ou de l'élément de conception aval ;
- toute évolution d'une hypothèse interpelle les éléments qui s'y appuient ;
- toute évolution d'une preuve interpelle la revendication de sûreté qu'elle étaye (rôle `supportedBy`, orienté revendication → preuve) ;
- toute évolution d'un artefact interpelle le rédacteur du livrable qui le documente (rôle `documents`, orienté livrable → artefact).

## 2. Les rôles de liens (26 ; catalogue complet en annexe A3)

Les quatre rôles SysML cités (*deriveReqt*, *refine*, *satisfy*, *verify*) sont les relations normalisées du langage de modélisation SysML entre exigences et éléments de conception ; ils servent de référence sémantique pour les échanges MBSE (Capella) et ReqIF.

| Famille | Rôle (id) | Sens direct / inverse | Usage | Suspicion |
|---|---|---|---|---|
| Structure | `parent` (natif) | a pour parent / a pour enfant | Arborescences FBS, PBS (fonctionnelle, produit), actions, structure des LiveDocs (titres) | Non (natif : pas de suspicion sur les liens parent) |
| Exigences | `flowsDownFrom` | découle de / se décline en | Déclinaison d'exigences (SysML *deriveReqt*) ; volontairement distinct du rôle système `derived_from` | Oui |
| | `refines` | précise / est précisée par | Scénario ou paramètre qui détaille une exigence (SysML *refine*) | Oui |
| Conception | `satisfies` | satisfait / est satisfaite par | Élément de conception → exigence (SysML *satisfy* ; le sens inverse donne la matrice d'allocation) | Oui |
| | `realizes` | réalise / est réalisé par | L → F, P → L / F | Oui |
| | `allocatedTo` | est alloué à / porte | Paramètre ou budget → élément | Oui |
| | `sideA`, `sideB` | a pour côté A / B | Extrémités d'interface (registre ICD) | Oui |
| V&V | `verifies` | vérifie / est vérifiée par | Cas → exigence ou élément (SysML *verify* ; rôle déclaré dans la configuration *Testing* de Polarion pour la couverture) | Oui |
| | `validates` | valide / est validée par | Cas de validation → besoin ou scénario | Oui |
| Sûreté | `mitigates` | maîtrise / est maîtrisé par | Exigence, disposition, action → agression, risque, mode de défaillance | Oui |
| | `causes` | cause / est causé par | Chaînes causales (AMDEC, agressions induites) | Non |
| | `supportedBy` | est étayée par / étaye | Revendication (argumentaire CAE / GSN) → sous-revendication ou preuve | Oui |
| | `assumes` | s'appuie sur l'hypothèse | Tout artefact → hypothèse | Oui |
| Modifications | `impacts` | impacte / est impacté par | Demande de modification (DM), fiche de non-conformité (FNC), dérogation, fortuit, anomalie, remarque de revue, demande d'autorité → artefacts d'ingénierie | Non |
| | `resolves` | résout / est résolu par | Clôture des écarts, anomalies, remarques et demandes | Non |
| Documents | `documents` | documente / est documenté dans | Livrable → artefacts décrits ou justifiés | Oui |
| Ordonnancement | `dependsOn` | dépend de / est un prérequis de | Enchaînement de livrables, cas, actions, lots (inter-projets autorisé) | Oui |
| Historique | `supersedes` | remplace / est remplacé par | Nouvelle édition, exigence reformulée | Non |
| Revues | `raisedIn` | est émise lors de | Remarque → revue ou livrable relu | Non |
| REX | `capitalizes` | capitalise / est capitalisé dans | Fiche REX (`lessonLearned`) → événement dont elle tire les enseignements (fortuit, écart, anomalie, revue, modification, risque survenu, dérogation, demande d'autorité, déploiement par tranche) | Non |
| Qualité | `duplicates` | duplique | Doublons de fiches | Non |
| Lots | `inWorkPackage` | relève du lot / comprend | Artefact produit (livrable, analyse, cas, action, déploiement, décision, composant, DM, FNC, fortuit, revue) → lot de travaux `workPackage` (doc. 21) ; inter-projets autorisé | Non (le lot n'est pas une donnée d'entrée technique) |
| Réutilisation | `branched_from` (système) | est une branche de | Branchement de documents (bibliothèques, références) | Oui |
| | `derived_from` (système) | est réutilisé de | Document dérivé (réutilisation en lecture seule) | Oui |
| Informatif | `relates_to` (natif) | est en relation avec | Relation non qualifiée, **jamais comptée en couverture** (TR-17) | Non |

## 3. Règles d'autorisation

- Les règles sont générées comme éléments `<rule from="…" to="…"/>` dans `workitem-link-role-enum.xml` (format à confirmer sur la version cible, annexe D).
- Les rôles susceptibles de traverser les projets (bibliothèques, lignes de produits, interfaces inter-BU, lots) acceptent la cible `__other` (élément d'un autre projet).
- Les règles **ne s'appliquent pas rétroactivement** aux liens existants. Un rapport de conformité des liens est donc nécessaire après chaque évolution des règles.

Exemples de règles clés (liste complète en annexe A3) :

| Rôle | Source → Cibles autorisées |
|---|---|
| `flowsDownFrom` | `systemRequirement` → `sourceRequirement`, `regulatoryRequirement`, `stakeholderRequirement`, `safetyRequirement`, `systemRequirement`, `analysis` (+ autre projet) |
| `flowsDownFrom` | `softwareRequirement` → `sourceRequirement`, `stakeholderRequirement`, `systemRequirement`, `safetyRequirement`, `equipmentRequirement`, `softwareRequirement`, `regulatoryRequirement` |
| `satisfies` | `function`, `logicalComponent`, `physicalComponent`, `interface`, `designParameter`, `designDecision`, `analysis`, `deliverable` → toute exigence |
| `verifies` | `verificationCase` → toute exigence + `function`, `logicalComponent`, `physicalComponent`, `interface`, `designParameter`, `assumption`, `unitDeployment` |
| `mitigates` | exigences rédigées, fonctions, composants, décisions, actions, cas → `hazard`, `risk`, `fmeaItem` |
| `impacts` | demande de modification, FNC, dérogation, fortuit, anomalie, remarque, demande d'autorité → tout artefact d'ingénierie |

## 4. Règles de complétude (contrôles)

Chaque règle TR (*traceability rule*) est portée par `model/link_roles.yaml` et contrôlée soit par une condition de workflow (bloquante), soit par un rapport (LiveReport, doc. 13).

| Règle | Contenu | Sévérité | Mise en œuvre |
|---|---|---|---|
| TR-01 | Exigence aval approuvée : découle d'une exigence amont, ou justification d'origine interne | warn | Rapport |
| TR-02 | Exigence d'entrée acceptée : statut de conformité évalué **et** couverture | block | Condition `establishPosition` + rapport |
| **TR-03** | **Exigence définie : vérifiée par au moins un cas approuvé** | **block** | Rapport bloquant à la revue ; condition de clôture de V&V |
| TR-04 | Exigence approuvée : méthode de vérification + au moins un cas | warn | Condition (méthodes) + rapport (cas) |
| TR-05 | Exigence de sûreté : satisfaite par au moins un élément ou une analyse | block | Rapport (revue) |
| TR-06 | Fonction catégorisée : réalisée par au moins un élément | warn | Rapport |
| TR-07 | SSC EIP (structure, système ou composant important pour la protection) : classement validé par la Sûreté et satisfaction d'au moins une exigence | block | Condition `approve` (`classificationValidated`) + rapport |
| TR-08 | Interface : exactement un côté A et un côté B | block | Condition `define` |
| TR-09 | Agression retenue : maîtrisée | block | Rapport (revue de sûreté) |
| TR-10 | Cas de vérification : vérifie ou valide au moins un élément | block | Condition `submit` |
| TR-11 | FNC / dérogation affectant un EIP : impacts identifiés | block | Condition `propose` |
| TR-12 | Demande de modification de classe I : impacts identifiés avant CCB (comité de maîtrise des modifications) | block | Condition `toCcb` |
| TR-13 | Revendication : étayée | warn | Rapport |
| TR-14 | Aucun suspect à l'approbation d'un LiveDoc ou à la clôture d'une demande de modification | block | `ContainsNoMatchingWorkItems(suspect:true)` / script `fra-no-suspect.js` |
| TR-15 | Demande d'autorité : résolue par au moins un livrable, une analyse ou une action avant réponse | block | Condition `submitResponse` |
| TR-16 | Hypothèse confirmée : preuve | warn | Rapport |
| TR-17 | `relates_to` exclu de la couverture | info | Construction des rapports |
| TR-18 | Livrable rattaché à un lot de travaux (projets à lots) | warn | Rapport (doc. 21) |
| TR-19 | Criblage 10 CFR 50.59 (règle de la NRC américaine sur les modifications sans autorisation préalable) renseigné avant CCB (pack US) | block | Condition de workflow |
| TR-20 | Article commercial dédicacé (CGD : article du commerce qualifié pour un usage de sûreté) vérifié sur ses caractéristiques critiques | block | Rapport + revue de dossier |

## 5. Suspicion : comportement natif et politique cible

### 5.1 Comportement natif de Polarion [C, à confirmer sur la version cible : Q-TOOL-02, spike S1]

- Le drapeau « suspect » est un attribut **du lien**, stocké côté source (élément aval). Le champ indexé `suspect` de l'élément vaut `true` s'il possède au moins un lien sortant suspect (requête `suspect:true`).
- Déclenchement : option **Auto-Suspect** (globale, projet ou document) **à tout enregistrement** de l'élément cible ; aucun filtrage natif par champ ni par rôle.
- Exceptions : liens parent et liens structurels internes aux documents.
- Le mécanisme agit au niveau de l'interface utilisateur ; son comportement lors des imports et appels d'API est à vérifier (Q-TOOL-02).
- Levée : décocher « suspect » sur le lien, depuis l'élément aval.
- **Ni propagation transitive, ni condition de workflow native** « aucun suspect » (pour les Work Items). Pour les documents, `ContainsNoMatchingWorkItems(query="suspect:true")` est natif.

### 5.2 Politique cible (deux phases, ADR-20)

| Phase | Mécanisme | Avantage | Limite |
|---|---|---|---|
| 1 (pilotes) | Auto-Suspect natif activé au niveau projet ; condition bloquante `noSuspectLinks` (script `fra-no-suspect.js`) aux approbations et clôtures ; tableau de bord « suspects par propriétaire » | Natif, robuste, sans développement | Bruit : toute modification, même cosmétique, déclenche la suspicion |
| 2 (industrialisation) | Hook de sauvegarde (code exécuté à chaque enregistrement : Polarion Scripting 2410+ ou extension d'interception [à vérifier, Q-TOOL-02 / spike S1]) : ne pose la suspicion que si un champ listé dans `suspectTriggerFields` a changé (titre, description, critères d'acceptation, méthodes, classement, applicabilité, valeurs limites...) | Signal pertinent | Développement à qualifier ; dépend du comportement API |

### 5.3 Champs déclencheurs (politique cible)

| Famille amont | Champs |
|---|---|
| Exigences | titre, description, critères d'acceptation, méthodes de vérification, force, exigence définie, classe, applicabilité (paliers, tranches), états, conditions, texte original |
| Architecture | titre, description, classe, EIP, catégorie, classes mécanique / électrique / qualification / sismique, ESPN, données d'interface, applicabilité |
| Paramètres | valeurs (nominale, min, max, limite), unité |
| Agressions | fréquence, criblage, critères |
| Preuves (analyse, cas, livrable) | conclusion, résultat, indice, critères |

### 5.4 Propagation transitive : analyse d'impact

La suspicion native est **à un niveau**. Pour une demande de modification, l'analyse d'impact doit couvrir **N niveaux**. Algorithme du rapport « cône d'impact » (ensemble des éléments atteints de proche en proche depuis les éléments modifiés ; LiveReport, script de rendu) :

```
entrée : ensemble E0 = éléments liés à la DM par 'impacts'
rôles_aval = {flowsDownFrom, refines, satisfies, realizes, allocatedTo, verifies,
              validates, mitigates, assumes, sideA, sideB, documents, dependsOn,
              branched_from, derived_from, supportedBy(inverse)}
niveau = 0 ; visités = E0
tant que niveau < N et frontière non vide :
    frontière_suivante = { x | x a un lien d'un rôle de rôles_aval vers un élément de la frontière }
                         ∪ { revendications c | c supportedBy élément de la frontière }
    frontière_suivante -= visités
    visités ∪= frontière_suivante ; niveau += 1
sortie : tableau (élément, type, niveau, chemin, propriétaire, statut, EIP, classe)
```

- Le résultat est attaché à la demande de modification (champ `impactAnalysis` + liens `impacts` complétés par le demandeur) et présenté en CCB.
- Contrôle à la clôture (TR-14) : aucun suspect sur le périmètre impacté (`noSuspectLinks`, portée `impactedItems`).

### 5.5 Procédure de levée d'un suspect (règle utilisateur)

1. Le propriétaire de l'élément aval ouvre l'élément, consulte la différence de l'élément amont (historique, comparaison de révisions).
2. Il décide :
   - (a) **sans impact** : il lève le suspect et laisse un commentaire de justification ;
   - (b) **impact** : il met à jour l'élément aval, en le rouvrant si nécessaire sous demande de modification, puis lève le suspect.
3. Indicateurs :
   - âge des suspects ;
   - nombre par propriétaire ;
   - taux de levée sans modification (mesure du bruit, ADR-20).

## 6. Couverture : définitions normalisées des indicateurs

| Indicateur | Définition | Rôles comptés |
|---|---|---|
| Couverture de déclinaison | % d'exigences amont approuvées ayant au moins une exigence aval (`flowsDownFrom` entrant) ou une satisfaction directe | `flowsDownFrom`, `satisfies` |
| Couverture d'allocation | % d'exigences satisfaites par au moins un élément d'architecture | `satisfies` |
| Couverture de vérification (planifiée) | % d'exigences ayant au moins un cas approuvé | `verifies`, `validates` |
| Couverture de vérification (réalisée) | % d'exigences dont `verificationStatus ∈ {passed, passedWithReserves}` | idem, via les Test Runs (campagnes d'essais) |
| Couverture des exigences définies | Idem, restreint à `definedRequirement = yes` (objectif : 100 % à la clôture) | idem |
| Couverture de maîtrise des agressions | % d'agressions retenues maîtrisées | `mitigates` |
| Couverture de l'argumentaire | % de revendications étayées | `supportedBy` |
| Orphelins | Éléments sans aucun lien qualifié (hors `relates_to`) | tous sauf `relates_to` |

Requêtes types (Lucene, le langage de requête de Polarion, et SQL) : voir le doc. 13.
