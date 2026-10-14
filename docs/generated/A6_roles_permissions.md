# Annexe A6 — Rôles, licences et permissions

> Document **généré** par `tools/generate_docs.py` depuis `model/*.yaml` — ne pas éditer à la main.

## Types de licences

- **ALM** : Licence complète (exigences, tests, tâches, rapports, administration projet)
- **REQUIREMENTS** : Gestion des exigences et LiveDocs
- **QA** : Gestion des tests et de la qualité
- **PRO** : Contribution (édition limitée aux éléments existants selon configuration)
- **REVIEWER** : Lecture, commentaires, approbation de Work Items ; signature de documents (à confirmer sur la version cible) ; pas de création
- **VARIANTS** : Module complémentaire de gestion des variantes (feature model, pvSCL)

## Rôles globaux

| id | Rôle | Note |
|---|---|---|
| `admin` | Administrateur plateforme (DSI) | Effectif minimal, comptes nominatifs à privilèges, journalisés. |
| `designAuthority` | Autorité de conception du modèle de données (Design Authority ALM) | Valide toute évolution de la configuration globale (CCB du modèle). |
| `globalConfigManager` | Gestionnaire de configuration globale | Déploie la configuration versionnée (ce dépôt) sur les environnements. |
| `user` | Utilisateur authentifié | Rôle de base, aucun droit projet implicite. |
| `auditor` | Auditeur (qualité interne, autorité, client) | Lecture seule, habilitation temporaire et tracée, par projet. |

## Rôles projet — matrice des droits

R lire · C créer · E modifier · T transitions · A approuver · S signer · L lier · X administrer

| Rôle | Licence | REQ | ARC | SAF | VV | CHG | PRJ | DOC | LIB | Note |
|---|---|---|---|---|---|---|---|---|---|---|
| `projectAdmin` Administrateur projet | ALM | R | R | R | R | R | RCE | RX | R | Administration locale limitée (droits, plans, requêtes) – ne modifie pas le modèle global. |
| `projectManager` Chef de projet | ALM | R | R | RCET | R | RCETL | RCETL | R | R |  |
| `technicalLead` Responsable technique / architecte système | ALM | RCETAL | RCETAL | RCETL | RTL | RCETAL | RCETL | RCETS | R |  |
| `requirementsManager` Responsable exigences | REQUIREMENTS | RCETL | RL | R | RL | RCL | R | RCET | R |  |
| `disciplineEngineer` Ingénieur discipline (rédacteur) | ALM | RCETL | RCETL | RCETL | RCEL | RCETL | RCETL | RCETS | R |  |
| `verifier` Vérificateur (contrôle technique) | REVIEWER | RTAS | RTAS | RTAS | RTAS | RTAS | RTAS | RTS | R | Licence REVIEWER suffisante si le vérificateur ne crée pas d'éléments ; sinon ALM. Ne peut jamais vérifier ses propres productions (condition approverNotAuthor). |
| `approver` Approbateur (responsable hiérarchique / technique) | REVIEWER | RTAS | RTAS | RTAS | RTAS | RTAS | RTAS | RTS | R |  |
| `safetyEngineer` Ingénieur sûreté | ALM | RCETAL | RAL | RCETAL | RL | RCETAL | RCL | RCETS | R |  |
| `safetyLead` Responsable sûreté projet | ALM | RTAS | RTAS | RCETAS | R | RTAS | R | RTS | R |  |
| `qualityEngineer` Ingénieur qualité / surveillance | ALM | R | R | R | RA | RCETAS | RCETL | RA | R |  |
| `configurationManager` Gestionnaire de configuration | ALM | RTL | RTL | RT | RT | RCETS | RCET | RTX | R | Seul habilité à créer / supprimer des baselines et à rendre obsolètes les éléments sous référence. |
| `ccbChair` Président du CCB | REVIEWER | R | R | R | R | RTAS | R | R | R |  |
| `ccbMember` Membre du CCB | REVIEWER | R | R | R | R | RA | R | R | R |  |
| `vvLead` Responsable V&V / essais | QA | RL | RL | R | RCETAS | RCETL | RCET | RCETS | R |  |
| `vvEngineer` Ingénieur V&V / essais | QA | RL | RL | R | RCETL | RCETL | RCE | RCE | R |  |
| `testExecutor` Exécutant d'essais / technicien | QA | R | R | - | RT | RC | R | R | - | Saisit les résultats des Test Runs ; ne modifie pas les cas de vérification. |
| `independentVerifier` V&V indépendante (logiciel catégorie A, revue de sûreté indépendante) | QA | R | R | R | RCETAS | RC | RC | RS | R | Appartient à une organisation distincte de l'équipe de développement (exigence d'indépendance). |
| `licensingEngineer` Ingénieur licensing / relations autorités | ALM | R | R | RCETL | R | RCETS | RCETL | RCETS | RCE |  |
| `interfaceManager` Gestionnaire d'interfaces | ALM | RL | RCETAL | R | R | RCL | RCE | RCETS | R |  |
| `documentController` Gestionnaire documentaire | PRO | R | R | R | R | R | RET | RT | R |  |
| `documentOwner` Propriétaire de document (rôle dynamique = auteur du LiveDoc) | ALM |  |  |  |  |  |  | RCETS |  |  |
| `libraryCurator` Référent bibliothèque (réglementaire, produit, terminologie) | REQUIREMENTS |  |  |  |  |  |  | RCETS | RCETSL |  |
| `reviewer` Relecteur interne | REVIEWER | RA | RA | RA | RA | RA | RTA | RA | R |  |
| `customerReviewer` Relecteur client (externe) | REVIEWER | R | R | - | R | - | RTA | RA | - | Accès restreint aux documents explicitement partagés (Space dédié) ; contrôle export préalable ; alternative : échange ReqIF / PDF signé. |
| `supplierContributor` Contributeur fournisseur (externe) | PRO | R | - | - | RE | RC | RE | R | - | Projet ou Space de collaboration dédié ; jamais d'accès au projet principal. |
| `reader` Lecteur interne | REVIEWER | R | R | R | R | R | R | R | R |  |
| `exportControlOfficer` Responsable contrôle export | REVIEWER | RE | RE | RE | RE | RE | RE | RE | RE | Seul habilité à abaisser le champ exportControl (élévation libre pour tous). |
| `securityOfficer` Responsable sécurité de l'information projet | REVIEWER | R | R | R | R | R | R | R | R | Contrôle le respect des classifications ; déclenche la purge vers l'instance sensible si nécessaire. |
| `anyProjectMember` Tout membre du projet (pseudo-rôle) | - |  |  |  |  |  |  |  |  |  |
| `designAuthority` Autorité de conception (projet bibliothèque / produit) | ALM |  |  |  |  |  |  | RTS | RCETAS |  |
| `workitem.assignee` Responsable de l'élément (rôle dynamique Polarion) | - |  |  |  |  |  |  |  |  |  |
| `workitem.author` Auteur de l'élément (rôle dynamique Polarion) | - |  |  |  |  |  |  |  |  |  |

## Règles de permission

- **PR-01** — Aucune suppression de Work Item par les utilisateurs : seule la transition vers un état 'obsolète / annulé / rejeté' est permise (l'historique fait foi).
- **PR-02** — Les champs de classement de sûreté (sscClassification, functionSafety) ne sont modifiables que par safetyEngineer / safetyLead une fois l'élément approuvé.
- **PR-03** — Les éléments à l'état approuvé / gelé ne sont modifiables qu'après réouverture tracée (transition), jamais en édition directe (permission 'modifier' retirée par état).
- **PR-04** — Les signatures (documents et Work Items) exigent une ré-authentification ; en SSO, l'authentification alternative LDAP 'autorisée pour les e-signatures' doit être activée.
- **PR-05** — Les projets bibliothèques sont en lecture pour tous les projets ; écriture réservée aux libraryCurator / designAuthority.
- **PR-06** — Les comptes externes (client, fournisseur) n'ont accès qu'aux projets / Spaces de collaboration et jamais aux requêtes inter-projets.
- **PR-07** — Le champ exportControl ne peut être abaissé que par exportControlOfficer ; tout projet 'US 10 CFR 810' est restreint aux personnes autorisées.
- **PR-08** — Revue des habilitations semestrielle (export des rôles par projet) tracée par la Qualité.
