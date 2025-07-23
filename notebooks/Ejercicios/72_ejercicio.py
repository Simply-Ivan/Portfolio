
# Crear un histograma a partir de una lista de enteros.

def histograma(lista, simbolo = '*'):
    
    for i in lista:
        print(i * simbolo)


lista = [2, 4, 7, 1, 3]
print(histograma(lista))