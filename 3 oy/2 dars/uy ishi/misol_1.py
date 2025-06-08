class Date:
    def __init__(self, day: int, month: int, year: int):
        self.__day = None
        self.__month = None
        self.__year = None
        self.set_date(day, month, year)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if not (1 <= value <= 31):
            raise ValueError("kun 1 dan 31 gacha bolishi kerak.")
        self.__day = value

    @day.deleter
    def day(self):
        self.__day = None

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if not (1 <= value <= 12):
            raise ValueError("oy 1 dan 12 gacha bo00000000000lishi kerak.")
        self.__month = value

    @month.deleter
    def month(self):
        self.__month = None

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not (1900 <= value <= 9999):
            raise ValueError("yil 1900 dan 9999 gacha bolishi kerak.")
        self.__year = value

    @year.deleter
    def year(self):
        self.__year = None

    def set_date(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        d = f"{self.day:02}" if self.day is not None else "None"
        m = f"{self.month:02}" if self.month is not None else "None"
        y = f"{self.year}" if self.year is not None else "None"
        return f"{d}/{m}/{y}"

    @property
    def kabisa_yili(self):
        if self.year is None:
            return False
        y = self.year
        return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


d = Date(5, 8, 2024)
print(d)
print(d.kabisa_yili)

d.day = 15
d.month = 12
d.year = 2000
print(d)

del d.day
print(d)
