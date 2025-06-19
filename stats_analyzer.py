def analyser_index(chemin_dossier):
    stats = {
        "Nombre de fichiers": 0,
        "Total mots": 0,
        "Mots uniques": set(),
        "Fréquence des mots": Counter()
    }

    # Vérifier si le dossier existe
    if not os.path.isdir(chemin_dossier):
        print("Dossier introuvable.")
        return stats

    # Parcourir les fichiers du dossier
    for fichier in os.listdir(chemin_dossier):
        chemin_fichier = os.path.join(chemin_dossier, fichier)
        
        if os.path.isfile(chemin_fichier):  # Vérifier que c'est bien un fichier
            stats["Nombre de fichiers"] += 1
            
            try:
                with open(chemin_fichier, "r", encoding="utf-8") as f:
                    contenu = f.read()
                    mots = contenu.split()
                    stats["Total mots"] += len(mots)
                    stats["Mots uniques"].update(mots)
                    stats["Fréquence des mots"].update(mots)
            except Exception as e:
                print(f"Erreur de lecture du fichier {fichier}: {e}")

    stats["Mots uniques"] = len(stats["Mots uniques"])
    return stats
    # Exemple d'utilisation
chemin = "TP"
resultats = analyser_index(chemin)
for cle, valeur in resultats.items():
    if cle == "Fréquence des mots":
        for m in valeur:
            print(m)
    else:
        print(f"{cle}: {valeur}")

