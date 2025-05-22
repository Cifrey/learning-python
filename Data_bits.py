# .append() sólo funciona con listas, no tuplas

# .add() es sólo para sets

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