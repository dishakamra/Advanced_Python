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

# Generator Expressions (lazy one-liners)

# Generator Functions (yield)

# Format Strings (f-strings)

# .format() Method

# Legacy % Formatting (know it, rarely use it)
