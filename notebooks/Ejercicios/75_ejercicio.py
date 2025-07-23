
# Calcular la diferencia de conjuntos con colores
# A, B => A - B

colores_lista_1 = ['Negro', 'Rojo', 'Verde', 'Blanco']
colores_lista_2 = ['Blanco', 'Azul', 'Verde', 'Gris', 'Amarillo', 'verde']

conjunto_colores_1 = set(colores_lista_1)
conjunto_colores_2 = set(colores_lista_2)

diferencia = conjunto_colores_1.difference(conjunto_colores_2)
print(diferencia)