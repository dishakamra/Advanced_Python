'''
Stable sort by two keys
Task: Sort a list of dicts by dept (A→Z) and within each dept by -salary. Use one stable sorted call.
'''
print("Stable sort by two keys")
employees = [
{"name": "Amy", "dept": "Eng", "salary": 120},
{"name": "Bob", "dept": "HR", "salary": 90},
{"name": "Cara","dept": "Eng", "salary": 130},
{"name": "Dan", "dept": "HR", "salary": 100},
]
print("Employees: ", employees)
# Solution
res = sorted(employees, key=lambda e: (e["dept"], -e["salary"]))
print("Sorted: ", res)


'''
Deduplicate while preserving order
Task: Remove duplicates from a sequence while keeping the first occurrence.
'''
print("Deduplicate while preserving order")
items = [3,1,2,3,2,3,1]
# Solution
seen = set(); out = []
for x in items:
    if x not in seen:
        seen.add(x); out.append(x)
        print(out)
# out == [3,1,2]

'''
for-else search with predicate
Task: Find first string with length divisible by 5 or return "NONE".
'''
print("for-else search with predicate")
words = ["engineerin", "awsbed", "compute", "llmops"]
for word in words:
    if len(word) % 5 == 0:
        print(word)
        break
else:
    print("NONE")
        

