class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"
    
    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book("Python Crash Course", "Eric Matthes")
print(b)          # Calls __str__
print(repr(b))    # Calls __repr__

b1 = Book("Programming Fundamentals", "Jon Johnson")
print(b1)          # Calls __str__
print(repr(b1))    # Calls __repr__
