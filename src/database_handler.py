'''
a jugé pour les stats si l'objet ne serait pas plus efficace et maintenable
'''

import sqlite3
import os
import sys
sys.path.append('.')
from utils.utils import concatenate, create_condition, plus_grand


class DatabaseHandler:
    def __init__(self):
        chemin = os.path.abspath(__file__)
        self.con = sqlite3.connect(f"{os.path.abspath(os.path.join(chemin, '..', '..'))}/data/database.db")
        self.con.row_factory = sqlite3.Row
    
    def select_return(self, **kwargs):
        columns : list = kwargs.get('columns', False)
        table : str = kwargs.get('table', False)
        condition : str = kwargs.get('condition', False)
        condition_value : str = kwargs.get('condition_value', False)

        if not columns or not table: 
            raise NameError
        elif not condition:
            pass
        else:
            condition = create_condition(condition, condition_value)

        columns = concatenate(columns)

        #cursor = self.con.cursor()
        query = f"SELECT {columns} FROM {table} {condition}"
        print(query)
        #cursor.execute(query)
        #output = cursor.fetchall()
        #cursor.close()
        #self.con.commit()

        #return output

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

        
        '''#cursor = self.con.cursor()
        for i in range(len(values)):
            if type(columns) is str:
                query = f"UPDATE {table} SET {columns}={values[i]} WHERE {condition}"
            else:
                query = f"UPDATE {table} SET {columns[i]}={values[i]} WHERE {condition}"
            print(query)
            #cursor.execute(query)
'''
        list_list = [columns, values, condition, condition_value]
        #print(list_list)
        list_2 = []
        n = 0
        for args in list_list:
            if type(args) is str:
                list_2.append(n)
            else:
                pass
            n = n+1

        for i in range(plus_grand(list_list)):
            print("prout")
            pass


        #cursor.close()
        #self.con.commit()



test = DatabaseHandler()
test.update(columns = ['zouzou','jjyotty', 'jotoo'], values = ["feur","quoicoubeh"], table = 'team', condition_value = "prout", condition = 'caca')