# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Multiplica tots els elements d'una llista per 2
# Especificacions d'entrada: Llista de nombres

# Variables
try:
 # Creem una llista amb números
    numeros = [1, 2, 3, 4, 5]

    print("Llista original:", numeros)

 # Creem una llista buida per guardar els resultats
    resultats = []

 # Recorrem la llista original
    for num in numeros:
        # Multipliquem per 2 i afegim el resultat
        resultat = num * 2
        resultats = resultats + [resultat]

 # Mostrem el resultat
    print("Llista multiplicada per 2:", resultats)

# Excepcions
except KeyboardInterrupt:
    print("Has cancelat la operacio!")