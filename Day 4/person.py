class ValidateAttributes(type):
    def __new__(cls, name, base, dct):
        if 'greet' not in dct:
            raise TypeError(f"{name} must have a 'greet' method")
        return super().__new__(cls, name, base, dct)

class Person(metaclass=ValidateAttributes):
    def gret(self):
        print("Hello")