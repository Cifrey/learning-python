# input() = a function that prompts the user to enter data
# Returns the entered data as a string 

name = input("What is your name?: ")
age = input("How old are you?: ")

# age = age + 1 // No podríamos poner esto porque es una string,
# hay que convertirlo antes a int o bool//

age = int(age) # Podemos ahorrar esta línea si ponemos int en frente de la primera//

# De esta forma:

age = int(input("How old are you?: "))
age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calc

length = float(input("Enter the length: ")) # Si no ponemos float, 
width = float(input("Enter the width: ")) # devuelve el input como string//
area = length * width

print(f"The area is: {area}cm²")

# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} {item}/s")
print(f"You have to pay {total}€")

# Exercise: Madlibs game
# Word game where you create a story
# by filling in blanks with random words

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a nounverb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")