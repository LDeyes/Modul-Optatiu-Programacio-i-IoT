# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Guarda cada lletra d'una paraula en una llista 
# Especificacions d'entrada: Text introduit per l'usuari 

# Variables
try:
# Demanem una paraula
    paraula = input("Posa una paraula: ")

# Creem una llista buida
    lletres = []

# Afegim cada lletra a la llista
    for lletra in paraula:
        lletres = lletres + [lletra]

# Mostrem la llista
    print(lletres)

# Excepcions
except KeyboardInterrupt:
    print("Has cancelat l'operació")