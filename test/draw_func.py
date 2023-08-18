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
players = ['équipe1', 'équipe2', 'équipe3', 'équipe4', 'équipe5', 'équipe6',
             'équipe7', 'équipe8', 'équipe9', 'équipe10', 'équipe11', 'équipe12', 'équipe13',
             'équipe14', 'équipe15', 'équipe16', 'équipe17', 'équipe18', 'équipe19', 'équipe20',
             'équipe21', 'équipe22', 'équipe23', 'équipe24', 'équipe25', 'équipe26', 'équipe27', 'équipe28',
             'équipe29', 'équipe30', 'équipe31', 'équipe32', 'équipe33', 'équipe34', 'équipe35', 'équipe36', 'équipe37',
             'équipe38', 'équipe39', 'équipe40', 'équipe41', 'équipe42', 'équipe43', 'équipe44', 'équipe45', 'équipe46',
             'équipe47', 'équipe48', 'équipe49', 'équipe50']
matches = create_matches(players)

# Affichage des matchs
for match in matches:
    player1, player2 = match
    if player2:
        print(f"{player1} vs {player2}")
    else:
        print(f"{player1} - Bye")