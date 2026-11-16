# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Canvia "a" per "@"
# Especificacions d'entrada: Text introduït per l'usuari

# Variables
try:
    frase = input("Posa una frase: ")
    frase_nova = " "

# Bucle que compara lletra per "a" si és la canvia per "@"
    for lletra in frase:
        if lletra == "a":
            frase_nova = frase_nova + "@"
        else:
            frase_nova = frase_nova + lletra

# Resultats    
    print(frase_nova)

# Excepcions 
except KeyboardInterrupt:
    print("S'ha cancelat l'operació")