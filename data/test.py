import sqlite3
con = sqlite3.connect("database.db")
for i in range(0,100):
    matche_name = "match" + str(i)
    cursor = con.cursor()
    query = f"SELECT * FROM {matche_name}"
    print(i)
    try :
        cursor.execute(query)
    except sqlite3.OperationalError :
        break

con.commit()
print("finito pipo")
