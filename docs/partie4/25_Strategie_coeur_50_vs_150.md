# 25 — Stratégie de modèle : cœur à 50 % ou modèle à 150 % ? Arbitrage et conséquences

> Version 0.4. Question posée par le responsable IS. Faut-il :
> - **A.** un cœur commun réduit (« 50 % »), que les BU / UO / projets complètent localement (types, liens, attributs), les ajouts pertinents remontant ensuite au CCB pour enrichir le cœur ;
> - **B.** un modèle complet (« 150 % ») couvrant toutes les typologies, filtré par gabarit de projet ?
>
> Décision proposée : **ADR-29**. Modèle de référence : `model/extension_policy.yaml`.
>
> *Nota.* « 150 % » désigne ici le **modèle de configuration**. Ce n'est pas la ligne de produits 150 % des **conceptions** (spécification maître et variantes, doc. 11 § 6), qui est un autre sujet.

## 1. La question a deux axes

L'alternative mélange deux décisions indépendantes :

| Axe | Question | Pôles |
|---|---|---|
| **Qui définit ?** | Les types, liens, workflows et attributs sont-ils définis centralement ou localement ? | Central ↔ local |
| **Quand construit-on ?** | Construit-on et qualifie-t-on tout avant le premier projet, ou par incréments ? | Tout d'abord ↔ par incréments |

L'option A combine « local » et « par incréments ». L'option B, prise au pied de la lettre, combine « central » et « tout d'abord ». **La bonne réponse combine un axe de chaque option.**

## 2. Les faits Polarion qui pèsent sur la décision

| Fait | Conséquence |
|---|---|
| La configuration est **héritée** du niveau global vers les projets. Une **surcharge projet remplace** l'élément global pour ce projet [P] | Toute surcharge locale devient une **dérive silencieuse** : les évolutions ultérieures du cœur n'atteignent plus ce projet pour cet élément |
| Les **règles de rôles de liens** portent sur des **identifiants de types** | Deux projets qui nomment différemment le même concept ne peuvent pas être liés proprement, ni couverts par les mêmes règles TR |
| La **réutilisation** (branche de document, document dérivé, copie) suppose les **mêmes types et champs** dans les projets source et cible | Bibliothèques, lignes de produits et référentiel du parc deviennent inutilisables entre projets divergents |
| Requêtes, LiveReports et indicateurs de portefeuille reposent sur des **identifiants de champs** | Un attribut local, même équivalent, est **invisible** pour la consolidation |
| Changer le type d'éléments existants est possible, mais **migrer** champs, liens et états à grande échelle est coûteux et risqué | Converger après coup coûte beaucoup plus cher que converger d'emblée |
| L'outil est le support d'activités importantes pour la protection : chaque **variante de workflow** est une configuration à **qualifier** (OQ) | Des workflows locaux multiplient le coût et le risque de validation |
| Un projet peut n'exposer qu'un **sous-ensemble** des types et des documents (surcharge de l'énumération des types) | Le filtrage d'un modèle complet par gabarit est **natif** : l'option B n'impose pas d'écrans surchargés |

## 3. Comparaison

| Critère | A — Cœur 50 % + ajouts locaux libres | B — 150 % construit d'un bloc | **C — Recommandée** |
|---|---|---|---|
| Traçabilité inter-projets, bibliothèques, lignes de produits | ❌ Divergence des types et des rôles | ✅ | ✅ |
| Indicateurs de portefeuille, audits transverses | ❌ Concepts locaux invisibles | ✅ | ✅ |
| Cohérence réglementaire (même sens de « approuvé », socle partout) | ⚠️ Dépend de chaque projet | ✅ | ✅ |
| Coût de validation de l'outil | ⬆️ Chaque variante locale | ⬆️ Tout qualifier avant le premier projet | ➡️ Qualifié par incrément |
| Délai jusqu'au premier pilote | ✅ Court | ❌ Long | ✅ Court (seul l'incrément 1 est construit) |
| Adaptation au terrain, innovation | ✅ | ❌ Rigide | ✅ Zones d'extension + promotion |
| Charge de gouvernance | Faible au début, puis **explosive** (harmonisation) | Forte, goulot central | Moyenne, outillée (CI, revue trimestrielle) |
| Ergonomie (nombre de champs à l'écran) | ✅ | ⚠️ Si non filtré | ✅ Filtré par profil et par pack |
| Risque de divergence | Élevé, quasi irréversible | Faible | Faible et **mesuré** |
| Risque de « mauvais cœur » (conçu loin du terrain) | Faible | Élevé | Moyen, maîtrisé (ateliers, incréments, scénarios) |
| Coût de convergence ultérieur | Très élevé (migration de données) | Nul | Faible (promotion de champs locaux par script) |

## 4. Recommandation : ni 50 %, ni 150 % au sens strict

**« 150 % conçu, cœur gouverné à 100 %, déployé par incréments, extensions locales délimitées, promotion par le CCB. »**

1. **Concevoir à 150 %, comme c'est déjà fait.** Le modèle YAML couvre les 32 typologies et le validateur le prouve. Concevoir coûte peu (des fichiers texte et une CI) et c'est l'actif qui évite les incompatibilités futures. Le cœur ne doit pas être découvert projet après projet.
2. **Gouverner le cœur à 100 %.** Tout ce qui traverse une frontière de projet ne se définit jamais localement :
   - types ;
   - rôles et règles de liens ;
   - états et workflows ;
   - attributs de sûreté, de classement et d'export ;
   - énumérations utilisées par une règle ;
   - types de documents.
3. **Construire et déployer par incréments.** Les définitions du cœur peuvent être chargées en bloc (elles sont inertes). Mais un type n'est **exposé** aux projets qu'une fois « terminé » : formulaire, scripts, gabarit, cas OQ, aide (définition de « terminé » dans `extension_policy.yaml`).
   - **INC-1** = tranche NUWARD (28 types) ;
   - **INC-2** = base installée (fortuit / outillage) ;
   - **INC-3** = C-C et logiciel ;
   - **INC-4** = bibliothèques transverses.

   Chaque projet ne voit que son sous-ensemble, par surcharge **générée**.
4. **Ouvrir des zones d'extension locales**, déclarées et limitées :
   - champs informatifs préfixés `x_` (5 par type, 15 par projet au plus) ;
   - énumérations locales ;
   - valeurs des énumérations de portée projet ;
   - gabarits de documents, pages, requêtes et Spaces locaux.

   **Interdits en local :** types, rôles de liens, workflows, redéfinition d'un champ du cœur, surcharge d'un fichier hors de la liste fermée.
5. **Promouvoir ce qui est utile.** Une revue trimestrielle exporte les extensions de tous les projets. Le CCB promeut dans le cœur ce qui sert à au moins deux projets ou BU, ou ce qu'exige un client ou une autorité. La migration se fait par script : champ `x_` → champ du cœur, valeurs recopiées, `x_` déprécié puis retiré. **C'est l'intuition de l'option A, appliquée là où elle est sans danger.**
6. **Incuber les besoins structurants.** Un besoin de type, de rôle ou de workflow nouveau ne s'implémente pas localement. Il est prototypé en bac à sable, décrit par un scénario de couverture, décidé par le CCB (20 jours ouvrés), puis il entre dans le cœur **pour tous**.

### Pourquoi pas l'option A, malgré ses atouts

Dans le nucléaire, la valeur de l'outil est précisément ce qui **traverse** les projets :
- bibliothèques réglementaires ;
- réutilisation par palier et par produit ;
- démonstration de sûreté ;
- consolidation des écarts ;
- audits.

Les divergences de types et de rôles sont les plus chères à corriger, car il faut migrer des données. Chaque workflow local est aussi un objet de validation. L'option A donne de la vitesse au départ et une dette ensuite. Son mécanisme de promotion est excellent, mais pour les **extensions**, pas pour la structure.

### Pourquoi pas l'option B au pied de la lettre

Tout construire et tout qualifier avant le premier projet repousse le pilote d'un an. Cela figerait des hypothèses OSINT non validées et produirait des éléments que personne n'utilise. Le 150 % doit rester une **conception**, pas un chantier de construction initial.

## 5. Ce que cela implique concrètement

### 5.1 Configuration

| Élément | Règle | Outillage |
|---|---|---|
| Configuration globale | Le cœur complet, généré | `tools/generate_polarion.py` |
| Exposition par projet | Sous-ensemble des types et documents « terminés » et utiles à la typologie ; surcharges générées uniquement | `tools/generate_project.py`, `model/pilots/*.yaml` |
| Fichiers surchargeables par un projet | Liste fermée (`overridableProjectFiles`) : énumération des types, énumération des documents, énumérations de portée projet, champs d'un type (cœur + `x_` seulement) | `model/extension_policy.yaml` |
| Champs locaux | Préfixe `x_`, jamais dans une condition, une règle TR, un rapport de portefeuille ou un échange ReqIF | Contrôle CI : aucun champ du cœur n'utilise le préfixe |
| Contrôle des projets en production | Export périodique de la configuration de chaque projet ; contrôle « seulement des fichiers autorisés, seulement des ajouts `x_` » | Outil à développer après le pilote (`tools/lint_project_config.py`) |
| Incréments | Chaque type appartient à un incrément planifié ; aucun type n'est exposé avant sa définition de « terminé » | Contrôle CI : « types sans incrément » |

### 5.2 Gouvernance

- **CCB du modèle :**
  - **composition :** responsable IS (président), Design Authority, ingénieur configuration, SE Referents, Sûreté et Qualité invités selon le sujet ;
  - **cadence :** tous les quinze jours pendant les pilotes, mensuelle ensuite ;
  - **délais :** 10 jours ouvrés pour une évolution du cœur, 3 jours pour une valeur d'énumération.
- **Délégation :** les valeurs des énumérations de portée projet relèvent des SE Referents de BU, sans passage en CCB.
- **Indicateurs de la stratégie :**
  - extensions par projet ;
  - taux de promotion ;
  - surcharges hors liste (cible 0) ;
  - délai de traitement des demandes au CCB ;
  - nombre de types exposés par incrément.

### 5.3 Effet sur le guide pas à pas (doc. 23)

- **S1** charge le cœur complet. Les étapes **S3 à S7 ne portent que sur les types de l'incrément ouvert** : INC-1, soit 28 types, pour le pilote NUWARD.
- Chaque incrément suivant rejoue S3 à S7 et les OQ pour ses propres types : c'est le rythme de croissance du cœur exposé.

### 5.4 Effet sur l'onboarding (doc. 24)

- L'atelier **B1** prend la décision ADR-29.
- L'atelier **C1** entraîne chaque membre au circuit d'extension et de demande d'évolution. Ajouter un champ `x_` doit être aussi naturel que proposer sa promotion.

## 6. Signaux qui doivent faire réexaminer la décision

| Signal | Réponse |
|---|---|
| Les demandes s'accumulent au CCB (délais dépassés deux mois de suite) | Déléguer davantage aux SE Referents (énumérations, gabarits) ; voie rapide élargie |
| Une BU a besoin d'un cycle de vie radicalement différent (ex. défense) | Instance ou cœur dédié (déjà prévu pour la défense), jamais des types locaux dans l'instance commune |
| Beaucoup de champs `x_` identiques dans plusieurs projets | Le cœur est incomplet : promotion groupée et revue de la typologie concernée |
| Des types du cœur restent inutilisés après deux incréments | Les déprécier (identifiant conservé, non exposé) |

## 7. ADR-29 (résumé)

- **Décision :** cœur conçu à 150 % et gouverné à 100 % ; exposition et qualification par incréments ; extensions locales limitées ; promotion trimestrielle ; incubation des besoins structurants.
- **Statut :** proposée, à valider à l'atelier B1.
- **Conséquences :** `model/extension_policy.yaml`, surcharges projet générées, contrôles CI. Un outil de contrôle des configurations de projets est à développer.
