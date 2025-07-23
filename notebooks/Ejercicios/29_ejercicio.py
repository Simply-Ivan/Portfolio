
s = float(input("Ingrese su sueldo\n"))

while s <= 0:
    s = float(input("Valor incorrecto. Ingrese un sueldo mayor a 0\n"))
    
if s < 1000:
    au = 1.15 * s
    print(f"Su sueldo es {round(au,2)}")
    
if s >= 1000:
    print(f"Su sueldo es {s}")