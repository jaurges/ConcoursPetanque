'''
jugé pour les stats si l'objet ne serait pas plus efficace et maintenable
'''

import sqlite3
import os
import subprocess


class DatabaseHandler:
    def __init__(self, database_name: str):
        self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.con.row_factory = sqlite3.Row

<<<<<<< HEAD
    def create_competition(self, name: str, date: str, play_mod: str, location: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO general(name, date, play_mod, location) VALUES('{name}', '{date}', '{play_mod}', '{location}');"
=======
    def save_parameters(self, name: str, date: str, play_mod: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO parameters(name, date, play_mod) VALUES('{name}', '{date}', '{play_mod}');"
>>>>>>> parent of 4cf90b7 (ajout location les conflits sont réglé a l'aide de ses con,naissances)
        cursor.execute(query)
        cursor.close()
        self.con.commit()

        file_name = (f"{name.replace(' ', '')}_{date.replace(' ', '')}_"
                     f"{play_mod.replace(' ', '')}_{location.replace(' ', '')}")

        subprocess.run(["mkdir", file_name])
        directory = f"{os.path.dirname(os.path.abspath(__file__))}" + "/".join(["", file_name, f"{file_name}.db"])
        print(directory)
        self.con = sqlite3.connect(directory)
        self.con.row_factory = sqlite3.Row
        cursor = self.con.cursor()

        table = "CREATE TABLE IF NOT EXISTS parameters(id integer PRIMARY KEY, " \
                "name text," \
                "date text," \
                "play_mod integer," \
                "location integer)"
        insertion = (f"INSERT INTO parameters(name, date, play_mod, location) VALUES('{name}', '{date}', '{play_mod}', "
                     f"'{location}')")

        cursor.execute(table)
        cursor.execute(insertion)

        cursor.close()
        self.con.commit()

    def create_team(self, team: str, club: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO team(team_name, club_name) VALUES('{team}', '{club}');"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def return_team(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM team_example"
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return output

    def create_team2(self, team: str, club: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO team_example(team_name, club_name) VALUES('{team}', '{club}');"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def return_team1(self):
        cursor = self.con.cursor()
        query = """SELECT * FROM team_example ORDER BY random() LIMIT 1"""
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return records

    def return_team2(self):
        cursor = self.con.cursor()
        query = """SELECT * FROM team_example ORDER BY random() LIMIT 1"""
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return records

    def register_match(self, nb_match: int, match_name: str, team1: str, team2: str):
        cursor = self.con.cursor()
        table_name = " match" + str(nb_match)
        query = str(
            "INSERT INTO" + table_name + f"(match_name, team1, team2) VALUES('{match_name}','{team1}', '{team2}')")
        table = "CREATE TABLE IF NOT EXISTS " + table_name + "(id integer PRIMARY KEY, " \
                                                             "match_name text," \
                                                             "team1 text," \
                                                             "output1 integer," \
                                                             "team2 text," \
                                                             "output2 integer)"
        cursor.execute(table)
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def return_nb_match(self):
        cursor = self.con.cursor()
        query = f"SELECT * FROM nb_match"
        cursor.execute(query)
        output = cursor.fetchall()
        n = 0

        for row in output:
            n = n + 1

        cursor.close()
        self.con.commit()

        return n

    def match_nb_register(self):
        cursor = self.con.cursor()
        query = f"INSERT INTO nb_match(nb_match) VALUES({1})"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    '''def troutrou(self):

        i = 0
        while True:
            cursor = self.con.cursor()
            i = +1
            match_name = "match" + str(i)
            # try:
            query1 = f"SELECT * FROM {match_name}"
            cursor.execute(query1)
            # except:
            print("ok")
        self.con.commit()'''
    
    def return_all_team(self):
        cursor = self.con.cursor()
        query = f"SELECT * FROM team_example"
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        self.con.commit()
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> parent of 4cf90b7 (ajout location les conflits sont réglé a l'aide de ses con,naissances)
        return output


#DatabaseHandler.troutrou("database.db")
<<<<<<< HEAD
=======
>>>>>>> 116ac35 (ajout location)
=======
>>>>>>> 116ac35 (ajout location)
=======
>>>>>>> aa24cb2 (nouvelle méthiode de la baase de donnée)
=======
>>>>>>> parent of 4cf90b7 (ajout location les conflits sont réglé a l'aide de ses con,naissances)
