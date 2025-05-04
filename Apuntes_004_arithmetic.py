# Sumas, restas, multiplicaciones, divisiones, potencias y modulo operator
friends = 10

friends = friends + 1 # //Podemos ahorrar texto si lo hacemos así:
friends += 1 # //Esto se llama augmented assignment operator
friends = friends - 2
friends -= 2
friends = friends * 3
friends *= 3
friends = friends / 2
friends /= 2
friends = friends ** 2
friends **= 2
remainder = friends % 3 # //Se divide en grupos iguales y sale lo que sobra, en este caso 1//
print(remainder)

#####################################################

x = 3.14
y = 4
z = 5
result = round(x) # //Para redondear números
result = abs(y) # //'Absolute value', la distancia hasta el 0
result = pow(4, 3) # //La potencia de a elevado a b (4^3)
result = max(x, y, z) # //El valor máximo entre esas 3 variables
result = min(x, y, z) # //El valor mínimo entre esas 3 variables
print(result)

#####################################################

import math # Para importar un módulo

x = 9.9

print(math.pi) 
print(math.e)
result = math.sqrt(x) # Square root, la raíz cuadrada de una variable
result = math.ceil(x) # Redondea un float hacia arriba siempre
result = math.floor(x) # Redondea un float hacia abajo siempre
print(result)

######################################################

# Exercise 1

import math

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")

# Exercise 2

import math

radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")

# Exercise 3

import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = round(math.sqrt((pow(a, 2) + pow(b, 2))), 2)

print(f"Side C = {c}cm")