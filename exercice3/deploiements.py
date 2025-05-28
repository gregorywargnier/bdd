from datetime import datetime
from db import connection_to_database


def add_deploiements(releases_id, environnements_id, etat = "planifié"):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with connection_to_database() as connection:
        connection.start_transaction()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO deploiements (id_release, id_env, etat, date_deploiement) values (%s, %s, %s, %s)
                """, (releases_id, environnements_id, etat, date))
            connection.commit()
        except:
            print("Une erreur grave lors de ajout deploiements")
            connection.rollback()

def get_deploiements():
    with connection_to_database() as connection:
        connection.start_transaction()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM deploiements")
                deploiements = cursor.fetchall()
                return deploiements
        except:
            print("Une erreur grave lors de l'affichage des environnements")