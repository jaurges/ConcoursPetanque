import random
import sys
sys.path.append('.')
from src.application import Application
from src.database_handler import DatabaseHandler
from src.json_handler import JsonHandler
import csv
import pandas as pd
import sqlite3
import re

club_name_fix = ["club1", "club2", "club3"]


def add_team_database(n):
    x=0
    for i in range(n):
        x = x+1
        app = Application()
        team = "équipe" + str(x)
        club = random.choice(club_name_fix)

        #app.create_team(team, club)
        print(team, club)

ls1 = []
ls2= []
ls3=[]
ls_ls = [ls1, ls2, ls3]
def add_team_csv(n):
    for i in range(n):
        team_name = "team" + str(i+1)
        ls = random.choice(ls_ls)
        ls.append(team_name)
    df1 = pd.DataFrame({'club1': ls1})
    df2 = pd.DataFrame({'club2': ls2})
    df3 = pd.DataFrame({'club3': ls3})
    pd.concat([df1,df2, df3],axis=1).to_csv('team_1.csv', index = False)

def create_match(n):
    app = Application()
    database_handler = DatabaseHandler()
    for i in range(n):
        match_list = app.draw()
        database_handler.create_table(match=True, name=f'match_example_{i}')
        for row in match_list:
            output1 = random.randint(0,13)
            output2 = random.randint(0,13)
            database_handler.insert(table=f'match_example_{i}', columns=['team1', 'output1','team2', 'output2'], values=[row[0], output1, row[1], output2])

def get_number_of_match(competition_id):
    ls = []
    n = 0
    database_handler = DatabaseHandler()
    tables_names = database_handler.select(columns='name', table='sqlite_master', condition='type', condition_value="'table'")
    for row in tables_names:
        ls.append(row[0])
    for i in ls:
        if i.startswith(f"match_{competition_id}"):
            n = n+1
        else:
            pass
    return n


def main_dicto():
    json_hanlder = JsonHandler()
    database_handler = DatabaseHandler()
    id = 'example'#json_hanlder.read_log(id=True)
    dicto = {}
    n = get_number_of_match(id)
    for i in range(n):
        output = database_handler.select(columns='*', table=f"match_{id}_{i}")
        for row in output:
            dicto.setdefault(f'output{i}', []).append({row[1]:row[2]})
            dicto.setdefault(f'output{i}', []).append({row[3]:row[4]})
    #liste_de_listes = [list(i.values()) for i in dicto['output0']]
    #liste_aplatie = [nombre for sous_liste in liste_de_listes for nombre in sous_liste]
    return dicto#[nombre for sous_liste in [list(i.values()) for i in dicto['output0']] for nombre in sous_liste]
    

def total():
    main = main_dicto()
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

def add_to_overall():
    id = 'example'
    table = f'overall_{id}'
    total_ = total()
    main_dict = main_dicto()
    database_handler = DatabaseHandler()
    raw_columns = database_handler.pragma(table=table)
    columns = [column[1] for column in raw_columns if column[1].startswith('output')]
    for i in main_dict:
        if i in columns:
            pass
        else:
            database_handler.alter_table(name=i, table=table, type='INTEGER')
        database_handler.update(columns=i, 
                                table=table, 
                                value=[n for sl in [list(i.values()) for i in main_dict[i]] for n in sl], 
                                condition='team',
                                condition_value=[n for sl in [list(i.keys()) for i in main_dict[i]] for n in sl])
    
    database_handler.update(columns='total', 
                            table=table, 
                            value=[total_[i] for i in total_], 
                            condition='team',
                            condition_value=[i for i in total_])
    '''print([i for i in total_])
    print([total_[i] for i in total_])'''


def add_team_overall(n):
    x=0
    database_handler = DatabaseHandler()
    for i in range(n):
        x = x+1
        team = "team" + str(x)
        database_handler.insert(table="overall_example", 
                                columns=['team', 'output0', 'output1', 'output2', 'output3', 'output4','total'],
                                values=[f"{team}", str(None), str(None), str(None), str(None), str(None), str(None)])

def draw_by_overall():
    '''database_handler = DatabaseHandler()
    json_hanlder = JsonHandler()
    table_ = f"overall_{json_hanlder.read_log(id=True)}"
    overall = database_handler.select(table=table_, columns=['team','total'])
    
    dict_overall = {}
    for row in overall:
        dict_overall[row[0]]= row[1]
    print(dict_overall)
    num = [n for n in dict_overall.values()]
    num_class = []
    for _ in range(len(num)):
        n = max(num)
        num_class.append(n)
        num.remove(n)
    print(num_class)
    team_list = [team for team in dict_overall.keys()]
    team_class = []
    for value_ in num_class:
        key_asso = next(key for key, value in dict_overall.items() if value == value_ and key in team_list)
        team_list.remove(key_asso)
        team_class.append(key_asso)
    print(team_class)
    match_list = []
    for i in range(0, len(team_class), 2):
        print(i)
        match_list.append([team_class[i], team_class[i+1]])
    print(match_list)'''
    database_handler = DatabaseHandler()
    json_handler = JsonHandler()
    table_name = f"overall_{json_handler.read_log(id=True)}"
    
    overall = database_handler.select(table=table_name, columns=['team', 'total'])
    
    dict_overall = dict(overall)
    print(dict_overall)
    grouped_by_value = {}
    [grouped_by_value.setdefault(value, []).append(key) for key, value in dict_overall.items()]

    grouped_by_value = list(grouped_by_value.values())

    print(grouped_by_value)
    
    # Tri par ordre décroissant des valeurs et récupération des équipes classées
    team_class = [key for key, _ in sorted(dict_overall.items(), key=lambda x: x[1], reverse=True)]
    #print(team_class)
    
    # Création des paires d'équipes
    match_list = [team_class[i:i+2] for i in range(0, len(team_class), 2)]
    #print(match_list)

def meilleur_grind():
    # 1ere phase : qui a gagné la dernière manche, si encore égalité suivante
    database_handler = DatabaseHandler()
    json_handler = JsonHandler()
    table_name = f"overall_{json_handler.read_log(id=True)}"
    # 2eme phase : qui a gagné le plus grand écart de point dans cette manche, si encore égalité suivante

    # 3eme phase : qui a gagné le plus grand écart de point sur tout ses matchs 
    pass


draw_by_overall()