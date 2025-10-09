class MyList:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __len__(self):
        return len(self.items)
    
    def __contains__(self, item):
        return item in self.items

fruits = MyList(["apple", "banana", "cherry"])
print(len(fruits))         # 3 → __len__
print(fruits[1])           # 'banana' → __getitem__
print("apple" in fruits)   # True → __contains__
