
from src.database_handler import DatabaseHandler

class Application:
    def __init__(self):
        self.database_handler = DatabaseHandler("database.db")
    def return_team(self):
        pass
    def return_nb_match(self):
        pass
    def return_team_per_row(self):
        pass
    def create_competition(self, name, date, play_mod, location):
        pass
    def create_team(self, name, club):
        pass
    def draw(self):
        pass
    def register_result(self, row, n, output1, output2):
        pass