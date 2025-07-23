import math

l1 = float(input("Ingrese el primer lado del triángulo\n"))

while l1 <= 0:
    l1 = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
l2 = float(input("Ingrese el segundo lado del triángulo\n"))

while l2 <= 0:
    l2 = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
l3 = float(input("Ingrese el tercer lado del triángulo\n"))

while l3 <= 0:
    l3 = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
s = (l1 + l2 + l3) / 2
a = math.sqrt(s * (s - l1) * (s - l2) * (s - l3))

print(f"El área del triángulo es {round(a,2)}")