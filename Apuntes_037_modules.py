# Module = a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files

print(help("modules"))
print(help("math"))

import math
import math as m # Se puede cambiar el nombre al módulo
print(m.pi)

from math import pi
print(pi)

# Para evitar problemas de legibilidad, es mejor importar el módulo de forma normal

import Apuntes_037_modules_module as example

result = example.pi
result2 = example.square(3)
result3 = example.cube(3)
result4 = example.circumference(3)
result5 = example.area(3)

print(result5)