
# Calcular la suma de tres números, e incluir una condición de igualdad.

def suma_numeros(a, b, c):
    suma = a + b + c
    
    if a == b and a == c:
        suma *= 3
        
    return suma

print(suma_numeros(6, 7, 9))
print(suma_numeros(9, 9, 9))
    