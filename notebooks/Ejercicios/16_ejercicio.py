
d = float(input("Ingrese su dinero\n"))

while d <= 0:
    d = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
c = float(input("Ingrese el costo\n"))

while c <= 0:
    c= float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))

v = d - c

print(f"El vuelto es {round(v,2)}")