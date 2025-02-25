from datetime import datetime
fecha = datetime.now()
print(fecha)

import datetime 
fecha = datetime.datetime.now()
print(fecha)

año = datetime.datetime.strftime(fecha, "%Y")
print(año)

#%d Dia
#%m Mes
#%Y Año
#%H Hora
#%M Minutos
#%S Segundos

