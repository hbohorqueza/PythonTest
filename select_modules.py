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