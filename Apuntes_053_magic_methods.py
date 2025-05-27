# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations
#                 They allow developers to define or customize the behavior of objects

class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other): # Equal
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other): # Less than = lt
        return self.num_pages < other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("And then there were none", "Agatha Christie", 256)
book3 = Book("Dracula", "Bram Stoker", 576)

print(book3) # This returns the memory address if there's no __str__ method
print(book1 == book2) # This returns false even if we write the same parameters if there's no __eq__ method
print(book2 < book3) # This returns error if there's no __lt__ method
print(book2 + book3) # This returns error if there's no __ad__ method
print("Dracula" in book3) # This returns error if there's no __contains__ method
print(book2['title']) # This returns error if there's no __getitem__ method
print(book2['author']) # This returns error if there's no __getitem__ method
print(book2['num_pages']) # This returns error if there's no __getitem__ method