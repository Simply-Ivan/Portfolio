
gal = int(input("Ingrese el número de galones que desee comprar\n"))

while gal <= 0:
    gal = int(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
cant = 3.785 * gal
total = 8.2 * cant

print(f"El precio es {round(total,2)}")