# Conditionals
items = [1,2,3,4,5,6,7]
status = "empty" if not items else "non-empty"
print(status)

if (n := len(items)) == 0:
    print("No items found")
elif n < 5:
    print("Few items found")
else:
    print("Too many items found")

# Loops
# for over iterables   ; while for conditions
# break, continue, else on loops
# find prime using for-else
n=29
for i in range(2, int(n**0.5)+1):
    if n%i == 0:
        print("Not Prime")
        break
else:
    print("prime")