class Student:
    def __init__(self, name, grades):
        self.name = name
        self._grades:list = grades

    @property
    def average(self):
        return sum(self._grades) / len(self._grades)

    @property
    def grade(self):
        return self._grades

    @grade.setter
    def grade(self,grade):
        self._grades.append(grade)

s = Student("Laylo", [90, 85, 80])
print(f"{s.name} o‘rtacha: {s.average}")
print(s.grade)
# s.average = 100  → Xato: read-only property
