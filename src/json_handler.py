import os
import sys
from datetime import datetime
import json
sys.path.append('.')
from src.database_handler import DatabaseHandler

class JsonHandler:
    def __init__(self):
        self.path = f"{os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))}/data/log.json"
        self.database_handler = DatabaseHandler()
    
    def write_log(self, parameters):#, parameters : list ###à compléter 
        id = 2 #self.database_handler.select(columns='id', table='general', condition='name', condition_value=parameters[0])
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dicto = {'id':id, 'time':current_time,"match_rank":0}
        with open(self.path, 'w') as fichier_json:
            json.dump(dicto, fichier_json)

    def read_log(self, **kwargs):
        id : bool = kwargs.get('id', False)
        time : bool = kwargs.get('time', False)
        match_rank : bool = kwargs.get('match_rank', False)

        with open(self.path, 'r') as fichier_json:
            dicto = json.load(fichier_json)
        
        if id:
            return dicto['id']
        if time:
            return dicto['time']
        if match_rank:
            return dicto['match_rank']

'''test = JsonHandler()
p = test.read_log(id=True)
print(p)'''