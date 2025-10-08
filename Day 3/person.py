class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# creat an instance (object)
p1 = Person("Alice", 25)

print(p1.name)
print(p1.age)

# Add and read a new attribute
p1.city = "New York"
print(p1.city)