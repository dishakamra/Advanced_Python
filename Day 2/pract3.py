'''
Dict Comprehension

Task: Build {word: word.upper()} for ["aws","bedrock","lambda"].
'''
words = ["aws","bedrock","lambda"]
mapping = {w: w.upper() for w in words}
print(mapping)


'''
Set Comprehension

Task: From ["apple","pear","plum","pear"], build a set of first letters.
'''
fruits = ["apple","pear","plum","pear"]
first_letters = {f[0] for f in fruits}
print(first_letters)



'''
Generator Expression

Task: Create a generator that yields cubes n**3 for n in range(4). Print the list of remaining values after one next().
'''


'''
Generator Function

Task: Write even_up_to(n) that yields even numbers from 0..n (inclusive). Print numbers for n=7.
'''

'''
String Formatting

Task: Using an f-string, print:
Learners: 20 | CSAT: 4.82/5 | City: Seattle
'''


