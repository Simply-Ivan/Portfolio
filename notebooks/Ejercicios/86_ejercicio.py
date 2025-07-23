
# Calcular el valor futuro para una cantidad, interés, y número de años específicos.

def valor_futuro(cantidad, interes, años):
    
    resultado = cantidad * ((1 + interes/100) ** años) 

    return f'La cantidad futura es {resultado}'

print(valor_futuro(2000, 10, 5))