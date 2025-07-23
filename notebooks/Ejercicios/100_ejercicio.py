
num1 = int(input('Dame el primer número: '))
operador = str(input('Seleccione el operador: '))
num2= int(input('Dame el segundo número: '))
igual = str(input('Desea seguir operando: ')) 

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    resultado = num1 / num2
else:
    print('Operador no definido')
     
if igual == 'no':
    print(f'El resultado es igual a {resultado}')
elif igual == 'si':
    continuar = str(input('Seleccione el operador: '))
    while continuar != '=':
        if operador == '+':
            num3 = int(input('Dame un número: '))
            resultado += num3
        elif operador == '-':
            num3 = int(input('Dame un número: '))
            resultado -= num3
        elif operador == '*':
            num3 = int(input('Dame un número: '))
            resultado *= num3
        elif operador == '/':
            num3 = int(input('Dame un número: '))
            resultado /= num3
        else:
            print('Operador no definido')

        continuar = str(input('Seleccione el operador, si desea la respuesta presione =: '))

        if continuar == '=':
            print(f'El resultado es igual a {resultado}')
