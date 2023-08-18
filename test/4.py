import sqlite3
from time import sleep

# Créer une connexion à la base de données en mémoire
conn = sqlite3.connect(':memory:')

# Créer un curseur pour exécuter des requêtes
cursor = conn.cursor()

# Exemple de création d'une table
cursor.execute('''CREATE TABLE users
                  (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Exemple d'insertion de données dans la table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("John Doe", "john@example.com"))
sleep(5)
# Valider les changements
conn.commit()

# Exemple de sélection des données de la table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Afficher les données
for row in rows:
    print(row)

# Fermer la connexion à la base de données
conn.close()