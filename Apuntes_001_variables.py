# This is my first Python program
# Variable = a container for a value (string, integer, float, boolean)

# Strings
first_name = "Cifrey"
food = "arroz con curry"
email = "solastet@fake.com"

print(f"Hello, {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers
age = 20
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 9.99
gpa = 3.2
distance = 5.5

print(f"The price is {price}€")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")

# Boolean
is_student = True
for_sale = False
is_online = False

print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if is_online:
    print("You are online")
else:
    print("You are offline")
