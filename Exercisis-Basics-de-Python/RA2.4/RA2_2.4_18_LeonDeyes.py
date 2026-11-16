# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: CURRENT_DAY/11/2026
# Versió: 1.0
#
# Descripció: Retorna una llista a l'inversa
# Especificacions d'entrada: Text introduit per l'usuari

# Variables
try:
 # Creem una llista
    noms = ["Marc", "Anna", "Pere", "Laia", "Jordi"]

    print("Llista original:", noms)

# Creem una llista buida per guardar la versió invertida
    al_reves = []

 # Comencem pel últim element i baixem fins al primer
    i = len(noms) - 1
    while i >= 0:
        al_reves = al_reves + [noms[i]]
        i = i - 1

 # Mostrem la llista invertida
    print("Al revés:", al_reves)

except KeyboardInterrupt:
    print()