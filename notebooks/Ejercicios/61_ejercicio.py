
# Calcular la diferencia de fechas dadas

from datetime import date

hoy = date(2024,3,1)
otra_fecha = date(2020,3,6)

diferencia = hoy - otra_fecha

print(diferencia.days)
