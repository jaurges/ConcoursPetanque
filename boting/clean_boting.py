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

def main_overall():
    database_handler = DatabaseHandler()
    json_handler = JsonHandler()
    table_name1 = f"overall_{json_handler.read_log(id=True)}"
    grouped_by_value = {}
    inter_class = {}
    grouped_by_value_ls = []
    
    overall = database_handler.select(table=table_name1, columns=['team', 'total'])
    dict_overall = dict(overall)
    [grouped_by_value.setdefault(value, []).append(key) for key, value in dict_overall.items()]

    for i in grouped_by_value.values():
        if len(i) >= 2:
            grouped_by_value_ls.append(i)
        else:
            pass
    for i in grouped_by_value_ls:
        inter_class[tuple(i)]=[]
    
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
    
    for i in grouped_by_value_ls:
        print(i)
        ls_1 = []
        ls_removable = []
        for j in i:
            if j in winner[0]:
                ls_1.append(1)
            else:
                ls_1.append(0)
        if ls_1.count(1)==1:
            ls_removable.append({i[ls_1.index(1)]:'better'})
        if ls_1.count(0)==1:
            ls_removable.append({i[ls_1.index(0)]:'worse'})
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
        
    print('---------------------------------------')
    print(inter_class)
    print('---------------------------------------')
    list2 = []
    for i in inter_class.items():
        key, value = i[0], i[1]
        #print(key,value)
        if value.count(min(value)) and value.count(max(value))>=2:
            for j in key:
                #print(j)
                if value[key.index(j)]==0:
                    list2.append(j)
                    #print(value[key.index(j)])
                else:
                    pass
        else: 
            pass
    #print(list2)
    gap_dict = {}
    for i in match_ls:
        if i[0] in list2:
            gap_dict[i[0]]=i[1]-i[3]
        if i[2] in list2:
            gap_dict[i[2]]=i[3]-i[1]

    items_list = [i for i in gap_dict.items()]
    combined_ls = list(zip(list2, items_list))
    ls_classed = sorted(combined_ls, key=lambda x: x[0], reverse=True)
    list2, class_teams_lst = zip(*ls_classed)
    
    for i in class_teams_lst:
        for j in inter_class.keys():
            if i[0] in j:
                #print(i[0], j)
                index = j.index(i[0])
                inter_class[j][index]=i[1]
                #print(index)
            else: 
                pass
    print(inter_class)
    print('---------------------------------------')
    print(grouped_by_value)
    print('---------------------------------------')
    sorted_dict = dict(sorted(grouped_by_value.items(), key=lambda item: item[0], reverse=True))

    #print(sorted_dict)
    final_overall = []
    n=0
    for i in sorted_dict.items():
        #print(i)
        key, value = i[0], i[1]
        if len(value)>=2:
            for j in inter_class.keys():
                if j==tuple(value):
                    for _ in range(len(j)):
                        #print(inter_class[j])
                        index_max = inter_class[j].index(max(inter_class[j]))
                        #print(index_max)
                        team = j[index_max]
                        #print(j)
                        final_overall.append(team)
                        inter_class[j][index_max] = -1000
                else:
                    pass
        else:
            final_overall.append(value)

    print(inter_class)
    flat_list = [item[0] if isinstance(item, list) else item for item in final_overall]
    print(flat_list)
    print(len(final_overall))

    match_list = [final_overall[i:i+2] for i in range(0, len(final_overall), 2)]
    print(match_list)


main_overall()