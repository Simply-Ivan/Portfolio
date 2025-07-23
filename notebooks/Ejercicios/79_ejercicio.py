
# Calcular la suma de tres números si todos son diferentes, en caso contrario la será 0

def suma_diferente(a, b, c):
    
    if a == b == c:
        return 0
    else:
        return a + b + c
    
print(suma_diferente(5, 6, 7))
print(suma_diferente(6, 6, 6))
