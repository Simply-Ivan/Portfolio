
al = float(input("Ingresar la altura\n"))

while al <= 0:
    al = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
b = float(input("Ingresar la base\n"))

while b <= 0:
    b = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
ar = (al * b) / 2
print(f"El área del triángulo es {round(ar,2)}")