
# Emular el funcionamiento de join para concaatenar una lista

def funcion_join(lista):
    resultado = ''
    
    for i in lista:
        resultado += str(i)
        
    return resultado

lista = [1, 3, 5, 7, 8]
lista_1  = ['m', 'a', 'l', 'o']

print(funcion_join(lista))
print(funcion_join(lista_1))        