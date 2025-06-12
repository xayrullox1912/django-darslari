class Developer:
    def __init__(self,surname,position,salary):
        self.surname = surname
        self.position = position
        self.salary = salary

class SoftwareEngineer(Developer):
    def __init__(self,surname, position, salary, bonus, department):
        super().__init__(surname,position,salary)
        self.bonus = bonus
        self.department = department

    def total_payment(self):
        return self.salary + self.bonus


engineers = []

for i in range(5):
    surname = input("familya kiriting: ")
    position = input("position kiriting: ")
    salary = int(input("oylik kiriting: "))
    bonus = int(input("bonus miqdorini kiriting: "))
    department = input("bo`limini kiriting: ")

    engineer = SoftwareEngineer(surname,position,salary,bonus,department)
    engineers.append(engineer)


department_stats = {}

for eng in engineers:
    dep = eng.department
    total = eng.total_payment()
    if dep not in department_stats:
        department_stats[dep] = [1, total]
    else:
        department_stats[dep][0] += 1
        department_stats[dep][1] += total

for dep in sorted(department_stats):
    count, total = department_stats[dep]
    print(f"{dep}: {count} ta dasturchi jami to‘lov: {total}")
