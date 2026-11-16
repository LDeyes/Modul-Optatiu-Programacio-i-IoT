# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 9/11/2026
# Versió: 1.0
#
# Descripció: Mostra la taula de multiplicar del nº introduït per l'usuari.
# Especificacions d'entrada: Número enter positiu introduït per l'usuari.

# Variables

try:
    numero = int(input("Posa un nº enter: "))
    

    for i in range (1,11):
        resultat = numero * i 
        print(resultat)

except ValueError:
    print ("Has de posar un nº enter vàlid!")
