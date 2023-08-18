from object.object import Match, Team


class Prout:
    def __init__(self):
        self.database_handler1 = Match("database.db")
        self.selected_list = []
        self.match_list = []
        self.n = self.database_handler1.match_nb_return()
        self.database_handler2 = Team("database.db")

    def draw(self):
        w = self.database_handler2.return_team("team_example")
        x = len(w)#//2
        n = 1
        print(x)

        while True:
            output1 = self.database_handler2.return_rd_team_1()
            output2 = self.database_handler2.return_rd_team_2()

            for raw in output1:
                team1 = raw[1]
                club1 = raw[2]

            for raw in output2:
                team2 = raw[1]
                club2 = raw[2]

            if club1 == club2 and team1 not in self.selected_list and team2 not in self.selected_list:
                if n < x:
                    self.selected_list.append(team1)
                    self.selected_list.append(team2)
                    match_name = team1 + " vs " + team2
                    self.match_list.append([match_name, team1, team2])
                    n = n + 1
                    print(n)
                    print(match_name)
                else:
                    break
        print(self.selected_list)
        print(self.match_list)
        ls = []
        for x in range(len(self.match_list)):
            for y in range(3):
                for z in range(len(self.match_list)):
                    if z != x:
                        if self.match_list[x][y] == self.match_list[z][y]:
                            ls.append("nulos l'algo")
                        else:
                            pass
        print(ls)
        print(len(self.match_list))

    def test(self):
        print(self.database_handler2.return_team("team_example"))

x = Prout()
x.draw()
