'''
sorted() function (doesn’t change the original)

sorted(iterable, key=None, reverse=False) returns a new sorted list.
'''
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(sorted(nums)) # ascending
print(nums) # original unchanged
print(sorted(nums, reverse=True))


'''
Custom Sort Keys

Use key= to tell Python how to compare.
'''
words =["aws", "bedrock", "lambda", "ec2"]
# by length
print(sorted(words, key=len)) # key function applied to each element

#by last letter
print(sorted(words, key=lambda w: w[-1]))


'''
Lambda Functions (tiny, throwaway functions)

Anonymous functions written inline.
'''
add = lambda x, y: x + y
print(add(3, 5))

# square of a number
sq = lambda n: n*n
print(sq(4))

# using lambda inside sorted()
students =[("John", 22), ("Alice", 25), ("Bob", 20)]
# Sort by age (2nd element of each tuple)
sorted_students = sorted(students, key=lambda s: s[0])
print(sorted_students)

# lambda with map(), filter(), and reduce()
nums = [1, 2, 3, 4, 5]
print(nums)
sq = list(map(lambda n: n**2, nums))
print(sq)

even_nums = list(filter(lambda n: n % 2 == 0, nums))
print(even_nums)

from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)

# Lambda inside another function
def multiplier(factor):
    return lambda x: x * factor

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(10))