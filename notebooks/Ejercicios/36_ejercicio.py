
e = int(input("Ingrese su edad\n"))

while e <= 0:
    e = int(input("Valor incorrecto. Ingrese una edad mayor a 0\n"))
    
if e >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")