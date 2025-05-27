from db import connection_to_database


def add_environements(nom):
    with connection_to_database() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO environnements (nom) values (%s)
            """, (nom))
        connection.commit()
