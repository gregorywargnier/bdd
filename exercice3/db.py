import mysql.connector
from dotenv import load_dotenv
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
            CREATE TABLE IF NOT EXISTS releases (
                id INT AUTO_INCREMENT PRIMARY KEY,
                version VARCHAR(50),
                tag_git VARCHAR(50),
                date_creation DATETIME
            );""")
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS environnements (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(50) UNIQUE CHECK (nom IN ('dev', 'staging', 'prod'))
            );""")
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS deploiements (
                id INT PRIMARY KEY AUTO_INCREMENT,
                id_release INT,
                id_env INT,
                etat ENUM('planifié', 'validé', 'en_cours', 'réussi', 'échec', 'annulé'),
                date_deploiement DATETIME,
                FOREIGN KEY (id_release) REFERENCES releases(id),
                FOREIGN KEY (id_env) REFERENCES environnements(id)                
            );""")
    create_tables()