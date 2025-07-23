
# Imprimir el calendario para un año y mas específicos.

import calendar
import datetime

year = int(input('Escibir el año:\n'))
month = int(input('Escibir el mes:\n'))

print(calendar.month(year, month))
