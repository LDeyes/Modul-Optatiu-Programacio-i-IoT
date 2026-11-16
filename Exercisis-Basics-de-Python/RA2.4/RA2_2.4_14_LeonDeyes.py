# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Demana 10 numeros a l'usuari i els ordena amb dos llistes parells i senars
# Especificacions d'entrada: 10 numeros enters

# Variables
try:
    parells = []
    senars = []

# Bucles de comparacions de parell o senar
    for i in range(10):
        num = int(input("Posa un numero: "))

# Comparem si és parell o senar
        if num % 2 == 0:
            parells = parells + [num]
        else:
            senars = senars + [num]

# Resultats 
    print("Els numeros parells són: " + str(parells))
    print("Els numeros senar són: " + str(senars))

# Excepcions 
except KeyboardInterrupt:
    print("Has cancelat la operació!")