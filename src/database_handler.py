'''
a jugé pour les stats si l'objet ne serait pas plus efficace et maintenable
'''

import sqlite3
import os


class DatabaseHandler:
    def __init__(self, database_name: str):
        #self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        chemin = os.path.abspath(__file__)
        self.con = sqlite3.connect(f"{os.path.abspath(os.path.join(chemin, '..', '..'))}/data/{database_name}")
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
        data_directory = f"{os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))}/data/competition"
        data_directory = os.path.join(data_directory, file_name)
        os.makedirs(data_directory, exist_ok=True)
        self.directory = f"{os.path.dirname(os.path.abspath(__file__))}" + "/".join(["/competition", file_name,
                                                                                f"{file_name}.db"])
        self.directory = self.directory.replace("src", "data")
        con = sqlite3.connect(self.directory)
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

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
                "start_hour text," \
                "finish_hour text," \
                "match_hour text)"
        insertion = (f"INSERT INTO parameters(name, date, play_mod, location) VALUES('{name}', '{date}', '{play_mod}', "
                     f"'{location}')")

        cursor.execute(table1)
        cursor.execute(table2)
        cursor.execute(table3)
        cursor.execute(insertion)

        cursor.close()
        self.con.commit()
        con.commit()

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

    def return_team_example(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM team_example"
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return output

    def create_team2(self, team: str, club: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO team_example(name, club) VALUES('{team}', '{club}');"
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
        #database_name = f"competition/{ls[0]}_{ls[1]}_{ls[2]}_{ls[3]}/{ls[0]}_{ls[1]}_{ls[2]}_{ls[3]}.db"
        database_name = "competition/competition_example.db"
        chemin = os.path.abspath(__file__)
        file_name = f"{os.path.abspath(os.path.join(chemin, '..', '..'))}/data/{database_name}"
        cursor.close()
        self.con.commit()

        return file_name
    
    def return_nb_match(self):
        n = 0
        # dir = self.return_actual_dir()
        database_name = f"competition/competition_example.db"
        chemin = os.path.abspath(__file__)
        dir = f"{os.path.abspath(os.path.join(chemin, '..', '..'))}/data/{database_name}"
        con = sqlite3.connect(dir)
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table'"
        cursor.execute(query)
        output = cursor.fetchall()
        for _ in output:
            n = n + 1
        n = n - 4
        cursor.close()
        con.commit()
        return n
    
    def return_team_per_row(self, current_row, n):
        dir = self.return_actual_dir()
        con = sqlite3.connect(dir)
        #con.row_factory = sqlite3.Row
        cursor = con.cursor()
        match_id = f"match{n}"
        ls = []
        query = f"SELECT team1, team2 FROM {match_id} WHERE id={current_row}"
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        con.commit()

        return output

    def return_n_match(self, n):
        dir = self.return_actual_dir()
        con = sqlite3.connect(dir)
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        match = "match" + str(n)
        query = f"SELECT * FROM {match}"
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        con.commit()

        return output

    def test(self):
        name = 'prout'
        date = 'zizi'
        play_mod = 'triplandouille'
        location = 'boulogone sur mer'
        file_name = (f"{name.replace(' ', '')}_{date.replace(' ', '')}_"
                     f"{play_mod.replace(' ', '')}_{location.replace(' ', '')}")
        data_directory = f"{os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))}/data/competition"
        data_directory = os.path.join(data_directory, file_name)
        os.makedirs(data_directory, exist_ok=True)
        self.directory = f"{os.path.dirname(os.path.abspath(__file__))}" + "/".join(["/competition", file_name,
                                                                                f"{file_name}.db"])
        self.directory = self.directory.replace("src", "data")
        print(self.directory)
    
    def insert_team_into_match(self, n, q):
        dir = self.return_actual_dir()
        print(dir)
        con = sqlite3.connect(dir)
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        match_name = f"match{q}"
        for i in range(n):
            team1 = f"team{i}"
            team2 = f"team{i}{i}"
            opponent = f"{team1} vs {team2}"
            query = f"INSERT INTO {match_name}(match_name, team1, team2) VALUES('{opponent}', '{team1}', '{team2}');"
            cursor.execute(query)
            print(query)
        cursor.close()
        con.commit()

    def register_result(self, current_row, n, output1, output2):
        dir = self.return_actual_dir()
        print(dir)
        con = sqlite3.connect(dir)
        cursor = con.cursor()
        query = f"UPDATE match{n} SET output1={output1}, output2={output2} WHERE id={current_row}"
        print(query)
        cursor.execute(query)
        cursor.close()
        con.commit()

test = DatabaseHandler("databasev2.db")
test.register_result(2, 3, 6, 26)
