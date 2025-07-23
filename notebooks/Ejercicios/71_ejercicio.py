
# Simular el funcionamiento del operador in

print(8 in [5, 7, 8, 9, 10])
print(2 in [5, 7, 8, 9, 10])
print('t' in 'mula')
print('u' in 'mula')
print('mu' in 'mula')
print('ua' in 'mula')
print('ut' in 'mula')


def pertenece_a(lista, elemento):
    
    for i in lista:
        if elemento == i:
            return True
    
    return False

print('-' * 50)

print(pertenece_a([5, 7, 8, 9, 10], 8))
print(pertenece_a([5, 7, 8, 9, 10], 2))
print(pertenece_a('mula','t'))
print(pertenece_a('mula','u'))
print(pertenece_a('mula','mu'))
print(pertenece_a('mula','ua'))
print(pertenece_a('mula','ut'))

print('-' * 50)

print(pertenece_a(['m', 'u', 'l', 'a'],'t'))
print(pertenece_a(['m', 'u', 'l', 'a'],'u'))
