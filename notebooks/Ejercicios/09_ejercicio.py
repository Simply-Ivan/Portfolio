
p = float(input("Ingrese el peso en kilogramos\n"))

while p <= 0 and p > 300:
    p = float(input("Valor incorrecto.Ingrese un número mayor a 0\n"))
    
e = float(input("Ingrese la estatura en metros\n"))

while e <= 0 and e > 3:
    e = float(input("Valor incorrecto. Ingrese un núemro meyor a 0\n"))
    
imc = p / (e ** 2)

print(f"El imc es {round(imc, 2)}")