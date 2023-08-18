import sqlite3
import os


class Team:
    def __init__(self, database_name: str):
        path = database_name
        self.con = sqlite3.connect(path)
        self.con.row_factory = sqlite3.Row

    def return_team_all(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM team_example"
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        self.con.commit()
        ls = []
        dict_team = {}
        dict_club = {}
        for row in records:
            #ls.append(row[1] + " " + row[2])
            key = row[2]
            value = row[1]
            #dict_team[key] = value
            dict_club.setdefault(key, []).append(value)
        #print(dict_team)
        print(dict_club)
        key1 = "ASC Cordemais"
        key2 = "Bouée"
        print(len(dict_club[key1]))
        print(len(dict_club[key2]))
        for i in dict_club:
            print(i)

x = Team("database.db")
x.return_team_all()
