"""Tests de la persistance."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from models import Bibliotheque
from storage import Storage


def test_sauvegarde_et_chargement():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        fichier = Path(tmp) / "test.json"
        storage = Storage(str(fichier))
        biblio = Bibliotheque()
        biblio.ajouter("Test", "Auteur", "Cat", 2024)
        storage.sauvegarder(biblio)

        biblio2 = storage.charger()
        assert len(biblio2.tous()) == 1
        assert biblio2.tous()[0].titre == "Test"
        assert biblio2.tous()[0].annee == 2024


def test_fichier_vide():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        fichier = Path(tmp) / "vide.json"
        storage = Storage(str(fichier))
        biblio = storage.charger()
        assert len(biblio.tous()) == 0
