
I = float(input("El ingreso mnesual es:\n"))

while I <= 0:
    I = float(input("Valor incorrecto. Escriba un ingreso mayor a 0\n"))
    
if I > 300:
    if I > 1000:
        NC = 75
        CI = 30
    else:
        NC = 120
        CI = 15
    print(f"La cuota inicial es {CI}% del costo de la casa y el neto se distribuirá es {NC} cuotas mensuales")
else:
    print("Ingreso mensuela insuficiente")