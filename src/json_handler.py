import os
import sys
import datetime
import json
sys.path.append('.')
from src.database_handler import DatabaseHandler

class JsonHandler:
    def __init__(self):
        self.path = f"{os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))}/data/log.json"
        self.database_handler = DatabaseHandler()
    
    def write_log(self, parameters : list):
        id = self.database_handler.select(columns='id', table='general', condition='name', condition_value=parameters[0])
        time = datetime.now().strftime("%H:%M:%S")
        dicto = {'id':id, 'time':time}
        with open(self.path, 'w') as fichier_json:
            json.dump(dicto, fichier_json)

    def read_log(self, **kwargs):
        id : bool = kwargs.get('id', False)
        time : bool = kwargs.get('time', False)

        with open(self.path, 'r') as fichier_json:
            dicto = json.load(fichier_json)
        
        if id:
            return dicto[id]
        if time:
            return dicto[time]
