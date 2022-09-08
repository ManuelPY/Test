#Uso del paquete dateutil en un entorno virtual de Python

from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print("\nActual")
print(now)
print("\nCon 1 mes de diferencia")
now = now + relativedelta(months=1, days=1, hours=10)
print(now)
print("\n")