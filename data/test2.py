import sqlite3


def search_term(database_path, term):
    # Créer une connexion à la base de données
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Obtenir la liste des tables dans la base de données
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Parcourir chaque table et rechercher le terme
    for table in tables:
        #table_name = table[0]
        table_name = "match5"
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        column_names = [column[1] for column in columns]

        for column_name in column_names:
            query = f"SELECT * FROM {table_name} WHERE {column_name} LIKE '%{term}%';"
            cursor.execute(query)
            rows = cursor.fetchall()

            if len(rows) > 0:
                print(f"Le terme '{term}' a été trouvé dans la table '{table_name}', colonne '{column_name}'.")
                for row in rows:
                    print(row)

    # Fermer la connexion à la base de données
    conn.close()


# Exemple d'utilisation
database_path = "database.db"
search_term(database_path, "équipe49")