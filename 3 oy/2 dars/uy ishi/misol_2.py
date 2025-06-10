class Book:
    def __init__(self, name: str, page_count: int, price: float):
        self.__name = name
        self.__page_count = page_count
        self.__price = price



    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def page_count(self):
        return self.__page_count

    @page_count.setter
    def page_count(self, value: int):
        print("== 1 ==")
        if value < 0:
            raise ValueError("Sahifalar soni manfiy bo'lishi mumkin emas.")
        self.__page_count = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Narx manfiy bo'lishi mumkin emas.")
        self.__price = value

    @price.deleter
    def price(self):
        self.__price = None


    def increase_pages(self, increment: int):
        if increment < 0:
            raise ValueError("sahifa oshirish miqdori manfiy bo'lishi mumkin emas.")
        self.page_count += increment


    def reduce_price(self, factor: float):
        if factor <= 0:
            raise ValueError("kamaytirish omili musbat bo'lishi kerak.")
        self.price = self.price / factor


    def process_books(self):
        self.page_count += 10
        if self.page_count > 100:
            self.reduce_price(2)


    @property
    def is_thick(self) -> bool:
        return self.page_count > 300


book = Book("Python Darslari", 280, 75000)
print("0")
print(book.get_name())
print("1")
print(book.get_price())
print("2")
book.increase_pages(30)
print("3")
book.process_books()

print(book.get_page_count())
print(book.page_count)
print(book.is_thick)
print(book.get_price())
