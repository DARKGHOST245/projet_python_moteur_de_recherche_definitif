import os
import re
import logging

# Configuration du fichier pour enregistrer les erreurs
logging.basicConfig(filename="erreurs.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def explorer_dossier(dossier):
    """Explore un dossier et retourne une liste des fichiers .txt"""
    if not os.path.exists(dossier):
        logging.error(f"Dossier non trouvé : {dossier}")
        raise FileNotFoundError(f"Le dossier '{dossier}' n'existe pas.")
    
    fichiers = [f for f in os.listdir(dossier) if f.endswith('.txt')]
    
    if not fichiers:
        logging.warning(f"Aucun fichier .txt trouvé dans le dossier : {dossier}")
    
    return fichiers

def lire_fichier(chemin_fichier):
    """Lit le contenu d'un fichier .txt et retourne ses lignes"""
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            return fichier.readlines()
    except Exception as e:
        logging.error(f"Erreur lors de la lecture du fichier '{chemin_fichier}': {e}")
        raise IOError(f"Erreur lors de la lecture du fichier '{chemin_fichier}': {e}")

def nettoyer_texte(lignes):
    """Nettoie le texte : minuscules + supprime la ponctuation"""
    lignes_nettoyees = [ligne.strip().lower() for ligne in lignes]
    lignes_nettoyees = [re.sub(r"[^a-z0-9\s]", "", ligne) for ligne in lignes_nettoyees]
    return lignes_nettoyees

def rechercher_ligne(lignes_nettoyees, ligne_recherchee):
    """Cherche une ligne et découpe en mots si elle est trouvée"""
    ligne_recherchee = ligne_recherchee.strip().lower()
    if ligne_recherchee in lignes_nettoyees:
        return ligne_recherchee.split()
    else:
        logging.warning(f"Ligne non trouvée : {ligne_recherchee}")
        raise ValueError("❌ La ligne recherchée n'existe pas dans le fichier.")

# ----------------------- Programme principal -----------------------

while True:
    dossier = input("📁 Entrez le nom du dossier à explorer : ").strip()
    if not dossier:
        print("❌ Le nom du dossier ne peut pas être vide. Réessaie.")
        continue

    try:
        fichiers_txt = explorer_dossier(dossier)
        if not fichiers_txt:
            print("⚠️ Aucun fichier texte trouvé dans ce dossier.")
            break

        print("✅ Fichiers texte trouvés :", fichiers_txt)

        for nom_fichier in fichiers_txt:
            chemin_fichier = os.path.join(dossier, nom_fichier)
            lignes = lire_fichier(chemin_fichier)
            lignes_nettoyees = nettoyer_texte(lignes)

            while True:
                ligne_recherchee = input("\n🔍 Tape une ligne exacte à rechercher : ").strip()
                if not ligne_recherchee:
                    print("❌ Tu n'as rien tapé. Réessaie.")
                    continue

                try:
                    mots = rechercher_ligne(lignes_nettoyees, ligne_recherchee)
                    print("✅ Mots trouvés dans la ligne :")
                    for i, mot in enumerate(mots):
                        print(f"Mot {i+1} : {mot}")
                    break
                except ValueError as e:
                    print(e)
                    retry = input("↩️ Veux-tu réessayer avec une autre ligne ? (oui/non) : ").strip().lower()
                    if retry != "oui":
                        break

        break  # Sortie du programme après analyse du dossier

    except FileNotFoundError as e:
        print(e)
        retry = input("↩️ Voulez-vous entrer un autre dossier ? (oui/non) : ").strip().lower()
        if retry != "oui":
            break
    except IOError as e:
        print(e)
        break
