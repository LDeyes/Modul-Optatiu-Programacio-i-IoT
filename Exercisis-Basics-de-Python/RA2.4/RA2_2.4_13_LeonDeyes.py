# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Suma tots els numeros d'una llista
# Especificacions d'entrada: Numeros Enters 

# Variables 
try:
    numeros = [10, 25, 30, 5, 20]
    suma = 0

# Bucle que recorre la llista i suma els numeros 
    for numero in numeros:
        suma = suma + numero

# Resultats 
    print("La suma total de " + str(numeros) + " és: " + str(suma))

# Excepcions 
except KeyboardInterrupt:
    print("Has cancelat la operacio")