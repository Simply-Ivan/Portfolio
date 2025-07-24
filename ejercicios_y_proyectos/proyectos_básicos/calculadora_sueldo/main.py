
print('Bienvenido a la calculadora de sueldo con aumento')
sueldo = int(input('Ingrese su sueldo: '))
 
while sueldo <= 0:
    sueldo = int(input('Ingrese su sueldo: '))

if sueldo < 1000:
    sueldo += 0.15 * sueldo

print(f'Su sueldo es: {sueldo}')