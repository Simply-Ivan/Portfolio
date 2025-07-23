
p = float(input("Cuanto es el procentaje de pérdida de peso\n"))

while p <= 0:
    p = float(input("Valoe incorrecto. Ingrese un porcentaje de perdida de peso mayor a 0"))
    
if p > 1:
    if p > 5:
        if p > 10:
            if p > 30:
                print("No resistente")
            else:
                print("Muy poco resistente")
        else:
            print("Moderadamente resistente")
    else:
        print("Resistente")
else:
    print("Altamente resistente")