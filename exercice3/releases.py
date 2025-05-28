from datetime import datetime

from db import connection_to_database


def add_releases(version, tag_git):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with connection_to_database() as connection:
        connection.start_transaction()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                               INSERT INTO releases (version, tag_git, date_creation)
                               values (%s, %s, %s)
                               """, (version, tag_git, date))
            connection.commit()
        except:
            print("Une erreur grave lors de l'ajout releases")
            connection.rollback()


def get_releases():
    with connection_to_database() as connection:
        connection.start_transaction()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM releases")
                releases = cursor.fetchall()
                return releases
        except:
            print("Une erreur grave lors de l'affichage des  releases")