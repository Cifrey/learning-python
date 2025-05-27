# Static method = a method that belongs to a class rather than any object from that class (instance)
#                 usually used for general utility functions

# Instance methods = best for operations on instances of the class (objects)
# Example: 

def get_info(self):
    return f"{self.name} = {self.position}"

# Static methods = best for utility functions that do not need access to class data
# Example:

@staticmethod
def km_to_miles(kilometers):
    return kilometers * 0.621371

#####################################

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self): # instance method
        return f"{self.name} = {self.position}" 
    
    @staticmethod # For making a static method, we need to put a decorator first
    def is_valid_position(position): # No need for 'self' because we're not working with any objects created from this class
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Beato", "Manager")
employee2 = Employee("Battler", "Janitor")
employee3 = Employee("Rance", "Cook")

print(employee1.get_info()) # Instance method *
print(employee2.get_info())
print(employee3.get_info())

print(Employee.is_valid_position("Cook")) # Static method **

# * For an instance method, we access the object ('employee1'), then call the instance method ('get_info()')
# ** For a static method, we only need to access the class ('Employee'), we don't need to create an object