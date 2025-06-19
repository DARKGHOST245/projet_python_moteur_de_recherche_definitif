import json
import os
import re

# Construit un index des mots présents dans les fichiers
def construire_index(fichiers_lus):
    index = {}
    for nom_fichier in fichiers_lus:
        lignes = fichiers_lus[nom_fichier]
        for num_ligne in range(len(lignes)):
            ligne = lignes[num_ligne]
            mots = re.findall(r'\b\w+\b', ligne.lower())
            for position in range(len(mots)):
                mot = mots[position]
                occurrence = {
                    "fichier": nom_fichier,
                    "ligne": num_ligne + 1,
                    "position": position + 1
                }
                if mot in index:
                    index[mot].append(occurrence)
                else:
                    index[mot] = [occurrence]
    return index

def sauvegarder_index(index, chemin="index.json"):
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

def charger_index(chemin="index.json"):
    if os.path.exists(chemin):
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return None

