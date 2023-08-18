import random


def create_matches(players):
    random.shuffle(players)  # Mélanger la liste des joueurs pour les répartir aléatoirement

    num_players = len(players)
    num_matches = num_players // 2  # Nombre de matchs (chaque match oppose 2 joueurs)

    matches = []

    for i in range(num_matches):
        player1 = players[i]
        player2 = players[i + num_matches]
        match = (player1, player2)
        matches.append(match)

    # Gérer le cas où le nombre de joueurs est impair
    if num_players % 2 == 1:
        unpaired_player = players[-1]
        matches.append((unpaired_player, None))

    return matches


# Exemple d'utilisation
players = ["Joueur1", "Joueur2", "Joueur3", "Joueur4", "Joueur5"]
matches = create_matches(players)

# Affichage des matchs
for match in matches:
    player1, player2 = match
    if player2:
        print(f"{player1} vs {player2}")
    else:
        print(f"{player1} - Bye")