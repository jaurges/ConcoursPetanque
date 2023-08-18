import random
from data.database_handler import DatabaseHandler

club_name = ["ASC Cordemais", "Bouée"]


def add_team(n):
    x=0
    for i in range(n):
        x = x+1
        database_handler = DatabaseHandler("database.db")
        team = "équipe" + str(x)
        club = random.choice(club_name)

        database_handler.create_team2(team, club)
        print(team, club)

add_team(50)