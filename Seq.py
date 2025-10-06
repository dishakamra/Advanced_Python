# list
lst = [1,2,3]
print(lst)
lst.append(4)
print(lst)

# tuple
tpl = (1,2,3)
print(tpl)

seq = [10,20,30,40,50]
print(seq)
#first
print(seq[0])
#last
print(seq[-1])
# step (10, 20, 50)
print(seq[::2])
# Assigning to a slice can replace parts of a list
nums = [1,2,3,4]
print("NUMS", nums)
nums[1:3] = [99,100,101]
print("REPLACED 1:3", nums)

#Iterating, membership, length
for ch in "abc":
    print(ch)

print(3 in [1,2,3])
print(len((1,2,3)))


print("LIST examples")
# List opeartions (mutating vs non-mutating)
lst = [3,1,2]
print(lst)
# non-mutating (create a new list)
sorted_lst =  sorted(lst)
print("SORTED", sorted_lst)
print("ORIGINAL", lst)

# mutating (in place)
lst1 = [3,1,2]
print(lst1.sort())
print(lst1.append(4))

lst2 = [3,1,2]
lst2.remove(3) # remove first match
print(lst2)
#remove & return last
x= lst2.pop()
print(x)
lst2.clear()
print(lst2)

# Slice practice
# Given a = [0,1,2,3,4,5,6,7,8,9], produce [1,3,5,7,9] with a single slice.
a = list(range(10))
print(a)
res = a[1::2]
print(res)

# Safe reverse
# Return a reversed copy of list a without mutating a
rev = a[::-1]
print(rev)
