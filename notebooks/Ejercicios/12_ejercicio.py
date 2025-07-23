a = float(input("La base de la potencia\n"))

while a <= 0:
    a = float(input("Valor incorrecto, ingrese un número mayor a 0"))
    
n = int(input("El exponente de la potencia\n")) 

while n <= 0:
    n = float(input("Valor incorrecto, ingrese un número mayor a 0"))
    
pot = a ** n

print(f"La potencia es {round(pot,2)}")