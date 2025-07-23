
pi = 3.14159
r = float(input("Ingrese el radio\n"))

while r <= 0:
    r = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
area = (r ** 2) * pi
print(f"El área de la circunferencia es {round(area,2)}")