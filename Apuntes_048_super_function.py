# super() = function used in a child class to call methods from a parent class (superclass)
#           allows you to extend the functionality of the inherited methods

# Se usa super() porque si necesitas usar __init__ en una clase hija, estás reescribiendo el __init__ de la 
# clase padre. Al usar super(), heredas el __init__ y aparte añades más cosas específicas

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe() # Para heredar el método 'describe' del padre. Se puede poner abajo para cambiar el orden
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2") # Method overriding, lo sobreescribe
        # en caso de que no hayamos escrito super(). antes

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width * self.width}cm^2")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")

circle = Circle("red", True, 5) # También podríamos escribir (si queremos ser más claros) color="red", is_filled=True, etc.
square = Square("blue", False, 6) 
triangle = Triangle("yellow", True, 7, 8)

circle.describe()
square.describe()
triangle.describe()

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

# Se podría cambiar 'super().' por 'Shape.' pero es peor opción (menos flexible, puede romperse, etc)