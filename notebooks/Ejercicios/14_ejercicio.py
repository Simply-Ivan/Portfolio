a = float(input("Ingresar el radicando\n"))

while a <= 0:
    a = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
n = int(input("Ingresa el radical\n"))

while n <= 1:
    n = int(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
r = a ** (1/n)

print(f"La raíz es {round(r,2)}")