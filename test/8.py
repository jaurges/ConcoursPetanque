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

    teams = [team for club in clubs for team in club.teams]
    random.shuffle(teams)

    num_teams = len(teams)
    if num_teams % 2 != 0:
        teams.append(None)

    num_rounds = num_teams - 1

    for round_num in range(num_rounds):
        round_matches = []

        half = num_teams // 2
        for i in range(half):
            team1 = teams[i]
            team2 = teams[i + half]

            if team1 is None or team2 is None:
                continue

            match = Match(team1, team2)
            round_matches.append(match)

        matches.extend(round_matches)

        # Rotation des équipes
        teams = [teams[0]] + [teams[-1]] + teams[1:-1]

    return matches


# Exemple d'utilisation avec 39 équipes réparties dans 2 clubs
club1 = Club("Club A", [Equipe(f"Equipe {i + 1}", "Club A") for i in range(39)])
club2 = Club("Club B", [Equipe(f"Equipe {i + 40}", "Club B") for i in range(39)])

clubs = [club1, club2]

matches = create_matches(clubs)

# Affichage des matchs
for match in matches:
    home_team_name = match.home_team.name if match.home_team else "Bye"
    away_team_name = match.away_team.name if match.away_team else "Bye"
    home_team_club_name = match.home_team.club.name if match.home_team else "N/A"
    away_team_club_name = match.away_team.club.name if match.away_team else "N/A"
    print(f"{home_team_name} ({home_team_club_name}) vs {away_team_name} ({away_team_club_name})")
