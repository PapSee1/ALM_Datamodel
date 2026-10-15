# 20 — Facteurs de succès du déploiement non couverts par la v0.1

> Version 0.3. Les docs 16 (feuille de route) et 17 (gouvernance) traitent la méthode de déploiement. Ce document liste ce qui manquait pour **réussir** : des sujets sociaux, juridiques, de sécurité, d'exploitation, économiques et de pérennité. Ils sont rarement portés par l'équipe projet ALM, mais ils font échouer les déploiements.
>
> Chaque facteur est rattaché à une phase de la feuille de route (doc. 16) et à un porteur. Confiance : [C] confirmé, [P] probable, [H] hypothèse.

## 1. Social et juridique

| # | Facteur | Risque s'il est ignoré | Ancrage | Action | Porteur | Phase |
|---|---|---|---|---|---|---|
| F-01 | **Consultation des instances représentatives du personnel** (CSE en France, Betriebsrat en Allemagne) | Blocage ou suspension du déploiement. L'outil trace nominativement les actions, horodatages et signatures : il peut permettre un contrôle de l'activité des salariés. | France : consultation du CSE sur l'introduction de nouvelles technologies et les moyens de contrôle de l'activité [C]. Allemagne : codécision du Betriebsrat sur les dispositifs techniques de surveillance (BetrVG § 87) [C]. | Dossier d'information-consultation dès le cadrage ; accord d'entreprise allemand (Betriebsvereinbarung) ; engagement écrit de non-usage des journaux pour l'évaluation individuelle. | DRH + DSI + Design Authority | Cadrage (chemin critique) |
| F-02 | **Protection des données personnelles** | Non-conformité RGPD ; refus du DPO | RGPD : registre des traitements (art. 30), analyse d'impact si traitement à risque (art. 35) [C] | Fiche de registre ; analyse d'impact (AIPD) sur journaux, signatures et habilitations ; durées de conservation alignées sur l'archivage des AIP | DPO | Cadrage |
| F-03 | **Protection du potentiel scientifique et technique (PPST / ZRR)** | Accès d'un ressortissant non autorisé à des informations protégées | Dispositif PPST, zones à régime restrictif [C] | Option d'énumération `frPpst` ; habilitations d'accès par projet ; règle de provisioning (instance ou projet dédié) ; revue des comptes externes (PR-11) | Sécurité / FSD | Fondations |
| F-04 | **Licences des normes** (IEC, ISO, AFCEN, ASME, IEEE) | Contrefaçon si le texte intégral est chargé dans les bibliothèques | Droit d'auteur (ADR-14) [C] | Références et paraphrases par défaut ; contrats de licence « intranet » avant tout chargement intégral ; champ `copyrightRestricted` | Juridique + documentation | Fondations |
| F-05 | **Valeur probante des signatures électroniques** auprès des clients et des autorités | Refus d'un livrable signé électroniquement ; double circuit papier persistant | Signature électronique simple au sens eIDAS [P] ; exigences contractuelles client ; 21 CFR 11 pour les BPF [C] | Accord écrit avec les principaux clients (dont l'exploitant français) sur la recevabilité des PDF signés + manifeste ; présentation du dispositif à l'autorité avant les pilotes | Qualité + licensing | Cadrage → pilotes |

## 2. Sécurité et conformité de la plateforme

| # | Facteur | Risque | Ancrage | Action | Porteur | Phase |
|---|---|---|---|---|---|---|
| F-06 | **Cybersécurité de la plateforme ALM elle-même** | Compromission de la démonstration de sûreté ; arrêt d'activité | Directive NIS2 et sa transposition (statut d'entité essentielle probable) [P] ; doctrine de l'ANSSI [C] | Homologation de sécurité de chaque instance ; durcissement ; supervision SOC ; tests d'intrusion avant ouverture aux externes | RSSI | Fondations |
| F-07 | **Validation du système informatisé** (support d'AIP, et BPF pour la santé) | Enregistrements non recevables | Arrêté INB (AIP) ; EudraLex annexe 11 / 21 CFR 11 pour le pack `medicalGmp` [C] | Dossier IQ / OQ / PQ (doc. 15) ; requalification à chaque montée de version et à chaque évolution du modèle (la CI fournit la liste des changements) | Qualité + DSI | Fondations, puis en continu |
| F-08 | **Contrôle export et ségrégation des instances** | Infraction export (US 10 CFR 810, double usage UE) | ADR-03 ; règles de provisioning D05 / D06 [C] | Criblage avant création (étape 3 du provisioning) ; filtres d'export ReqIF (XC-01) | Contrôle export | Cadrage |

## 3. Qualité, réglementaire et processus

| # | Facteur | Risque | Ancrage | Action | Porteur | Phase |
|---|---|---|---|---|---|---|
| F-09 | **Mise à jour du système de management** (procédures, modes opératoires, plans qualité) | Deux référentiels contradictoires : l'outil impose un workflow, la procédure en décrit un autre | ISO 19443 / ISO 9001 § 7.5 [C] | Chaque workflow du modèle devient la référence d'une procédure ; les procédures renvoient aux annexes générées A4 / A6 ; revue Qualité dans le CCB du modèle | Qualité | Fondations → chaque vague |
| F-10 | **Acceptation des échanges ReqIF et des tableaux de bord par les clients** | Le client continue d'exiger des matrices Excel ; double saisie | Pratiques contractuelles [H] | Profils ReqIF validés avec chaque client majeur (doc. 22) ; clause contractuelle de format d'échange dans les nouveaux contrats | Chefs de projet + achats | Pilotes |
| F-11 | **Interopérabilité avec les programmes de transformation numérique des clients** (ex. programme d'ingénierie numérique de l'exploitant français) | Formats incompatibles ; ressaisie | Annonces publiques de l'exploitant [P] | Groupe de travail bilatéral ; ReqIF + identifiants pivots ; aucune hypothèse d'outil client figée dans le modèle | Design Authority | Cadrage → vague 1 |

## 4. Exploitation et continuité

| # | Facteur | Risque | Ancrage | Action | Porteur | Phase |
|---|---|---|---|---|---|---|
| F-12 | **Accès terrain et mode dégradé en arrêt de tranche** | Fortuit traité hors outil faute d'accès réseau en zone contrôlée ; perte de traçabilité | Contraintes des sites nucléaires (réseaux, matériels admis en zone) [P] | Aller-retour Excel `XL-FIELD-CAPTURE` ; procédure de saisie différée avec horodatage d'origine ; postes autorisés en bureau de site | BU Base installée | Pilotes |
| F-13 | **Calendrier des arrêts de tranche** | Mise en production ou montée de version pendant un pic d'arrêts : indisponibilité sur le chemin critique | Les arrêts du parc sont concentrés hors période de forte demande hivernale [P] | Périodes de gel des mises en production ; astreinte renforcée pendant les campagnes d'arrêts ; montées de version programmées en conséquence | Exploitation ALM | Industrialisation |
| F-14 | **Continuité de service et réversibilité** | Indisponibilité prolongée ; dépendance à l'éditeur sur plus de 60 ans | Durée de vie des installations ; archivage de référence en GED (ADR-11) [C] | PRA / PCA testés ; exports périodiques ReqIF + PDF/A ; plan de sortie documenté (formats ouverts, modèle « as code » indépendant de l'outil) | DSI | Fondations |
| F-15 | **Pérennité des données sur plus de 60 ans** | Données illisibles après plusieurs générations d'outils | Archivage numérique (modèle OAIS, ISO 14721) [C] | La GED reste l'archive de référence ; manifeste de signatures ; le dépôt du modèle documente la sémantique de chaque champ | Documentation + DSI | En continu |
| F-16 | **Coexistence et migration** (Word, Excel, outils d'exigences existants) | Deux sources de vérité pendant des années | ADR-23 [C] | Règle « une affaire = un outil » ; import ciblé (doc. 22) ; date de gel de l'ancien outil par BU | Design Authority + BU | Vagues |
| F-17 | **Performances et volumétrie** | Lenteur et rejet par les utilisateurs | Volumétrie d'un grand projet (plus de 100 000 éléments) [H] | Tirs de charge sur données synthétiques générées depuis les scénarios A9 ; seuils de réponse contractualisés avec l'hébergeur | DSI | Fondations |

## 5. Humain et compétences

| # | Facteur | Risque | Ancrage | Action | Porteur | Phase |
|---|---|---|---|---|---|---|
| F-18 | **Référentiel des habilitations nominatives** | La politique `habilitationBased` est inapplicable sans source de vérité des habilitations | ISO 19443 § 7.2 [C] | Référentiel RH-compétences synchronisé en groupes `HAB-<domaine>-<niveau>` ; administrateur des habilitations (rôle global) ; revue semestrielle | RH + Qualité | Fondations |
| F-19 | **Centre de compétences et contribution interne** (scripts, rapports, gabarits) | Développements dispersés, non qualifiés | ADR-16 [C] | Centre de compétences ALM ; dépôt unique des scripts sous revue (modèle de contribution interne) ; qualification des scripts comme la configuration | Design Authority | Industrialisation |
| F-20 | **Formation par rôle et accompagnement des non-spécialistes IS** | Usage minimal (« Word dans Polarion ») ; données pauvres | Cible : accessibilité « au plus grand nombre » [H] | Parcours par rôle (A6) ; gabarits de LiveDocs proches des documents connus ; champions par UO ; aide contextuelle dans les gabarits | Conduite du changement | Pilotes → vagues |
| F-21 | **Transition des gabarits IS existants** (kits de gabarits Word / Excel) | Rejet si les nouveaux gabarits s'écartent sans raison des formats éprouvés | Pratique interne [H] | Correspondance gabarit existant → LiveDoc (doc. 12) ; conservation des plans types ; retrait progressif des anciens gabarits | SE Referents | Fondations |

## 6. Écosystème : fournisseurs et partenaires

| # | Facteur | Risque | Ancrage | Action | Porteur | Phase |
|---|---|---|---|---|---|---|
| F-22 | **Intégration des fournisseurs** | Fournisseurs incapables de répondre en ReqIF ou dans un projet sas | Chaîne d'approvisionnement nucléaire (CFSI, surveillance) [C] | Kit fournisseur (profil ReqIF, gabarit Excel `XL-SUPPLIER`, guide) ; licences REVIEWER / PRO dans les projets `EXT-*` ; clause contractuelle | Achats + qualité fournisseurs | Vague 1 |
| F-23 | **Modèle économique des licences** | Coût prohibitif d'un déploiement « tout ALM » | ADR-18 [C] | Profilage des licences par rôle (A6) ; licences REVIEWER pour vérificateurs, approbateurs et clients ; revue trimestrielle d'usage | DSI + achats | Cadrage |

## 7. Pilotage de la valeur

| # | Facteur | Risque | Ancrage | Action | Porteur | Phase |
|---|---|---|---|---|---|---|
| F-24 | **Mesure de maturité IS initiale et cible** | Impossible de démontrer le gain ; perte du sponsor | SECM / EIA-731 ; INCOSE MBCM [C] | Évaluation de maturité au cadrage, cible niveau 3 (« défini ») ; réévaluation à la fin de chaque vague | Design Authority | Cadrage, fin de vague |
| F-25 | **Indicateurs de valeur** | Le déploiement est jugé sur son coût | Doc. 13 [C] | Indicateurs : délai de réponse fortuit, taux de couverture des exigences définies, coût de non-qualité lié aux exigences, nombre de remarques client par livrable, délai de bouclage CCB, part d'échanges ReqIF vs ressaisie | PMO | Pilotes → vagues |
| F-26 | **Processus de provisioning** | Projets créés hors gabarit, configuration divergente | Doc. 21 [C] | Guichet unique, questionnaire, règles de dérivation (`project_setup.yaml`) ; aucun administrateur de projet ne crée de projet | Design Authority | Fondations |

## 8. Intégration à la feuille de route (doc. 16)

| Phase | Facteurs à traiter avant la sortie de phase |
|---|---|
| Cadrage | F-01, F-02, F-05 (amorce), F-08, F-11, F-23, F-24 |
| Fondations | F-03, F-04, F-06, F-07, F-09, F-14, F-17, F-18, F-21, F-26 |
| Pilotes | F-05 (accord client), F-10, F-12, F-20, F-25 |
| Industrialisation | F-13, F-19 |
| Vagues | F-16, F-22 ; réévaluation F-24 |
| En continu | F-07, F-15 |

**Chemin critique :** F-01 (instances représentatives) et F-07 (validation du système) conditionnent l'ouverture des pilotes à des données réelles. Démarrées tard, elles décalent l'ensemble du programme.
