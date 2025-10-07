person = ("Disha", 42, "Female")
print(person)
print(person[0])
print(len(person))

# Iterable Unpacking
city, state, country = "Pune", "Maharashtra", "India"
print(city, state, country)

# Extended Iterable Unpacking (*rest)
first, *middle, last = [1, 2, 3, 4, 5]
print(first)
print(middle)
print(last)

# Unpacking Function Arguments (* and **)

def greet(first, last, title="Ms."):
    print(f"Hello {title} {first} {last}!")

args = ("Disha", "Kamra")
kwargs = {"title": "Dr."}

greet(*args) # uses tuple for first and last
greet(*args, **kwargs) # adds tittle from dict

