import random

class Club:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams


class Equipe:
    def __init__(self, name, club):
        self.name = name
        self.club = club


class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team


def create_matches(clubs):
    matches = []

    # Mélanger la liste des clubs pour répartir les matchs aléatoirement
    random.shuffle(clubs)

    num_teams = sum(len(club.teams) for club in clubs)
    num_matches = num_teams // 2

    # Créer les matchs en associant une équipe d'un club à une autre équipe d'un club différent
    for _ in range(num_matches):
        club1, club2 = random.sample(clubs, 2)

        team1 = random.choice(club1.teams)
        team2 = random.choice(club2.teams)

        match = Match(team1, team2)
        matches.append(match)

    return matches


# Exemple d'utilisation avec 39 équipes réparties dans 2 clubs
club1 = Club("Club A", [Equipe(f"Equipe {i + 1}", "Club A") for i in range(39)])
club2 = Club("Club B", [Equipe(f"Equipe {i + 40}", "Club B") for i in range(39)])

clubs = [club1, club2]

matches = create_matches(clubs)

# Affichage des matchs
for match in matches:
    print(f"{match.home_team.name} ({match.home_team.club}) vs {match.away_team.name} ({match.away_team.club})")

'''
varA = []
varB = []
for raw in range(len(return_team)):
     
club1 = Club("Club A", [Equipe(f"team", "Club A") for data in data=return_clubA])
club2 = Club("Club B", [Equipe(f"Equipe {i + 40}", "Club B") for data in data=return_clubB])
'''