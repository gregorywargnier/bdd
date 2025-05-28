from db import create_tables
from environements import add_environements, get_environnements
from deploiements import get_deploiements
from releases import add_releases, get_releases


def display_menu():
    print("------ Menu -------")
    print("1- Ajouter une release")
    print("2- Afficher des releases")
    print("3- Ajouter des environnements")
    print("4- Afficher des environnements")
    print("5- Ajouter des prod")
    print("6- Afficher des prod")
    print("0- Quitter")


def main_add_releases():
    version = input("Merci de saisir le numéro de version : ")
    tag_git = input("Merci de saisir le numéro de tag git : ")
    add_releases(version=version, tag_git=tag_git)
    print("Release ajouté")

def main_get_releases():
    print("===== Liste des releases =====")
    for (id, version, tag_git, date_creation ) in get_releases():
        print(f"ID {id}, version {version}, tag_git {tag_git}, date_creation {date_creation}")

def main_add_environements():
    nom = input("Merci de saisir le nom (dev/staging/prod): ")
    if nom == "":
        add_environements()
    print("Ajout de l'environnement")

def main_get_environnements():
    print("===== Liste des environnements =====")
    for (id, nom) in get_environnements():
        print(f"ID {id}, nom {nom}")

def main_add_deploiements():
    pass

def main_get_deploiements():
    print("===== Liste des prods =====")
    for (id, id_release, id_env, etat, date_deploiement) in get_deploiements():
        print(f"ID {id}, id_release {id_release}, id_env {id_env}, etat {etat}, date_deeploiement {date_deploiement}")

if __name__ == "__main__":

    create_tables()

    while True:
        display_menu()
        choice = input("Votre choix : ")
        match (choice):
            case "1":
                main_add_releases()
            case "2":
                main_get_releases()
            case "3":
                main_add_environements()
            case "4":
                main_get_environnements()
            case "5":
                pass
            case "6":
                main_get_deploiements()
            case "0":
                break
            case _:
                print("Erreur de menu")
