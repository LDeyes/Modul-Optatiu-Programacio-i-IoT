# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Imprimeix el major i menor d'una llista 
# Especificacions d'entrada: 5 numeros enters

# Variables
try: 
    numeros = [20,4,60,84,5]
    major = numeros[0]
    menor = numeros[0]

# Bucle que compara els numeros de la llista pel major i menor
    for numero in numeros:
        if numero > major:
            major = numero
        if numero < menor:
            menor = numero

# Resultats 
    print("El numero més gran és: " + str(major))
    print("El numero més petit és: " + str(menor))
    print("La llista és: " + str(numeros))

# Excepcions
except KeyboardInterrupt:
    print("S'ha cancelat l'operació")
        