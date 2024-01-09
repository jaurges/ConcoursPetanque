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
    database_handler = DatabaseHandler()
    json_handler = JsonHandler()
    table_name = f"overall_{json_handler.read_log(id=True)}"
    
    overall = database_handler.select(table=table_name, columns=['team', 'total'])
    
    dict_overall = dict(overall)
    #print(dict_overall)
    grouped_by_value = {}
    [grouped_by_value.setdefault(value, []).append(key) for key, value in dict_overall.items()]
    #print(grouped_by_value)

    grouped_by_value_ls = []#list(grouped_by_value.values())
    for i in grouped_by_value.values():
        #print(i)
        if len(i) >= 2:
            grouped_by_value_ls.append(i)
        else:
            pass

    #print(grouped_by_value_ls)
    meilleur_grind(grouped_by_value)
    
    # Tri par ordre décroissant des valeurs et récupération des équipes classées ----> en dernier
    #team_class = [key for key, _ in sorted(dict_overall.items(), key=lambda x: x[1], reverse=True)]
    #print(team_class)
    
    # Création des paires d'équipes
    #match_list = [team_class[i:i+2] for i in range(0, len(team_class), 2)]
    #print(match_list)

def meilleur_grind(dicto):
    # 1ere phase : qui a gagné la dernière manche, si encore égalité suivante
    database_handler = DatabaseHandler()
    json_handler = JsonHandler()
    n_match = get_number_of_match(json_handler.read_log(id=True))-2
    match_name = f"match_{json_handler.read_log(id=True)}_{n_match}"
    match_raw = database_handler.select(table=match_name, columns='*')
    match_ls = [[row[1], row[2], row[3], row[4]] for row in match_raw]
    winner=[[],[]]

    for i in match_ls:
        if i[1]>i[3]:
            winner[0].append(i[0])
        if i[1]<i[3]:
            winner[0].append(i[2])
        if i[1]==i[3]:
            winner[1].append([i[0],i[2]])
    #print(winner)

    inter_class = []
    print(dicto)
    n = 0
    for i in dicto.items():
        #print(i)
        ###print('\n')
        if len(i)>=2:
            ls_1 = []
            ls_removable = []
            for j in i[1]:
                #print(j)
                if j in winner[0]:
                    ls_1.append(1)
                    #print("ya")
                else:
                    ls_1.append(0)
            if ls_1.count(1)==1:
                #better.append(i[ls_1.index(1)])
                #i.insert(0, i.pop(i[ls_1.index(1)]))
                ls_removable.append({ls_1.index(1):'better'})
            if ls_1.count(0)==1:
                #worse.append(i[ls_1.index(0)])
                ls_removable.append({ls_1.index(0):'worse'})
            inter_class.append([])
            x = 0
            for k in ls_removable:
                key, value = k.popitem()
                if value=='better':
                    #print(dicto[i[0]])
                    #dicto[i[0]].insert(0, dicto[i[0]].pop(key))
                    inter_class[n].append({x:value})
                if value=='worse':
                    #print(dicto[i[0]])
                    inter_class[n].append({x:value})
                    #dicto[i[0]].insert(-1, dicto[i[0]].pop(key))
                x=x+1
            print(inter_class)
        else:
            pass
        n=n+1
    
    print('---------------------------------------')
    print(dicto)
    #print(worse)
    #print(dicto)
    
     # 2eme phase : qui a perdu le plus petit écart de point dans cette manche, si encore égalité suivante, un dictionnaire qui repertorie tous les gains ou les perte

    better2 = []
    worse2 = []
    flatted_ls = [item for sublist in dicto.items() for item in sublist]
    #print('---------------------------------------')
    #print(flatted_ls)

    gap_dict = {}
    for i in match_ls:
        if i[0] in flatted_ls:
            gap_dict[i[0]]=i[1]-i[3]
        if i[2] in flatted_ls:
            gap_dict[i[2]]=i[3]-i[1]

    #print(gap_dict)

    for n in dicto.items():
        if len(n)>=2:
            ls_2 = [gap_dict[u] for u in n]
            combined_ls = list(zip(ls_2, n))
            ls_classed = sorted(combined_ls, key=lambda x: x[0], reverse=True)
            ls_2, class_n = zip(*ls_classed)
            #print(class_n)
            
        else:
            pass


    # 3eme phase : qui a gagné le plus grand écart de point sur tout ses matchs 

def add_random_players():
    fichier_csv = '/home/antonin/Python/ConcoursPetanque/boting/Prenoms.csv'
    premiere_colonne = []
    with open(fichier_csv, newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.reader(csvfile)
        for ligne in lecteur_csv:
            if ligne:  
                premiere_colonne.append(ligne[0])
    for valeur in premiere_colonne:
        print(valeur)




add_random_players()