
nom = str(input("Ingresar el nombre del dinosaurio\n"))

li = float(input("Ingresar el peso en libras\n"))

while li <= 0:
    li = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
pi = float(input("Ingresar la longitud en pies\n"))

while li <= 0:
    li = float(input("Valor incorrecto. Ingrese un número mayor a 0\n"))
    
m = pi * 0.3048
kg = li * 0.453592

print(f"El dinosaurio {nom} tiene un peso de {round(kg,2)}kg y tiene una longitud de {round(m,2)}m")