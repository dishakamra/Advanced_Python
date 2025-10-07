# Returning multiple values
def stats(x, y):
    total = x + y
    avg = total / 2
    return total, avg

t, a = stats(10, 20)
print(f"Total: {t} | Average: {a}")

# Default parameters
def power(base, exp=2):
    return base ** exp

print(power(5)) #uses defaul exp=2
print(power(5, 3)) #overwrites default exp=2

# Default Pitfall
def append_bad(item, bucket=[]):  # BAD: one shared list!
    bucket.append(item)
    return bucket

print(append_bad(1))
print(append_bad(2))   # surprise: keeps old data!

def append_good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(append_good(1))
print(append_good(2))  # no carry-over

def demo(a, b, /, c, d=0, *args, e, f=1, **kwargs):
    # a, b: positional-only (must be passed by position)
    # c, d: either position or keyword
    # *args: extra positional arguments (tuple)
    # e, f: keyword-only (must be passed by name)
    # **kwargs: extra keyword arguments (dict)
    print(a, b, c, d, args, e, f, kwargs)

demo(1, 2, 3, 4, 5, 6, e=7, g=8)    # ok
# demo(a=1, b=2, c=3, e=7)          # TypeError: a,b are positional-only

# Argument unpacking'
def area(w, h):
    return w * h

pair = (3, 4)
print(area(*pair))   # unpack tuple into w, h

opts = {"w": 5, "h": 6}
print(area(**opts))  # unpack dict by matching names

# Pass-by-object-reference
# Rebinding
x = [1, 2]
y = x
x = [3, 4]
print("x:", x)
print("y:", y)

# Mutating
a = [1, 2]
b = a
a.append(3)
print("a:", a)
print("b:", b)



