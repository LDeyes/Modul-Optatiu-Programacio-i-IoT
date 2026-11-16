# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Determina si la paraula és palindrom 
# Especificacions d'entrada: Text introduit per l'usuari

# Variables
try: 
    paraula = input("Posa una paraula: ")
    inversa = paraula[::-1]

# Bucle que compara les paraules (en minuscules) per veure si és palindrom
    if paraula.lower() == inversa.lower():
        print(paraula + " és palíndrom!")
    else:
        print(paraula + " no és palíndrom!")

# ExcepcionsSSS
except KeyboardInterrupt:
    print("S'ha cancelat l'operació")