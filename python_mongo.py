import pymongo

# Client pour le serveur mongodb
client_mongodb = pymongo.MongoClient("mongodb://localhost:27017")

# Choix de la base de données
custom_db = client_mongodb["custom_db"]

# Choix de la collection
# utilisateurs = custom_db.get_collection("utilisateurs")
utilisateurs = client_mongodb.get_database("custom_db").get_collection("utilisateurs")

# Simple crud

while True:
    print("1 - Ajouter dans la collection")
    print("2 - Affiche les données de la collection")
    print("3 - Supprimer de la collection")
    print("4 - Modifier une ressource dans la collection")
    choix = input("Votre choix : ")
    match choix:
        case "1":
            utilisateur1 = {
                "nom": "titi",
                "prenom": "minet",
                "age": 80
            }
            utilisateur2 = {
                "nom": "titi",
                "prenom": "minet",
                "age": 80
            }
            # utilisateurs.insert_one(utilisateur)
            utilisateurs.insert_many([utilisateur1, utilisateur2])
        case "2":
            # for u in utilisateurs.find():
            #     if "nom" in u:
            #         print(u["nom"])
            # for u in utilisateurs.find({"nom": "titi"}):
            for u in utilisateurs.find({"age": {"$gt": 30}}):
                if "nom" in u:
                    print(u["nom"])

            pass
        case "3":
            pass
        case "4":
            pass
        case _:
            break

