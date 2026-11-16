# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: CURRENT_DAY/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari 5 paraules i les guarda a una llista
# Especificacions d'entrada: 5 dades de text introduides per l'usuari

# Variables
try:
   paraules = input("Introdueix 5 paraules sepadarades per espais: ").split()

# Resultats
   print("La llista de paraules és: " + str(paraules))

# Excepcions 
except KeyboardInterrupt:
   print("S'ha cancelat la operació")
