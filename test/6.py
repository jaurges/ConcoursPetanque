import sys
sys.path.append(".")
from data.database_handler import DatabaseHandler

var = DatabaseHandler("databasev2.db").return_actual_dir()
ls = []
for row in var:
    ls.append(row[0])
print(ls)