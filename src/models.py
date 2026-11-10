"""Modèles de données pour la bibliothèque personnelle."""

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional
import uuid


@dataclass
class Livre:
    """Représente un livre dans la bibliothèque."""
    titre: str
    auteur: str
    categorie: str
    annee: Optional[int] = None
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    date_ajout: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Livre":
        return cls(
            titre=data["titre"],
            auteur=data["auteur"],
            categorie=data["categorie"],
            annee=data.get("annee"),
            id=data.get("id", str(uuid.uuid4())),
            date_ajout=data.get("date_ajout", datetime.now().isoformat()),
        )


class Bibliotheque:
    """Gère une collection de livres."""

    def __init__(self):
        self.livres: list[Livre] = []

    def ajouter(self, titre: str, auteur: str, categorie: str, annee: Optional[int] = None) -> Livre:
        livre = Livre(titre=titre, auteur=auteur, categorie=categorie, annee=annee)
        self.livres.append(livre)
        return livre

    def modifier(self, livre_id: str, **kwargs) -> Optional[Livre]:
        for livre in self.livres:
            if livre.id == livre_id:
                for key, value in kwargs.items():
                    if hasattr(livre, key) and value is not None:
                        setattr(livre, key, value)
                return livre
        return None

    def supprimer(self, livre_id: str) -> bool:
        for i, livre in enumerate(self.livres):
            if livre.id == livre_id:
                self.livres.pop(i)
                return True
        return False

    def rechercher(self, terme: str) -> list[Livre]:
        terme = terme.lower()
        return [
            l for l in self.livres
            if terme in l.titre.lower() or terme in l.auteur.lower()
        ]

    def trier(self, par: str = "date") -> list[Livre]:
        if par == "date":
            return sorted(self.livres, key=lambda l: l.date_ajout)
        elif par == "categorie":
            return sorted(self.livres, key=lambda l: l.categorie.lower())
        return list(self.livres)

    def tous(self) -> list[Livre]:
        return list(self.livres)

    def trouver_par_id(self, livre_id: str) -> Optional[Livre]:
        for livre in self.livres:
            if livre.id == livre_id:
                return livre
        return None
