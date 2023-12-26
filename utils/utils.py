def concatenate(list):
    if type(list) is str:
        return list
    else :
        output = ", ".join(list)
        return output

def create_condition(condition, value):
    output = f"WHERE {condition}={value}"
    return output

def plus_grand(list):
    for i in range(4):
        if type(list[i]) is str:
            list[i] = 'a'
        else:
            pass
    return max(len(list[i]) for i in range(4))