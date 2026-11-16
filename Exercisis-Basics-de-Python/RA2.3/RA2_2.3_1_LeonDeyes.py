# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 9/11/2026
# Versió: 1.0
#
# Descripció: Genera una sequencia de nombres des de 0 fins a un nº de l'usuari 
# Especificacions d'entrada: Numero enter positiu introduit per l'usuari.

# Variable
try:

    numero = int(input("Posa un numero enter positiu: "))

    for i in range (0, numero + 1):
        print(i)


except ValueError:
    print("Error: Introdueix un número enter positiu.") 