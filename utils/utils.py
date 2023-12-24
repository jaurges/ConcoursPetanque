def concatenate(list : list):
    output = ", ".join(list)
    return output

def create_condition(condition, value):
    output = f"WHERE {condition}={value}"
    return output