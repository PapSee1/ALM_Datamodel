# Partie 1.1 — Organisation et périmètres : BU, BL, UO, filiales et écosystème

> **Statut** : cartographie OSINT, état octobre 2026. Chaque fait porte un niveau de confiance :
> **[C]** confirmé (source officielle ou ≥ 2 sources concordantes) · **[P]** probable (1 source crédible ou sources divergentes) · **[H]** hypothèse de modélisation à valider en atelier interne.
> Les sources sont listées en [Annexe C](../annexes/C_Sources_OSINT.md). Aucune donnée interne n'a été utilisée.

## 1. Identité de l'entreprise (éléments structurants pour l'ALM)

| Élément | Constat OSINT | Conf. | Conséquence pour le déploiement Polarion |
|---|---|---|---|
| Actionnariat | EDF 80,5 %, Mitsubishi Heavy Industries 19,5 %. Assystem a cédé ses 5 % à EDF en janvier 2024. Les « boilerplates » de certains communiqués 2025 sont périmés. | C | Le premier client (EDF) est aussi l'actionnaire majoritaire. Les flux de données avec EDF et ses filiales (Edvance) sont massifs. Prévoir des échanges ReqIF industrialisés et des espaces de collaboration. |
| Siège | Courbevoie (Paris-La Défense) | C | Hébergement primaire en France (souveraineté, contrôle export). |
| Taille | CA 2025 : 5 399 M€ (+15,5 % organique), prises de commandes 5 924 M€, EBITDA 665 M€. Plus de 22 000 salariés, plus de 70 sites, plus de 20 pays (chiffres variables selon les pages). | C/P | Dimensionnement : plusieurs milliers d'utilisateurs nommés potentiels. Licences mixtes (nommées + concurrentes + REVIEWER). Cluster Polarion. |
| Implantations majeures | France (≈ 7 500 à 15 000 selon la page), Allemagne (≈ 3 000, dont ≈ 2 200 à Erlangen), États-Unis (≈ 2 400, 10 sites), Royaume-Uni (≈ 350, 4 sites), Chine, Canada, Inde (hub Navi Mumbai) [P] | C/P | Multi-juridiction : export control UE/FR/DE/US, RGPD, résidence des données. Voir ADR-03 (instances). |
| Gouvernance | Conseil de surveillance et Comité exécutif. Direction générale renouvelée en 2025. | C | Sponsor exécutif à positionner au niveau du Comex (transformation transverse). |

## 2. Business Units (BU) publiées

L'organisation publiée (page *Governance*, communiqués 2024-2026) fait apparaître **quatre BU opérationnelles** et une direction technique transverse, plus des marques hors électronucléaire.

| BU (id modèle) | Périmètre public | Sites / entités clés | Conf. | Typologies de projets portées (`projectType`) |
|---|---|---|---|---|
| **Base installée** (`ib`) | Services et maintenance du parc (arrêts de tranche), remplacement de gros composants (maître d'œuvre des RGV), inspection en service (dont la machine d'inspection de cuve, plus de 350 cuves inspectées), outillages et robotique, ingénierie de la base installée. Intercontrôle (Rungis) y est rattachée [P]. | Lyon, Paris-La Défense, Rungis (Intercontrôle), Maubeuge (ex-SOMANU, ICPE depuis 2018) [P], États-Unis, Royaume-Uni, Afrique du Sud (Koeberg) | C | `steamGeneratorReplacement`, `periodicSafetyReview`, `plantModification`, `fortuit`, `specialTooling`, `inspectionService`, `icRefurbishment` (avec ICS) |
| **Combustible & excellence opérationnelle** (`fuel`) | Conception, licensing et fabrication d'assemblages REP/REB/VVER, combustibles ATF (GAIA + PROtect E-ATF), combustible et cibles de réacteurs de recherche (CERCA), filière zirconium, études de cœur et recharges. | Romans-sur-Isère (REP + CERCA), filière Zr (Jarrie, Ugine, Rugles, Montreuil-Juigné, Paimboeuf), Lingen (ANF, D), Karlstein (D), Richland (US) | C | `fuelDesign`, `fuelReload`, `componentManufacturing` (gaines, structures) |
| **Contrôle-commande** (`ics`) | Systèmes de C-C de sûreté (plateformes TELEPERM XS, ex-Rolls-Royce Spinline/Rodline/Hardline, ex-Schneider Tricon/SPEC 200), instrumentation nucléaire et de terrain, rénovations, **BL Cybersécurité** (Cyberwatch, FoxGuard, Allentis). Organisation interne publiée en « pilier EPR/SMR » + centre de compétences « ingénierie transverse » (Grenoble) [P]. | Erlangen (D), Grenoble (ex-RR), Lyon, Lachine (CA) [P], Chine | C | `icPlatform`, `icApplication`, `icRefurbishment` |
| **Projets & fabrication de composants (PCM)** (`pcm`) | Grands projets (EPR2 : conception, fabrication, montage et mise en service du circuit primaire pour 6 tranches + 6 systèmes d'instrumentation nucléaire et C-C de sûreté ; HPC ; SZC) et usines de gros composants. Dénomination « Large Projects » jusqu'en 2019, « PCM » depuis 2020. | Saint-Marcel (cuves, GV), Le Creusot (forge, internes ; nouvel atelier internes EPR2 en 2026), Jeumont (pompes primaires, mécanismes de grappes), Montbard (tubes GV) | C | `newBuildLarge`, `componentDesign`, `componentManufacturing` |
| **Direction technique & ingénierie (DTI)** (`dti`) | Développement, conception et licensing des chaudières. Basée à La Défense, antenne mécanique à Saint-Marcel [P]. | Paris-La Défense, Saint-Marcel, Lyon | P | `newBuildSmr`, `newBuildLarge` (conception), `rdProgram`, appui à `periodicSafetyReview` |
| **BL Robinetterie** (`valves`, au niveau BL) | Nouvelle business line (2024-2026) issue d'acquisitions : Sebim (soupapes), Valserve (ex-Velan SAS), Vanatome, Segault (avec TechnicAtome, 70/30). BU de rattachement non trouvée. | Divers sites FR | C (existence) / NT (rattachement) | `componentDesign`, `componentManufacturing` |
| Marques hors électronucléaire | **Framatome Healthcare** (Lu-177, Yb-176, Cernavodă, Bruce Power via Isogen ; At-211 avec IBA), **Framatome Space** (vers 2023 ; Am-241 pour l'ESA), **Framatome Defense** (octobre 2020 ; Le Creusot, Jeumont). | Erlangen, Romans, Le Creusot, Jeumont | C/P | Hors vague 1. **Defense : instance séparée si informations protégées** (ADR-03). |

> **[H] Hypothèse de modélisation.** Le niveau « Unité opérationnelle (UO) » n'est pas publié. Le modèle prévoit l'énumération `businessLine` (portée projet). Elle est amorcée par les sources publiques et doit être complétée en atelier avec l'organigramme interne, sans jamais coder l'organigramme nominatif dans l'outil.

### 2.1 Business Lines et unités opérationnelles (amorce)

| BU | BL / UO identifiées publiquement ou déduites | Conf. | Activité SE dominante |
|---|---|---|---|
| Base installée | Services d'arrêts de tranche ; gros composants (RGV) ; inspection / CND (Intercontrôle) ; ingénierie de la base installée (modifications, justifications, réexamens) ; outillages et robotique | P/H | Cycles courts, justification technique, interfaces avec l'existant, RP/ALARA, requalification |
| Combustible | Conception et licensing ; études de cœur et recharges ; fabrication (Romans, Lingen, Richland) ; filière zirconium ; CERCA | P | Critères de conception, qualification (assemblages précurseurs), dossiers de licensing multi-pays, recharges récurrentes |
| Contrôle-commande | Systèmes de sûreté (plateformes qualifiées) ; instrumentation ; cybersécurité ; projets (application / rénovation) | P | Cycle IEC 61513, logiciel IEC 60880/62138, V&V indépendante, FAT/SAT, cybersécurité IEC 62645 |
| PCM | Grands projets (EPR2, HPC, SZC) ; gros composants (Saint-Marcel, Le Creusot) ; pompes et mécanismes (Jeumont) | P | Conception RCC-M, ESPN N1, fabrication avec points d'arrêt, FNC/dérogations, dossiers de fin de fabrication |
| DTI | Conception et licensing chaudière ; sûreté ; méthodes et codes de calcul | P/H | Démonstration de sûreté, classement, études d'accidents, MBSE |

## 3. Filiales, coentreprises et entités partenaires

| Entité | Nature | Conf. | Impact ALM |
|---|---|---|---|
| **Framatome GmbH** (Erlangen) | Filiale allemande (≈ 3 000 pers.) : ingénierie, C-C (TXS), combustible | C | Instance STD partagée France/Allemagne (UE) ; contrôle export allemand AWG/AWV (`deAwg`). |
| **Framatome Inc.** (Lynchburg ; Richland) | Filiale US : services, combustible, C-C (Tricon, TXS Compact approuvé NRC) | C | Exigences NQA-1 / 10 CFR 50 App. B / Part 21 / Part 810 → **instance US probable** (ADR-03). |
| **Advanced Nuclear Fuels (ANF)**, Lingen | Fabrication d'assemblages. Autorisation VVER-1000 sous licence TVEL délivrée par la Basse-Saxe le 22/07/2026, sous conditions strictes (isolement des logiciels russes, accès restreint) | C | Projets VVER cloisonnés : droits d'accès stricts, aucune interface automatique avec des systèmes tiers non maîtrisés. |
| **European Hexagonal Fuel SAS** | Coentreprise 75/25 avec TVEL (licence de combustible VVER) | P | Données de licence tierces : classification `customerConfidential`, cloisonnement. |
| **Intercontrôle** (Rungis) | Filiale à 100 % : inspection, CND, machine d'inspection de cuve | C | Projets `inspectionService` : qualification des procédés CND (RSE-M, ASME), exigences outillage. |
| **CERCA** (Romans) | Combustible de réacteurs de recherche et cibles médicales (nouvel atelier en 2025) | C | Typologie spécifique (réacteurs de recherche, `researchReactor`). |
| **Jeumont Electric** | Acquise en 2024 avec Naval Group | C | Interfaces défense → classification et cloisonnement. |
| **Sebim, Valserve, Vanatome, Segault** | BL Robinetterie | C/P | Composants ESPN : FNC/dérogations, fabrication. |
| **Cyberwatch, FoxGuard, Allentis** | BL Cybersécurité (C-C) | C | Les exigences de sécurité (IEC 62645 / 63096) et les données de vulnérabilité sont sensibles : classification. |
| **Edvance** | Coentreprise EDF 80 % / Framatome 20 % (2017) : ingénierie de l'îlot nucléaire et du C-C des nouveaux réacteurs (FA3, HPC, SZC, EPR2, NUWARD). Salariés Framatome mis à disposition. Réorganisation de gouvernance en 2026 [P]. Framatome annonce en 2026 une « intégration complète de l'îlot nucléaire » EPR2 [P, une seule source]. | C/P | **Frontière ALM critique** : comptes à double appartenance, droits par projet, échanges ReqIF avec l'architecte-ensemblier, propriété des exigences à clarifier (ADR-12). |
| **Isogen** (avec Kinectrics) | Production de Lu-177 en réacteurs CANDU | C | Hors vague 1. |
| **Reaktortest** (Slovaquie), **BHR Group** (UK) | Filiales | P | Hors vague 1. |

## 4. Écosystème externe structurant

| Acteur | Rôle vis-à-vis de Framatome | Conf. | Impact sur le modèle |
|---|---|---|---|
| **EDF** (exploitant, licensee) | Client principal du parc (56 + 1 réacteurs) et des nouveaux réacteurs ; programme numérique **SWITCH** (Dassault Systèmes 3DEXPERIENCE pour le PLM depuis 2018, avec Capgemini ; AVEVA E3D / Unified Engineering depuis 2021) | C | `customerVisa`, `customerApprovalRequired`, `regulatoryModificationClass` (qualification par l'exploitant), interopérabilité ReqIF / 3DEXPERIENCE |
| **ASNR** (Autorité de sûreté nucléaire et de radioprotection, créée le 01/01/2025 par fusion ASN + IRSN, loi 2024-450) | Autorité de contrôle ; inspections des fabricants ESPN ; instruction des dossiers | C | `authority = asnr`, `regulatoryCommitment`, lettres de suite (demandes) |
| Organismes agréés ESPN | Évaluation de conformité N2/N3 (agrément décision 2020-DC-0688, ISO/CEI 17020) ; N1 par l'ASNR ou ses mandataires | C | `witnessParty = notifiedBody`, points d'arrêt (H) |
| Exploitants étrangers | TVO (OL3), NNB GenCo (HPC), SZC (Sizewell C), Eskom (Koeberg), ČEZ (Temelín), Vattenfall (Ringhals), KKG (Gösgen), Slovenské elektrárne… | C | Juridictions multiples (`region`), autorités (`authority`), langues |
| Autorités étrangères | ONR (UK), NRC (US), STUK (FI), SÚJB (CZ), autorités allemandes | C | Exigences de *safety case* CAE (ONR) → `safetyClaim` ; Part 21 (US) → `part21Evaluation` |
| Partenaires constructeurs | Arabelle Solutions (îlot conventionnel, groupe EDF), génie civil, Eviden/Schneider (C-C non classé EPR2) | C | `interfaceScope = partnerOem` |
| Fournisseurs (dont gros forgés, Manoir France, participation minoritaire en 2026) | Chaîne d'approvisionnement ESPN | C/P | `supplierContributor`, CFSI, surveillance (`actionType = surveillance`) |

## 5. Environnement d'outillage d'ingénierie (OSINT)

| Constat public | Conf. | Conséquence d'architecture |
|---|---|---|
| Framatome déploie un « **Core Model** » intégrant l'**ingénierie système et le PLM sur 3DEXPERIENCE** (Dassault Systèmes), avec des interfaces MES/ERP. Au Creusot, la traçabilité des exigences est affichée « du cahier des charges aux preuves de fabrication » (offres d'emploi 2026). | C | **Décision structurante (ADR-07).** Le périmètre de Polarion doit être délimité sans doublon avec le Core Model. Polarion porte les exigences, la V&V, la démonstration, les écarts d'ingénierie et la gestion de configuration documentaire. 3DEXPERIENCE porte la définition produit (BOM, CAO), la fabrication et les preuves de fabrication. Les deux sont reliés par des identifiants pivots (`plmItemId`) et OSLC/REST. |
| **Capella / Arcadia** utilisé sur les grands projets, avec intégration PLM ; outil maison d'échanges Capella–Excel présenté au Capella Day 2019 ; article INCOSE IS2018 (avec Thales). | C | MBSE Capella = maître de l'architecture (ADR-08) ; synchronisation vers Polarion (patron open source *capella2polarion*). |
| C-C : outil **SPACE** (édition des diagrammes fonctionnels TXS, génération de code) et **SIVAT** (validation par simulation). | C | Traçabilité exigences logicielles → diagrammes fonctionnels par ID (`modelElementId`) ; preuves V&V SIVAT en `evidenceReference`. |
| Aucune mention publique de DOORS, Polarion, Cameo ou Teamcenter chez Framatome. | NT | Inventaire interne de l'existant à mener (Partie 2, Q-ARCH-01). Hypothèse « greenfield » confirmée par la demande. |

## 6. Matrice BU × typologies × classes de tailoring (synthèse)

| Typologie (`projectType`) | IB | FUEL | ICS | PCM | DTI | Classe par défaut |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Nouveau nucléaire grand réacteur (EPR2, HPC, SZC) |  | ● | ● | ●● | ● | A |
| SMR NUWARD |  | ● | ● | ● | ●● | A |
| RGV / SGR | ●● |  |  | ● |  | B |
| Réexamen périodique / VD | ●● |  | ● |  | ● | B |
| Modification base installée | ●● |  | ● |  | ● | C |
| Fortuit | ●● |  |  |  |  | D |
| Outillage spécial / service d'inspection | ●● |  |  |  |  | C |
| Conception combustible (dont ATF) |  | ●● |  |  |  | A |
| Recharges |  | ●● |  |  |  | C |
| Plateforme C-C |  |  | ●● |  |  | A |
| Projet / rénovation C-C | ● |  | ●● |  |  | B |
| Conception / fabrication de composants |  |  |  | ●● | ● | B / C |
| R&D |  | ● | ● | ● | ●● | C |

●● = BU pilote ; ● = BU contributrice.

## 7. Ce que l'organisation impose au modèle Polarion

1. **Propriété par BU, réutilisation transverse.** Chaque projet appartient à une BU (champ projet + groupe de projets). Les bibliothèques (réglementaire, terminologie, agressions, cas V&V) sont transverses, sous la responsabilité de la Design Authority ALM.
2. **Multi-entités juridiques.** France, Allemagne, États-Unis et Royaume-Uni ont des obligations différentes : contrôle export, assurance qualité (ISO 19443 vs NQA-1), signalement des défauts (Part 21). D'où les champs `region`, `exportControl` et `qaProgramLevel`, et la décision ADR-03 sur les instances.
3. **Coentreprises et mise à disposition.** Des comptes ont une double appartenance (Framatome / Edvance), et il existe des projets partagés avec EDF. Les droits sont accordés par projet via des groupes d'annuaire, jamais globalement. Les échanges avec un partenaire passent par des espaces de collaboration ou par ReqIF.
4. **Réorganisations fréquentes.** BL Valves et Cybersécurité ont été créées en 2024-2025, et les BU renommées en 2019-2020. L'organisation ne doit donc **jamais** être codée dans les identifiants de projet ou de type. Elle vit dans des énumérations (`businessUnit`, `businessLine`) révisables sans migration.
5. **Activités sensibles** (défense, sécurité nucléaire, VVER sous licence tierce). Elles sont cloisonnées par instance ou par projet, avec une classification obligatoire (`informationClassification`).
6. **Héritage du Creusot** (irrégularités découvertes en 2016 : environ 430 « dossiers barrés », revue d'environ 6 000 dossiers, reprise de la production autorisée en 2018 sous conditions ; dispositif CFSI de l'ASN, puis de l'ASNR). Exigence forte d'**intégrité des données** : piste d'audit, signatures, baselines figées, absence de suppression, champ `cfsiSuspected`. Voir le document 15.
7. **Organisation matricielle BU × UO** (v0.3). Une BU pilote, des UO réalisent. Elle est représentée par des lots de travaux (`workPackage`) et par les attributs `responsibleUnit` / `performingUnit`, et non par un projet par UO (ADR-24, doc. 21). L'énumération `operationalUnit` n'est qu'une amorce de sites publics, à remplacer par le référentiel interne (Q-ORG-01).
