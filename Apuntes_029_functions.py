# function = a block of reusable code
# place () after the fuction name to invoke it


def happy_birthday(name, age): # Parameter: temporal variable inside a fuction
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Miss", 28) # Data inside a function is called "arguments"
happy_birthday("Frey", 29)
happy_birthday("Lin", 30)

def display_invoice(username, amount, due_date):
    print(f"Hello,  {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Frey", 34.99, "24/07")

# return = statement used to end a function and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("frey", "lin")

print(full_name)