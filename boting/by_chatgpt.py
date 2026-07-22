from collections import defaultdict
from src.database_handler import DatabaseHandler
from src.json_handler import JsonHandler

def get_number_of_match(competition_id):
    database_handler = DatabaseHandler()
    tables_names = database_handler.select(columns='name', table='sqlite_master', condition='type', condition_value="'table'")
    return sum(table[0].startswith(f"match_{competition_id}") for table in tables_names)

def main_overall():
    database_handler = DatabaseHandler()
    json_handler = JsonHandler()
    competition_id = json_handler.read_log(id=True)
    
    table_name1 = f"overall_{competition_id}"
    overall = database_handler.select(table=table_name1, columns=['team', 'total'])
    
    # Group teams based on their total scores
    grouped_by_value = defaultdict(list)
    for team, total in overall:
        grouped_by_value[total].append(team)
    
    # Filter teams with more than one occurrence
    grouped_by_value_ls = [teams for teams in grouped_by_value.values() if len(teams) >= 2]

    # Get the number of matches and the corresponding match name
    n_match = get_number_of_match(competition_id) - 2
    match_name = f"match_{competition_id}_{n_match}"
    
    # Retrieve match data
    match_raw = database_handler.select(table=match_name, columns=['team1', 'output1', 'team2', 'output2'])
    match_ls = [[row[0], row[1], row[2], row[3]] for row in match_raw]

    # Determine match winners
    winners = [i[0] if i[1] > i[3] else i[2] if i[1] < i[3] else [i[0], i[2]] for i in match_ls]
    
    # Create a dictionary to store inter-class values
    inter_class = defaultdict(list)
    

    # Populate inter_class dictionary
    for teams in grouped_by_value_ls:
        for team in teams:
            if team in winners:
                inter_class[tuple(teams)].append(100 if team == winners[0] else -100)
            else:
                inter_class[tuple(teams)].append(0)

    # Extract teams with max and min values from inter_class
    max_min_teams = [team[0] for team, values in inter_class.items() if values.count(min(values)) and values.count(max(values)) >= 2]

    # Calculate the gap and create a dictionary
    gap_dict = {}
    for i in match_ls:
        if i[0] in max_min_teams:
            gap_dict[i[0]] = i[1] - i[3]
        if i[2] in max_min_teams:
            gap_dict[i[2]] = i[3] - i[1]

    # Sort the dictionary based on teams
    sorted_dict = dict(sorted(gap_dict.items(), key=lambda item: item[0], reverse=True))

    # Create a final list of teams
    final_overall = []
    for _, teams in grouped_by_value.items():
        if len(teams) >= 2:
            for key, values in inter_class.items():
                if tuple(teams) == key:
                    index_max = values.index(max(values))
                    final_overall.append(key[index_max])
                    values[index_max] = -1000

    # Flatten the final list
    flat_list = [item if isinstance(item, str) else item[0] for item in final_overall]

    # Create a list of matches
    match_list = [flat_list[i:i+2] for i in range(0, len(flat_list), 2)]

    '''print('---------------------------------------')
    print(inter_class)
    print('---------------------------------------')
    print(grouped_by_value)
    print('---------------------------------------')
    print(flat_list)
    print(len(final_overall))
    print(match_list)'''

main_overall()
