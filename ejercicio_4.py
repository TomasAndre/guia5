"""4. Lea el radio (r) de una circunferencia y halle:
*la longitud de la circunferencia (2*PI*r) y área del círculo (PI*r^2)..
"""

import math


r = int(input("ingrese el radio: "))

longitud = (2*math.pi*r )
area = (math.pi*r**2)

print(f"longitud : {longitud}")
print(f"area: {area}")