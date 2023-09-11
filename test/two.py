import tkinter as tk
from tkinter import ttk

# Fonction pour ajouter ou enlever des joueurs d'une équipe
def gerer_equipe():
    club = club_entry.get()
    nb_joueurs = int(joueurs_entry.get())
    
    if club not in clubs:
        clubs[club] = {'team1': []}
    
    equipe_num = 1
    while True:
        equipe = f'team{equipe_num}'
        if equipe not in clubs[club]:
            clubs[club][equipe] = []
            break
        equipe_num += 1
    
    if ajouter_var.get():
        for _ in range(nb_joueurs):
            clubs[club][equipe].append(f'Joueur{len(clubs[club][equipe]) + 1}')
    else:
        for _ in range(nb_joueurs):
            if clubs[club][equipe]:
                clubs[club][equipe].pop()

    update_qtable()


# Fonction pour mettre à jour le QTableWidget
def update_qtable():
    qtable.delete(*qtable.get_children())
    for club, equipes in clubs.items():
        for equipe, joueurs in equipes.items():
            qtable.insert('', 'end', values=[club, equipe, ', '.join(joueurs)])

# Initialisation du dictionnaire des clubs
clubs = {}

# Création de l'interface graphique
root = tk.Tk()
root.title("Gestion des Clubs et des Équipes")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

club_label = ttk.Label(frame, text="Nom du Club:")
club_label.grid(row=0, column=0, padx=5, pady=5)

club_entry = ttk.Entry(frame)
club_entry.grid(row=0, column=1, padx=5, pady=5)

joueurs_label = ttk.Label(frame, text="Nombre de Joueurs:")
joueurs_label.grid(row=1, column=0, padx=5, pady=5)

joueurs_entry = ttk.Entry(frame)
joueurs_entry.grid(row=1, column=1, padx=5, pady=5)

ajouter_var = tk.BooleanVar()
ajouter_checkbox = ttk.Checkbutton(frame, text="Ajouter des joueurs", variable=ajouter_var)
ajouter_checkbox.grid(row=2, column=0, padx=5, pady=5)

gerer_button = ttk.Button(frame, text="Gérer l'équipe", command=gerer_equipe)
gerer_button.grid(row=2, column=1, padx=5, pady=5)

qtable = ttk.Treeview(root, columns=("Club", "Équipe", "Joueurs"), show="headings")
qtable.heading("Club", text="Club")
qtable.heading("Équipe", text="Équipe")
qtable.heading("Joueurs", text="Joueurs")
qtable.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
