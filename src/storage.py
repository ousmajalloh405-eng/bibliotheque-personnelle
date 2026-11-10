"""Persistance des données en JSON."""

import json
from pathlib import Path
from models import Livre, Bibliotheque


class Storage:
    """Gère la lecture et l'écriture du fichier JSON."""

    def __init__(self, fichier: str = "data/bibliotheque.json"):
        self.fichier = Path(fichier)
        self.fichier.parent.mkdir(parents=True, exist_ok=True)

    def charger(self) -> Bibliotheque:
        biblio = Bibliotheque()
        if not self.fichier.exists():
            return biblio
        try:
            with open(self.fichier, "r", encoding="utf-8") as f:
                data = json.load(f)
            biblio.livres = [Livre.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            pass
        return biblio

    def sauvegarder(self, biblio: Bibliotheque) -> None:
        data = [livre.to_dict() for livre in biblio.livres]
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
