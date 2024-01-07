# Deux listes parallèles
list1 = [5, 2, 8, 1, 7]
list2 = ['a', 'b', 'c', 'd', 'e']

# Utiliser zip pour regrouper les éléments correspondants
combined_lists = list(zip(list1, list2))

# Trier la liste combinée en fonction des éléments de la première liste (ordre décroissant)
sorted_combined = sorted(combined_lists, key=lambda x: x[0], reverse=True)

# Séparer les listes après le tri
sorted_list1, sorted_list2 = zip(*sorted_combined)

print(sorted_list1)
print(sorted_list2)