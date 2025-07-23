
t = int(input("Ingrese el tiempo en segundos\n"))

while t <= 0:
    t = int(input("Valor incorrecto. Ingresar un número mayor a 0\n"))
    
hor = t // 3600
hor_rest = t % 3600
min = hor_rest // 60
seg = hor_rest % 60

print(f"El tiempo es {hor} horas {min} minutos {seg} segundos")