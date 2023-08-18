import sqlite3 as mdb
import os
database_name = "database.db"
dir_path = os.path.dirname(os.path.realpath(__file__))
path = dir_path.replace("object", "data") + f"//{database_name}"

def chk_conn(conn):
     try:
        conn.cursor()
        return True
     except Exception as ex:
        return False

myconn = mdb.connect(path)
print(chk_conn(myconn))
print(path)