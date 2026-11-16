# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Elimina els espais d'una cadena
# Especificacions d'entrada: Text introduit per l'usuari

# Variables
try:
    cadena = input("Posa una frase: ")
    espai = " "
    cadena_nova = cadena.replace(" ", "")

# Resultats
    print("Frase Nova: " + cadena_nova)

# Excepcions 
except KeyboardInterrupt:
    print("Has cancelat l'operacio")