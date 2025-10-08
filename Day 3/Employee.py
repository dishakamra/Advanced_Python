"""
Create Employee with name. Create Manager(Employee) that adds team_size. Override __str__ in both to show their info.
 
"""

class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee({self.name})"

class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

    def __str__(self):
        return f"Manager({self.name}, team_size={self.team_size})"


print(str(Employee("Alice"))) 
print(str(Manager("Victor", 5)))