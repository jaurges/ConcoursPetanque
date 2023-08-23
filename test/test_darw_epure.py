import random
import numpy


class Application:
    def __init__(self):
        self.match_list = []
        self.last_players = []
        self.dict_club = {}
        self.activated_print = bool

    def test_draw(self):
        for _ in range(200):
            self.activated_print = False
            self.match_list = []
            self.last_players = []
            self.dict_club = {}
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

            self.draw()
            if len(self.last_players) == 1:
                match_name = "alone : " + str(self.last_players)
                self.match_list.append(match_name)
                for value in self.last_players:
                    self.last_players.remove(value)
            
            if not self.n//2 + 1 == len(self.match_list) and self.n != 1 and self.n!=0 and not self.n%2==0:
                self.activated_print = True
                print(self.dict_club)
                print("the half of that: " + str(self.n))
                print("is it equal ?" + str(len(self.match_list)))
                print(self.match_list)
                print("last players : ")
                print(self.last_players)
                print("\n")    

    def draw(self):  
        dict_club_var = self.dict_club
        self.n = 0
        for i in self.dict_club:
            self.n = self.n + len(self.dict_club[i])

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
            
        elif len(self.last_players) == 0:
            pass

x = Application()
x.test_draw()