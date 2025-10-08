class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_str):
        y, m, d = map(int, date_str.split('-'))
        return cls(y, m, d)
    
d1 = Date(2025, 10, 7)
d2 = Date.from_string('2025-10-07')

print(d1.year, d1.month, d1.day)
print(d2.year, d2.month, d2.day)