c = float(input("Ingrese el grado en celsius\n"))

while c <= -273:
    c = float(input("Valor incorrecto. Ingrese un número mayor a -273\n"))
    
f = 32 + (9 * c) / 5

print(f"El grado en Fahrenheit es {round(f,2)}")