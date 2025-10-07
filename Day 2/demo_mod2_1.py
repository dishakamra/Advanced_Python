# List Comprehensions
nums = [1, 2, 3, 4, 5]
ev_sq = [n*n for n in nums if n % 2 == 0]
print(ev_sq)

# Dictionary Comprehensions
names = ["alice", "bob", "charlie"]
length_map = {name: len(name) for name in names}
print(length_map)

# Set Comprehensions
words = ["aws", "bedrock", "lambda", "aws", "ec2", "lambda"]
unique_lengths = {len(w) for w in words}
print(unique_lengths)


# Iterables (what you can loop over)
for ch in "AI":
    print(ch)

print(list(range(3))) # range is iterable; list() realizes it

# Generator Expressions (lazy one-liners)
gen = (n*n for n in range(5)) # 0, 1, 2, 3, 4
print(next(gen))  # 0
print(next(gen))  # 1
print(list(gen))  # consume the rest: [4, 9, 16]


# Generator Functions (yield)
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(3):
    print(value)


# Format Strings (f-strings)
name = "Disha"
score = 4.82
print(f"Hello {name}, CSAT is {score:.2f}/5")  # .2f = 2 decimals


# .format() Method
template = "Hello {0}, CSAT is {1:.1f}/5"
print(template.format("Disha", 4.8))

named = "Hello {name}, city={city}"
print(named.format(name="Disha", city="New Delhi"))


# Legacy % Formatting (know it, rarely use it)
name = "Disha"
score = 4.8
print("Hello %s, CSAT is %.1f/5" % (name, score))
