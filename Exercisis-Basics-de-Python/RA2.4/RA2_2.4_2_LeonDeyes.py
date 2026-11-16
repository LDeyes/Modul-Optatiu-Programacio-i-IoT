# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: 
# Especificacions d'entrada: 

# Variables
try:
    frase = input("Posa una frase: ")
    comptador = 0
# Bucle que recorre cada posició de la frase per determinar si és vocal o non
    for i in range(len(frase)):
        if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
            comptador = comptador + 1
# Resultats  
    print("La frase té", comptador, "vocals.")
# Excepcions
except KeyboardInterrupt:
    print("Has cancelat l'operació")