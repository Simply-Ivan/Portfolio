
def es_palíndromo(palabra_1):
    if palabra_1 == palabra_1[::-1]:
        print('Es políndromo')
    else:
        print("No es políndromo")

        
    
a = input('Ingrese la primera palabra: ')

es_palíndromo(a)
