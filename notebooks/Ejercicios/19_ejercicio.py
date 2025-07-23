
c = float(input("Ingresar el capital\n"))

while c <= 0:
    c = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
t = int(input("Ingrese el tiempo\n"))

while t <= 0:
    t = int(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
r = int(input("Ingresar la tasa de interés\n"))

while r <= 0:
    r = int(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
m = ((1 + (r / 100)) ** t) * c
i = m - c

print(f"El interés es {round(i,2)}")