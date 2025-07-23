a = int(input("Ingrese el primer cateto\n"))

while a <= 0:
    a = int(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
b = int(input("Ingrese el segundo cateto\n"))
 
while b <= 0:
    b = int(input("Valor incorrecto. Ingrese un número mayor a 0\n"))

c = (a ** 2) * (b ** 2)

print(f"La hipotenuesa es {c}")