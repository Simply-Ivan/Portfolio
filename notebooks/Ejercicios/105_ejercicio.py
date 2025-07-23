
print('-- PIZZERIA IVANCITO --')

dinero = float(input('Cuanto dinero tienes:\n'))

error = True

if dinero > 0:
    print('Estos son los tipos de pizza que tenemos')
    print('1- Pizza Americana')
    print('2- Pizza Hawaiana')
    print('3- Pizza Napolitana')
    eleccion = int(input('Elija que tipo de pizza desee:\n'))
    match eleccion:
        case 1:
            print('El tipo de pizza que escogio es la Americana')
        case 2:
            print('El tipo de pizza que escogio es la Hawaiana')
        case 3:
            print('El tipo de pizza que escogio es la Napolitana')
        case _:
            print('La opción no existe')
            error = False

else:
    print('Vuelva intentarlo')

 
