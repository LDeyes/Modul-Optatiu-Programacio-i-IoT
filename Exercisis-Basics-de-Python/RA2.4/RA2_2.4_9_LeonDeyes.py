# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Divideix una frase en paraules i les mostra una per una  
# Especificacions d'entrada: Text introduit per l'usuari

# Variables
try: 
    frase = input("Posa una frase: ")
    paraules = frase.split()

# Bucle que mostra les paraules una a una
    for paraula in paraules:
        print(paraula)

# Resultats
    print("Aquestes son les paraules de: " + frase)

# Excepcions 
except KeyboardInterrupt:
    print("Has cancelat l'operació")