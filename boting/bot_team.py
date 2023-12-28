import random
import sys
sys.path.append('.')
from src.application import Application
from src.database_handler import DatabaseHandler
import csv
import pandas as pd

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

def overall_writting(competion):
    pass