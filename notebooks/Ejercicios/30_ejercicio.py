
e = int(input("Ingresar tú edad\n"))

while e <= 0:
    e = int(input("Valor incorrecto. Ingresar una edad mayor a 0\n"))
    
if e >= 18:
    print("Es mayor de edad")

if e < 18:
    print("Es menor de edad")