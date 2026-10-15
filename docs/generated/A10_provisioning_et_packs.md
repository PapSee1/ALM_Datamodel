# Annexe A10 — Provisioning des projets et packs réglementaires

> Document **généré** par `tools/generate_docs.py` depuis `model/*.yaml` — ne pas éditer à la main.

## Questionnaire de création

| # | Paramètre | Question | Valeurs | Obligatoire |
|---|---|---|---|---|
| Q01 | `projectType` | Typologie de projet | énumération [`projectType`](A2_enumerations.md#projecttype) | oui |
| Q02 | `businessUnit` | BU maître d'ouvrage | énumération [`businessUnit`](A2_enumerations.md#businessunit) | oui |
| Q03 | `businessLine` | Business Line | énumération [`businessLine`](A2_enumerations.md#businessline) |  |
| Q04 | `responsibleUnit` | UO responsable du projet | énumération [`operationalUnit`](A2_enumerations.md#operationalunit) | oui |
| Q05 | `performingUnits` | UO réalisatrices (lots de travaux prévus) | énumération [`operationalUnit`](A2_enumerations.md#operationalunit) (multiple) |  |
| Q06 | `regulatoryFrameworks` | Cadres réglementaires applicables (packs) | énumération [`regulatoryFramework`](A2_enumerations.md#regulatoryframework) (multiple) | oui |
| Q07 | `reactorTechnologies` | Filières / technologies concernées | énumération [`reactorTechnology`](A2_enumerations.md#reactortechnology) (multiple) | oui |
| Q08 | `plantSeries` | Paliers / modèles concernés (base installée) | énumération [`plantSeries`](A2_enumerations.md#plantseries) (multiple) |  |
| Q09 | `safetyClassScheme` | Référentiel de classement de sûreté du projet | énumération [`safetyClassScheme`](A2_enumerations.md#safetyclassscheme) | oui |
| Q10 | `maxClassification` | Classification maximale des données prévues | énumération [`informationClassification`](A2_enumerations.md#informationclassification) | oui |
| Q11 | `exportControl` | Contrôle export (criblage préalable) | énumération [`exportControl`](A2_enumerations.md#exportcontrol) | oui |
| Q12 | `language` | Langue contractuelle | énumération [`language`](A2_enumerations.md#language) | oui |
| Q13 | `signaturePolicy` | Politique de signature électronique (PR-10) | `roleBased` *(défaut)*, `habilitationBased` | oui |
| Q14 | `customerExchange` | Mode d'échange avec le client | `none` *(défaut)*, `pdfOnly`, `reqif`, `sas` | oui |
| Q15 | `externalParticipants` | Participants externes | `none` *(défaut)*, `customer`, `suppliers`, `partners` | oui |
| Q16 | `mbseTool` | Outil MBSE | `none` *(défaut)*, `capella`, `catiaMagic`, `other` | oui |
| Q17 | `plmSystem` | PLM de référence de la nomenclature | `none` *(défaut)*, `teamcenter`, `threeDx`, `other` | oui |
| Q18 | `tailoringScore` | Cotation de la grille de tailoring (7 critères, model/tailoring.yaml) | cotation 7 critères (A7) | oui |
| Q19 | `tailoringJustification` | Justification si la classe retenue diffère de la classe par défaut de la typologie | texte |  |

## Règles de dérivation

| # | Règle | Condition | Effet |
|---|---|---|---|
| D01 | Gabarit = gabarit par défaut de la typologie (tailoring.projectTypeDefaults) | toujours | template = projectTypeDefaults[projectType].template |
| D02 | Classe = max(classe issue de la cotation, plancher éliminatoire) ; écart à la classe par défaut → justification Q19 obligatoire et visa Qualité | toujours | projectClass = scoringGrid(tailoringScore) |
| D03 | Programme défense → instance DEF | projectType ∈ ['defenseProgram'] | instance = DEF |
| D04 | Cybersécurité d'installation → instance SENS (inventaire d'actifs numériques critiques) | projectType ∈ ['cybersecurityCompliance'] | instance = SENS |
| D05 | Données sensibles sécurité / diffusion restreinte → instance SENS | maxClassification ∈ ['sensitiveSecurity', 'restricted'] | instance = SENS |
| D06 | Contrôle export US (10 CFR 810 / 110 / EAR) → instance US | exportControl ∈ ['us810', 'us110', 'usEar'] | instance = US |
| D06bis | Potentiel scientifique et technique (PPST / ZRR) → instance SENS | exportControl ∈ ['frPpst'] | instance = SENS |
| D07 | Par défaut → instance standard | toujours | instance = STD |
| D08 | Packs réglementaires = cadres déclarés (Q06) : champs activés / masqués, bibliothèques branchées, règles additionnelles (model/regulatory_packs.yaml) | toujours | packs = regulatoryFrameworks |
| D09 | Participants externes ou échange 'sas' → création d'un projet EXT-<partenaire>-<affaire> (gabarit TPL-EXT), jamais d'accès au projet interne | externalParticipants ∈ ['customer', 'suppliers', 'partners'] | extProject = TPL-EXT |
| D10 | Plusieurs UO réalisatrices → lots de travaux activés, tableau de bord par UO, document de remise de lot | performingUnits ∈ multiple | enableTypes = ['workPackage']; enableDocuments = ['workPackageHandover'] |
| D11 | Politique 'habilitationBased' → paramètre projet signaturePolicy et condition qualifiedSignatory active ; correspondance discipline → domaine d'habilitation pré-remplie (requiredHabilitation) | signaturePolicy ∈ ['habilitationBased'] | qualifiedSignatory = active |
| D12 | Énumérations projet surchargées : tranches (plantUnit), UO (operationalUnit restreinte aux UO déclarées), Business Lines | toujours | projectEnums = ['plantUnit', 'operationalUnit', 'businessLine'] |
| D13 | Outil MBSE déclaré → connecteur correspondant activé (model/import_export.yaml) ; la présence de modelElementId sur les éléments synchronisés est contrôlée par rapport (TR, pas par le workflow) | mbseTool ∈ ['capella', 'catiaMagic'] | connectors = {'capella': 'CX-MBSE-CAPELLA', 'catiaMagic': 'CX-MBSE-CAMEO'} |
| D14 | PLM déclaré → connecteur PLM correspondant activé | plmSystem ∈ ['teamcenter', 'threeDx'] | connectors = {'teamcenter': 'CX-PLM-TC', 'threeDx': 'CX-PLM-3DX'} |

## Domaine d'habilitation par défaut selon la discipline

| Discipline | Domaine |
|---|---|
| `sur` | `safetyAnalysis` |
| `eps` | `safetyAnalysis` |
| `neu` | `coreDesign` |
| `cmb` | `coreDesign` |
| `mec` | `pressureEquipment` |
| `fab` | `welding` |
| `cnd` | `nde` |
| `icc` | `safetyIc` |
| `cyb` | `cybersecurity` |
| `rpr` | `radiationProtection` |

## Processus de provisioning

| Étape | Activité | Délai cible |
|---|---|---|
| 1 | Demande de création (chef de projet) via formulaire ; SE Referent de la BU assiste au questionnaire | J |
| 2 | Cotation de tailoring et choix de classe ; visa Qualité (et Sûreté si classe A / B ou EIP) | J+3 |
| 3 | Criblage contrôle export et classification (exportControlOfficer, securityOfficer) → instance | J+5 |
| 4 | Création automatisée (provisioningOfficer) : gabarit, paramètres, énumérations projet, groupes d'annuaire, projet sas | J+6 |
| 5 | Branchement des bibliothèques (packs) et des lignes de produits ; import des données d'entrée (ReqIF / Word) | J+10 |
| 6 | Lancement : formation ciblée des rôles, démonstration des tableaux de bord, plan de management IS | J+15 |
| 7 | Revue de démarrage à 3 mois (usage, écarts au gabarit, REX vers la Design Authority) | M+3 |

## Packs réglementaires

| Pack | Autorités | Schéma de classement | Champs affichés | Champs masqués | Types / documents imposés | Règles |
|---|---|---|---|---|---|---|
| **frAsnr** — France – INB / ESPN | asnr, dgprNotified | `frLegacy` | definedRequirement, regulatoryModificationClass, espnLevel, espnCategory, ipsLegacy, aip | cfr5059Screening, cfr5059Outcome, cfr5059Reference, part21Evaluation | — | — |
| **usNrc** — États-Unis – NRC / DOE | nrc | `usNrc` | cfr5059Screening, cfr5059Outcome, cfr5059Reference, part21Evaluation, safetyReportImpact | regulatoryModificationClass, espnLevel, espnCategory, ipsLegacy | — | TR-19 |
| **deKta** — Allemagne – AtG / KTA (services, combustible, démantèlement) | germanAuthority | `deKta` | — | cfr5059Screening, cfr5059Outcome, cfr5059Reference, espnLevel, espnCategory, ipsLegacy, regulatoryModificationClass | — | — |
| **ukOnr** — Royaume-Uni – ONR (licence de site, GDA, ALARP) | onr | `eprUk` | definedRequirement | cfr5059Screening, cfr5059Outcome, cfr5059Reference, espnLevel, espnCategory, ipsLegacy, regulatoryModificationClass | safetyClaim, safetyCase | TR-13 |
| **caCnsc** — Canada – CNSC / CSA | cnsc | `caCnsc` | — | cfr5059Screening, cfr5059Outcome, cfr5059Reference, espnLevel, espnCategory, ipsLegacy, regulatoryModificationClass | — | — |
| **intlIaea** — International – socle AIEA (export, clients sans référentiel propre) | other, customer | `iaeaSsg30` | — | cfr5059Screening, cfr5059Outcome, cfr5059Reference | — | — |
| **medicalGmp** — Pharmaceutique – bonnes pratiques de fabrication (isotopes médicaux) | healthAuthority | `other` | — | cfr5059Screening, cfr5059Outcome, cfr5059Reference, espnLevel, espnCategory, ipsLegacy | qualificationDossier | — |
| **defense** — Défense – principe seul (instance DEF) | other | `other` | — | — | — | — |

### Textes de référence — `frAsnr`

- Code de l'environnement, livre V, titre IX (régime des INB, dispositions de l'ex-décret 2007-1557 codifiées) *(confiance H)*
- Arrêté du 7 février 2012 fixant les règles générales relatives aux INB (EIP, AIP, exigences définies, écarts) *(confiance H)*
- Arrêté du 30 décembre 2015 relatif aux équipements sous pression nucléaires (ESPN) *(confiance H)*
- Décision ASN relative aux modifications notables des INB (n° 2017-DC-0616) *(confiance P)*
- Guide ASN n° 28 – qualification des outils de calcul scientifique utilisés dans la démonstration de sûreté *(confiance P)*
- Codes AFCEN RCC-M, RCC-E, RSE-M, RCC-C (références uniquement, textes sous licence) *(confiance H)*

### Textes de référence — `usNrc`

- 10 CFR 50 Appendix B – Quality assurance criteria *(confiance H)*
- 10 CFR 50.59 – Changes, tests and experiments (guide d'application NEI 96-07) *(confiance H)*
- 10 CFR Part 21 – Reporting of defects and noncompliance *(confiance H)*
- 10 CFR 50.55a – Codes and standards (ASME BPVC III / XI) *(confiance H)*
- 10 CFR 73.54 – Cyber security (RG 5.71) *(confiance H)*
- 10 CFR Part 810 (DOE) / Part 110 (NRC) – contrôle des exportations *(confiance H)*
- ASME NQA-1 – Quality assurance requirements *(confiance H)*

### Textes de référence — `deKta`

- Atomgesetz (AtG) *(confiance H)*
- Règles de sûreté KTA (Kerntechnischer Ausschuss) *(confiance H)*
- Sicherheitsanforderungen an Kernkraftwerke (SiAnf) *(confiance P)*

### Textes de référence — `ukOnr`

- ONR Safety Assessment Principles (SAPs) *(confiance H)*
- ONR Technical Assessment Guides (TAGs) *(confiance H)*
- Conditions de licence de site nucléaire (Nuclear Site Licence Conditions) *(confiance H)*

### Textes de référence — `caCnsc`

- Documents d'application de la réglementation CNSC (REGDOC) *(confiance H)*
- Normes CSA N285 / N286 / N290 / N299 (références) *(confiance P)*

### Textes de référence — `intlIaea`

- IAEA SSR-2/1 – Safety of NPPs: Design *(confiance H)*
- IAEA SSG-30 – Safety classification of SSCs *(confiance H)*
- IAEA GSR Part 2 – Leadership and management for safety (approche graduée) *(confiance H)*
- IAEA SSR-6 – Regulations for the safe transport of radioactive material *(confiance H)*

### Textes de référence — `medicalGmp`

- EudraLex vol. 4 – BPF UE, annexe 15 (qualification et validation : QI / QO / QP) *(confiance H)*
- EudraLex vol. 4 – annexe 11 (systèmes informatisés) et annexe 3 (radiopharmaceutiques) *(confiance H)*
- 21 CFR Part 11 – enregistrements et signatures électroniques (FDA) *(confiance H)*
