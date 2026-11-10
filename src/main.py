"""Interface en ligne de commande pour la bibliothèque."""

from models import Bibliotheque
from storage import Storage


def afficher_livres(livres: list) -> None:
    if not livres:
        print("Aucun livre trouvé.")
        return
    for livre in livres:
        annee = f" ({livre.annee})" if livre.annee else ""
        print(f"[{livre.id[:8]}] {livre.titre} — {livre.auteur} | {livre.categorie}{annee}")


def menu() -> None:
    storage = Storage()
    biblio = storage.charger()

    while True:
        print("\n=== Bibliothèque personnelle ===")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Rechercher")
        print("4. Trier")
        print("5. Modifier un livre")
        print("6. Supprimer un livre")
        print("0. Quitter")
        choix = input("Choix : ").strip()

        if choix == "1":
            titre = input("Titre : ").strip()
            auteur = input("Auteur : ").strip()
            categorie = input("Catégorie : ").strip()
            annee_str = input("Année (optionnel) : ").strip()
            annee = int(annee_str) if annee_str.isdigit() else None
            if titre and auteur and categorie:
                livre = biblio.ajouter(titre, auteur, categorie, annee)
                storage.sauvegarder(biblio)
                print(f"Livre ajouté : {livre.titre}")
            else:
                print("Titre, auteur et catégorie sont obligatoires.")

        elif choix == "2":
            afficher_livres(biblio.tous())

        elif choix == "3":
            terme = input("Recherche (titre ou auteur) : ").strip()
            resultats = biblio.rechercher(terme)
            afficher_livres(resultats)

        elif choix == "4":
            print("1. Par date d'ajout")
            print("2. Par catégorie")
            sous = input("Choix : ").strip()
            if sous == "1":
                afficher_livres(biblio.trier("date"))
            elif sous == "2":
                afficher_livres(biblio.trier("categorie"))

        elif choix == "5":
            livre_id = input("ID du livre (8 premiers caractères) : ").strip()
            livre = None
            for l in biblio.livres:
                if l.id.startswith(livre_id):
                    livre = l
                    break
            if not livre:
                print("Livre non trouvé.")
                continue
            print(f"Modification de : {livre.titre}")
            nouveau_titre = input(f"Nouveau titre [{livre.titre}] : ").strip() or None
            nouvel_auteur = input(f"Nouvel auteur [{livre.auteur}] : ").strip() or None
            nouvelle_cat = input(f"Nouvelle catégorie [{livre.categorie}] : ").strip() or None
            biblio.modifier(
                livre.id,
                titre=nouveau_titre,
                auteur=nouvel_auteur,
                categorie=nouvelle_cat,
            )
            storage.sauvegarder(biblio)
            print("Livre modifié.")

        elif choix == "6":
            livre_id = input("ID du livre (8 premiers caractères) : ").strip()
            for l in biblio.livres:
                if l.id.startswith(livre_id):
                    if biblio.supprimer(l.id):
                        storage.sauvegarder(biblio)
                        print("Livre supprimé.")
                    break
            else:
                print("Livre non trouvé.")

        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    menu()
