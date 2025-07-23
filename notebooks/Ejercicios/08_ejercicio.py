g = 9.8
m = float(input("Ingrese la masa\n"))

while m <= 0:
    m = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
p = m * g

print(f"El peso es {round(p,2)}")