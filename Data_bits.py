# logical operator = and, or, not
# membership operator = in, not in
# compound condition = 2 ó más logical operators en un if
# comparison operator = (==, !=, <, >, <=, >=)
# ternary operator = one-line of if-else

# .append() sólo funciona con listas, no tuplas

# list comprehension sólo funciona con listas (con una excepción específica)

# random.choice() espera una secuencia, no funciona con diccionarios

# Para asegurarme del input de usuario, es buena idea usar try-except. Ejemplo:
while True:
    try:
        bet = int(input("Place your bet amount: "))
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        break
    except ValueError:
        print("Invalid bet")

# \n para hacer una línea vacía antes o después

Principles = {
       "ETC = Easy To Change", 
       "DRY = Don't Repeat Yourself",
       "KISS = Keep It Simple, Stupid"
}

# Colores originales del tema: 
# "workbench.colorCustomizations": {
#   "editor.selectionBackground": "#264F78",
#   "editor.selectionHighlightBackground": "#FFFFFF0B",
#   "editor.wordHighlightBackground": "#575757B8"
# }

# dunder method = double underscore (así se llama a __)

# CamelCase = UpperCamelCase
#             lowerCamelCase (most common)
           
# PascalCase = capitalized, no " " or "_"
#              ex. FirstName

# snake_case = all minus, "_" instead of " " 

# dot operator = attribute access operator

# instanciar significa crear un objeto a partir de una clase 

# @abstractmethod es un decorador, se pone encima de la función que queremos que todas las subclases 
# hereden para que escriban su propia versión. Si no escribimos la subclase, no podemos instanciarla 
# (es decir, convertirla en objeto). Por ejemplo, si tenemos Shapes y queremos que la subclase Circle,
# Square, Triangle, etc, tenga su propia fórmula de calcular el área, y queremos asegurarnos que sí o sí
# está implementada en el código, podemos convertirlo en un método abstracto y así para poder trabajar con
# ello, hay que definir la fórmula para cada subclase obligatoriamente

# Event loop = like an infinite loop, constantly waiting for more user input (like an app or a videogame)

# Events in PyQt6 are referred to as Signals, it's the notifications emitted by widgets when something happens.
# Which can be used also to provide additional context about what happened.
# Slots are the receivers of signals. Any function can be used a slot by connecting the signal to it.
# Many Qt Widgets have their own built-in slots, meaning we can hook widgets together directly.
