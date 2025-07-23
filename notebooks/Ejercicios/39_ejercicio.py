
p = float(input("Ingrese el pago\n"))

while p <= 0:
    p = float(input("Valor incorrecto ingrese el pago\n"))
    
n = float(input("Ingrese un número\n"))

if n % 5 == 0 and n % 3 == 0:
    d = 0.25
    ne = 0.75 * p
else:
    if n % 5 == 0 and n % 3 != 0:
        d = 0.2
        ne = 0.8 * p
    else:
        if n % 5 != 0 and n % 3 == 0:
            d = 0.15
            ne = 0.85 * p
        else:
            d = 0.1
            ne = 0.9 * p

dp = 100 * d

print(f"El monto del descuento es {round(dp,2)}% y el monto neto es {round(ne,2)}")