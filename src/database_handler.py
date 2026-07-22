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
        #print(query)
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return output

    def insert(self, **kwargs):
        columns : list = kwargs.get('columns', False)
        table : str = kwargs.get('table', False)
        values : list = kwargs.get('values', False)
        values = [f"'{value}'" if isinstance(value, str) else str(value) for value in values]

        if not columns or not table or not values: 
            raise NameError
        
        columns = concatenate(columns)
        values = concatenate(values)
        
        cursor = self.con.cursor()
        query = f"INSERT INTO {table}({columns}) VALUES({values})"
        
        print(query)
        cursor.execute(query)

        cursor.close()
        self.con.commit()

    # pour les listes suivantes elles doivent être équilibrés ou alors ce sont des string
    def update(self, **kwargs):
        columns : list = kwargs.get('columns', False)
        table : str = kwargs.get('table', False)
        condition : list = kwargs.get('condition', False)
        condition_value : list = kwargs.get('condition_value', False)
        value : list = kwargs.get('value', False)
        
        if not columns or not table or not condition or not condition_value or not value: 
            raise NameError

        list_1 = [columns, value, condition, condition_value]
        list_2 = type_elements_liste(list_1)

        #print(plus_grand(list_1))
        #print('\n')
        cursor = self.con.cursor()
        # revoir l'utilité de la chose si récurrence faite dans application
        for i in range(plus_grand(list_1)):
            
            list_list = [columns, value, condition, condition_value]
            query = []
            n = 0
            for j in list_list:
                if list_2[n]:#==list:
                    
                    var = j[i]
                else:
                    var = j
                n = n+1
                query.append(str(var))
            query = f"UPDATE {table} SET {query[0]}={query[1]} WHERE {query[2]}='{query[3]}'"
            print(query)
            cursor.execute(query)

        cursor.close()
        self.con.commit()
    
    #a completer dans le futur pour dautre verification
    def pragma(self, **kwargs):
        table : str = kwargs.get('table', False)

        cursor = self.con.cursor()
        query = f"PRAGMA table_info({table})"
        print(query)
        cursor.execute(query)
        output = cursor.fetchall()

        cursor.close()
        self.con.commit()

        return output

        
    
    def create_table(self, **kwargs):
        match : bool = kwargs.get('match', False)
        overall : bool = kwargs.get('overall', False)
        name : str = kwargs.get('name', False)

        if not name:
            raise NameError

        match_schema = "CREATE TABLE " + name + "(id integer PRIMARY KEY, " \
                                                             "team1 text," \
                                                             "output1 integer," \
                                                             "team2 text," \
                                                             "output2 integer)"
        
        overall_schema = "CREATE TABLE overall(id integer PRIMARY KEY, " \
                "team text," \
                "total integer)"
        
        cursor = self.con.cursor()
        if match:
            query = match_schema
            print(query)
            cursor.execute(query)
        if overall:
            query = overall_schema
            print(query)
            cursor.execute(query)

        cursor.close()
        self.con.commit()
    
    def alter_table(self, **kwargs):
        name : str = kwargs.get('name', False)
        table : str = kwargs.get('table', False)
        type : str = kwargs.get('type', False)

        if not name or not table or not type: 
            raise NameError
        
        cursor = self.con.cursor()
        query = f"ALTER TABLE {table} ADD COLUMN {name} {type}"
        print(query)
        cursor.execute(query)
        cursor.close()
        self.con.commit()

'''test = DatabaseHandler()
test.alter_table(name='output0', table='overall', type='INTEGER')'''