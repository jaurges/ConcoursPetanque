import os
import subprocess
import sqlite3
file_name = "prout"
directory = f"{os.path.dirname(os.path.abspath(__file__))}" + "/".join(["", file_name, f"{file_name}.db"])
subprocess.run(["mkdir", file_name])
conn = sqlite3.connect(directory)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS utilisateurs
                  (id INTEGER PRIMARY KEY, nom TEXT, age INTEGER)''')
conn.commit()
conn.close()
print(directory)