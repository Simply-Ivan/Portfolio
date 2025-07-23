
a = float(input("Ingrese su altura\n"))

while a <= 0 and a > 3:
    a = float(input("Valor incorrecto. Ingresar una altura mayor a 0 y menor a 3\n"))
    
p = float(input("Ingrese su peso\n"))

while p <= 0 and p > 400:
    p = float(input("Valor incorrecto. Ingresar una peso mayor a 0 y menor a 3\n"))

i = p /(a ** 2)

if i > 16:
    if i > 17:
        if i > 18:
            if i > 25:
                if i > 30:
                    if i > 35:
                        if i > 40:
                            m = "Obesidad morbida"
                        else:
                            m = "Obesidad premórbida"
                    else:
                        m = "Sobrepeso crónico"
                else:
                    m = "Sobrepeso"
            else:
                m = "Saludable"
        else:
            m = "Bajo peso"
    else:
        m ="Infrapeso"
else:
    m = "Criterio de ingreso en hospital"
    
print(f"El diagnóstico es {m}")