
# Crear una subcadena de n caracteres replicada n cantidad de veces.

def subcadena(cadena, n):
    
    if len(cadena) < n:
        n = len(cadena)
        
    palabra = cadena[:n]
    
    resultado = ''
    
    for i in range(n):
        resultado += palabra
    
    return resultado

print(subcadena('Python', 2))
print(subcadena('Python', 10))