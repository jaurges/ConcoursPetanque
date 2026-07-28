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
        columns = kwargs.get('columns')
        table = kwargs.get('table')
        values = kwargs.get('values') # liste de tuple
        many_exec = kwargs.get('many_exec', False)

        # 1. Vérification des arguments obligatoires
        if not columns or not table or not values: 
            raise ValueError("Les paramètres 'table', 'columns' et 'values' sont requis.")
        
        # 2. Formatage des colonnes (ex: "nom_equipe, joueur_1")
        columns_str = ", ".join(columns)

        # 3. Calcul du nombre de "?" nécessaires
        # Si many_exec, on regarde la taille de la première sous-liste, sinon la liste entière
        nb_valeurs = len(values[0]) if many_exec else len(values)
        interro = ", ".join(["?"] * nb_valeurs)
        
        # 4. Création de la requête générique
        query = f"INSERT INTO {table} ({columns_str}) VALUES ({interro})"
        print(query)

        cursor = self.con.cursor()

        # 5. Exécution sécurisée (SQLite place lui-même les valeurs à la place des '?')
        if many_exec:
            cursor.executemany(query, values)
        else:
            cursor.execute(query, values)

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
        team : bool = kwargs.get('team', False)
        name : str = kwargs.get('name', False)

        if not name:
            raise NameError

        match_schema = "CREATE TABLE " + name + "(id integer PRIMARY KEY, " \
                                                             "team1 text," \
                                                             "output1 integer," \
                                                             "team2 text," \
                                                             "output2 integer)"
        
        overall_schema = "CREATE TABLE " + name + "(id integer PRIMARY KEY, " \
                "team text," \
                "total integer)"

        team_schema = "CREATE TABLE " + name + "(id integer PRIMARY KEY, " \
                        "team_name text," \
                        "player1 text," \
                        "player2 text)"
        
        cursor = self.con.cursor()
        if match:
            query = match_schema
            print(query)
            cursor.execute(query)
        if overall:
            query = overall_schema
            #print(query)
            cursor.execute(query)
        if team:
            query = team_schema
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

    def table_exists(self, table: str) -> bool:
        cursor = self.con.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name = ?",(table,)
        cursor.execute(query)
        exists = cursor.fetchone() is not None
        cursor.close()
        return exists

    def overwrite_team_data(self, table_name: str, values: list):
        """
        Crée la table d'équipe si elle n'existe pas, la vide si elle existe, 
        puis insère les nouvelles données.
        """
        # 1. Requêtes SQL
        # Note : On ne peut pas paramétrer (?) le nom d'une table, le f-string est obligatoire ici.
        create_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY, 
                team_name TEXT, 
                player1 TEXT, 
                player2 TEXT
            )
        """
        delete_query = f"DELETE FROM {table_name}"
        insert_query = f"INSERT INTO {table_name} (team_name, player1, player2) VALUES (?, ?, ?)"

        cursor = self.con.cursor()
        
        try:
            # 1. On s'assure que la table existe
            cursor.execute(create_query)
            
            # 2. On efface TOUTES les lignes existantes (le cas échéant)
            cursor.execute(delete_query)
            
            # 3. On insère la nouvelle liste de données (values doit être une liste de listes/tuples)
            cursor.executemany(insert_query, values)
            
            # 4. On valide toutes ces opérations en bloc !
            self.con.commit()
            print(f"Table {table_name} mise à jour avec succès ({len(values)} lignes insérées).")
            
        except sqlite3.Error as e:
            # TRÈS IMPORTANT : S'il y a une erreur pendant l'insertion, 
            # on annule TOUT (y compris l'effacement des données). 
            # Ainsi, on ne perd pas l'ancienne sauvegarde si la nouvelle plante.
            self.con.rollback()
            print(f"Une erreur est survenue, annulation des modifications : {e}")
            
        finally:
            cursor.close()

'''test = DatabaseHandler()
test.alter_table(name='output0', table='overall', type='INTEGER')'''