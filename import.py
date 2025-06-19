import schema_manager as sm  # type: ignore
def menu():
sm.charger_schemas()
while True:
    print("\n---MENU SCHEMAS---")
    print("1. créer un schéma")
    print("2. afficher les schémas")
    print("3. valider l'enregistrement")
    print("4. quitter")
    choix=input("choix : ")
    if choix == "1":
        nom=input("nom de la table : ")
        colonne={}
        while True:
            colonne=input("nom de la colonne(ou vide pour finir) : ")
            if colonne == "" :
                break
            colonnes_types=input("type(str, int, bool)")
            colonne[colonne]=colonnes_types
            sm.creer_schemas(nom, colonne)
    elif choix == "2":
        sm.afficher_schemas()
    elif choix == "3":
        sm.valider_enregistrement()
        print("validation de l'enregistrement.")
    elif choix == "4":
        break
    else :
        print("option invalide")
    if __name__ == "_main_"
        menu()