
c = float(input("Ingrese el monto de consumo\n"))

while c <= 0:
    c = float(input("Valor incorrecto. Ingresar un monto de consumo mayor a 0\n"))
    
i = 0.01 * c

if c > 100000:
    d = 0.02 * c
else:
    d = 0.01 * c
    
p = c - d + i

print(f"El descuento es {round(d,2)} el impuesto es {round(i,2)} y el importe a pagar es {round(p,2)}")