
var = str(input('Dame una palabra: '))

def mayu(var):
    
    resultado = var[0].upper() + var[1:].lower() 
    
    return resultado
    

print(mayu(var))
