
# Calcular el área de un triángulo

def area_triangulo(base, altura):
    area = 1/2 * base * altura
    respuesta = f'El área del triángulo es {area}'
    return respuesta

print(area_triangulo(25, 7))

print('-' * 50)

base = None
altura = None

while True:
    try:
        base = float(input('Escriba la base del triángulo:\t'))
        break
    except:
        print('Debe escribir un número.')
        
while True:
    try:
        altura = float(input('Escriba la altura del triángulo:\t'))
        break
    except:
        print('Debe escribir un número.')
        
area = (altura * base) / 2

print(f'El área del triángulo es igual: {area}')
