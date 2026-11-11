# Architecture — Bibliothèque personnelle

## Vue d'ensemble

Application en ligne de commande permettant de gérer une collection personnelle de livres avec persistance locale en JSON.

## Diagramme

```
┌────────────────────┐
│   Interface CLI     │
│     (main.py)       │
└──────────┬──────────┘
           │
           ▼
┌────────────────────┐
│    Bibliotheque     │
│    (models.py)      │
│  - ajouter()        │
│  - modifier()       │
│  - supprimer()      │
│  - rechercher()     │
│  - trier()          │
└──────────┬──────────┘
           │
           ▼
┌────────────────────┐
│      Storage        │
│    (storage.py)     │
│  - charger()        │
│  - sauvegarder()    │
└──────────┬──────────┘
           │
           ▼
┌────────────────────┐
│  bibliotheque.json  │
└────────────────────┘
```

## Responsabilités

| Module | Rôle |
|--------|------|
| `models.py` | Définition des classes `Livre` et `Bibliotheque`. Logique métier. |
| `storage.py` | Lecture et écriture du fichier JSON. |
| `main.py` | Menu interactif et orchestration des actions utilisateur. |
| `tests/` | Tests unitaires des modèles et de la persistance. |

## Flux de données

1. Au démarrage, `Storage.charger()` lit le JSON et reconstruit les objets.
2. L’utilisateur effectue une action via le menu.
3. La classe `Bibliotheque` modifie la liste en mémoire.
4. `Storage.sauvegarder()` écrit le nouvel état dans le JSON.
