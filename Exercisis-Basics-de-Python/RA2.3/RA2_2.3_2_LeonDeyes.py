# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 9/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari un nº enter i calcula la suma de tots fins el nº
# Especificacions d'entrada: Numero enter positiu introduit per l'usuari.

# Variable
try:
    numero = int(input("Posa un numero enter positiu: "))
    suma = 0

    for i in range (1, numero + 1):
        suma = suma + i
        print (str(suma))

except ValueError:
    print("Error: Has d'introduir un número enter positiu.")