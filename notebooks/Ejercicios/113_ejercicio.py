print('Bienvenido a Mi Red')

apellido_pat = input('Para empezar dime,¿Cuál es tu apellido paterno? ')
apellido_mat = input('¿Cuál es tu apellido materno? ')
nombre = input('¿Cuál es tu nombre? ')
dato = apellido_pat+' '+apellido_mat+' '+nombre

print('Hola', nombre, 'Bienvenido a Mi Red')
print()

año = int(input('Para preparar tu perfil, dime en que año naciste. '))
edad = 2023 - año - 1
print()

estatura = float(input('Cuentame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? damelo en metros. '))
estatura_cm = int(estatura*100)
print()

num_amigos = int(input('Muy bien. Finalmente cuantos amigos tienes. '))
print()

print('Muy bien amigo', nombre, 'con estos datos podemos crear tu perfil')
print('----------------------------------------------')
print('Nombre:', dato)
print('Edad:', edad)
print('Estatura:', estatura, 'en metros y', estatura_cm, 'centímetros')
print('Amigos: ',num_amigos)
print('-------------------------------------------------')
print('Gracias por la información espero que disfrude de Mi Red')
print()

mensaje = input('Ahora vamos públicar tu primer mensaje. ¿Qué piensas hoy? ')
print()
print('------------------------------------------------------')
print(nombre, 'dice:', mensaje)
