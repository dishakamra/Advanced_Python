def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclaim_decorator(func):
    def wrapper():
        result = func()
        return result + "!!!"
    return wrapper

@uppercase_decorator
@exclaim_decorator
def say_hello():
    return "hello world"

print(say_hello())

@uppercase_decorator
def say_name():
    return "My name is John"

print(say_name())