'''
Sorting with key

Task: Sort ["capgemini", "aws", "vanguard", "ai"] by length descending.
'''
items = ["capgemini", "aws", "vanguard", "ai"]
print(sorted(items, key=len, reverse=True))

'''
Lambdas & Comprehensions

Task: Given [1,2,3,4,5], make a list of squares of even numbers only.
'''
nums = [1,2,3,4,5]
ev_sq = [n*n for n in nums if n % 2 == 0]
print(ev_sq)

'''
Write a lambda function to check if a number is even.
'''
is_even = lambda n: n % 2 == 0
print(is_even(10))  # True
print(is_even(7))   # False

'''
Use filter() and a lambda to extract words that start with the letter “a”.
'''
words = ["apple", "banana", "apricot", "cherry", "avocado"]
a_words = list(filter(lambda w: w.startswith('a'), words))
print(a_words)

'''
Use reduce() and a lambda to find the maximum number in a list.
'''
from functools import reduce

nums = [10, 3, 45, 7, 9]
max_num = reduce(lambda a, b: a if a > b else b, nums)
print(max_num)