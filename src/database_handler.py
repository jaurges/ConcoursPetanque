import sqlite3
import os
import sys
sys.path.append('.')
from utils.utils import concatenate, create_condition, plus_grand, type_elements_liste


class DatabaseHandler:
    def __init__(self):
        chemin = os.path.abspath(__file__)
        self.con = sqlite3.connect(f"{os.path.abspath(os.path.join(chemin, '..', '..'))}/data/database.db")
        self.con.row_factory = sqlite3.Row
    
    def select(self, **kwargs):
        columns : list = kwargs.get('columns', False)
        table : str = kwargs.get('table', False)
        condition : str = kwargs.get('condition', False)
        condition_value : str = kwargs.get('condition_value', False)

        if not columns or not table: 
            raise NameError
        elif not condition:
            condition = ""
        else:
            condition = create_condition(condition, condition_value)

        columns = concatenate(columns)

        cursor = self.con.cursor()
        query = f"SELECT {columns} FROM {table} {condition}"
        print(query)
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return output

    def insert(self, **kwargs):
        columns : list = kwargs.get('columns', False)
        table : str = kwargs.get('table', False)
        values : list = kwargs.get('values', False)

        if not columns or not table or not values: 
            raise NameError
        
        columns = concatenate(columns)
        values = concatenate(values)
        
        #cursor = self.con.cursor()
        query = f"INSERT INTO {table}({columns}) VALUES({values})"
        print(query)
        #cursor.execute(query)

        ##cursor.close()
        #self.con.commit()

    # pour les listes suivantes elles doivent être équilibrés ou alors ce sont des string
    def update(self, **kwargs):
        columns : list = kwargs.get('columns', False)
        table : str = kwargs.get('table', False)
        condition : list = kwargs.get('condition', False)
        condition_value : list = kwargs.get('condition_value', False)
        values : list = kwargs.get('values', False)
        
        if not columns or not table or not condition or not condition_value or not values: 
            raise NameError

        list_1 = [columns, values, condition, condition_value]
        list_2 = type_elements_liste(list_1)

        #cursor = self.con.cursor()
    
        for i in range(plus_grand(list_1)):
            list_list = [columns, values, condition, condition_value]
            query = []
            n = 0
            for j in list_list:
                if list_2[n]:
                    var = j[i]
                else:
                    var = j
                n = n+1
                query.append(str(var))
            query = f"UPDATE {table} SET {query[0]}={query[1]} WHERE {query[2]}={query[3]}"
            #cursor.execute(query)
            print(query)

        #cursor.close()
        #self.con.commit()
    
    #a completer dans le futur pour dautre verification
    def pragma(self, **kwargs):
        table : str = kwargs.get('table', False)

        #cursor = self.con.cursor()
        query = f"PRAGMA table_info({table})"
        print(query)
        #cursor.execute(query)
        #output = cursor.fetchall
        #return output

        ##cursor.close()
        #self.con.commit()
    
    def create_table(self, **kwargs):
        match : bool = kwargs.get('match', False)
        overall : bool = kwargs.get('overall', False)

test = DatabaseHandler()
test.select(columns='*', table='general')