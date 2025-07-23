
# Crear una función únicamente para sumar números enteros.

def suma(x , y):
    
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise TypeError('Los valores deben ser enteros.')
    
try:
    print(sum(6, 7))
    print(suma(9, 'c'))
except TypeError as e:
    print(e)