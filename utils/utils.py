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
        if type(list[i]) is str or int:
            list[i] = 'b'
        else:
            pass
    return max(len(list[i]) for i in range(4))

def type_elements_liste(liste_principale):
    return [isinstance(element, list) for element in liste_principale]

def data_dict(data):
    dicto={}
    for row in data:
        key = row[2]
        value = row[1]
        dicto.setdefault(key, []).append(value)
    
    return dicto