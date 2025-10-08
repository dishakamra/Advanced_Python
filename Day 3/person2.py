# Inheriting and Reusing the Constructor
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # call parent __init__
        self.student_id = student_id

s = Student("Alice", "STU123")
print(s.name, s.student_id)
