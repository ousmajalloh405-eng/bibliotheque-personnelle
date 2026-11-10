# Bibliothèque personnelle

> Application CLI Python pour gérer une bibliothèque personnelle — bases de la POO, persistance JSON et tests unitaires.

**Statut** : 🟢 Réalisé et validé  
**Catégorie** : 🐍 Aventure en programmation  
**Portfolio** : [Profil GitHub](https://github.com/ousmajalloh405-eng)

---

## Problème métier

Permettre à un utilisateur de gérer sa collection personnelle de livres (ajout, modification, suppression, recherche, tri) avec sauvegarde locale simple, sans base de données.

## Architecture

```
src/
├── models.py      # Classes Livre et Bibliotheque (dataclasses)
├── storage.py     # Persistance JSON
└── main.py        # Interface CLI (menu)
tests/
├── test_models.py
└── test_storage.py
data/
└── bibliotheque.json   # Données (exemples inclus)
```

## Technologies

- **Python 3.10+**
- Bibliothèque standard : `json`, `dataclasses`, `datetime`, `uuid`, `pathlib`
- Tests : `pytest`

## Installation

```bash
git clone https://github.com/ousmajalloh405-eng/bibliotheque-personnelle.git
cd bibliotheque-personnelle
python3 -m venv venv
source venv/bin/activate   # Windows : venv\Scripts\activate
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

**Résultat** : 7 tests passés.

## Notions travaillées

- Programmation orientée objet (classes, dataclasses)
- Organisation en modules
- Persistance JSON
- Tests unitaires
- Gestion basique des erreurs

## Compétences pour le CV

Développement d'une application CLI en Python avec programmation orientée objet, persistance JSON et tests unitaires.

---

*Projet réalisé dans le cadre de la formation Data — Sonatel Academy.*
