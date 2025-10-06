x = 10 # bind name to int object
x = x + 1 # creates a new int object; int are immutable
print(x)

#multiple assignment / unpacking
name, age = "John", 20
print (name, age)

# Basic Python Data Types
# int
big = 10**100

# floats
val = 0.1 + 0.2
round(val, 10)

# complex numbers
z = 2 + 3j
z.real, z.imag

# bool behaves like int in arithetic
print(True + True == 2)

s = 'cafe'
print(s)
print(len(s))

def find(user):
    return None

if find("x") is None:
    print("Not found")

colors = ['red', 'green', 'blue', 'purple', 'pink', 'yellow', 'black']
# red
print(colors[0])
# green, blue, purple
print(colors[1:4])
# black
print(colors[-1])
# red, green, blue
print(colors[:3])
# purple, pink, yellow, black
print(colors[3:])