
nota = float(input("Ingresar la nota\n"))

while nota > 20 or nota < 0:
    nota = float(input("Valor incorrrecto la nota es menor o igual a 20 y mayor a 0\n"))

if nota >= 10.5:
    print("Aprobado")
    
if nota < 10.5:
    print("Desaprobado")