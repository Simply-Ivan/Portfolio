
def codigo(nombre, año):
    clave = ''
    for letra in nombre.split():
        bueno = letra.capitalize()
        clave += bueno[0]
    date = str(año)
    clave += date[-2:]
    return(clave)

print(codigo('gOMez  dAvid pARIPna ivAN', 2014))