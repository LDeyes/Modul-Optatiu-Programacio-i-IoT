# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: CURRENT_DAY/11/2026
# Versió: 1.0
#
# Descripció: Ordena alfabeticament noms d'una llista 
# Especificacions d'entrada: Text 

# Variables
try:
# Creem una llista amb noms
    noms = ["Marc", "Anna", "Pere", "Laia", "Jordi"]

# Imprimim la llista original 
    print("Llista original:", noms)

# Recorrem la llista dues vegades per comparar i intercanviar
    for i in range(4):
        for j in range(4):
            if noms[j] > noms[j + 1]:
                aux = noms[j]
                noms[j] = noms[j + 1]
                noms[j + 1] = aux

# Resultats
    print("Llista ordenada:", noms)

# Excepcions 
except KeyboardInterrupt:
    print("Has cancelat la operació!")