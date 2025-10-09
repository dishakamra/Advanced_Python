class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    def __add__(self, other):
        return Temperature(self.celsius + other.celsius)

    def __lt__(self, other):
        return self.celsius < other.celsius

t1 = Temperature(30)
t2 = Temperature(25)
print(t1 + t2)     # 55°C
print(t1 < t2)     # False
