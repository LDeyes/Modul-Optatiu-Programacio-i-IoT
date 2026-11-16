# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 15/11/2026
# Versió: 1.0
#
# Descripció: Filtra paraules que comencen per vocal
# Especificacions d'entrada: Llista de paraules

# Variables
try:
# Demanem les paraules separades per espais
    paraules = input("Introdueix paraules separades per espais: ").split()

# Creem una llista buida per guardar les paraules amb vocal
    vocals = []

# Llista de vocals
    lletres_vocal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Recorrem cada paraula
    for paraula in paraules:
        # Agafem la primera lletra
        primera = paraula[0]
        
        # Comprovem si la primera lletra és una vocal
        if primera in lletres_vocal:
            vocals = vocals + [paraula]

# Mostrem el resultat
    print("Paraules que comencen per vocal:", vocals)

# Excepcions 
except KeyboardInterrupt:
    print("Has cancelat la operacio!")