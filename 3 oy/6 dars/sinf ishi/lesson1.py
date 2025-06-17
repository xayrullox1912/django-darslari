products = []
class Product:
    def __init__(self,name,stock,price):
        self.name = name
        self.__stock = stock
        self.price = price

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self,new_stock):
        self.__stock = new_stock

    def __str__(self):
        return f"{self.name} {self.price}"

    @staticmethod
    def update(name,price):
        for product in products:
            if product["name"] == name:
                product["price"] = price
            return 1
        return None

    @staticmethod
    def read():
        return products

    @staticmethod
    def create(name_,stock_,price_):
        for product in products:
            if product["name"] == name_:
                return None

        products.append({"name":name_, "stock":stock_ , "price":price_})
        return 1

    @staticmethod
    def delete(name):
        for product in products:
            if product["name"] == name:
                products.remove(product)
                return 1
        return None


def product_menu():
    while True:
        try:
            tanlov = int(input("""Raqamlardan birini tanlang
            1. Ko'rish
            2. Qoshish
            3. O`zgartirish
            4. O`chirish
            5. Chiqish \n"""))
        except ValueError:
            print("Iltimos, faqat raqam kiriting.")
            continue

        if tanlov == 1:
            print(Product.read())
        elif tanlov == 2:
            name = input("ism kiriting: ")
            stock = input("sonini kiritng: ")
            price = input("summasi kiriting: ")
            print(Product.create(name,stock,price))

        elif tanlov == 3:
            name = input("ism kiriting: ")
            price = input("summasi kiriting: ")
            print(Product.update(name, price))

        elif tanlov == 4:
            name = input("ism kiriting: ")
            print(Product.delete(name))

        elif tanlov == 5:
            break

product_menu()