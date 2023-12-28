import sys
sys.path.append('.')
from src.database_handler import DatabaseHandler
from src.json_handler import JsonHandler
import numpy
from utils.utils import data_dict

class Application:
    def __init__(self):
        self.database_handler = DatabaseHandler()
        self.json_handler = JsonHandler()
    
    def set_competition_index(self, parameters:list):
        self.json_handler.write_log(parameters)

    def return_team(self):
        output = self.database_handler.select(columns='*', table='team')
        return output

    def return_nb_match(self):
        pass

    def return_team_per_row(self, row):
        pass

    def new_competition(self, name, date, play_mod, location):
        self.database_handler.insert(table='general', 
                                     columns=['name', 'date', 'play_mod', 'location'],
                                     values=[name, date, play_mod, location])

    def create_team(self, name, club):
        self.database_handler.insert(table='team', 
                                     columns=['name', 'club'],
                                     values=[name, club])

    def register_result(self, row, n, output1, output2):
        pass

    def return_general(self):
        output = self.database_handler.select(columns='*', table='general')
        return output

    def draw(self):
        last_players = []
        match_list = []
        dicto1 = data_dict(self.return_team())
        dicto2 = dicto1

        for i in dicto2:
            for _ in range(len(dicto2[i])//2):
                team1 = numpy.random.choice(dicto1[i])
                dicto1[i].remove(team1)
                team2 = numpy.random.choice(dicto1[i])
                dicto1[i].remove(team2)
                match_list.append([team1, team2])
            for value in dicto1[i]:
                last_players.append(value)
        if len(last_players) >= 2:
            for _ in range(len(last_players) // 2):
                team1 = numpy.random.choice(last_players)
                last_players.remove(team1)
                team2 = numpy.random.choice(last_players)
                last_players.remove(team2)
                match_list.append([team1, team2])
        
        if len(last_players) == 1:
                match_name = "alone : " + str(last_players)
                match_list.append(match_name)
                for value in last_players:
                    last_players.remove(value)
            
        elif len(last_players) == 0:
            pass

        return match_list
    
'''test = Application()
output = test.draw()
print(output)'''