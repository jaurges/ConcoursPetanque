def rendre_pair(chiffre):
    chiffre_arrondi = round(chiffre)
    chiffre_pair = chiffre_arrondi + chiffre_arrondi % 2
    return chiffre_pair

# Exemple d'utilisation
chiffre = 3.7
chiffre_pair = rendre_pair(chiffre)
print(chiffre_pair)