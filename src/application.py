from src.database_handler import DatabaseHandler
from src.json_handler import JsonHandler

class Application:
    def __init__(self):
        self.database_handler = DatabaseHandler()
        self.json_handler = JsonHandler()
    
    def set_competition_index(self, parameters:list):
        self.json_handler.write_log(parameters)

    def return_team(self):
        pass

    def return_nb_match(self):
        pass

    def return_team_per_row(self, row):
        pass

    def new_competition(self, name, date, play_mod, location):
        self.database_handler.insert(table='general', 
                                     columns=['name', 'date', 'play_mod', 'location'],
                                     values=[name, date, play_mod, location])

    def create_team(self, name, club):
        pass

    def draw(self):
        pass

    def register_result(self, row, n, output1, output2):
        pass

    def return_general(self):
        output = self.database_handler.select(columns='*', table='general')
        return output