def modify(x):
    print("Before:", x)
    x += [4]
    print("After:", x)

nums = [1, 2, 3]
modify(nums)
print("Outside function:", nums)
