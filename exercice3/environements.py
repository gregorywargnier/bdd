from db import connection_to_database


def add_environements(nom="dev"):
    with connection_to_database() as connection:
        connection.start_transaction()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO environnements (nom) values (%s)
                """, (nom,))
            connection.commit()
        except:
            print("Une erreur grave lors de l'ajout environnements")
            connection.rollback()

def get_environnements():
    with connection_to_database() as connection:
        connection.start_transaction()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM environnements")
                environnements = cursor.fetchall()
                return environnements
        except:
            print("Une erreur grave lors de l'affichage des environnements")