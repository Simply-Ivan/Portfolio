import math

r = float(input("Ingrese el radio\n"))

while r <= 0:
    r = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
area = (r ** 2) * math.pi

print(f"El área del circulo es {round(area,2)}")