# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 9/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari un numero enter i imprimeix tots els nombres parells fins el numero donat
# Especificacions d'entrada: Numero enter positiu donat per l'usuari

try:

    # Variables
    numero = int(input("Posa un numero enter positiu: "))

    for i in range (0, numero + 1, 2):
        print(i)

except ValueError:
    print("Posa un numero enter positiu vàlid!!!")
