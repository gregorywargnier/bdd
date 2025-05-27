import mysql.connector
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()


DB_CONFIG = {
    "host": os.getenv("HOST"),
    "user": os.getenv("USER"),
    "password": os.getenv("MYSQL_ROOT_PASSWORD"),
    "database": os.getenv("DATABASE"),
}

def connection_to_database():
    return mysql.connector.connect(**DB_CONFIG)

def create_tables():
    with connection_to_database() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS emprunts (
                id INT primary key auto_increment,
                date_emprunted DATETIME DEFAULT CURRENT_TIMESTAMP,
                date_sortie DATETIME,
                utilisateurs_id INT NOT NULL,
                livres_id INT NOT NULL,
                FOREIGN KEY (utilisateurs_id) REFERENCES utilisateurs(id),    
                FOREIGN KEY (livres_id) REFERENCES livres(id)      
            );
        """)

def add_utilisateurs(nom,email):
    with connection_to_database() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO utilisateurs (nom, email) 
                VALUES (%s, %s)
            """, (nom, email))
            connection.commit()
            print("Utilisateurs a été correctement crée")

def add_livres(titre,auteur):
    with connection_to_database() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO livres (titre, auteur) 
                VALUES (%s, %s)
            """, (titre, auteur))
            connection.commit()
            print("livre a été correctement crée")

def display_utilisateurs():
    with connection_to_database() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, nom, email from utilisateurs3")
            utilisateur = cursor.fetchall()
            if utilisateur:
                print("------ Liste des utilisateurs -------")
                for (id, nom, email) in utilisateur:
                    print(f"ID : {id}, nom : {nom}, email : {email}")

def display_livres():
    with connection_to_database() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, titre, auteur from livres")
            livre = cursor.fetchall()
            if livre:
                print("------ Liste des livres -------")
                for (id, titre, auteur) in livre:
                    print(f"ID : {id}, titre : {titre}, auteur : {auteur}")

def main():
    create_tables()
    while True:
        print("======= Gestion =========")
        print("1- Ajouter un utilisateur")
        print("2- Ajouter un livre")
        print("3- voir utilisateur")
        print("4- voir livre")
        choice = input("Votre choix: ").strip()
        if choice == "1":
            nom = input("Nom du utilisateur: ")
            email = input("Email du utilisateur: ")
            add_utilisateurs(nom,email)
        elif choice == "2":
            titre = input("Titre: ")
            auteur = input("Auteur: ")
            add_livres(titre,auteur)
        elif choice == "3":
            display_utilisateurs()
        elif choice == "4":
            display_livres()

        else:
            print("choix incorrecte")

if __name__ == "__main__":
    main()
