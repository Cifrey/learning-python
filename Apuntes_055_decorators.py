# Decorator = a function that extends the behavior of another function
#             w/o modifying the base function
#             pass the base function as an argument to the decorator

def add_sprinkles(func):
    def wrapper(*args, **kwargs): # Tenemos que poner una función dentro para que sólo se imprima si llamamos
        print("*You add sprinkles 🎊*") # a la función 'get_ice_cream()' y se llame automáticamente al poner el decorador
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge 🍫*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("vanilla") # Returns error if we don't write arguments in 'wrapper()'