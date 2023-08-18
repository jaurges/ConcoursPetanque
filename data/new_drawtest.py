import sqlite3
import os
import random
import numpy
from time import sleep


class Application:
    def __init__(self, database_name: str):
        self.match_list = []
        self.last_players = []
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

        return records

    def create_team(self, team: str, club: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO team_example(team_name, club_name) VALUES('{team}', '{club}');"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def del_table(self):
        cursor = self.con.cursor()
        query  = "DROP TABLE team_example;"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def create_team_example(self):
        cursor = self.con.cursor()
        query = "CREATE TABLE IF NOT EXISTS team_example(id integer PRIMARY KEY,team_name text,club_name text);"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def test_draw(self):
        for o in range(5000):
            self.create_team_example()
            club_name = ["ASC Cordemais", "Bouée", "StEtienne", "Savenay"]
            club_removable = club_name
            list_club = []
            number_of_club = random.randint(1,4)
            number_of_players = random.randint(0,49)

            for _ in range(number_of_club):
                club = random.choice(club_removable)
                club_removable.remove(club)
                list_club.append(club)
            #print(list_club)

            for i in range(number_of_players):
                team_name = "team" + str(i+1)
                club_team = random.choice(list_club)
                self.create_team(team_name, club_team)

            #print("tirage : " + str(o + 1))
            #self.draw1()
            self.draw2()
            #print("\n")
            self.del_table()


    def draw1(self):
        """premier tirage soit tirage de match équipe de mm club contre équipe de
        mm club""" # add a var pour les équipes qui jouent pas
        self.match_list = []
        self.last_players = []
        n = 0
        output = self.return_team_all()
        dict_club = {}
        even = []
        key_dict = {}
        for row in output:
            key = row[2]
            value = row[1]
            dict_club.setdefault(key, []).append(value)
            n = n + 1
        dict_club_var = dict_club

        print(n)

        n = 0
        for i in dict_club.keys():
            n = n + 1
            if len(dict_club[i]) % 2 == 0:
                even.append(True)
                key_dict[n] = i
                #print(k)
                #print(len(dict_club[k]))
                #print(n)
            else:
                even.append(False)
                key_dict[n] = i
        print(even)
        print(key_dict)

        n = 0
        if all(x == even[0] for x in even):
            print("visiblement pair")
            for i in dict_club:
                #print(len(dict_club[i]))
                for _ in range(len(dict_club[i])//2):
                    team1 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team1)
                    team2 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team2)
                    #n = n + 1

                    match_name = str(team1 + " vs " + team2)
                    self.match_list.append([match_name, team1, team2])
                #print(n)
            #print(self.match_list)
            #print(dict_club_var)

        else:
            n = 0
            for i in even:
                n = n + 1
                if i:
                    for _ in range(len(dict_club_var[key_dict[n]])//2):
                        team1 = random.choice(dict_club_var[key_dict[n]])
                        dict_club_var[key_dict[n]].remove(team1)
                        team2 = random.choice(dict_club_var[key_dict[n]])
                        dict_club_var[key_dict[n]].remove(team2)

                        match_name = str(team1 + " vs " + team2)
                        self.match_list.append([match_name, team1, team2])
                    #print(self.match_list)
                    #print(dict_club_var)
                else:
                    for _ in range(len(dict_club_var[key_dict[n]])//2):
                        team1 = random.choice(dict_club_var[key_dict[n]])
                        dict_club_var[key_dict[n]].remove(team1)
                        team2 = random.choice(dict_club_var[key_dict[n]])
                        dict_club_var[key_dict[n]].remove(team2)

                        match_name = str(team1) + " vs " + str(team2)
                        self.match_list.append([match_name, team1, team2])
                        self.last_players.append(dict_club_var[key_dict[n]])
                    #print(self.match_list)
            #print(dict_club_var)
            n = 0
            for _ in range(len(self.last_players)):
                n = n + 1
            if n % 2 == 0:
                for _ in range(len(self.last_players) // 2):
                    team1 = random.choice(self.last_players)
                    self.last_players.remove(team1)
                    team2 = random.choice(self.last_players)
                    self.last_players.remove(team2)

                    match_name = str(team1) + " vs " + str(team2)
                    self.match_list.append([match_name, team1, team2])
                #print(dict_club_var)
                #print(self.last_players)
            else:
                for i in range(n):
                    if n <= 1:
                        team_name = "sans match : " + str(self.last_players)
                        self.match_list.append(team_name)
                    else:
                        team1 = random.choice(self.last_players)
                        self.last_players.remove(team1)
                        team2 = random.choice(self.last_players)
                        self.last_players.remove(team2)

                        match_name = str(team1) + " vs " + str(team2)
                        self.match_list.append([match_name, team1, team2])
                        n = n - 2
        print(self.last_players)
        print(dict_club_var)
        print(self.match_list)


        ls = []
        for x in range(len(self.match_list)):
            for y in range(3):
                for z in range(len(self.match_list)):
                    if z != x:
                        if self.match_list[x][y] == self.match_list[z][y]:
                            ls.append("nulos l'algo")
                        else:
                            #ls.append("c good")
                            pass
        if all(x == "c good" for x in ls):
            print("c good")
        #print(len(self.match_list))
        print(ls)

    def draw2(self):
        self.match_list = []
        self.last_players = []
        n = 0
        output = self.return_team_all()
        dict_club = {}
        even = []
        key_dict = {}
        for row in output:
            key = row[2]
            value = row[1]
            dict_club.setdefault(key, []).append(value)
            n = n + 1
        dict_club_var = dict_club

        #print(n)
        '''
        n = 0
        for i in dict_club.keys():
            n = n + 1
            if len(dict_club[i]) % 2 == 0:
                even.append(True)
                key_dict[n] = i
                # print(k)
                # print(len(dict_club[k]))
                # print(n)
            else:
                even.append(False)
                key_dict[n] = i
        print(even)
        print(key_dict)
        '''

        n = 0
        for i in dict_club:
            #print(i)
            #print(len(dict_club[i]))
            if len(dict_club[i]) % 2 == 0:
                for _ in range(len(dict_club[i])//2):
                    team1 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team1)
                    team2 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team2)
                    #n = n + 1

                    match_name = str(team1 + " vs " + team2)
                    self.match_list.append([match_name, team1, team2])
            else:
                #print("attention : " + str(len(dict_club[i])//2))
                for _ in range(len(dict_club[i])//2):
                    team1 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team1)
                    team2 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team2)
                    #n = n + 1

                    match_name = str(team1 + " vs " + team2)
                    self.match_list.append([match_name, team1, team2])
                for value in dict_club_var[i]:
                    self.last_players.append(value)
                #dict_club_var[i].remove(dict_club_var[i])
            #print(self.last_players)
        if len(self.last_players) >= 2:
            for _ in range(len(self.last_players) // 2):
                team1 = numpy.random.choice(self.last_players)
                self.last_players.remove(team1)
                team2 = numpy.random.choice(self.last_players)
                self.last_players.remove(team2)
                match_name = str(team1 + " vs " + team2)
                self.match_list.append([match_name, team1, team2])
            if not self.last_players:
                pass
            else:
                match_name = "le solo : " + str(self.last_players)
                self.match_list.append(match_name)
                for value in self.last_players:
                    self.last_players.remove(value)
        elif not self.last_players:
            pass
        else:
            match_name = "le solo : " + str(self.last_players)
            self.match_list.append(match_name)
            for value in self.last_players:
                self.last_players.remove(value)

        ls = []
        for x in range(len(self.match_list)):
            for y in range(3):
                for z in range(len(self.match_list)):
                    if z != x:
                        if self.match_list[x][y] == self.match_list[z][y]:
                            #ls.append("nulos l'algo")
                            print("nulos l'algo")
                        else:
                            # ls.append("c good")
                            pass
        #if all(x == "c good" for x in ls):
            #print("c good")
        # print(len(self.match_list))
        #print(ls)
        #print(self.last_players)
        #print(self.match_list)
        #print(len(self.match_list))


x = Application("file::memory:?cache=shared")
x.test_draw()