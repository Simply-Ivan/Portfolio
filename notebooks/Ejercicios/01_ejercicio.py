import math

r = int(input("Ingresa el número del radio\n"))

while r <= 0:
    r = int(input("Valor incorrecto, infrese un número mayor a 0\n"))

area = (r ** 2) * math.pi

print(f"El área de la circunferencia es {round(area,2)}")