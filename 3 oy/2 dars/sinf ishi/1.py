class Employee:
    def __init__(self,id,first_name,last_name,salary):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_salary(self):
        return self.__salary

    def set_first_name(self,new_name):
        self.__first_name = new_name

    def set_last_name(self,new_last_name):
        self.__last_name = new_last_name

    def set_salary(self,new_salary):
        self.__salary = new_salary

    def raise_salary(self,value):
        return self.__salary * (1+value/100)

    def get_annual_salary(self,value):
        return self.__salary * 12

hodim = Employee(1,"xayrullox","komiljonov",300)

hodim.set_salary(300)
print(hodim.get_salary())