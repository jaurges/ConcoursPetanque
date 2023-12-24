'''
a jugé pour les stats si l'objet ne serait pas plus efficace et maintenable
'''

import sqlite3
import os
import sys
sys.path.append('.')
from utils.utils import concatenate, create_condition


class DatabaseHandler:
    def __init__(self, database_name: str):
        chemin = os.path.abspath(__file__)
        self.con = sqlite3.connect(f"{os.path.abspath(os.path.join(chemin, '..', '..'))}/data/{database_name}")
        self.con.row_factory = sqlite3.Row
    
    def select_return(self, **kwargs):
        columns : list = kwargs.get('columns', False)
        table : str = kwargs.get('table', False)
        condition : str = kwargs.get('condition', False)
        condition_value : str = kwargs.get('condition_value', False)

        if not columns or not table: 
            raise NameError
        elif condition:
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
            return NameError
        
        columns = concatenate(columns)
        
        cursor = self.con.cursor()
        query = f"INSERT INTO {table}({columns}) VALUES({values})"
        cursor.execute(query)

        cursor.close()
        self.con.commit()


    def update(self, **kwargs):
        columns : list = kwargs.get('columns', False)
        table : str = kwargs.get('table', False)
        condition : str = kwargs.get('condition', False)
        condition_value : str = kwargs.get('condition_value', False)
        values : list = kwargs.get('values', False)
        
        if not columns or not table or not condition or not condition_value or not values: 
            return NameError
        elif not len(columns) == len(values):
            return NameError
        
        cursor = self.con.cursor()
        for i in range(len(columns)):
            query = f"UPDATE {table} SET {columns[i]}={values[i]} WHERE {condition}"
            cursor.execute(query)

        cursor.close()
        self.con.commit()



test = DatabaseHandler("database.db")
test.select_return(columns = ['zouzou', 'zaza'], condition = "id", table = 'team', condition_value = "prout")