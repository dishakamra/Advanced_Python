'''
Tuples & Unpacking
Task: Given record = ("AWS Bedrock", "GenAI", 2025), unpack into course, topic, year and print:
Course: AWS Bedrock | Topic: GenAI | Year: 2025
'''
record = ("AWS Bedrock", "GenAI", 2025)
course, topic, year = record
print(f"Course: {course} | Topic: {topic} | Year: {year}")

'''
Extended Unpacking

Task: From [100, 200, 300, 400, 500], bind head=100, tail=500, and body=[200,300,400] and print them.
'''

nums = [100, 200, 300, 400, 500]
head, *body, tail = nums
print(head, body, tail)

'''
Unpacking Function Args

Task: Write area(w, h) returning w*h. Call it using a tuple (7, 5) and a dict {"w": 3, "h": 9}.
'''
def area(w, h): 
    return w * h

dims = (7, 5)
print(area(*dims))

params = {"w": 3, "h": 9}
print(area(**params))
