# inheritance = allows a class to inherit attributes and methods from another class
#               helps with code reusability and extensibility
#               class Child(Parent), also called Sub and Super classes

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_mine = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Salchicha!")

class Raccoon(Animal):
    def speak(self):
        print("No sé qué dicen los mapaches")

dog = Dog("Nikita")
cat = Cat("Solanum")
raccoon = Raccoon("Rocket")

print(cat.name)
print(cat.is_mine)
cat.eat()
cat.sleep()

dog.speak()
cat.speak()
raccoon.speak()