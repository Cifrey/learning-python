# *args    = allows you to pass multiple non-key arguments (TUPLE)
# **kwargs = allows you to pass multiple keyword-arguments (DICTIONARY)
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY 

# def add(*nums): # El nombre del argumento puede ser el que sea, pero se suele poner *args
#     total = 0   # Y se convierte en una tupla
#     for num in nums:
#         total += num
#     return total

# print(add(1, 2, 3))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Battler", "Ushiromiya", "san")

# def print_address(**kwargs): # Se convierte en un diccionario
#     for key, value in kwargs.items():
#         print(f"{key.capitalize()}: {value}")

# print_address(street="123 Fake St.",
#               apt="100",
#               city="Detroit",
#               state="MI",
#               zip="54321")

def shipping_label(*args, **kwargs): # Importante el orden, primero args, luego kwargs
    for arg in args:
        print(arg, end=" ")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zip="54321")



