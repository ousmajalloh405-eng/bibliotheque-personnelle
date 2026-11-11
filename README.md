# Bibliothèque personnelle

> Application CLI Python pour gérer une bibliothèque personnelle — bases de la POO, persistance JSON et tests unitaires.

**Statut** : 🟢 Réalisé et validé  
**Catégorie** : 🐍 Aventure en programmation  
**Portfolio** : [Profil GitHub](https://github.com/ousmajalloh405-eng)

---

## 1. Problème métier

Permettre à un utilisateur de gérer sa collection personnelle de livres (ajout, modification, suppression, recherche, tri) avec sauvegarde locale simple.

## 2. Architecture

```
          Interface CLI (main.py)
                    │
                    ▼
              Bibliotheque (models.py)
                    │
                    ▼
               Storage (storage.py)
                    │
                    ▼
            data/bibliotheque.json
```

**Séparation des responsabilités** :
- `models.py` → logique métier (classes Livre et Bibliotheque)
- `storage.py` → persistance JSON
- `main.py` → interaction utilisateur

## 3. Structure du projet

```
bibliotheque-personnelle/
├── src/
│   ├── models.py
│   ├── storage.py
│   └── main.py
├── tests/
│   ├── test_models.py
│   └── test_storage.py
├── data/
│   └── bibliotheque.json
├── requirements.txt
└── README.md
```

## 4. Technologies

- Python 3.10+
- Bibliothèque standard (json, dataclasses)
- pytest (tests)

## 5. Installation et exécution

```bash
git clone https://github.com/ousmajalloh405-eng/bibliotheque-personnelle.git
cd bibliotheque-personnelle
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python3 src/main.py
```

## 6. Tests

```bash
pytest tests/ -v
```

7 tests passés.

## 7. Compétences pour le CV

Développement d’une application CLI en Python avec programmation orientée objet, persistance JSON et tests unitaires.

---

*Projet réalisé dans le cadre de la formation Data — Sonatel Academy.*
