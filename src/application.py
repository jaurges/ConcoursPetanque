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

    def return_overall(self):
        output = self.database_handler.select(table=f"overall_{self.json_handler.read_log(id=True)}",
                                     columns='*')
        return output
    
    def overall(self):
        table_name1 = f"overall_{self.json_handler.read_log(id=True)}"
        grouped_by_value = {}
        inter_class = {}
        grouped_by_value_ls = []
        
        overall = self.database_handler.select(table=table_name1, columns=['team', 'total'])
        dict_overall = dict(overall)
        [grouped_by_value.setdefault(value, []).append(key) for key, value in dict_overall.items()]

        for i in grouped_by_value.values():
            if len(i) >= 2:
                grouped_by_value_ls.append(i)
            else:
                pass
        for i in grouped_by_value_ls:
            inter_class[tuple(i)]=[]
        
        # à mettre à -1 quand match_example_5 sera rempli
        n_match = self.get_match_n()-2
        match_name = f"match_{self.json_handler.read_log(id=True)}_{n_match}"
        match_raw = self.database_handler.select(table=match_name, columns='*')
        match_ls = [[row[1], row[2], row[3], row[4]] for row in match_raw]

        winner=[[],[]]
        for i in match_ls:
            if i[1]>i[3]:
                winner[0].append(i[0])
            if i[1]<i[3]:
                winner[0].append(i[2])
            if i[1]==i[3]:
                winner[1].append([i[0],i[2]])
        
        for i in grouped_by_value_ls:
            stock = []
            ls_removable = []
            for j in i:
                if j in winner[0]:
                    stock.append(1)
                else:
                    stock.append(0)
            if stock.count(1)==1:
                ls_removable.append({i[stock.index(1)]:'better'})
            if stock.count(0)==1:
                ls_removable.append({i[stock.index(0)]:'worse'})

            inter_class[tuple(i)]=[0 for _ in i]

            for k in ls_removable:
                key, value = k.popitem()
                if value=='better':
                    for j in range(len(i)):
                        if i[j] == key:
                            inter_class[tuple(i)][j]=100
                        else:
                            pass
                if value=='worse':
                    for j in range(len(i)):
                        if i[j] == key:
                            inter_class[tuple(i)][j]=-100
                        else:
                            pass
            
        stock = []
        for i in inter_class.items():
            key, value = i[0], i[1]
            if value.count(min(value)) and value.count(max(value))>=2:
                for j in key:
                    if value[key.index(j)]==0:
                        stock.append(j)
                    else:
                        pass
            else: 
                pass

        gap_dict = {}
        for i in match_ls:
            if i[0] in stock:
                gap_dict[i[0]]=i[1]-i[3]
            if i[2] in stock:
                gap_dict[i[2]]=i[3]-i[1]

        items_list = [i for i in gap_dict.items()]
        combined_ls = list(zip(stock, items_list))
        ls_classed = sorted(combined_ls, key=lambda x: x[0], reverse=True)
        stock, class_teams_lst = zip(*ls_classed)
        
        for i in class_teams_lst:
            for j in inter_class.keys():
                if i[0] in j:
                    index = j.index(i[0])
                    inter_class[j][index]=i[1]
                else: 
                    pass

        sorted_dict = dict(sorted(grouped_by_value.items(), key=lambda item: item[0], reverse=True))

        final_overall = []
        for i in sorted_dict.items():
            key, value = i[0], i[1]
            if len(value)>=2:
                for j in inter_class.keys():
                    if j==tuple(value):
                        for _ in range(len(j)):
                            index_max = inter_class[j].index(max(inter_class[j]))
                            team = j[index_max]
                            final_overall.append(team)
                            inter_class[j][index_max] = -1000
                    else:
                        pass
            else:
                final_overall.append(value)

        flat_list = [item[0] if isinstance(item, list) else item for item in final_overall]
        #match_list = [final_overall[i:i+2] for i in range(0, len(final_overall), 2)]
        
        return flat_list

    def draw_overall(self):
        flat_list = self.overall()
        match_list = [flat_list[i:i+2] for i in range(0, len(flat_list), 2)]

        return match_list


    
'''test = Application()
output = test.draw_overall()
print(output)'''