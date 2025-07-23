
# Generar un conjunto de números aleatorios y determinar cuales son impares.

from random import randint

numeros_aleatorios = [randint(1, 1000) for _ in range(50)]

print(numeros_aleatorios)

numeros_impares = filter(lambda n: n % 2 == 1, numeros_aleatorios)

print()

print(list(numeros_impares))

print('-' * 50)

def number_impar(lista):
    impares = []
    
    for n in lista:
        if n % 2 == 1:
            impares.append(n)
            
    return impares

print(number_impar(numeros_aleatorios))