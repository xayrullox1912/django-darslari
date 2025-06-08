class Masofa:
    def __init__(self,metr):
        self.__m = metr

    @property
    def km(self):
        return self.__m / 1000

    @km.setter
    def km(self,kilom):
        self.__m = kilom * 1000

    @property
    def sm(self):
        return self.__m * 100

    @sm.setter
    def sm(self,santim):
        self.__m = santim / 100






m = Masofa(5)
print(m.km)
print(m.sm)