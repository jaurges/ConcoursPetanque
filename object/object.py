import sqlite3
import os


class Player:
    def __init__(self):
        pass


class Match:
    def __init__(self, database_name: str):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = dir_path.replace("object", "data") + f"//{database_name}"
        self.con = sqlite3.connect(path)
        self.con.row_factory = sqlite3.Row

    def register_match(self, nb_match: int, match_name: str, team1: str, team2: str):
        cursor = self.con.cursor()
        table_name = " match" + str(nb_match)
        query = str("INSERT INTO" + table_name + f"(match_name, team1, team2) VALUES('{match_name}','{team1}', '{team2}')")
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

    def register_result(self, row: int, nb_match: int, output1: int, output2: int):
        cursor = self.con.cursor()
        table_name = "match" + str(nb_match)
        row = str(row)
        query = f"UPDATE " + table_name + f" SET output1 = {output1}, output2 = {output2} WHERE rowid = {row};"
        cursor.execute(query)
        cursor.close()
        self.con.commit()
        print(query)

    def match_nb_return(self):
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

    def return_match(self, n):
        cursor = self.con.cursor()
        match = "match" + str(n)
        query = f"SELECT * FROM {match}"
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return output


class Team:
    def __init__(self, database_name: str):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = dir_path.replace("object", "data") + f"//{database_name}"
        self.con = sqlite3.connect(path)
        self.con.row_factory = sqlite3.Row

    def create_team(self, team: str, club: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO team(team_name, club_name) VALUES('{team}', '{club}');"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def return_team(self, team):  #team_example
        cursor = self.con.cursor()
        query = f"SELECT * FROM {team}"
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return output

    def return_rd_team_1(self):
        cursor = self.con.cursor()
        query = """SELECT * FROM team_example ORDER BY random() LIMIT 1"""
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return records

    def return_rd_team_2(self):
        cursor = self.con.cursor()
        query = """SELECT * FROM team_example ORDER BY random() LIMIT 1"""
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return records

    def return_team_per_row(self, row: int, nb_match: int):
        output = []
        cursor = self.con.cursor()
        table_name = "match" + str(nb_match)
        row = str(row)
        query = str("SELECT team1, team2 FROM " + table_name + " WHERE rowid = " + row)
        cursor.execute(query)
        team1, team2 = cursor.fetchone()
        cursor.close()
        self.con.commit()
        output.append(team1)
        output.append(team2)

        return output


class Competition:
    def __init__(self, database_name: str):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = dir_path.replace("object", "data") + f"//{database_name}"
        self.con = sqlite3.connect(path)
        self.con.row_factory = sqlite3.Row

    def save_parameters(self, name: str, date: str, play_mod: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO parameters(name, date, play_mod) VALUES('{name}', '{date}', '{play_mod}');"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def set_classement(self):

        for i in range(0,100):
            cursor = self.con.cursor()
            match_name = "match" + str(i)
            query1 = f"SELECT * FROM {match_name}"
            try :
                cursor.execute(query1)
            except sqlite3.OperationalError:
                break

        self.con.commit()


class Club:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams
