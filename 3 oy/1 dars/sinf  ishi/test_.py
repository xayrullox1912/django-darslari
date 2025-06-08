class Test:

    def __init__(self, name, price, stock):
        self.name = name
        assert price > 0, "Narx >0 bo'lishi kerak"
        assert stock > 0, "Soni 0 dan katta emas"
        self.__price = price
        self.__stock = stock

    def total_price(self):
        return self.__price * self.__stock


    def  get_price(self):
        return self.__price

    def set_price(self, value):
        assert value > 0, "soni > 0 bo'lishi kerak"
        self.__price = value

    def get_stock(self):
        return self.__stock

    def set_stock(self,value):
        assert  value > 0, "soni > 0 bolishi kerak"
        self.__stock = value
