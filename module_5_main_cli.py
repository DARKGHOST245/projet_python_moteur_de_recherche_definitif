import os
import json

# Importation des fonctions utiles (tu dois avoir ces fichiers)
"""from file_reader import read_txt_files_and_clean
from word_indexer import build_index, save_index, load_index
from search_core import search_word
from stats_analyzer import show_statistics"""

# Chemin par défaut pour sauvegarder l’index
INDEX_FILE = "index.json"

# Affiche le menu  
def afficher_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Indexer les fichiers texte")
    print("2. Rechercher un mot")
    print("3. Voir les statistiques")
    print("4. Quitter")

# Demande le dossier, lit les fichiers et construit l’index
def indexer_fichiers():
    dossier = input("Chemin du dossier contenant les fichiers .txt : ")

    if not os.path.isdir(dossier):
        print("❌ Ce dossier n'existe pas.")
        return {}

    print("🔍 Lecture des fichiers...")
    fichiers = read_txt_files_and_clean(dossier)

    print("⚙️ Construction de l'index...")
    index = build_index(fichiers)

    save_index(index, INDEX_FILE)
    print("✅ Index sauvegardé dans", INDEX_FILE)
    return index

# Charge l’index depuis le fichier JSON
def charger_index():
    if os.path.exists(INDEX_FILE):
        return load_index(INDEX_FILE)
    else:
        print("⚠️ Aucun index trouvé. Veuillez indexer d'abord.")
        return {}

# Permet à l’utilisateur de rechercher un mot
def rechercher(index):
    mot = input("Mot à rechercher : ").lower()
    resultats = search_word(index, mot)

    if not resultats:
        print("Aucune occurrence trouvée.")
    else:
        print(f"🔎 Résultats pour '{mot}':")
        for occ in resultats:
            print(f"- {occ['fichier']} | Ligne {occ['ligne']} | Position {occ['position']}")

# Fonction principale avec boucle de menu
def menu():
    index = {}  # Index vide au début

    while True:
        afficher_menu()
        choix = input("Choix : ")

        if choix == "1":
            index = indexer_fichiers()
        elif choix == "2":
            if not index:
                index = charger_index()
            if index:
                rechercher(index)
        elif choix == "3":
            if not index:
                index = charger_index()
            if index:
                show_statistics(index)
        elif choix == "4":
            print("👋 Fin du programme.")
            break
        else:
            print("❌ Choix invalide. Réessayez.")

# Lancement du programme
if __name__ == "__main__":
    menu()
