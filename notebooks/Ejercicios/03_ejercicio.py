import math

r = int(input("Ingrese el radio\n"))

while r <= 0:
    r = int(input("Valor incorrecto, ingrese un número mayor a 0\n"))
    
lon = 2 * r * math.pi

print(f"La longitud del círculo es + {round(lon,2)}")