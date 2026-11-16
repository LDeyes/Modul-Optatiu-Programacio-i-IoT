# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Concatena dos cadenes amb un guió (-)
# Especificacions d'entrada: Text introduit per l'usuari

# Variables
try: 
    frase = input("Posa una frase: ")
    frase_nova = frase.replace(" ", "-")

# Resultats
    print("La frase nova és :" + frase_nova)

# Excepcions
except KeyboardInterrupt:
    print("S'ha cancelat la operacio") 