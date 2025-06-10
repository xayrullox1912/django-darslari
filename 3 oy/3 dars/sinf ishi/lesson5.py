class Kitob:

    def __init__(self, muallifi, kitob_nomi):
        self.muallifi = muallifi
        self.kitob_nomi = kitob_nomi
        self.narxi = 10


    @property
    def narxi(self):
        return self.__price

    @narxi.setter
    def narxi(self, value):
        assert isinstance(value, (int,float)), "int yoki float bo'lishi kerak"
        assert value > 0, "Musbat bo'lishi kerak"
        self.__price = value

    def __str__(self):
        return f"{self.muallifi} {self.kitob_nomi} {self.narxi}"

class Kutubhona:

    def __init__(self, nomi):
        self.nomi = nomi
        self.__kitoblar = []

    def qosh(self, kitob):
        self.__kitoblar.append(kitob)

    def kitob_ol(self, index):
        return self.__kitoblar[index]

    def __len__(self):
        return len(self.__kitoblar)

    def __getitem__(self, key):
        return self.__kitoblar[key]

    def __contains__(self, key):
        for i in self.__kitoblar:
            if i == self.kitob_nomi
        return key in self.__kitoblar




kitob1 = Kitob("Abdullo Qodiriy", "Mehrobdan Chayon")
kitob2 = Kitob("ABC", "Python")
kitob3 = Kitob("ABC", "Java")
kutubhona = Kutubhona("Alisher Navoiy")
kutubhona.qosh(kitob1)
kutubhona.qosh(kitob2)
kutubhona.qosh(kitob3)
print(kutubhona[1])
print(len(kutubhona))
print(kitob2 in kutubhona)
print("Python" in kutubhona)