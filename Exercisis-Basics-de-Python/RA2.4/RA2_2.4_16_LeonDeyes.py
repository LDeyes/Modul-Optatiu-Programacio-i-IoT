# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Elimina els duplicats d'una altra llista 
# Especificacions d'entrada: Text 

# Variables
try:
# Creem una llista amb dades duplicades
    numeros = [5, 3, 8, 3, 1, 5, 9, 1, 7]

# Creem una llista buida per guarda els elements unics
    uniques = []

# Recorrem la llista
    for numero in numeros:
        # Si la dada no esta a la llista uniques s'afegeix 
        if numero not in uniques:
            uniques = uniques + [numero]

# Resultats
    print("Llista sense duplicats: ", uniques)

# Excepcions
except KeyboardInterrupt:
    print("Has cancelat la operacio!")