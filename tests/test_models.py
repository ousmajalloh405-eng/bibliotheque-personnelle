"""Tests des modèles."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from models import Livre, Bibliotheque


def test_creation_livre():
    livre = Livre(titre="Python", auteur="Guido", categorie="Informatique")
    assert livre.titre == "Python"
    assert livre.auteur == "Guido"
    assert livre.categorie == "Informatique"
    assert livre.id
    assert livre.date_ajout


def test_ajouter_et_rechercher():
    biblio = Bibliotheque()
    biblio.ajouter("Clean Code", "Robert Martin", "Informatique")
    biblio.ajouter("Le Petit Prince", "Saint-Exupéry", "Roman")
    resultats = biblio.rechercher("code")
    assert len(resultats) == 1
    assert resultats[0].titre == "Clean Code"


def test_modifier():
    biblio = Bibliotheque()
    livre = biblio.ajouter("Titre", "Auteur", "Cat")
    modifie = biblio.modifier(livre.id, titre="Nouveau titre")
    assert modifie is not None
    assert modifie.titre == "Nouveau titre"


def test_supprimer():
    biblio = Bibliotheque()
    livre = biblio.ajouter("A", "B", "C")
    assert biblio.supprimer(livre.id) is True
    assert len(biblio.tous()) == 0
    assert biblio.supprimer("inexistant") is False


def test_trier_categorie():
    biblio = Bibliotheque()
    biblio.ajouter("Z", "A", "Zzz")
    biblio.ajouter("A", "B", "Aaa")
    tries = biblio.trier("categorie")
    assert tries[0].categorie == "Aaa"
    assert tries[1].categorie == "Zzz"
