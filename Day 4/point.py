class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

p1 = Point(2, 3)
p2 = Point(3, 3)
print(p1 == p2)   # True → __eq__ called
