# Annexe A7 — Tailoring (approche graduée)

> Document **généré** par `tools/generate_docs.py` depuis `model/*.yaml` — ne pas éditer à la main.

## Grille de cotation

Chaque critère est coté 0 à 3. Score total → classe. Un critère 'éliminatoire' fixe une classe minimale.

| Critère | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Enjeu de sûreté (fonctions catégorisées, EIP, exigences définies)** | aucun EIP | EIP non classés / F2 / cat. 3 | F1B / cat. 2 / classe 2 | F1A / cat. 1 / classe 1 / ESPN N1 |
| **Nouveauté (FOAK vs répétitif)** | réplique à l'identique | adaptation mineure | adaptation significative | première de série / nouvelle technologie |
| **Taille (charge d'ingénierie)** | < 1 000 h | 1 000 – 20 000 h | 20 000 – 200 000 h | > 200 000 h |
| **Nombre de disciplines / interfaces** | 1-2 | 3-5 | 6-10 | > 10 ou multi-partenaires |
| **Instruction réglementaire** | aucune | information de l'exploitant | dossier soumis (déclaration, ESPN N2/N3) | autorisation / instruction approfondie / licensing export |
| **Exigences contractuelles de traçabilité** | aucune | matrice de conformité | échanges ReqIF / livrables de traçabilité | traçabilité intégrale auditée par le client |
| **Durée / pérennité des données** | < 3 mois | 3-12 mois | 1-5 ans | > 5 ans / produit générique |

Seuils : **classA** >= 15 ; **classB** 9 – 14 ; **classC** 4 – 8 ; **classD** <= 3 ou urgence (fortuit) – le socle non négociable reste dû

## Socle non négociable

- **NN-01** — Identification des EIP concernés et des exigences définies (champ definedRequirement / eip renseigné, jamais laissé 'À déterminer' à l'approbation).
- **NN-02** — Contrôle technique des AIP par une personne différente de l'auteur (condition approverNotAuthor), avec signature électronique.
- **NN-03** — Traçabilité exigence définie → vérification → preuve (règle TR-03).
- **NN-04** — Gestion des écarts : tout écart détecté est enregistré, caractérisé (impact EIP), traité et soldé (workflow FNC).
- **NN-05** — Gestion de configuration : toute modification d'un élément approuvé passe par une demande de modification ou une révision tracée.
- **NN-06** — Classification de l'information et contrôle export renseignés ; aucune donnée sensible sécurité / DR sur l'instance standard.
- **NN-07** — Archivage du livrable approuvé (PDF signé) dans la GED de référence.
- **NN-08** — Hypothèses de sûreté explicitées et confirmées avant clôture.

## Profils par classe

| Aspect | classA | classB | classC | classD |
|---|---|---|---|---|
| fr | Programme majeur | Projet significatif | Projet courant / récurrent | Express (fortuit, petite adaptation) |
| documentWorkflow | wfDocumentFull | wfDocumentFull | wfDocumentFull | wfDocumentLight |
| reviews | kickoff, requirementsReview, preliminaryDesign, criticalDesign, manufacturingReadiness, testReadiness, qualificationReview, acceptance, safetyReview, gate | kickoff, requirementsReview, criticalDesign, testReadiness, acceptance, safetyReview | kickoff, criticalDesign, acceptance | interventionReadiness |
| mbse | Obligatoire (Capella / SysML) pour l'architecture ; synchronisation fonctions / composants / interfaces | Recommandé pour les architectures multi-disciplines | Non requis | Non requis |
| icd | Registre d'interfaces complet + ICD par périmètre contractuel | Registre d'interfaces (site / existant / partenaires) | Interfaces portées par les exigences d'interface | Non requis (interfaces décrites dans la note) |
| variants | Ligne de produits (spécification maître + variantes) si plusieurs tranches / paires | Attributs d'applicabilité (paliers / tranches) | Réutilisation de gabarits / documents génériques (branches) | Non requis |
| safetyCase | Argumentaire CAE/GSN structuré | Chapitres de démonstration sans GSN formel | Note de justification | Note de justification signée |
| ccb | CCB à 2 niveaux (projet + programme) ; Design Authority | CCB projet | CCB projet allégé (gestionnaire de configuration + responsable technique) | Décision par le responsable technique + avis sûreté si EIP |
| vvIndependence | Selon catégorie ; V&V indépendante pour logiciel cat. A | Personne différente minimum | Personne différente | Personne différente (non négociable) |
| kpiReview | Mensuelle | Mensuelle | Trimestrielle | Au fil de l'eau (SLA) |

### Types de Work Items actifs par classe

| Type | classA | classB | classC | classD |
|---|---|---|---|---|
| `sourceRequirement` | ● | ● | ● |  |
| `regulatoryRequirement` | ● | ● | ● |  |
| `stakeholderRequirement` | ● | ● |  |  |
| `systemRequirement` | ● | ● | ● | ● |
| `equipmentRequirement` | ● | ● | ● | ● |
| `softwareRequirement` | ● | ● |  |  |
| `hardwareRequirement` | ● | ● |  |  |
| `safetyRequirement` | ● | ● | ● |  |
| `assumption` | ● | ● | ● | ● |
| `operationalScenario` | ● | ● |  |  |
| `function` | ● | ● |  |  |
| `logicalComponent` | ● |  |  |  |
| `physicalComponent` | ● | ● | ● |  |
| `interface` | ● | ● |  |  |
| `designParameter` | ● | ● | ● |  |
| `designDecision` | ● | ● |  |  |
| `hazard` | ● | ● |  |  |
| `safetyClaim` | ● |  |  |  |
| `risk` | ● | ● | ● |  |
| `fmeaItem` | ● | ● |  |  |
| `analysis` | ● | ● | ● | ● |
| `regulatoryCommitment` | ● | ● |  |  |
| `verificationCase` | ● | ● | ● | ● |
| `anomaly` | ● | ● |  |  |
| `changeRequest` | ● | ● | ● | ● |
| `nonConformance` | ● | ● | ● | ● |
| `waiver` | ● | ● | ● |  |
| `technicalIssue` | ● | ● | ● | ● |
| `deliverable` | ● | ● | ● | ● |
| `review` | ● | ● |  |  |
| `reviewFinding` | ● | ● | ● |  |
| `action` | ● | ● | ● | ● |
| `term` | ● |  |  |  |

## Typologie de projet → classe et gabarit par défaut

| Typologie | Classe | Gabarit | BU |
|---|---|---|---|
| Nouveau nucléaire – grand réacteur (EPR, EPR2) (`newBuildLarge`) | classA | `TPL-NEWBUILD` | pcm, dti, ics, fuel |
| Nouveau nucléaire – SMR (NUWARD) (`newBuildSmr`) | classA | `TPL-NEWBUILD` | dti, pcm, ics, fuel |
| Remplacement de générateurs de vapeur (RGV/SGR) (`steamGeneratorReplacement`) | classB | `TPL-IB-PROJECT` | ib, pcm |
| Réexamen périodique / VD / dossier de réexamen (RDS) (`periodicSafetyReview`) | classB | `TPL-IB-PSR` | ib, dti |
| Étude de modification base installée (`plantModification`) | classC | `TPL-IB-MOD` | ib, dti, ics |
| Fortuit / aléa en arrêt de tranche (cycle court) (`fortuit`) | classD | `TPL-IB-FORTUIT` | ib |
| Outillage spécial (mécatronique, robotique, manutention) (`specialTooling`) | classC | `TPL-TOOLING` | ib |
| Prestation d'inspection / CND / ISI (`inspectionService`) | classC | `TPL-TOOLING` | ib |
| Conception combustible (nouvel assemblage, ATF) (`fuelDesign`) | classA | `TPL-FUEL-DESIGN` | fuel |
| Contrat de recharge (études de cœur) (`fuelReload`) | classC | `TPL-FUEL-RELOAD` | fuel |
| Plateforme C-C (produit générique) (`icPlatform`) | classA | `TPL-IC-PLATFORM` | ics |
| Application / projet C-C (`icApplication`) | classB | `TPL-IC-PROJECT` | ics |
| Rénovation C-C base installée (`icRefurbishment`) | classB | `TPL-IC-PROJECT` | ics, ib |
| Conception de composant (GV, pressuriseur, RCP, MCG...) (`componentDesign`) | classB | `TPL-COMPONENT` | pcm, dti |
| Fabrication de composant (ESPN) (`componentManufacturing`) | classC | `TPL-COMPONENT` | pcm |
| Programme R&D / innovation (`rdProgram`) | classC | `TPL-RD` | dti |
| Projet bibliothèque / référentiel (`library`) | classA | `TPL-LIBRARY` | corp |
