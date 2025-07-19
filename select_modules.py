## The function returns an alphabetically sorted list containing all the names of the entities available in the module.

import math
  
for name in dir(math):
  print(name, end="∖t")

###   Funciones selectas del módulo math  ###

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)


###  Funciones selectas del módulo random    #####

## produce un número flotante x entre el rango (0.0, 1.0) - en otras palabras: (0.0 <= x < 1.0).

from random import random

for i in range(5):
    print(random())



from random import random, seed

seed(0)

for i in range(5):
    print(random())


## La función processor
## La función processor() devuelve una cadena con el nombre real del procesador (si lo fuese posible)

from platform import processor, machine, system, version

print(processor())
print(machine())
print(system())
print(version())
