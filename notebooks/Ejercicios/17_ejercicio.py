
n = int(input("Ingresar hasta que número se sumara\n"))

while n <= 0:
    n = int(input("Valor incorrecto. Ingresa un número mayor a 0\n"))
    
sum = (n * (n+1)) / 2

print(f"La suma de los primeros número enteros positivos es {sum}")