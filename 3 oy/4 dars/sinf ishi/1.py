class Person:
    def __init__(self,name,adress):
        self.__name = name
        self.__adress = adress

    @property
    def name(self):
        return f"{self.__name}"

    @property
    def adress(self):
        return f"{self.__adress}"

    @adress.setter
    def adress(self,new_adress):
        self.__adress == new_adress

    def __str__(self):
        return f"{self.__name} {self.__adress}"

class Student(Person):
    def __init__(self,name,adress,course:list=[],grades:list=[]):
        super().__init__(name,adress)
        self.course = course
        self.grades = grades


    def add_course_grade(self,new_course,new_grades):
        self.course.append(new_course)
        self.grades.append(new_grades)

    def get_average_grade(self):
        avg_grade = sum(self.grades)  / len(self.grades)
        return avg_grade

    def __str__(self):
        return f"{self.course} {self.grades}"


class Teacher(Person):
    def __init__(self, name, adress ,courses: list=[] ):
        super().__init__(name, adress)
        self.courses = courses

    def add_course(self,new_course):
        self.courses.append(new_course)

    def remove_course(self,course:str):
        if course in self.courses:
            self.courses.remove(course)

    def __str__(self):
        return f"{self.courses}"



s1 = Student("Ali", "Tashkent")
s1.add_course_grade("Math", 90)
s1.add_course_grade("English", 80)


print("O'rtacha baho:", s1.get_average_grade())

t1 = Teacher("Gulbahor", "Samarqand")
t1.add_course("Math")
t1.add_course("Physics")
t1.remove_course("Math")


