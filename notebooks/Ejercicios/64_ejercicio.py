
# Crear una función para determinar si un número es cercano a 1000 o 2000

def aproximacion(n):
    return (abs(1000 - n) < 100) or (abs(2000 - n) < 100)
    
print(aproximacion(1096))
print(aproximacion(1789))