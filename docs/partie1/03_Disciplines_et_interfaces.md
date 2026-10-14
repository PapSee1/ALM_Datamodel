# Partie 1.3 — Disciplines d'ingénierie et interfaces

> Les codes de discipline correspondent à l'énumération `discipline` ([Annexe A2](../generated/A2_enumerations.md#discipline)). Les normes citées sont détaillées au [document 04](04_Referentiels_normatifs_reglementaires.md).

## 1. Catalogue des disciplines

| Code | Discipline | Mission dans le cycle de vie | Artefacts Polarion dominants | Référentiels clés | Données d'interface produites |
|---|---|---|---|---|---|
| SYS | Ingénierie système & architecture | Besoin, architecture RFLP, allocation, gestion des interfaces, intégration, cohérence | `stakeholderRequirement`, `systemRequirement`, `function`, `logicalComponent`, `interface`, `designDecision` | ISO/IEC/IEEE 15288, 29148, 42010 ; INCOSE | Architecture, allocations, ICD |
| SUR | Sûreté nucléaire (déterministe) | Démonstration de sûreté, études d'accidents, classement, défense en profondeur | `safetyRequirement`, `hazard`, `safetyClaim`, `analysis`, `classificationList` | Arrêté INB, guide ASN 22, SSR-2/1, SSG-30 | Classement, exigences de sûreté, hypothèses d'études |
| EPS | Études probabilistes | EPS niveaux 1 et 2, objectifs probabilistes, contributeurs | `analysis` (psa), `designParameter` (fréquences) | SSG-3/SSG-4 (AIEA) | Exigences de fiabilité, contributeurs dominants |
| AGR | Agressions internes et externes | Incendie, inondation, explosion, projectiles, séisme, climat, chute d'avion | `hazard`, `analysis`, `safetyRequirement` | RCC-F, guides AIEA agressions | Zones de feu, sectorisation, exigences de séparation |
| NEU | Neutronique / physique du cœur | Conception de cœur, recharges, paramètres de sûreté | `designParameter` (coreParameter), `analysis` (neutronic) | SSG-52 ; méthodes qualifiées | Paramètres de cœur, puissances, coefficients |
| THY | Thermohydraulique | Transitoires, marges (ébullition critique), dimensionnement des circuits | `analysis`, `designParameter` | Codes qualifiés | Conditions de fonctionnement, sollicitations thermiques |
| CMB | Conception et mécanique combustible | Assemblage, crayon, critères de conception | `equipmentRequirement` (designCriterion), `analysis` (fuelThermomechanical) | RCC-C | Données assemblage, limites |
| MEC | Mécanique & calculs | Cuve, GV, pressuriseur, tuyauteries, supports, internes ; analyses RCC-M / ASME | `equipmentRequirement`, `analysis` (mechanicalStress, fatigue, fractureMechanics) | RCC-M 2024, RSE-M 2024, ASME III / XI, ESPN | Charges, efforts aux ancrages, encombrements, transitoires de dimensionnement |
| MAT | Matériaux, métallurgie, chimie | Choix de matériaux, chimie de l'eau, vieillissement | `equipmentRequirement` (materials), `analysis` (chemistry) | RCC-M (partie M) | Spécifications matériaux, mécanismes de vieillissement |
| PRO | Procédés / systèmes fluides | Schémas de procédé, dimensionnement des systèmes élémentaires | `function`, `logicalComponent`, `systemRequirement`, `designParameter` | Codes procédés | Débits, pressions, températures, listes de matériels |
| HVA | Ventilation / HVAC | Confinement dynamique, conditions d'ambiance | `systemRequirement`, `analysis` (hvacStudy) | Normes ventilation nucléaire | Ambiances, charges thermiques |
| ELE | Électricité | Distribution, alimentations secourues, bilans | `systemRequirement`, `analysis` (electricalStudy) | RCC-E 2025, IEC | Bilans de puissance, classement électrique, alimentations |
| ICC | Contrôle-commande | Architecture C-C, systèmes, logiciel, matériel, HDL | `function` (catégories A/B/C), `softwareRequirement`, `hardwareRequirement`, `verificationCase` | IEC 61513 éd. 3 (2026), 61226, 60880, 62138, 60987, 62566, 62340, 60709 | Listes de signaux, seuils, temps de réponse, logiques |
| CYB | Cybersécurité | Analyse de risques, degrés de sécurité, mesures | `analysis` (cyberRisk), `systemRequirement` (cybersecurity) | IEC 62645, 63096, 62859 ; NSS 17-T | Zones et degrés de sécurité, flux autorisés |
| GCV | Génie civil & structures | Bâtiments, ancrages, traversées, enceinte | `systemRequirement`, `analysis` (structural) | RCC-CW 2025 / ETC-C | Spectres de plancher, charges admissibles, réservations |
| SIS | Sismique & dynamique | Séisme de dimensionnement, spectres, qualification sismique | `analysis` (seismic), `verificationCase` | IEC/IEEE 60980-344 | Spectres, classement sismique |
| RPR | Radioprotection | Zonage, protections biologiques, ALARA, dosimétrie d'intervention | `analysis` (radiological, doseAlara), `operationalScenario.doseEstimate` | Code du travail (RP), guides | Débits de dose, objectifs de dose, zonage |
| FOH | Facteurs organisationnels & humains | Analyse des tâches, IHM, salle de commande, validation intégrée | `analysis` (humanFactors), `function` (hmi), `verificationCase` (validation) | SSG-51, IEC 60964, IEC 61772 | Allocation homme / machine, exigences IHM |
| ENV | Environnement | Rejets, déchets, impact | `systemRequirement` (environment), `analysis` | Code de l'environnement | Limites de rejets, volumes de déchets |
| FAB | Fabrication, soudage | Fabricabilité, procédés spéciaux, qualification des modes opératoires | `equipmentRequirement` (manufacturability), `verificationCase` (manufacturing) | RCC-M parties F / S | Contraintes de fabrication, séquences |
| CND | Contrôles non destructifs / inspection | Inspectabilité, qualification des procédés, inspection en service | `verificationCase` (inService), `systemRequirement` (inspectability) | RSE-M, ASME XI | Accessibilité, zones à contrôler |
| QMT | Qualification des matériels | Conditions K1 / K2 / K3, séisme, CEM, vieillissement | `verificationCase` (qualificationTest), `physicalComponent.qualificationStatus` | IEC/IEEE 60780-323, 60980-344, IEC 62003 | Programmes et statuts de qualification |
| ESS | Essais & mise en service | Programmes d'essais, procédures, PV | `verificationCase`, Test Runs, `testProcedure` | Règles d'essais | Prérequis d'essais, configurations |
| SDF | Sûreté de fonctionnement | Fiabilité, disponibilité, maintenabilité, AMDEC | `fmeaItem`, `analysis` (reliability) | IEC 60812, IEC 61025 | Taux de défaillance, modes communs |
| MNT | Maintenance, soutien logistique intégré, exploitabilité | Maintenabilité, documentation d'exploitation | `systemRequirement` (maintainability, operability) | — | Exigences de maintenance, pièces de rechange |
| OUT | Outillages, mécatronique, robotique, manutention | Conception de machines et d'outillages, levage | `function` (toolFunction), `hazard` (machinery), `fmeaItem` (intervention) | Règlement (UE) 2023/1230, EN ISO 12100, NF EN 16271 | Encombrements, interfaces avec l'installation, séquences |
| LAY | Implantation / CAO 3D | Implantation des matériels, cheminements | `interface` (layout) | — (maître dans 3DEXPERIENCE / AVEVA) | Réservations, accès |
| SEC | Sécurité nucléaire (malveillance) | Protection physique | **Instance SENS uniquement** | Code de la défense | — |
| CFG | Gestion de configuration | Identification, maîtrise des modifications, baselines, audits | `changeRequest`, baselines, collections | ISO 10007:2017, EIA-649 | État de configuration |
| QAL | Qualité / surveillance | Surveillance des AIP, des intervenants extérieurs et des fournisseurs ; FNC ; CAPA | `nonConformance`, `action` (surveillance) | Arrêté INB (titre II), ISO 19443, NQA-1 | Écarts, actions |
| PMO | Management de projet | Planification, risques, revues | `risk`, `review`, `action`, Plans | ISO 21500 | Jalons |
| ACH | Achats / chaîne d'approvisionnement | Spécifications d'approvisionnement, surveillance des fournisseurs | `equipmentSpec`, `deliverable` | ISO 19443 (CFSI) | Commandes, fournisseurs |
| LIC | Licensing / relations avec les autorités | Dossiers réglementaires, engagements, réponses | `regulatoryCommitment`, `safetyCase` | Code de l'environnement, décisions | Engagements, échéances |

## 2. Matrice des interfaces inter-disciplines (N², interfaces dominantes)

Chaque couple porte un ou plusieurs types d'interface (`interfaceType`) et des données échangées (`interfaceData`). Le tableau suit la convention « fournisseur → client de la donnée » (côté A → côté B).

| Côté A → Côté B | Type d'interface | Données échangées | Fréquence de changement | Criticité |
|---|---|---|---|---|
| SUR → toutes | organisationnelle | Classement, exigences de sûreté, hypothèses d'études | Moyenne | Très haute |
| PRO → MEC | fluid / mechanical | Conditions de conception (P, T), transitoires, routage | Haute (conception) | Haute |
| MEC → GCV | civil / mechanical | Efforts aux ancrages, charges de supportage, réservations | Haute | Très haute (planning génie civil) |
| GCV / SIS → MEC, ELE, ICC | civil | Spectres de plancher, accélérations | Moyenne | Très haute |
| PRO → ICC | icSignal | Liste des capteurs et actionneurs, plages, seuils | Haute | Très haute |
| ICC → ELE | electricalPower | Bilans de puissance, alimentations secourues, classement | Moyenne | Haute |
| ELE → ICC | electricalPower | Disponibilité et qualité des alimentations | Moyenne | Haute |
| ICC → FOH | humanMachine | Affichages, alarmes, commandes | Haute | Haute |
| FOH → ICC / PRO | humanMachine | Allocation homme / machine, délais d'action opérateur | Moyenne | Haute |
| NEU ↔ THY ↔ CMB | software / organisational | Couplage cœur : distributions de puissance, marges, données combustible | Par cycle | Très haute |
| THY → MEC | mechanical | Transitoires thermiques et hydrauliques de dimensionnement | Moyenne | Haute |
| MAT → MEC / FAB | organisational | Spécifications matériaux, propriétés, vieillissement | Faible | Haute |
| FAB → MEC | organisational | Contraintes de fabrication, joints soudés, tolérances | Moyenne | Moyenne |
| CND → MEC / FAB | organisational | Exigences d'inspectabilité, zones et méthodes | Faible | Haute |
| RPR → LAY / GCV / OUT | radiological / layout | Débits de dose, protections biologiques, zonage | Moyenne | Haute |
| HVA → ICC / ELE | hvac / electricalPower | Conditions d'ambiance, charges thermiques des armoires | Moyenne | Moyenne |
| QMT → ELE / ICC / MEC | organisational | Conditions de qualification (K1-K3), statuts | Faible | Haute |
| AGR → LAY / GCV / PRO | layout / civil | Sectorisation incendie, séparation des voies, protection inondation | Moyenne | Très haute |
| CYB → ICC | software | Degrés de sécurité, zones, flux autorisés | Moyenne | Haute |
| ESS → toutes | organisational | Prérequis d'essais, configurations d'essai | Moyenne | Moyenne |
| OUT → site (installation existante) | handling / layout / mechanical | Encombrements, points d'ancrage, alimentations, accès | Haute (fortuits) | Haute |
| LIC → SUR / toutes | organisational | Demandes de l'autorité, engagements, échéances | Moyenne | Très haute |

## 3. Interfaces externes (périmètres contractuels)

| Interface | Portée (`interfaceScope`) | Objets | Mécanisme d'échange recommandé |
|---|---|---|---|
| Architecte-ensemblier (EDF / Edvance) ↔ Framatome (NSSS, C-C, combustible) | customer | Exigences d'entrée, ICD îlot nucléaire, données de site, visas | ReqIF aller-retour + espace de collaboration + PDF signés en GED |
| Îlot nucléaire ↔ îlot conventionnel (Arabelle Solutions) | partnerOem | Interfaces GV / turbine, vapeur, eau alimentaire, C-C | ICD contractuel, registre `interface` |
| Chaudière ↔ génie civil | partnerOem | Charges, ancrages, réservations, spectres | ICD + données 3D (3DEXPERIENCE / AVEVA) |
| Framatome ↔ fournisseurs | supplier | Spécifications d'approvisionnement, matrices de conformité, FNC fournisseurs | Projet de collaboration fournisseur ou ReqIF ; documents en GED |
| Framatome ↔ installation existante (base installée) | plantExisting | Configuration réelle, relevés, contraintes d'intervention | `assumption` (donnée de site) + `interface` |
| Inter-BU (ex. PCM ↔ ICS ↔ Fuel ↔ DTI) | interBu | Exigences allouées, interfaces de périmètre | Liens inter-projets (`__other`) |

## 4. Mise en œuvre dans Polarion

1. **Une interface = un Work Item `interface`**, avec exactement un côté A et un côté B (`sideA`, `sideB`, règle TR-08), des types (`interfaceType`), une portée (`interfaceScope`), les données échangées et la maturité.
2. **Cycle de vie dédié** (`wfInterface`) : identifiée → définie → accordée (deux approbations : propriétaires A et B) → gelée → révision sous demande de modification.
3. **Exigences d'interface** : `systemRequirement` ou `equipmentRequirement` de catégorie `interface`, reliée à l'interface par `satisfies` (l'interface satisfait l'exigence).
4. **Suspicion** : toute modification d'un élément côté A ou côté B rend l'interface suspecte, et le gestionnaire d'interfaces est interpellé.
5. **ICD** : LiveDoc `interfaceControlDocument` par périmètre contractuel, généré à partir du registre (requête par `interfaceScope` et par partenaire).
6. **Indicateurs** (document 13) :
   - interfaces gelées / total, par partenaire ;
   - interfaces suspectes ;
   - interfaces sans propriétaire ;
   - date de gel dépassée.
7. **Matrice N²** : rapport LiveReport croisant les éléments côté A et côté B (vue « qui dépend de qui »), filtrable par discipline (`discipline` de l'élément lié).
