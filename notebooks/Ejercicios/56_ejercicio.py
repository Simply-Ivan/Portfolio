
# Mostrar la fecha de un evento almacenada en una tabla.

fecha_evento = (2024, 3, 1)
print(f'La fecha es: {fecha_evento[2]}/{fecha_evento[1]}/{fecha_evento[0]}')

print('La fecha es: %i/%i/%i' % fecha_evento)

year, month, day = fecha_evento

print('La fecha es: {}/{}/{}'.format(day, month, year))