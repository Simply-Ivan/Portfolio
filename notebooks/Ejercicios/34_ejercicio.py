
s = float(input("Ingrese su sueldo\n"))

while s <= 0:
    s = float(input("Valor incorrecto ingrese su sueldo mayor a 0\n"))
    
if s > 1000:
    c = 1.12 * s
else:
    c = 1.15 * s

print(f"EL nuevo sueldo es {c}")