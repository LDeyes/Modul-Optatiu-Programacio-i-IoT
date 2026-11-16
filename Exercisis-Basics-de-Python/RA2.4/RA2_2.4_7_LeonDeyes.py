# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Compta quantes vegades apareix una lletra donade per una cadena de l'usuari 
# Especificacions d'entrada: Text introduit per l'usuari

# Variables
try:
    cadena = (input("Posa una cadena de text: "))
    lletra = (input("Posa una lletra que vols comptar: "))
    comptador = 0

# Bucles que compara lletres per comptar o no
    for i in cadena:
        if i == lletra:
            comptador = comptador + 1
        else:
            comptador

# Resultats 
    print("La lletra " + str(lletra) + " apareix " + str(comptador) + " vegades")

# Excepcions 
except KeyboardInterrupt:
    print("S'ha cancelat l'operacio")