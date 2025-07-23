
# Emular el funcionamiento del producto de cadenas

def producto_cadenas(cadena, repeticiones):
    resultado = ''
    
    for i in range(repeticiones):
        resultado += cadena
    
    return resultado

print(producto_cadenas('Andy', 2))