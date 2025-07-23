
'''
paises = ['Afganistán', 'Albania', 'Alemania', 'Andorra',\
'Angola', 'Antigua y Barbuda', 'Arabia Saudita', 'Argelia',\
'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaiyán',\
'Bahamas', 'Bangladés', 'Barbados', 'Baréin', 'Bélgica',\
'Belice', 'Benín', 'Bielorrusia', 'Birmania', 'Bolivia',\
'Bosnia y Herzegovina', 'Botsuana' ,'Brasil', 'Bruné']
'''

for i in range(7, 15):
    print(f'el valor del bucle es: {i}.')

lista_numeros = [10, 45, 356, 10, 10, 10, 46, 67, 45, 10, 10, 43, 10, 65, 10, 10]

lista_numeros.sort()

for numero in lista_numeros:
    if numero == 10:
        continue
    elif numero == 356:
        break
    else:
        print(f'El valor del elemento es: {numero}.')