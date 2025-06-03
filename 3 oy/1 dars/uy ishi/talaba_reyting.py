class student:
    def __init__(self,name):
        self.name = name
        self.__grades = []

    def add_grade(self,grade):
        if isinstance(grade,(int,float)) and 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("xatolik 0 dan 100 oraligidan ball bolishi kerak")
        
    def remove_grade(self,index):
        if 0 <= index < len(self.__grades):
            removed = self.__grades.pop(index)
            print(f"{removed} baho ochirildi")

        else:
            print("xatolik index notogri")

    @property
    def average(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        return 0

    @property
    def grades_count(self):
        return len(self.__grades)


    def get_rating(self):
        avg = self.average
        if avg == 100:
            return "zor"
        elif avg >= 90:
            return "barakalla"
        elif avg >= 75:
            return "yaxshi"
        elif avg >= 60:
            return "otdingiz"
        else:
            return "yiqildingiz"

s = student("Xayrullox")
s.add_grade(95)
s.add_grade(87)
s.add_grade(76)

print(f"{s.name} ortacha: {s.average:.1f}")      
print(f"reyting: {s.get_rating()}")                

s.name = "Sardor"
print(f"yangi ism: {s.name}")                    

s.remove_grade(1)                                 
print(f"ortacha: {s.average:.1f}")              
print(f"baho soni: {s.grades_count}")            

s.remove_grade(10)          