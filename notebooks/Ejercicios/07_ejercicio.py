n1 = float(input("Ingrese la primera nota\n"))

while n1 < 0 or n1 > 20:
    n1 = float(input("Valor incorrecto. Ingrese un número mayor a 0 y menor a 20\n"))
    
n2 = float(input("Ingrese la segunda nota\n"))

while n2 < 0 or n2 > 20:
    n2 = float(input("Valor incorrecto. Ingrese un número mayor a 0 y menor a 20\n"))

n3 = float(input("Ingrese la tercera nota\n"))

while n3 < 0 or n3 > 20:
    n3 = float(input("Valor incorrecto. Ingrese un número mayor a 0 y menor a 20\n"))
    
prom = (n1 + n2 + n3) / 3

print(f"El promedio de las 3 notas es {round(prom,2)}")