def outer():
    count = 0
    def inner():
        nonlocal count # refers to the enclosing count
        count = count + 1  
        print(count)
    inner()
    inner()
    print("Outer ", count)

outer()
