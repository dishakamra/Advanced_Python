# Using import
import math_utils

print(math_utils.PI)
print(math_utils.circle_area(3))

# from X import name
from math_utils import circle_area
print(circle_area(2))

# import as (alias)
import math_utils as mu
print(mu.circle_area(1))

'''
# Why from module import * can bite you
# bad_practice.py
from math import *
# Which sqrt is this? Could shadow something else named sqrt.
print(sqrt(9))
'''
