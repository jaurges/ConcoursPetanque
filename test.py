import sqlite3

con = sqlite3.connect("data/database.db")
con.row_factory = sqlite3.Row

i = 0

while True:
    cursor = con.cursor()
    i = +1
    match_name = "match" + str(i)
    #try:
    query1 = f"SELECT * FROM {match_name}"
    cursor.execute(query1)
    #except:
    cursor.close()
    print("ok")

