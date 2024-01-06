dict_overall = {'team1': 35, 'team2': 33, 'team3': 41, 'team4': 21, 'team5': 32, 'team6': 30, 'team7': 40, 'team8': 25, 'team9': 35, 'team10': 43, 'team11': 28, 'team12': 26, 'team13': 38, 'team14': 35, 'team15': 33, 'team16': 26, 'team17': 45, 'team18': 26, 'team19': 30, 'team20': 42}

grouped_by_value = {}
[grouped_by_value.setdefault(value, []).append(key) for key, value in dict_overall.items()]

grouped_by_value = list(grouped_by_value.values())

print(grouped_by_value)
