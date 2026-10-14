# Partie 3.4 — Workflows, signatures électroniques, rôles et permissions

> Diagrammes d'états et tableaux de transitions exhaustifs : [Annexe A4](../generated/A4_workflows.md). Rôles et matrice des droits : [Annexe A6](../generated/A6_roles_permissions.md). Fichiers générés : `generated/polarion/<lang>/.polarion/tracker/workflow/*.xml` et `documents/workflow/*.xml`.

## 1. Principes de conception des workflows

| # | Principe |
|---|---|
| WF1 | **Bloquer ce qui relève du socle non négociable** (contrôle technique indépendant, EIP / exigences définies, suspects, classification), **signaler le reste** par des rapports, pour ne pas paralyser l'usage |
| WF2 | Pas de suppression : la sortie d'un élément se fait par un état terminal (`obsolete`, `rejected`, `cancelled`, `superseded`) avec un motif (`transitionNote`) |
| WF3 | Toute modification d'un élément approuvé passe par une **réouverture tracée**, sous demande de modification après la première baseline |
| WF4 | **Indépendance** (contrôle technique) : l'exécutant d'une transition d'approbation n'est ni l'auteur ni le dernier rédacteur |
| WF5 | La signature électronique matérialise le contrôle technique et l'approbation ; elle porte une **signification** (rédigé, vérifié, approuvé, avis sûreté, visa qualité, décision CCB, levée) |
| WF6 | Les signatures conditionnelles n'étant pas natives, la signature est **systématique** sur les transitions concernées (choix conservateur). Alternative : dédoubler l'action (« approuver » / « approuver avec signature ») avec des conditions exclusives |
| WF7 | Les workflows sont **partagés par famille** (24 workflows de Work Items pour 36 types, + 3 workflows documentaires) pour limiter la charge de formation |

## 2. Catalogue des workflows

| Workflow | Types | États principaux | Signatures |
|---|---|---|---|
| `wfRequirement` | 6 types d'exigences rédigées | Brouillon → En vérification → Approuvée ⇄ En révision → Obsolète / Rejetée | Vérifié (approbation) |
| `wfInputRequirement` | Exigence d'entrée | Importée → En analyse ⇄ Clarification → Position établie → Remplacée | — (signature au niveau de la matrice de conformité) |
| `wfLibraryItem` | Exigence réglementaire, terme | Brouillon → Validé → Publié → Remplacé / Retiré | Approuvé (publication) |
| `wfAssumption` | Hypothèse | À confirmer → Confirmée / Infirmée | Vérifié (si pertinente pour la sûreté) |
| `wfArchitecture` | Scénario, fonction, éléments L / P, paramètre | Brouillon → En vérification → Approuvé ⇄ En révision → Obsolète | Vérifié |
| `wfInterface` | Interface | Identifiée → Définie → Accordée (A + B) → Gelée ⇄ En révision | Approuvé (accord) |
| `wfDecision` | Décision de conception | Proposée → En évaluation → Décidée → Remplacée | Approuvé |
| `wfSafetyAnalysisItem` | Agression, revendication, AMDEC | Brouillon → En vérification → Approuvé ⇄ En révision | Avis sûreté |
| `wfAnalysis` | Analyse / note de calcul | Planifiée → En cours → En contrôle technique → Approuvée → Remplacée | Rédigé + Vérifié |
| `wfRisk` | Risque | Identifié → Évalué → En traitement → Sous surveillance → Clos / Survenu | — |
| `wfCommitment` | Demande d'autorité | Enregistrée → Plan → En cours → Réponse transmise → Soldée | Approuvé (réponse) |
| `wfVerificationCase` | Cas de vérification | Brouillon → En vérification → Approuvé ⇄ En révision | Vérifié |
| `wfAnomaly` | Anomalie | Ouverte → Analysée → En correction → Corrigée → Vérifiée → Close | Levée (si impact sûreté) |
| `wfChangeRequest` | Demande de modification | Émise → Qualification → Analyse d'impact → CCB → Approuvée → Réalisation → Vérification → Close | Décision CCB + Approuvé (clôture) |
| `wfNonConformance` | FNC | Déclarée → Caractérisée → Traitement proposé → Traitement approuvé → Actions → Efficacité vérifiée → Soldée | Approuvé (traitement) + Visa qualité (clôture) |
| `wfWaiver` | Dérogation | Demandée → Instruction → Accord externe → Accordée → Échue | Vérifié + Approuvé |
| `wfTechnicalIssue` | Fortuit | Nouveau → Pris en charge → Analyse → Solution proposée → Acceptée → Mise en œuvre → Clos | Vérifié (solution) |
| `wfDeliverable` | Livrable | Planifié → Rédaction → Vérification → Approuvé → Diffusé → Visa → Définitif | Rédigé + Approuvé |
| `wfReview` | Revue | Planifiée → Prête → Tenue → Prononcée | Approuvé |
| `wfReviewFinding` | Remarque | Ouverte → Répondue → Levée → Close | — |
| `wfAction` | Action | Ouverte → En cours → Réalisée → Efficacité vérifiée / Close | — |
| `wfDocumentFull` | LiveDocs formels | Rédaction → Relecture → Vérification → Approbation → Approuvé → Remplacé | Rédigé + Vérifié + Approuvé (politique « all ») |
| `wfDocumentLight` | LiveDocs express (classe D) | Rédaction → Vérification → Approuvé | Rédigé + Approuvé |
| `wfDocumentLibrary` | Bibliothèques, produits génériques | Préparation → Approbation → Publié → Remplacé | Rédigé + Approuvé (Design Authority) |

## 3. Correspondance avec les mécanismes natifs Polarion

Format de workflow vérifié :

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
| Champs obligatoires | `<required><field name/>` | Oui |
| Champ non vide | `FieldNonEmpty(field.name, negate)` | Oui |
| Lien requis | `LinkedWorkItem(link.role, backlink, target.work.item.type)` | Oui |
| Statut des éléments liés | `LinkedWorkItemsStatus(link.roles / back.link.roles, valid.states)` | Oui |
| Approbations | `ApprovalState(commonApprovalState)`, `AtLeastOneApprovedAndNooneDisapproved`, `AddDefaultApprovals` | Oui |
| Positionner / vider un champ | `ChangeField`, `ClearField`, `SetDate` | Oui |
| Créer un élément lié | `CreateLinkedWorkItem(type, link.role, backlink)` | Oui |
| Transition en cascade sur les éléments d'un document | `InvokeAction(statusId, actionId, query)` | Oui (documents) |
| Signataires d'un document | `AddDefaultSigners(signedBy.roles, signer.role, target.status.id)` + `<signatures><signature-policy name="all"/></signatures>` | Oui (documents) |
| Document sans suspect / sans élément non approuvé | `ContainsNoMatchingWorkItems(query)` | Oui (documents) |
| Indépendance, suspects (Work Item), cardinalités, règles conditionnelles | `ScriptCondition(engine=js, script=…)` | Script |
| SLA, notifications ciblées, baselines, indice documentaire | `ScriptFunction` | Script |
| Export GED | Extension (export PDF) + connecteur | Extension |

> Les fonctions `SetResolution`, `ClearResolution` et `SetFieldValue` **n'existent pas** sous ces noms dans Polarion. Le générateur utilise `ChangeField` / `ClearField`.

## 4. Spécification des scripts de workflow

Les scripts sont livrés en JavaScript dans `$POLARION_HOME/scripts`. Ils reçoivent `workflowContext` et `arguments` ; un retour `false` ou une chaîne bloque l'action et affiche le motif. Ils sont **versionnés dans ce dépôt** (lot d'industrialisation), testés en recette et couverts par la validation de l'outil.

> Les signatures d'API ci-dessous sont indicatives. Elles sont à valider sur le SDK de la version cible.

| Script | Rôle | Pseudo-code |
|---|---|---|
| `fra-independence.js` | Contrôle technique (arrêté INB 2.5.3) | `wi = target(); u = currentUser(); if (u == wi.author OR u == lastEditorOfContentFields(wi)) return "Contrôle technique : le vérificateur doit être différent de l'auteur / du rédacteur" ; return true` |
| `fra-no-suspect.js` | Aucun lien sortant suspect pour les rôles listés | `for l in wi.linkedWorkItems: if l.role in args.roles and l.suspect: return "Lien suspect non levé : " + l.target.id ; return true` |
| `fra-classification.js` | Données interdites sur l'instance STD | `if wi.informationClassification in {sensitiveSecurity, restricted}: return "Classification interdite sur cette instance"` |
| `fra-safety-approval.js` | Avis sûreté conditionnel | `if eval(args.rule, wi): if not exists approval(by user having role safetyEngineer, state approved): return "Avis Sûreté requis"` |
| `fra-field-rule.js` | Règles de valeur (`in`, `notIn`, `nonEmptyIf`, `equals`, `onlyIf`) | évaluation déclarative de `args.rule` |
| `fra-link-cardinality.js` | Cardinalités (`exactly`, `min`), filtres sur le type ou le statut de la cible, `onlyIfInBaseline` | comptage des liens |
| `fra-sla.js` | Échéance par urgence (fortuits : 24 h, 72 h, 14 j, 30 j) ; FNC (5 jours ouvrés, indicatif) | `wi.responseDueDate = now + delay(wi.urgency)` |
| `fra-verification-status.js` | Statut de vérification des exigences liées (dernier résultat des cas approuvés ; agrégation pire cas) ; complété par un script planifié nocturne (2506+) | voir document 13 |
| `fra-baseline.js` | Baseline nommée à l'approbation d'un document ou à la clôture d'une demande de modification | `createBaseline(name(template), project)` |
| `fra-revision-index.js` | Indice documentaire : A0, A1… (brouillons), puis A, B, C (diffusions) | |
| `fra-lock-fields.js` (hook) | Verrouillage du texte original d'une exigence d'entrée après acceptation | hook de sauvegarde : refuser la modification de `originalText` si `status = accepted` |

## 5. Signatures électroniques

### 5.1 Configuration

| Paramètre | Valeur cible | Source |
|---|---|---|
| `secure.approvals` | `true` (ré-authentification à l'approbation) | Aide Polarion [C] |
| `secure.dialog.title` / `secure.dialog.message` | Texte rappelant la portée juridique (« Je certifie avoir réalisé le contrôle technique… ») | [C] |
| `secure.approvals.comment` | Commentaire automatique avec `$user` | [C] |
| SSO | Authentification alternative LDAP « autorisée pour les e-signatures » | [C] |
| Signatures de documents | Politique `all` (tous les signataires invités) ; signataires ajoutés par `AddDefaultSigners` selon `docVerifier` / `docApprover` | [C] |
| Signatures de Test Runs | `<signatures>` sur la transition `resultsApproved` | [C] (`auto-signature` observé) |

### 5.2 Triptyque documentaire R / V / A

| Étape | Transition | Signataire | Signification |
|---|---|---|---|
| Rédaction | `submitVerification` | Propriétaire du document | « Rédigé par » |
| Vérification | `verify` | Vérificateur (≠ auteur) | « Vérifié par (contrôle technique) » |
| Approbation | `approve` | Approbateur (≠ auteur) | « Approuvé par » |
| Effets à l'approbation | — | — | Baseline + export PDF signé (manifeste des signatures) en GED |

### 5.3 Valeur probante (ADR-11)

- Signature électronique simple au sens d'eIDAS, adossée à :
  - l'authentification forte (MFA à l'ouverture de session) ;
  - la ré-authentification à la signature ;
  - l'horodatage serveur ;
  - l'historique immuable (SVN) ;
  - la procédure qualité qui définit les significations.
- Le **PDF signé archivé en GED** (PDF/A + manifeste) est l'enregistrement de référence.

## 6. Rôles et séparation des tâches

### 6.1 Séparation des tâches (contrôles bloquants)

| Paire incompatible sur un même élément | Contrôle |
|---|---|
| Auteur / vérificateur | `fra-independence.js` |
| Auteur / approbateur | idem |
| Demandeur d'une modification / président du CCB | Rapport + règle d'organisation |
| Exécutant d'un essai / approbateur des résultats | Signature de Test Run réservée à `vvLead` ≠ exécutant |
| Équipe de développement / V&V indépendante (logiciel cat. A) | Rôle `independentVerifier` attribué à une organisation distincte (groupe d'annuaire dédié) |

### 6.2 Rôles (synthèse)

32 rôles projet + 5 rôles globaux (Annexe A6). Licences cibles :

| Licence | Rôles |
|---|---|
| ALM | technicalLead, disciplineEngineer, safetyEngineer, qualityEngineer, configurationManager, licensingEngineer, interfaceManager… |
| REQUIREMENTS | requirementsManager, libraryCurator |
| QA | vvLead, vvEngineer, testExecutor, independentVerifier |
| REVIEWER | verifier, approver, ccbChair, ccbMember, reviewer, customerReviewer, reader, exportControlOfficer, securityOfficer |
| PRO | documentController, supplierContributor |

### 6.3 Règles de permission (PR-01 à PR-08)

- Pas de suppression (PR-01).
- Champs de classement réservés à la Sûreté après approbation (PR-02).
- Pas d'édition directe des éléments approuvés (PR-03).
- Ré-authentification à la signature (PR-04).
- Bibliothèques en lecture seule (PR-05).
- Externes cloisonnés (PR-06).
- Abaissement de `exportControl` réservé (PR-07).
- Revue semestrielle des habilitations (PR-08).

Permissions par état : Polarion permet de restreindre la modification des champs selon le statut. Configuration « champs non modifiables dans les états `approved`, `frozen`, `published`, `decided`, `closed` ».
