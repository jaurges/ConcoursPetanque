import os
chemin = os.path.abspath(__file__)
print(f"{os.path.abspath(os.path.join(chemin, '..', '..'))}/data/databasev2.db")