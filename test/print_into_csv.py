import sqlite3
import csv

# Étape 1 : Connexion à la base de données
db_connection = sqlite3.connect('test.db')
cursor = db_connection.cursor()

# Étape 2 : Récupération des noms de tables
cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
table_names = [table[0] for table in tables]

# Étape 3 : Pour chaque table, extraire les données et les écrire dans un CSV
for table_name in table_names:
    cursor.execute(f"SELECT * FROM {table_name};")
    data = cursor.fetchall()

    with open(f'{table_name}.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])  # Écrire les noms de colonnes
        csv_writer.writerows(data)  # Écrire les données

# Fermeture de la connexion à la base de données
db_connection.close()
