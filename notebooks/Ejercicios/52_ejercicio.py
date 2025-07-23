
# Obtener la representación inversa de una cadena de caracteres.

n = 'Hola mundo'
print(n[-1::-1])

for i in range(len(n)-1 , -1, -1):
    print(n[i], end='')
