# How to use @decorator

def decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()