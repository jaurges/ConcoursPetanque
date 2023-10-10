'''
a jugé pour les stats si l'objet ne serait pas plus efficace et maintenable
'''

import sqlite3
import os


class DatabaseHandler:
    def __init__(self, database_name: str):
        #self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        chemin = os.path.abspath(__file__)
        try:
            self.con = sqlite3.connect(f"{os.path.abspath(os.path.join(chemin, '..', '..'))}/data/{database_name}")
            print(f"{os.path.abspath(os.path.join(chemin, '..', '..'))}/data/{database_name}")
        except:
            print("\n##################prout#############\n")
        self.con.row_factory = sqlite3.Row
        self.directory = str

    def create_competition(self, name: str, date: str, play_mod: str, location: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO general(name, date, play_mod, location) VALUES('{name}', '{date}', '{play_mod}', '{location}');"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

        file_name = (f"{name.replace(' ', '')}_{date.replace(' ', '')}_"
                     f"{play_mod.replace(' ', '')}_{location.replace(' ', '')}")
        data_directory = os.path.join(f"{os.path.dirname(os.path.abspath(__file__))}", '..', 'data/competition')
        data_directory = os.path.join(data_directory, file_name)
        os.makedirs(data_directory, exist_ok=True)
        self.directory = f"{os.path.dirname(os.path.abspath(__file__))}" + "/".join(["/competition", file_name,
                                                                                f"{file_name}.db"])
        self.directory = self.directory.replace("gui", "data")
        self.con = sqlite3.connect(self.directory)
        self.con.row_factory = sqlite3.Row
        cursor = self.con.cursor()

        table1 = "CREATE TABLE IF NOT EXISTS parameters(id integer PRIMARY KEY, " \
                "name text," \
                "date text," \
                "play_mod text," \
                "location text)"
        table2 = "CREATE TABLE IF NOT EXISTS overall(id integer PRIMARY KEY, " \
                "team text," \
                "output1 integer," \
                "total integer)"
        table3 = "CREATE TABLE IF NOT EXISTS time(id integer PRIMARY KEY, " \
                "start_hour integer," \
                "finish_hour integer," \
                "match_hour integer)"
        insertion = (f"INSERT INTO parameters(name, date, play_mod, location) VALUES('{name}', '{date}', '{play_mod}', "
                     f"'{location}')")

        cursor.execute(table1)
        cursor.execute(table2)
        cursor.execute(table3)
        cursor.execute(insertion)

        cursor.close()
        self.con.commit()

    def create_team(self, team: str, club: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO team(name, club) VALUES('{team}', '{club}');"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def return_team(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM team"
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        self.con.commit()
        #print(output)

        return output

    '''def return_team_example(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM team_example"
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return output'''

    def create_team2(self, team: str, club: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO team_example(team_name, club_name) VALUES('{team}', '{club}');"
        cursor.execute(query)
        cursor.close()
        self.con.commit()


    def register_match(self, match_name: str, team1: str, team2: str):
        self.con = sqlite3.connect(self.directory)
        self.con.row_factory = sqlite3.Row
        cursor = self.con.cursor()
        n = self.return_nb_match() + 1
        table_name = str("match" + n)
        table = "CREATE TABLE IF NOT EXISTS " + table_name + "(id integer PRIMARY KEY, " \
                                                             "match_name text," \
                                                             "team1 text," \
                                                             "output1 integer," \
                                                             "team2 text," \
                                                             "output2 integer)"
        insertion = str("INSERT INTO" + table_name + f"(match_name, team1, team2) VALUES('{match_name}','{team1}', '{team2}')")
        cursor.execute(table)
        cursor.execute(insertion)
        cursor.close()
        self.con.commit()          

    
    def return_actual_dir(self):
        cursor = self.con.cursor()
        query = "SELECT seq FROM sqlite_sequence WHERE name='general'"
        cursor.execute(query)
        num = cursor.fetchall()
        for i in num:
            num = i[0]
        query = f"SELECT name, date, play_mod, location FROM general WHERE id={num}"
        cursor.execute(query)
        output = cursor.fetchall()
        ls = []
        for i in output:
            ls.append(i[0])
            ls.append(i[1])
            ls.append(i[2])
            ls.append(i[3])
        file_name = f"competition/{ls[0]}_{ls[1]}_{ls[2]}_{ls[3]}.db"
        cursor.close()
        self.con.commit()

        return file_name
    
    def return_nb_match(self):
        n = 0
        dir = self.return_actual_dir()
        self.con = sqlite3.connect(dir)
        self.con.row_factory = sqlite3.Row
        cursor = self.con.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table'"
        cursor.execute(query)
        output = cursor.fetchall()
        for _ in output:
            n = n + 1
        n = n - 3
        cursor.close()
        self.con.commit()
        return n