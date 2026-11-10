# Bibliothèque personnelle

Application Python simple pour gérer une bibliothèque personnelle.

## Problème métier

Permettre de gérer une collection de livres (ajout, modification, suppression, recherche, tri) avec persistance locale en JSON, sans dépendance externe lourde.

## Architecture

```
src/
├── models.py      # Classes Livre et Bibliotheque
├── storage.py     # Persistance JSON
└── main.py        # Interface CLI
tests/
├── test_models.py
└── test_storage.py
data/              # Fichier JSON généré à l'exécution
```

## Technologies

- Python 3.10+
- Bibliothèque standard : `json`, `dataclasses`, `datetime`, `uuid`, `pathlib`
- Tests : pytest

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Exécution

```bash
PYTHONPATH=src python3 src/main.py
```

## Fonctionnalités

- Ajouter un livre (titre, auteur, catégorie, année optionnelle)
- Afficher tous les livres
- Rechercher par titre ou auteur
- Trier par date d'ajout ou catégorie
- Modifier un livre
- Supprimer un livre
- Sauvegarde automatique dans `data/bibliotheque.json`

## Tests

```bash
pytest tests/ -v
```

## Notions travaillées

- Programmation orientée objet (classes, dataclasses)
- Modules et packages
- Persistance JSON
- Gestion d'erreurs basique
- Tests unitaires

## Compétences pour le CV

Développement d'une application CLI en Python avec POO, persistance JSON et tests unitaires.
