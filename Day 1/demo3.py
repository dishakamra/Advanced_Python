words = ["bedrock", "aws", "python"]
print(sorted(words, key=len)) # by length

def greet(name):
    return f"Hello {name}"

print(greet("Disha"))

def example_func(a, b, /, c):
    print(f"a = {a}, b = {b}, c = {c}")

example_func(1, 2, c=3)
#example_func(a=1, b=2, c=3) # Invalid a and b are positional-only

def another_func(a, *, b, c):
    print(f"a = {a}, b = {b}, c = {c}")

another_func(1, b=2, c=3)

#Default values
def greet1(name="Guest", message="Hello"):
    print(f"{message}, {name}")

greet1()
greet1("Alice")
greet1("Bob", "Hi")

# * args
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# *kwargs
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="New York")
