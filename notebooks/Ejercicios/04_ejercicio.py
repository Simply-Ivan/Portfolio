nom = str(input("Ingresar tú nombre: "))
genero = str(input("Ingresar tú género. Si es varon escriba v y si es mujer m: "))

while genero != "v" and genero != "V" and genero != "m" and genero != "M":
    genero = str(input("Ingresar correctamente el género: v = varon, m = mujer: "))
    
if genero != "v" or genero != "V":
    m = "Bienvenida " + nom
else:
    m = "Bienvenido" + nom

print(m)