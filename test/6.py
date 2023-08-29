import sys
sys.path.append(".")
from data.database_handler import DatabaseHandler

database_handler = DatabaseHandler("databasev2.db")
output = database_handler.return_actual_dir()

print(output)
