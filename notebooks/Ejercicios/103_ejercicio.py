
print("--- CALCULADORA CIENTÍFICA ---")

print("Hola, elija una opción:")
print("1- Suma")
print("2- Resta")
print("3- Multiplicación")
print("4- División")
print("5- Módulo")
print("6- Exponente")

seleccione = int(input("Escoja un número y pulse ENTER:\n"))

error = True

match seleccione:
    case 1:
        print("A elegido la opción suma")
    case 2:
        print("A elegido la opción resta")
    case 3:
        print("A elegido la opción multiplicación")
    case 4:
        print("A elegido la opción división")
    case 5:
        print("A elegido la opción módulo")
    case 6:
        print("A elegido la opción exponente")
    case _:
        print("Error, opción inválida.")
        error = False

if error:
    
    primero = float(input("Especifique el primer operador:\n"))
    segundo = float(input("Especifique el segundo operador:\n"))

    match seleccione:
        case 1:
            resultado = round(primero + segundo, 2)
            print(f"El resultado de sumar {primero} más {segundo} es: {resultado}.")
        case 2:
            resultado = round(primero - segundo, 2)
            print(f"El resultado de restar {primero} menos {segundo} es: {resultado}.")
        case 3:
            resultado = round(primero * segundo, 2)
            print(f"El resultado de multiplicar {primero} por {segundo} es: {resultado}.")
        case 4:
            resultado = round(primero / segundo, 2)
            print(f"El resultado de dividir {primero} entre {segundo} es: {resultado}.")
        case 5:
            resultado = round(primero % segundo, 2)
            print(f"El resultado del módulo {primero} entre {segundo} es: {resultado}.")
        case _:
            resultado = round(primero ** segundo, 2)
            print(f"El resultado de la potencia {primero} elevado a {segundo} es: {resultado}.")
else:
    print('Por favor, vuelva a ejecutar la calculadora.')
            