# class variables = shared among all instances of a class
#                   defined outside the constructor
#                   allow you to share data among all objects created from that class

class Car:
    
    wheels = 4 # class variable (class attribute)

    def __init__(self, model, year):
        self.model = model # instance variable (instance attribute)
        self.year = year # instance variable (instance attribute)

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Battler", 18)
student2 = Student("Beato", 19)
student3 = Student("Rance", 18)
student4 = Student("Saya", 13)

print(student1.name)
print(student1.age)
print(Student.class_year) # Aunque se puede poniendo el objeto (student1.class_year), es buena práctica
#                           poner la clase si es para llamar a una variable de clase

print(Student.num_students)

print(f"My graduation class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
