# object = a "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# __init__ = method called constructor (init is initialize)
# siempre se pone self primero
from Apuntes_044_python_oop_class import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Tesla", 2026, "yellow", True)

# print(car2.model) # dot operator = is called attribute access operator
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)

car1.stop()
car1.drive()
car1.describe()