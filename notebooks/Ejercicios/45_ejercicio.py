
lista = list(['Joel','Pepe','Tito','Charo',True,'Felix','Hiro'])
lista_1 = ['perro','gato','hasmter','hipopotamo']
lista_2 = [12,234,34,43,78,23,54,98,False,True]

numero = len(lista)
lista_1.append('elefante')
lista_1.insert(2,'cocodrilo')
lista_1.extend(['ardilla','mono','jirafa'])
lista_1.append('león')

lista.pop(4)
lista.remove('Hiro')
lista.clear()

lista_2.sort()
lista_1.reverse()
trabajo = lista_1.index('hipopotamo')

print(lista_1) 