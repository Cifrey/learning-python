name = input("Enter your full name: ")
phone_number = input("Enter your phone #: ")

result = len(name)
result = name.find("y") # Para encontrar la primera aparición de un carácter (empieza en 0)
result = name.rfind("a") # r significa reverse. Para encontrar la última aparición de un carácter
name = name.capitalize() # Convierte la primera letra en mayúsculas
name = name.upper() # Convierte todo en mayúsculas
name = name.lower() # Convierte todo en minúsculas
result = name.isdigit() # Comprueba si son todo dígitos (cuidado con los espacios)
result = name.isalpha() # Comprueba si son todo letras (cuidado con los espacios)
result = phone_number.count("-") # Cuenta cuántos carácteres existen
phone_number = phone_number.replace("-", "") # Reemplazar carácteres. Útil para cambiarlo por espacios o eliminarlos (dejándolo vacío)

print(phone_number)

print(help(str))

# Validate user input exercise 
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif username.find(" ") > 0:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")