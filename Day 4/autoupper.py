# modifying Class Automatically

class AutoUpper(type):
    def __new__(cls, name, bases, dct):
        new_attrs = {}
        for attr_name, attr_value in dct.items():
            if not attr_name.startswith("__"):
                new_attrs[attr_name.upper()] = attr_value
            else:
                new_attrs[attr_name] = attr_value
        return super().__new__(cls, name, bases, new_attrs)

class MyClass(metaclass=AutoUpper):
    var = "hello"

    def greet(self):
        print("Hi!")

obj = MyClass()
print(hasattr(obj, "var"))   # False
print(hasattr(obj, "VAR"))   # True
obj.GREET()                  # Hi!
