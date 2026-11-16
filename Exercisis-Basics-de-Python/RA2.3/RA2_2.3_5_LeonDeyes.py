# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 9/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari un nombre enter i torna els numeros primers
# Especificacions d'entrada: Numero enter positiu donada per l'usuari

def es_primer(n):
    """Retorna True si n és primer, False en cas contrari."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


try:
    numero = int(input("Posa un número enter positiu: "))

    if numero <= 0:
        raise ValueError

    for i in range(2, numero + 1):
        if es_primer(i):
            print(i)
except ValueError:
    print("Posa un numero enter!")