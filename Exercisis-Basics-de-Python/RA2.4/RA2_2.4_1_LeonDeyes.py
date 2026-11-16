# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Llegeix una cadena de l'usuari i mostra-la tota en majúscules.
# Especificacions d'entrada: Cadena de text introduit per l'usuari

# Variables
try:
    frase = input("Escriu una cadena: ")
    minuscules = "abcdefghijklmnopqrstuvwxyz"
    majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultat = ""

# Bucle que recorre la longitut de la cadena/frase
    for i in range(len(frase)):
        lletra = frase[i]       
        nova = lletra
# Bucle que si és minuscula la canvia per majuscula
        for j in range(26):
            if lletra == minuscules[j]:
                nova = majuscules[j]
        resultat = resultat + nova  

# Resultat
    print("En majúscules:", resultat)

# Excepcions
except KeyboardInterrupt:
    print("S'ha cancelat l'operació!")