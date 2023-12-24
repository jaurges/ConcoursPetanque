'''
a jugé pour les stats si l'objet ne serait pas plus efficace et maintenable
'''

import sqlite3
import os
import random


class DatabaseHandler:
    def __init__(self, database_name: str):
        chemin = os.path.abspath(__file__)
        self.con = sqlite3.connect(f"{os.path.abspath(os.path.join(chemin, '..', '..'))}/data/{database_name}")
        self.con.row_factory = sqlite3.Row
    
    def select_return(self, **kwargs):
        columns : list = kwargs.get('columns', True)
        table : str = kwargs.get('table', True)
        condition : str = kwargs.get('condition', True)
        condition_value : str = kwargs.get('condition_value', True)

        if columns or table: 
            return NameError
        
        cursor = self.con.cursor()
        query = f"SELECT {columns} FROM {table} {condition}"
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        self.con.commit()

        return output

    def insert(self, **kwargs):
        columns : list = kwargs.get('columns', True)
        table : str = kwargs.get('table', True)
        values : list = kwargs.get('values', True)

        if columns or table or values: 
            return NameError
        
        cursor = self.con.cursor()
        query = f"INSERT INTO {table}({columns}) VALUES({values})"
        cursor.execute(query)

        cursor.close()
        self.con.commit()


    def update(self, **kwargs):
        columns : list = kwargs.get('columns', True)
        table : str = kwargs.get('table', True)
        condition : str = kwargs.get('condition', True)
        condition_value : str = kwargs.get('condition_value', True)
        values : list = kwargs.get('values', True)
        
        if columns or table or condition or condition_value or values: 
            return NameError
        elif not len(columns) == len(values):
            return NameError
        
        cursor = self.con.cursor()
        for i in range(len(columns)):
            query = f"UPDATE {table} SET {columns[i]}={values[i]} WHERE {condition}"
            cursor.execute(query)

        cursor.close()
        self.con.commit()



test = DatabaseHandler("databasev2.db")
test.register_result_into_overall(5, 1, 8, 13)