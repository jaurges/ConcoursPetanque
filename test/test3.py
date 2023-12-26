def type_elements_liste(liste_principale):
    return [isinstance(element, list) for element in liste_principale]

# Exemple d'utilisation
ma_liste = [['prout', 'caca'], 'feur', ['quoicoucbeh', 'zfbfjzr', 'hohohoh'], 'uoi']
resultats = type_elements_liste(ma_liste)

for i, resultat in enumerate(resultats):
    if resultat:
        print(f"L'élément à l'index {i} est une liste.")
    else:
        print(f"L'élément à l'index {i} est une chaîne de caractères.")
