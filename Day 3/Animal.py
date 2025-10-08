'''
Basic Inheritance

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()
'''

'''

Extending Behavior(Override)

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()


'''

# Extending the parent (Using super())
class Animal1:
    def speak(self):
        print("Animal makes a sound")

class Cat(Animal1):
    def speak(self):
        super().speak()  # call parent version
        print("Cat meows")

c = Cat()
c.speak()

# Using ABC

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "Runs on four legs"

d = Dog()
print(d.speak())
print(d.move())





