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
    
    def return_match(self,n):
        output = self.database_handler.select(table=f"match_{self.json_handler.read_log(id=True)}_{n}",
                                              columns='*')
        return output

    def return_team(self):
        output = self.database_handler.select(columns='*', table='team')
        return output

    def new_competition(self, name, date, play_mod, location):
        self.database_handler.insert(table='general', 
                                     columns=['name', 'date', 'play_mod', 'location'],
                                     values=[name, date, play_mod, location])

    def create_team(self, name, club):
        self.database_handler.insert(table='team', 
                                     columns=['name', 'club'],
                                     values=[name, club])

    def register_result(self, row, n, output1, output2):
        table_name = f'match_{self.json_handler.read_log(id=True)}_{n}'
        self.database_handler.update(table=table_name,
                                     columns=['output1', 'output2'],
                                     value=[output1, output2],
                                     condition='id',
                                     condition_value=row)

    def return_general(self):
        output = self.database_handler.select(columns='*', table='general')
        return output

    def draw_random(self):
        '''last_players = []
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

        return match_list'''
        team_dict = data_dict(self.return_team())
        match_list = []

        for teams in team_dict.values():
            while len(teams) >= 2:
                team1, team2 = numpy.random.choice(teams, size=2, replace=False)
                teams.remove(team1)
                teams.remove(team2)
                match_list.append([team1, team2])

        last_players = [player for team_players in team_dict.values() for player in team_players]

        while len(last_players) >= 2:
            team1, team2 = numpy.random.choice(last_players, size=2, replace=False)
            last_players.remove(team1)
            last_players.remove(team2)
            match_list.append([team1, team2])

        if len(last_players) == 1:
            match_name = f"alone: {last_players[0]}"
            match_list.append(match_name)

        return match_list
    
    def set_overall(self):
        table_name = f'overall_{self.json_handler.read_log(id=True)}'
        dict_tot = self.dict_matchs_into_total()
        dict_main = self.matchs_into_dict()
        raw_columns = self.database_handler.pragma(table=table_name)
        columns = [column[1] for column in raw_columns if column[1].startswith('output')]
        for i in dict_main:
            if i in columns:
                pass
            else:
                self.database_handler.alter_table(name=i, table=table_name, type='INTEGER')
            self.database_handler.update(columns=i, 
                                    table=table_name, 
                                    value=[n for sl in [list(i.values()) for i in dict_main[i]] for n in sl], 
                                    condition='team',
                                    condition_value=[n for sl in [list(i.keys()) for i in dict_main[i]] for n in sl])
        
        self.database_handler.update(columns='total', 
                                table=table_name, 
                                value=[dict_tot[i] for i in dict_tot], 
                                condition='team',
                                condition_value=[i for i in dict_tot])

    def get_match_n(self):
        ls = []
        n = 0
        tables_names = self.database_handler.select(columns='name', table='sqlite_master', condition='type', condition_value="'table'")
        for row in tables_names:
            ls.append(row[0])
        for i in ls:
            if i.startswith(f"match_{self.json_handler.read_log(id=True)}"):
                n = n+1
            else:
                pass
        return n
    
    def matchs_into_dict(self):
        id = self.json_handler.read_log(id=True)
        dicto = {}
        n = self.get_match_n()
        for i in range(n):
            output = self.database_handler.select(columns='*', table=f"match_{id}_{i}")
            for row in output:
                dicto.setdefault(f'output{i}', []).append({row[1]:row[2]})
                dicto.setdefault(f'output{i}', []).append({row[3]:row[4]})
        
        return dicto
    
    def dict_matchs_into_total(self):
        main = self.matchs_into_dict()
        dicto = {}
        for i in main:
            for j in main[i]:
                var = list(j.keys())
                key = var[0]
                if key in dicto:
                    dicto[key] = dicto[key] + j[key]
                    
                else:
                    dicto[key] = j[key]
        return dicto
    
    def register_match(self, list):
        n = self.get_match_n()
        name_ = f'match_{self.json_handler.read_log(id=True)}_{n}'
        self.database_handler.create_table(match=True, 
                                           name=name_)
        for i in list:
            self.database_handler.insert(table=name_,
                                         columns=['team1', 'output1','team2', 'output2'],
                                         values=[f"{i[0]}", 0, f"{i[1]}", 0])

    def return_overall_col(self):
        team = self.database_handler.select(table=f"overall_{self.json_handler.read_log(id=True)}",
                                     columns='team')
        team = self.database_handler.select(table=f"overall_{self.json_handler.read_log(id=True)}",
                                     columns='team')
    
'''test = Application()
output = test.dict_matchs_into_total()
print(output)'''