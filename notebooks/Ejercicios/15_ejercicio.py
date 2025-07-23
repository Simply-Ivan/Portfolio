
b = float(input("Ingresar la base\n"))

while b <= 0:
    b = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
al = float(input("Ingresar la altura\n"))

while al <= 0:
    al = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
p = 2 * (b + al)
ar = al * b

print(f"El perímetro es {round(p,2)} y el área es {round(ar,2)}")