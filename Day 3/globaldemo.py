x = 10  # global variable

def change():
    global x
    x = 20  # creates a *local* variable, doesn't affect global one
    print("Inside function:", x)

change()
print("Outside function:", x)
