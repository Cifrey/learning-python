# Class methods = allow operations related to the class itself
#                 take (cls) as the first parameter, which represents the class itself
#                 (instead of 'self' as instance methods)

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    # CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Battler", 1.2)
student2 = Student("Beato", 4.0)
student3 = Student("Rance", 2.5)

print(Student.get_count())
# When calling a class method ('get_count'), we can access or modify class data ('cls.count'), ('count = 0')

print(Student.get_average_gpa())