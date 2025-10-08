class Book: # Defining the class
    def __init__(self, title, author): # constructor runs on creation
        self.title = title # instance attribute
        self.author = author #instance attribute

b1 = Book("Clean Code", "Robert C. Martin")  # instance of the class
b2 = Book("Fluent Python", "Luciano Ramalho") # instance of the class

print(b1.title)
print(b2.title)