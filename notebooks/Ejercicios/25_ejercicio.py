import math

r = float(input("Ingrese el número del radio\n"))

while r <= 0:
    r = float(input("Valor incorrecto. Ingresar un número mayor a 0\n"))
    
h = float(input("Ingrese la altura\n"))

while h <= 0:
    h = float(input("Valor incorrecto. Ingresar un número mayor a 0\n"))
    
area = 2 * math.pi * r * (r + h)
vol = math.pi * (r ** 2) * h

print(f"El área del cilindro es {round(area,2)} y el volumnen es {round(vol,2)}")