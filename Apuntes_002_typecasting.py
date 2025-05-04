# Typecasting = the process of converting a variable from one data type to another
# str(), int(), float(), bool()

name = "Frey"
age = 28
money = 20.99
is_student = True

print(type(name)) # Devuelve str
print(type(age)) # Devuelve int
print(type(money)) # Devuelve float
print(type(is_student)) # Devuelve bool

money = int(money) # Con esto, convertirmos un float en
print(money)       # un int, quitando los decimales//

age = float(age)   # Sale 28.0 
print(age)

age = str(age)     # El valor de {age} se vuelve una string,
print(type(age))   # lo mismo que si pusiéramos comillas: "28"//

# age += 1 Da error, porque ahora es una string
# Si al 1 le añadimos comillas, se convierte en 281

name = bool(name) # Pongamos lo que pongamos, sale verdadero,
print(name)       # a no ser que lo dejemos vacío ""//