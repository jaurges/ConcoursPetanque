import sqlite3
import os


class Team:
    def __init__(self, database_name: str):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = dir_path.replace("object", "data") + f"//{database_name}"
        self.con = sqlite3.connect(path)
        self.con.row_factory = sqlite3.Row

    def return_team_all(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM team_example"
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        self.con.commit()

        print(records)
        
x = Team("database.db")
x.return_team_all()
