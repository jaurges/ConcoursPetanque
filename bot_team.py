import random
from data.database_handler import DatabaseHandler
import csv
import pandas as pd

club_name_fix = ["club1", "club2", "club3"]


def add_team_database(n):
    x=0
    for i in range(n):
        x = x+1
        database_handler = DatabaseHandler("database.db")
        team = "équipe" + str(x)
        club = random.choice(club_name)

        database_handler.create_team2(team, club)
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

add_team_csv(20)
