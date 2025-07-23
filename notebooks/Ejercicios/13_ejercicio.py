matri = str(input("Ingrese el código del estudiante\n"))

n1 = float(input("Ingrese la primera nota\n"))

while n1 < 0 or n1 > 20:
    n1 = float(input("Valor incorrecto. Ingrese un número mayor o igual a 0 y menor o igual a 20"))
    
n2 = float(input("Ingrese la segunda nota\n"))

while n2 < 0 or n2 > 20:
    n2= float(input("Valor incorrecto. Ingrese un número mayor o igual a 0 y menor o igual a 20"))
    
n3 = float(input("Ingrese la tercera nota\n"))

while n3 < 0 or n3 > 20:
    n3 = float(input("Valor incorrecto. Ingrese un número mayor o igual a 0 y menor o igual a 20"))
    
n4 = float(input("Ingrese la cuarta nota\n"))

while n4 < 0 or n4 > 20:
    n4 = float(input("Valor incorrecto. Ingrese un número mayor o igual a 0 y menor o igual a 20"))

n5 = float(input("Ingrese la quinta nota\n"))

while n5 < 0 or n5 > 20:
    n5 = float(input("Valor incorrecto. Ingrese un número mayor o igual a 0 y menor o igual a 20"))
    
prom = (n1 + n2 + n3 + n4 + n5) / 5

print(f"La nota del alumno {matri} es {round(prom,2)}")