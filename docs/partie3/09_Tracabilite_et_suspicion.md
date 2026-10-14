# Partie 3.3 — Modèle de liens, traçabilité et propagation de la suspicion

> Catalogue exhaustif des rôles, règles d'autorisation et matrice type × type : [Annexe A3](../generated/A3_liens_et_tracabilite.md).

## 1. Convention fondamentale : aval → amont

Un lien est **toujours créé depuis l'artefact aval (source) vers l'artefact amont (cible)**.

**Pourquoi.** En natif, Polarion marque **suspects les liens entrants des éléments aval** lorsqu'on enregistre l'élément amont (cible) [C, aide Polarion]. La convention garantit que :
- toute évolution d'une exigence amont interpelle le propriétaire de l'exigence déclinée, du cas de vérification ou de l'élément de conception aval ;
- toute évolution d'une hypothèse interpelle les éléments qui s'y appuient ;
- toute évolution d'une preuve interpelle la revendication de sûreté qu'elle étaye (rôle `supportedBy`, orienté revendication → preuve) ;
- toute évolution d'un artefact interpelle le rédacteur du livrable qui le documente (rôle `documents`, orienté livrable → artefact).

## 2. Les 24 rôles de liens

| Famille | Rôle (id) | Sens direct / inverse | Usage | Suspicion |
|---|---|---|---|---|
| Structure | `parent` (natif) | a pour parent / a pour enfant | Arborescences FBS, PBS, actions, structure des LiveDocs (titres) | Non (natif : pas de suspicion sur les liens parent) |
| Exigences | `flowsDownFrom` | découle de / se décline en | Déclinaison d'exigences (SysML *deriveReqt*) ; volontairement distinct du rôle système `derived_from` | Oui |
| | `refines` | précise / est précisée par | Scénario ou paramètre qui détaille une exigence | Oui |
| Conception | `satisfies` | satisfait / est satisfaite par | Élément de conception → exigence (le sens inverse donne la matrice d'allocation) | Oui |
| | `realizes` | réalise / est réalisé par | L → F, P → L / F | Oui |
| | `allocatedTo` | est alloué à / porte | Paramètre ou budget → élément | Oui |
| | `sideA`, `sideB` | a pour côté A / B | Extrémités d'interface | Oui |
| V&V | `verifies` | vérifie / est vérifiée par | Cas → exigence ou élément (rôle déclaré dans la configuration *Testing*) | Oui |
| | `validates` | valide / est validée par | Cas de validation → besoin ou scénario | Oui |
| Sûreté | `mitigates` | maîtrise / est maîtrisé par | Exigence, disposition, action → agression, risque, mode de défaillance | Oui |
| | `causes` | cause / est causé par | Chaînes causales (AMDEC, agressions induites) | Non |
| | `supportedBy` | est étayée par / étaye | Revendication → sous-revendication ou preuve | Oui |
| | `assumes` | s'appuie sur l'hypothèse | Tout artefact → hypothèse | Oui |
| Modifications | `impacts` | impacte / est impacté par | Demande de modification, FNC, dérogation, fortuit, anomalie, demande d'autorité → artefacts | Non |
| | `resolves` | résout / est résolu par | Clôture des écarts, remarques et demandes | Non |
| Documents | `documents` | documente / est documenté dans | Livrable → artefacts décrits ou justifiés | Oui |
| Ordonnancement | `dependsOn` | dépend de / est un prérequis de | Enchaînement de livrables, cas, actions | Oui |
| Historique | `supersedes` | remplace / est remplacé par | Nouvelle édition, exigence reformulée | Non |
| Revues | `raisedIn` | est émise lors de | Remarque → revue ou livrable relu | Non |
| Qualité | `duplicates` | duplique | Doublons de fiches | Non |
| Réutilisation | `branched_from` (système) | est une branche de | Branchement de documents (bibliothèques, références) | Oui |
| | `derived_from` (système) | est réutilisé de | Document dérivé (réutilisation en lecture seule) | Oui |
| Informatif | `relates_to` (natif) | est en relation avec | Relation non qualifiée, **jamais comptée en couverture** (TR-17) | Non |

## 3. Règles d'autorisation

- Les règles sont générées comme éléments `<rule from="…" to="…"/>` dans `workitem-link-role-enum.xml`.
- Les rôles susceptibles de traverser les projets (bibliothèques, lignes de produits, interfaces inter-BU) acceptent la cible `__other` (élément d'un autre projet).
- Les règles **ne s'appliquent pas rétroactivement** aux liens existants. Un rapport de conformité des liens est donc nécessaire après chaque évolution des règles.

Exemples de règles clés :

| Rôle | Source → Cibles autorisées |
|---|---|
| `flowsDownFrom` | `systemRequirement` → `sourceRequirement`, `regulatoryRequirement`, `stakeholderRequirement`, `safetyRequirement`, `systemRequirement`, `analysis` (+ autre projet) |
| `flowsDownFrom` | `softwareRequirement` → `systemRequirement`, `safetyRequirement`, `equipmentRequirement`, `softwareRequirement`, `regulatoryRequirement` |
| `satisfies` | `function`, `logicalComponent`, `physicalComponent`, `interface`, `designParameter`, `designDecision`, `analysis`, `deliverable` → toute exigence |
| `verifies` | `verificationCase` → toute exigence + `function`, `logicalComponent`, `physicalComponent`, `interface`, `designParameter`, `assumption` |
| `mitigates` | exigences rédigées, fonctions, composants, décisions, actions, cas → `hazard`, `risk`, `fmeaItem` |
| `impacts` | demande de modification, FNC, dérogation, fortuit, anomalie, remarque, demande d'autorité → tout artefact d'ingénierie |

## 4. Règles de complétude (contrôles)

| Règle | Contenu | Sévérité | Mise en œuvre |
|---|---|---|---|
| TR-01 | Exigence aval approuvée : découle d'une exigence amont, ou justification d'origine interne | warn | Rapport |
| TR-02 | Exigence d'entrée acceptée : statut de conformité évalué **et** couverture | block | Condition `establishPosition` + rapport |
| **TR-03** | **Exigence définie : vérifiée par au moins un cas approuvé** | **block** | Rapport bloquant à la revue ; condition de clôture de V&V |
| TR-04 | Exigence approuvée : méthode de vérification + au moins un cas | warn | Condition (méthodes) + rapport (cas) |
| TR-05 | Exigence de sûreté : satisfaite par au moins un élément ou une analyse | block | Rapport (revue) |
| TR-06 | Fonction catégorisée : réalisée par au moins un élément | warn | Rapport |
| TR-07 | SSC EIP : classement validé par la Sûreté et satisfaction d'au moins une exigence | block | Condition `approve` (`classificationValidated`) + rapport |
| TR-08 | Interface : exactement un côté A et un côté B | block | Condition `define` |
| TR-09 | Agression retenue : maîtrisée | block | Rapport (revue de sûreté) |
| TR-10 | Cas de vérification : vérifie ou valide au moins un élément | block | Condition `submit` |
| TR-11 | FNC / dérogation affectant un EIP : impacts identifiés | block | Condition `propose` |
| TR-12 | Demande de modification de classe I : impacts identifiés avant CCB | block | Condition `toCcb` |
| TR-13 | Revendication : étayée | warn | Rapport |
| TR-14 | Aucun suspect à l'approbation d'un LiveDoc ou à la clôture d'une demande de modification | block | `ContainsNoMatchingWorkItems(suspect:true)` / script |
| TR-15 | Demande d'autorité : résolue par au moins un livrable, une analyse ou une action avant réponse | block | Condition `submitResponse` |
| TR-16 | Hypothèse confirmée : preuve | warn | Rapport |
| TR-17 | `relates_to` exclu de la couverture | info | Construction des rapports |

## 5. Suspicion : comportement natif et politique cible

### 5.1 Comportement natif de Polarion [C]

- Le drapeau « suspect » est un attribut **du lien**, stocké côté source (élément aval). Le champ indexé `suspect` de l'élément vaut `true` s'il possède au moins un lien sortant suspect (requête `suspect:true`).
- Déclenchement : option **Auto-Suspect** (globale, projet ou document) **à tout enregistrement** de l'élément cible ; aucun filtrage natif par champ ni par rôle.
- Exceptions : liens parent et liens structurels internes aux documents.
- Le mécanisme agit au niveau de l'interface utilisateur ; son comportement lors des imports et appels d'API est à vérifier (Q-TOOL-02).
- Levée : décocher « suspect » sur le lien, depuis l'élément aval.
- **Ni propagation transitive, ni condition de workflow native** « aucun suspect » (pour les Work Items). Pour les documents, `ContainsNoMatchingWorkItems(query="suspect:true")` est natif.

### 5.2 Politique cible (deux phases, ADR-20)

| Phase | Mécanisme | Avantage | Limite |
|---|---|---|---|
| 1 (pilotes) | Auto-Suspect natif activé au niveau projet ; condition bloquante `noSuspectLinks` (script) aux approbations et clôtures ; tableau de bord « suspects par propriétaire » | Natif, robuste, sans développement | Bruit : toute modification, même cosmétique, déclenche la suspicion |
| 2 (industrialisation) | Hook de sauvegarde (Polarion Scripting 2410+ ou extension d'interception) : ne pose la suspicion que si un champ listé dans `suspectTriggerFields` a changé (titre, description, critères d'acceptation, méthodes, classement, applicabilité, valeurs limites...) | Signal pertinent | Développement à qualifier ; dépend du comportement API |

### 5.3 Champs déclencheurs (politique cible)

| Famille amont | Champs |
|---|---|
| Exigences | titre, description, critères d'acceptation, méthodes de vérification, force, exigence définie, classe, applicabilité (paliers, tranches), états, conditions, texte original |
| Architecture | titre, description, classe, EIP, catégorie, classes mécanique / électrique / qualification / sismique, ESPN, données d'interface, applicabilité |
| Paramètres | valeurs (nominale, min, max, limite), unité |
| Agressions | fréquence, criblage, critères |
| Preuves (analyse, cas, livrable) | conclusion, résultat, indice, critères |

### 5.4 Propagation transitive : analyse d'impact

La suspicion native est **à un niveau**. Pour une demande de modification, l'analyse d'impact doit couvrir **N niveaux**. Algorithme du rapport « cône d'impact » (LiveReport, script de rendu) :

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
- Contrôle à la clôture (TR-14) : aucun suspect sur le périmètre impacté.

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
| Couverture de vérification (réalisée) | % d'exigences dont `verificationStatus ∈ {passed, passedWithReserves}` | idem, via les Test Runs |
| Couverture des exigences définies | Idem, restreint à `definedRequirement = yes` (objectif : 100 % à la clôture) | idem |
| Couverture de maîtrise des agressions | % d'agressions retenues maîtrisées | `mitigates` |
| Couverture de l'argumentaire | % de revendications étayées | `supportedBy` |
| Orphelins | Éléments sans aucun lien qualifié (hors `relates_to`) | tous sauf `relates_to` |

Requêtes types (Lucene / SQL) : voir le document 13.
