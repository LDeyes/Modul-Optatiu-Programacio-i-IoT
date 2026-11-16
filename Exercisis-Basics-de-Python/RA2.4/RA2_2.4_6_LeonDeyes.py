# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Demana una cadena i mostra la primera i ultima lletra
# Especificacions d'entrada: Text introduit per l'usuari 

# Variables 
try:
    cadena = input("Posa una frase: ")
    primera = cadena[0]
    ultima = cadena[-1]

# Resultat
    print("La primera lletra és :" + " " + primera)
    print("La ultima lletra és :" + " " + ultima)

# Excepcions 
except KeyboardInterrupt:
    print("S'ha cancelat l'operació")