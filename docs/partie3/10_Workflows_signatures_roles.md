# Partie 3.4 — Workflows, signatures électroniques, rôles et permissions

> *Version du plan : 0.5 (octobre 2026) · Dépendance à l'outil Polarion : **moyenne** (§ 3, § 4 et § 6.3 spécifiques à Polarion) · Historique : [CHANGELOG](../../CHANGELOG.md) · Carte du dépôt : [guide de lecture](../GUIDE_DE_LECTURE.md).*
>
> **En bref**
> - Ce document décrit les cycles de vie (workflows : états et transitions) des Work Items et des LiveDocs, la façon dont le **contrôle technique** et les **signatures électroniques** y sont portés, les scripts de workflow à développer, puis les rôles et les règles de permission.
> - Lecteurs : SE Referents, Qualité, Sûreté (§ 1, 2, 5) ; ingénieurs configuration et intégrateur (§ 3, 4, 6).
> - À lire avant : doc. 08 (modèle) et doc. 09 (liens). À lire ensuite : doc. 12 (LiveDocs), doc. 21 § 3 (signatures habilitées), doc. 23 § 3 (priorités des scripts).
> - Diagrammes d'états et tableaux de transitions exhaustifs : [Annexe A4](../generated/A4_workflows.md). Rôles et matrice des droits : [Annexe A6](../generated/A6_roles_permissions.md). Source : `model/workflows.yaml`, `model/roles.yaml`. Fichiers générés : `generated/polarion/<lang>/.polarion/tracker/workflow/*.xml` et `documents/workflow/*.xml` ; manifeste `generated/polarion/<lang>/SIGNATURES_ET_SCRIPTS.md`.

## 1. Principes de conception des workflows

| # | Principe |
|---|---|
| WF1 | **Bloquer ce qui relève du socle non négociable** (contrôle technique indépendant, EIP / exigences définies, suspects, classification), **signaler le reste** par des rapports, pour ne pas paralyser l'usage |
| WF2 | Pas de suppression : la sortie d'un élément se fait par un état terminal (`obsolete`, `rejected`, `cancelled`, `superseded`) avec un motif (`transitionNote`) |
| WF3 | Toute modification d'un élément approuvé passe par une **réouverture tracée**, sous demande de modification après la première baseline (référence de configuration figée) |
| WF4 | **Indépendance** (contrôle technique) : l'exécutant d'une transition d'approbation n'est ni l'auteur ni le dernier rédacteur (condition `approverNotAuthor`, tracée par les *Approvals*, approbations nominatives natives de Polarion) |
| WF5 | La signature électronique matérialise une décision engageante (analyse, livrable, document, décision CCB, dérogation, accord de lot, levée) ; elle porte une **signification** (rédigé, vérifié, approuvé, avis sûreté, visa qualité, décision CCB, accepté, accord de lot). Pour les exigences, éléments d'architecture, cas de vérification et éléments d'analyse de sûreté, la signature est **portée par le LiveDoc** qui les contient (§ 2.1 et § 5.4) |
| WF6 | Les signatures conditionnelles n'étant pas natives, la signature est **systématique** sur les transitions concernées (choix conservateur). Alternative : dédoubler l'action (« approuver » / « approuver avec signature ») avec des conditions exclusives |
| WF7 | Les workflows sont **partagés par famille** (24 workflows de Work Items pour 36 types, + 3 workflows documentaires) pour limiter la charge de formation |
| WF8 | Chaque workflow déclare un **état de soumission** (`submitState`) ; les champs « requis à la soumission » du type sont exigés par le générateur sur toutes les transitions qui y mènent (doc. 08 § 1) |

## 2. Catalogue des workflows

États principaux abrégés (états terminaux entre parenthèses) ; la colonne Signatures indique les significations réellement générées (bloc `<signatures>`), d'après le manifeste `SIGNATURES_ET_SCRIPTS.md`.

| Workflow | Types | États principaux | Signatures |
|---|---|---|---|
| `wfRequirement` | 6 types d'exigences rédigées | Brouillon → En vérification → Approuvée ⇄ En révision (Obsolète, Rejetée) | — (contrôle technique tracé par Approvals + `approverNotAuthor` ; signature portée par le LiveDoc, cascade `approve`) |
| `wfInputRequirement` | Exigence d'entrée | Importée → En analyse ⇄ Clarification → Position établie (Remplacée) | — (position signée au niveau de la matrice de conformité, LiveDoc) |
| `wfLibraryItem` | Exigence réglementaire, terme | Brouillon → Validé → Publié (Remplacé, Retiré) ; transitions `submit` / `approve` | — (portée par le document de bibliothèque, `wfDocumentLibrary.publish`) |
| `wfAssumption` | Hypothèse | À confirmer → Confirmée / Infirmée (Retirée) | Vérifié à la confirmation (intention : si pertinente pour la sûreté ; rendue systématique, WF6) |
| `wfArchitecture` | Scénario, fonction, éléments L / P, paramètre | Brouillon → En vérification → Approuvé ⇄ En révision (Obsolète) | — (Approvals + `approverNotAuthor` ; signature portée par le LiveDoc) |
| `wfInterface` | Interface | Identifiée → Définie → Accordée (A + B) → Gelée ⇄ En révision (Obsolète) | Approuvé (accord, 2 approbations minimum) |
| `wfDecision` | Décision de conception | Proposée → En évaluation → Décidée (Remplacée, Rejetée) | Approuvé (décision) |
| `wfSafetyAnalysisItem` | Agression, revendication, AMDEC | Brouillon → En vérification → Approuvé ⇄ En révision (Obsolète) | — (avis Sûreté demandé à la soumission, approbation par `safetyLead` / `verifier` ; signature portée par le LiveDoc : dossier de sûreté, AMDEC) |
| `wfAnalysis` | Analyse / note de calcul | Planifiée → En cours → En contrôle technique → Approuvée (Remplacée, Annulée) | Rédigé (soumission) + Vérifié (approbation) |
| `wfRisk` | Risque | Identifié → Évalué → En traitement → Sous surveillance → Clos / Survenu | — |
| `wfCommitment` | Demande d'autorité | Enregistrée → Plan → En cours → Réponse transmise → Soldée (Sans objet) | Approuvé (réponse ; déclaration sans objet) |
| `wfVerificationCase` | Cas de vérification | Brouillon → En vérification → Approuvé ⇄ En révision (Obsolète) | — (Approvals + `approverNotAuthor` ; signature portée par le plan V&V / la procédure d'essais) |
| `wfAnomaly` | Anomalie | Ouverte → Analysée → En correction → Corrigée → Vérifiée → Close (Rejetée, Différée sous dérogation `waived`) | Accepté / levée (clôture ; intention : si impact sûreté, rendue systématique) |
| `wfChangeRequest` | Demande de modification | Émise → Qualification → Analyse d'impact → CCB → Approuvée → Réalisation → Vérification → Close (Rejetée, Reportée) ; voies : classe I `toCcb`, classe II `approveClassII`, éditoriale `fastTrackEditorial` | Décision CCB (`approveClassII`, `approve`, `reject`) + Approuvé (clôture) |
| `wfNonConformance` | FNC | Déclarée → Caractérisée → Traitement proposé → Traitement approuvé → Actions → Efficacité vérifiée → Soldée (Annulée) | Approuvé (traitement) + Visa qualité (clôture, annulation) |
| `wfWaiver` | Dérogation | Demandée → Instruction → Accord externe → Accordée → Échue (Refusée) | Vérifié (soumission externe) + Approuvé (accord interne ou externe) |
| `wfTechnicalIssue` | Fortuit | Nouveau → Pris en charge → Analyse → Solution proposée → Acceptée → Mise en œuvre → Clos (Sans suite) | Vérifié (solution ; intention : si EIP ou impact sûreté, rendue systématique) |
| `wfDeliverable` | Livrable | Planifié → Rédaction → Vérification → Approuvé → Diffusé → Visa → Définitif (Remplacé, Annulé) | Rédigé + Approuvé |
| `wfReview` | Revue | Planifiée → Prête → Tenue → Prononcée (Annulée) | Approuvé (prononcé) |
| `wfReviewFinding` | Remarque | Ouverte → Répondue → Levée → Close (Retirée) | — |
| `wfAction` | Action | Ouverte → En cours → Réalisée → Efficacité vérifiée / Close (Annulée) | — |
| `wfUnitDeployment` | Déploiement par tranche / cycle | Prévu → Programmé → En cours → Réalisé → Requalifié / soldé (Sans objet) | Vérifié (requalification) |
| `wfLessonLearned` | Fiche REX | Brouillon → Validée → Publiée (Retirée) | — (contrôle technique `approverNotAuthor` à la validation ; lien `capitalizes` requis) |
| `wfWorkPackage` | Lot de travaux | En préparation → Accordé → En réalisation → Remis → Réceptionné (Annulé) | Accord de lot (`agree`) + Rédigé (`deliver`) + Accepté (`accept`) |
| `wfDocumentFull` | LiveDocs formels | Rédaction → Relecture → Vérification → Approbation → Approuvé (Remplacé) | Rédigé + Vérifié + Approuvé (politique « all ») |
| `wfDocumentLight` | LiveDocs express (classe D) | Rédaction → Vérification → Approuvé (Remplacé) | Rédigé + Approuvé |
| `wfDocumentLibrary` | Bibliothèques, produits génériques | Préparation → Approbation → Publié (Remplacé) | Rédigé + Approuvé (`libraryDesignAuthority`) |

### 2.1 Cascade document → éléments

Chaque type de LiveDoc (`model/document_types.yaml`) déclare un type principal (`primaryType`), les types qu'il pilote (`cascadeTypes`) et, le cas échéant, les statuts admis pour d'autres types à l'approbation (`approvalGate`, ex. interfaces `agreed` / `frozen` dans une ST). Le workflow documentaire enchaîne alors :

1. **Mise en vérification** du document (`submitVerification`, signature « rédigé ») : les éléments pilotés encore en brouillon sont **soumis en cascade** (fonction `invokeOnDocItems`, Polarion `InvokeAction`, une par état cible) ; aucune classification interdite dans le document (`noForbiddenClassification`).
2. **Vérification** (`verify`, signature « vérifié ») : indépendance, signataire habilité si la politique du projet l'exige, aucun lien suspect parmi les éléments du document.
3. **Approbation** (`approve`, signature « approuvé ») : condition `cascadedItemsApproved` (tous les éléments pilotés approuvés, types sous `approvalGate` dans les statuts admis), puis cascade `approve` sur les éléments, baseline nommée (`fra-baseline.js`) et export en GED (`fra-export-edms.js`).

C'est par cette cascade que le socle NN-02 (contrôle technique signé) est couvert pour les Work Items dont le workflow ne porte pas de signature propre. Types autorisés et plans types par document : annexe A5 ; gabarits : doc. 12. Le comportement d'`InvokeAction` lorsqu'un élément de la requête n'admet pas l'action est à confirmer (annexe D, PF-07).

## 3. Correspondance avec les mécanismes natifs Polarion

Format de workflow (à confirmer sur la version cible, annexe D) :

```xml
<workflow initial-status="…" prototype="WorkItem|Module|TestRun">
  <transitions><transition action from to/></transitions>
  <actions>
    <action id name>
      <required><field name/></required>
      <conditions>…</conditions>
      <functions>…</functions>
      <signatures/>
    </action>
  </actions>
</workflow>
```

| Besoin | Mécanisme Polarion | Natif ? |
|---|---|---|
| Rôles autorisés | `RoleCondition(roles)` (rôles spéciaux `workitem.assignee` / `workitem.author` acceptés) | Oui |
| Propriétaire du document (pseudo-rôle `documentOwner`) | `ScriptCondition(fra-document-owner.js)` : aucun rôle spécial Polarion connu pour l'auteur d'un document | Script |
| Champs obligatoires | `<required><field name/>` | Oui |
| Champ non vide | `FieldNonEmpty(field.name, negate)` | Oui |
| Lien requis | `LinkedWorkItem(link.role, backlink, target.work.item.type)` | Oui |
| Statut des éléments liés | `LinkedWorkItemsStatus(link.roles / back.link.roles, valid.states)` ; `ScriptCondition(fra-link-status.js)` dès qu'un filtre par type ou par champ est nécessaire | Oui / Script |
| Approbations | `ApprovalState(commonApprovalState)`, `AtLeastOneApprovedAndNooneDisapproved`, `AddDefaultApprovals` ; avis Sûreté conditionnel par `fra-request-safety-approval.js` (`AddDefaultApprovals` n'est pas conditionnel) | Oui / Script |
| Positionner / vider un champ | `ChangeField`, `ClearField`, `SetDate` ; `ScriptFunction(fra-set-if-empty.js)` pour « seulement si vide » (`ChangeField` est inconditionnel) | Oui / Script |
| Créer un élément lié | `CreateLinkedWorkItem(type, link.role, backlink)` | Oui |
| Transition en cascade sur les éléments d'un document | `InvokeAction(statusId, actionId, query)` | Oui (documents) |
| Signataires d'un document | Désignés manuellement ou via les Approvals (la fonction `addSigners` a été retirée du catalogue) ; bloc `<signatures><signature-policy name="all"/></signatures>` [à vérifier, annexe D PF-02] | Oui (documents) |
| Document sans suspect / sans élément non approuvé | `ContainsNoMatchingWorkItems(query)` | Oui (documents) |
| Indépendance, suspects (Work Item), cardinalités, règles conditionnelles, habilitation | `ScriptCondition(engine=js, script=…)` | Script |
| SLA, notifications ciblées, baselines, indice documentaire, statut de vérification | `ScriptFunction` | Script |
| Export GED | `ScriptFunction(fra-export-edms.js)`, qui appelle l'extension d'export PDF (ex. pdf-exporter) et le connecteur GED (doc. 22) | Script + extension |

> Les fonctions `SetResolution`, `ClearResolution` et `SetFieldValue` **n'existent pas** sous ces noms dans Polarion. Le générateur utilise `ChangeField` / `ClearField`.

## 4. Spécification des scripts de workflow

Les scripts sont livrés en JavaScript dans `$POLARION_HOME/scripts` [à vérifier, spike S1]. Une `ScriptCondition` reçoit le contexte (`workflowContext` : élément ou document, utilisateur, projet) et ses paramètres (`rule`, `roles`, `args`, `projectParameter`) ; un retour `false` ou une chaîne bloque l'action et affiche le motif. Une `ScriptFunction` agit après la transition. Les scripts sont **versionnés dans ce dépôt** (dossier `scripts/`, lot d'industrialisation), testés en recette et couverts par la validation de l'outil (OQ, doc. 15 § 4). Priorités, occurrences et cas de test par script : doc. 23 § 3 ; liste à jour des scripts attendus : manifeste `SIGNATURES_ET_SCRIPTS.md`.

> Les signatures d'API ci-dessous sont indicatives (pseudo-code). Elles sont à valider sur le SDK (kit de développement) de la version cible.

Les 17 scripts, dans l'ordre décroissant de leur nombre d'occurrences dans la configuration générée :

| Script | But (catalogue `workflows.yaml`) | Entrées | Règle (pseudo-code) |
|---|---|---|---|
| `fra-document-owner.js` (condition) | Pseudo-rôle `documentOwner` : réserver une transition documentaire à l'auteur du LiveDoc | document, utilisateur courant | `doc = ctx.document ; u = ctx.user`<br/>`if (u == doc.author OR u == doc.field("docAuthor")) return true`<br/>`return "Transition réservée au propriétaire du document"` |
| `fra-independence.js` (condition) | Contrôle technique (`approverNotAuthor`, arrêté INB art. 2.5.3 : indépendance du vérificateur) | élément ou document, utilisateur | `wi = ctx.target ; u = ctx.user`<br/>`if (u == wi.author OR u == lastEditorOfContentFields(wi)) return "Contrôle technique : le vérificateur doit être différent de l'auteur / du dernier rédacteur"`<br/>`return true` |
| `fra-field-rule.js` (condition) | Règles de valeur (`fieldValue` : `in`, `notIn`, `equals`, `nonEmptyIf`, `nonEmptyAny`, `onlyIf`, `unlessFieldNonEmpty`, `onlyIfProjectSetting`) | `rule` sérialisée | `r = parse(rule)`<br/>`if (r.onlyIf && !eval(r.onlyIf, wi)) return true ; if (r.onlyIfProjectSetting && !projectSetting(r.onlyIfProjectSetting)) return true`<br/>`if (r.unlessFieldNonEmpty && nonEmpty(wi, r.unlessFieldNonEmpty)) return true`<br/>`return check(wi.field(r.field), r) ? true : message(r)` |
| `fra-habilitation.js` (condition) | Signataire habilité (`qualifiedSignatory`, ADR-27, doc. 21 § 3) | `rule` {field, level}, `projectParameter = signaturePolicy` | `if (project.param("signaturePolicy") != "habilitationBased") return true`<br/>`dom = wi.field(rule.field) ; if (!dom OR dom == "none") return true`<br/>`return userInGroup("HAB-" + dom + "-" + rule.level) ? true : "Habilitation " + dom + " requise"` |
| `fra-link-cardinality.js` (condition) | Cardinalités (`hasLink` : `exactly`, `min`), filtres sur le type ou le statut de la cible, gardes `onlyIf*` / `unlessFieldIn` | `rule` | `r = parse(rule) ; if (gardes non satisfaites) return true`<br/>`n = count(links(wi, r.role, r.direction) filtrés par type et par linkedStatus)`<br/>`ok = r.exactly ? n == r.exactly : n >= r.min`<br/>`return ok ? true : "Lien " + r.role + " requis (" + n + " trouvé(s))"` |
| `fra-revision-index.js` (fonction) | Indice documentaire : A0, A1… (brouillons), puis A, B, C (diffusions) | document ou livrable | `idx = target.field("revisionIndex")`<br/>`target.set("revisionIndex", next(idx))  // A0 → A1 … → A → B → C` |
| `fra-baseline.js` (fonction) | Baseline nommée à l'approbation d'un document ou à la clôture d'une demande de modification | `args.nameTemplate` (`${document}`, `${revisionIndex}`, `${id}`) | `name = expand(args.nameTemplate, target)`<br/>`createBaseline(project, name, scope = document ou élément)` |
| `fra-export-edms.js` (fonction) | Export du PDF signé + manifeste des signatures vers la GED (archivage de référence, NN-07) | document ou livrable | `pdf = pdfExporter.export(target, "PDF/A")`<br/>`manifest = signatures(target)`<br/>`ref = edmsConnector.archive(pdf, manifest, metadata(target))`<br/>`target.set("edmsReference", ref)` |
| `fra-no-suspect.js` (condition) | Aucun lien sortant suspect pour les rôles listés (`noSuspectLinks`) ; portées `documentItems` / `impactedItems` | `roles` ou portée | `items = scope(ctx)  // élément seul, éléments du document ou périmètre 'impacts'`<br/>`for l in links(items): if (l.role in roles AND l.suspect) return "Lien suspect non levé : " + l.target.id`<br/>`return true` |
| `fra-classification.js` (condition) | Données interdites sur l'instance standard (`noForbiddenClassification`, NN-06) | élément, instance courante | `if (instance != "STD") return true`<br/>`if (wi.informationClassification in {sensitiveSecurity, restricted}) return "Classification interdite sur cette instance"`<br/>`return true` |
| `fra-safety-approval.js` (condition) | Avis Sûreté conditionnel (`safetyApprovalIf`) | `rule` (expression) | `if (!eval(rule, wi)) return true`<br/>`if (!exists approval(wi, by = user having role safetyEngineer, state = approved)) return "Avis Sûreté requis"`<br/>`return true` |
| `fra-request-safety-approval.js` (fonction) | Ajout conditionnel d'un approbateur Sûreté (`requestSafetyApproval`) | `args.onlyIf` (absent = toujours) | `if (args.onlyIf && !eval(args.onlyIf, wi)) return`<br/>`for u in safetyApprovers(project)  // détenteurs du rôle safetyEngineer désignés`<br/>`    wi.addApproval(u)` |
| `fra-notify.js` (fonction) | Notification ciblée (`notifyRoles`), en complément des notifications natives | `args.roles`, `args.onlyIf`, `args.scope` | `if (args.onlyIf && !eval(args.onlyIf, wi)) return`<br/>`to = usersWithRoles(project, args.roles) ∪ resolveScope(args.scope, wi)`<br/>`notify(to, template(transition), wi)` |
| `fra-verification-status.js` (fonction) | Statut de vérification des exigences (`recomputeVerificationStatus`) ; complété par un script planifié nocturne (2506+ [à vérifier, spike S1]) | élément approuvé | `for req in requirementsLinkedBy(wi, [verifies, validates]):`<br/>`    results = lastRecordResults(approvedCases(req))`<br/>`    req.set("verificationStatus", worstOf(results))  // agrégation pire cas` |
| `fra-set-if-empty.js` (fonction) | Positionner un champ seulement s'il est vide (`setFieldValue.valueIfEmpty`) | `args` {field, value} | `if (isEmpty(wi.field(args.field))) wi.set(args.field, args.value)` |
| `fra-link-status.js` (condition) | Statut des éléments liés filtrés par type ou par champ (`linkedItemsStatus` non natif) | `rule` {role, direction, type, field / in, statuses} | `items = linked(wi, r.role, r.direction).filter(type == r.type).filter(r.field ? field in r.in : true)`<br/>`bad = items.filter(i => !(i.status in r.statuses))`<br/>`return bad.empty ? true : "Éléments liés non terminés : " + ids(bad)` |
| `fra-sla.js` (fonction) | Échéance (`setDueDateFromNow`) : caractérisation des FNC (5 jours, indicatif, **P0** au pilote) ; fortuits par urgence (24 h, 72 h, 14 j, 30 j ; INC-2) | `args` {days \| byUrgency, field} | `delay = args.days ? days(args.days) : parse(args.byUrgency[wi.urgency])`<br/>`wi.set(args.field, now() + delay)` |

Le verrouillage du texte original d'une exigence d'entrée après `establishPosition` n'est **pas** un script : il relève des permissions par état (PR-03, § 6.3).

## 5. Signatures électroniques

### 5.1 Configuration

| Paramètre | Valeur cible | Source |
|---|---|---|
| `secure.approvals` | `true` (ré-authentification à l'approbation) | Aide Polarion [C] ; nom exact de la propriété [à vérifier, spike S1 / Q-TOOL-01] |
| `secure.dialog.title` / `secure.dialog.message` | Texte rappelant la portée juridique (« Je certifie avoir réalisé le contrôle technique… ») | [C] [à vérifier, spike S1] |
| `secure.approvals.comment` | Commentaire automatique avec `$user` | [C] [à vérifier, spike S1] |
| SSO (authentification unique) | Authentification alternative LDAP (annuaire) « autorisée pour les e-signatures » (PR-04) | [C] |
| Signatures de documents | Politique `all` (tous les signataires invités) ; signataires désignés manuellement ou via les Approvals (fonction `addSigners` retirée du catalogue) ; politique `signaturePolicy` du projet (rôle seul ou habilitation, doc. 21 § 3, PR-10) | [C] / annexe D PF-02 |
| Signatures de Test Runs | Transition vers le statut `resultsApproved` du workflow de Test Run, configuré manuellement (doc. 23, S5 ; non généré) | [P] (« auto-signature » observée [à vérifier, spike S1]) |
| Licence REVIEWER et signature de documents | À confirmer sur la version cible | Q-TOOL-03 |

### 5.2 Triptyque documentaire R / V / A

| Étape | Transition | Signataire | Signification |
|---|---|---|---|
| Rédaction | `submitVerification` | Propriétaire du document (`documentOwner`) | « Rédigé par » |
| Vérification | `verify` | Vérificateur (≠ auteur) | « Vérifié par (contrôle technique) » |
| Approbation | `approve` | Approbateur (≠ auteur) | « Approuvé par » |
| Effets à l'approbation | — | — | Cascade `approve` sur les éléments pilotés (§ 2.1) + baseline + export PDF signé (manifeste des signatures) en GED |

### 5.3 Valeur probante (ADR-11)

- Signature électronique simple au sens du règlement européen eIDAS (identification électronique et services de confiance), adossée à :
  - l'authentification forte (MFA, authentification à plusieurs facteurs, à l'ouverture de session) ;
  - la ré-authentification à la signature ;
  - l'horodatage serveur ;
  - l'historique immuable (dépôt Subversion, SVN, sous-jacent à Polarion) ;
  - la procédure qualité qui définit les significations.
- Le **PDF signé archivé en GED** (PDF/A, format d'archivage à long terme, + manifeste) est l'enregistrement de référence.

### 5.4 Décision : signature portée par le document pour les Work Items d'ingénierie

Les workflows `wfRequirement`, `wfArchitecture`, `wfVerificationCase`, `wfSafetyAnalysisItem` et `wfLibraryItem` n'exigent **aucune signature électronique individuelle** à l'approbation. Le contrôle technique y est tracé par les Approvals et la condition `approverNotAuthor` ; la signature R / V / A est portée par le LiveDoc (ST, STB, SDM, dossier de sûreté, plan V&V, procédure, bibliothèque) dont l'approbation cascade la transition `approve` (§ 2.1). Conséquences :
- un Work Item approuvé **hors** de tout LiveDoc n'est pas signé ; le socle NN-02 n'est alors couvert que si l'élément est ensuite intégré dans un document approuvé — cas à surveiller par un rapport « éléments approuvés hors document signé », à ajouter au catalogue du doc. 13 [H] ;
- les cas de validation OQ (doc. 15 § 4) portent sur la signature du document et sur la cascade, non sur une signature par exigence ;
- si le retour d'expérience du pilote l'exige, l'option inverse (clé `signature: {required: true, meaning: verified}` sur l'action `approve` de ces workflows) est une évolution mineure du modèle (CCB du modèle, doc. 17 § 2).

## 6. Rôles et séparation des tâches

### 6.1 Séparation des tâches (contrôles bloquants)

| Paire incompatible sur un même élément | Contrôle |
|---|---|
| Auteur / vérificateur | `fra-independence.js` |
| Auteur / approbateur | idem |
| Demandeur d'une modification / président du CCB | Rapport + règle d'organisation |
| Exécutant d'un essai / approbateur des résultats | Signature de Test Run réservée à `vvLead` ≠ exécutant |
| Équipe de développement / V&V indépendante (logiciel de catégorie A) | Rôle `independentVerifier` attribué à une organisation distincte (groupe d'annuaire dédié) |

### 6.2 Rôles (synthèse)

34 rôles projet (dont 4 pseudo-rôles : `anyProjectMember`, `documentOwner`, `workitem.assignee`, `workitem.author`) + 7 rôles globaux (`admin`, `designAuthority`, `globalConfigManager`, `user`, `auditor`, `provisioningOfficer`, `habilitationAdministrator`) ; matrice des droits en annexe A6. Licences cibles (ALM = licence complète ; REQUIREMENTS = exigences et LiveDocs ; QA = tests et qualité ; REVIEWER = lecture, commentaires, approbation, signature de documents à confirmer ; PRO = contribution limitée) :

| Licence | Rôles |
|---|---|
| ALM | projectAdmin, projectManager, technicalLead, disciplineEngineer, safetyEngineer, safetyLead, qualityEngineer, configurationManager, licensingEngineer, interfaceManager, workPackageManager, libraryDesignAuthority |
| REQUIREMENTS | requirementsManager, libraryCurator |
| QA | vvLead, vvEngineer, testExecutor, independentVerifier |
| REVIEWER | verifier, approver, ccbChair, ccbMember, reviewer, customerReviewer, reader, exportControlOfficer, securityOfficer, unitManager |
| PRO | documentController, supplierContributor |

### 6.3 Règles de permission (PR-01 à PR-11)

- Pas de suppression (PR-01).
- Champs de classement réservés à la Sûreté après approbation (PR-02).
- Pas d'édition directe des éléments approuvés ou gelés : réouverture tracée (PR-03).
- Ré-authentification à la signature (PR-04).
- Bibliothèques en lecture seule (PR-05).
- Externes cloisonnés dans les projets sas `EXT-*` (PR-06).
- Abaissement de `exportControl` réservé au `exportControlOfficer` (PR-07).
- Revue semestrielle des habilitations (PR-08).
- Un Space (dossier d'un projet) n'est pas une frontière de sécurité : cloisonnement par projet distinct (PR-09, ADR-28, doc. 21 § 4).
- Politique de signature choisie au provisioning et figée (PR-10, ADR-27, doc. 21 § 3).
- Comptes externes `EXT-*` : expiration automatique, revue trimestrielle, aucune licence nommée partagée (PR-11).

Permissions par état : Polarion permet de restreindre la modification des champs selon le statut. Configuration « champs non modifiables dans les états `approved`, `frozen`, `published`, `decided`, `closed` », et `originalText` non modifiable à l'état `accepted` d'une exigence d'entrée (PR-03). Point de vigilance [à vérifier au spike S1] : la saisie du champ requis `transitionNote` lors d'un retour pour reprise doit rester possible sans droit général de modification (annexe D, PF-13).
