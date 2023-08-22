import random
import numpy


class Application:
    def __init__(self):
        self.match_list = []
        self.last_players = []
        self.dict_club = {}

    def test_draw(self):
        for o in range(20):
            club_name = ["club1", "club2", "club3", "club4"]
            club_removable = club_name
            list_club = []
            number_of_club = random.randint(1,4)
            number_of_players = random.randint(0,19)

            for _ in range(number_of_club):
                club = random.choice(club_removable)
                club_removable.remove(club)
                list_club.append(club)

            for i in range(number_of_players):
                team_name = "team" + str(i+1)
                club_team = random.choice(list_club)
                self.dict_club.setdefault(club_team, []).append(team_name)
                print(team_name)

            self.draw()

    def draw(self):
        self.match_list = []
        self.last_players = []
        self.dict_club = {}
        dict_club_var = self.dict_club
        n = 0
        for i in self.dict_club:
            n = n + len(self.dict_club[i])
        print("the half of that: " + str(n))

        for i in self.dict_club:
            if len(self.dict_club[i]) % 2 == 0:
                for _ in range(len(self.dict_club[i])//2):
                    team1 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team1)
                    team2 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team2)
                    match_name = str(team1 + " vs " + team2)
                    self.match_list.append([match_name, team1, team2])
            else:
                for _ in range(len(self.dict_club[i])//2):
                    team1 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team1)
                    team2 = numpy.random.choice(dict_club_var[i])
                    dict_club_var[i].remove(team2)
                    match_name = str(team1 + " vs " + team2)
                    self.match_list.append([match_name, team1, team2])
                for value in dict_club_var[i]:
                    self.last_players.append(value)
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
                match_name = "alone : " + str(self.last_players)
                self.match_list.append(match_name)
                for value in self.last_players:
                    self.last_players.remove(value)
        else:
            match_name = "alone : " + str(self.last_players)
            self.match_list.append(match_name)
            for value in self.last_players:
                self.last_players.remove(value)

        print("is it equal ?" + str(len(self.match_list)))
        ls = []
        for x in range(len(self.match_list)):
            for y in range(3):
                for z in range(len(self.match_list)):
                    if z != x:
                        if self.match_list[x][y] == self.match_list[z][y]:
                            ls.append("fail")
                        else:
                            pass
        if all(x == "ok" for x in ls):
            print("ok")
        else:
            print("fail")

        print("\n")

        self.last_print()

    def last_print(self):
        print(self.dict_club)
        print(self.match_list)


x = Application()
x.test_draw()