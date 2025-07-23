
# Validar dos números. Si son iguales o la suma o el valor absoluto son 5.

def validar_numeros(a, b):
    if a == b or (a + b) == 5 or abs(a - b) == 5:
        return True
    else:
        return False
    
print(validar_numeros(7, 8))
print(validar_numeros(4, 4))
print(validar_numeros(5, 10))
print(validar_numeros(4, 1))    