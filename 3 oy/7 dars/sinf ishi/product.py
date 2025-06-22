"""
Product
[
    {"name": "",
     "stock": 0,
     "price": 0,
     "category": ""}
]

User [
{"username": "",
"password": "",
"role": ""}
]

Cart

[
"products": [{"name": "", "total": 0 , "price":4000}]
"username": "",
"date": ""
"status" : "tasdiqlanmagan" # tasdiqlangan, qabul qilingan
]

"""
import json
from load_save_menu import save,load,menu


class Product:
    def __init__(self, name, stock, price, category):
        self.id = None
        self.name = name
        self.stock = stock
        self.price = price
        self.category = category


    #CRUD
    # Create
    @staticmethod
    def create(name, stock, price, category):
        products = load("products.json")
        lst = []
        for product in products:
            lst.append(product['id'])
        max_id = max(lst)
        products.append(
            {
            "id": max_id + 1,
            "name": name,
             "stock": stock,
             "price": price,
             "category": category})
        save("products.json",products)
    #
    # Read
    @staticmethod
    def read():
        return load("products.json")
    #
    # Update
    @staticmethod
    def update(name, atribut, value):
        products = load("products.json")
        for product in products:
            if product["name"] == name:
                if atribut in product:
                    product[atribut] = value
        save("products.json", products)
    #
    # Delete
    @staticmethod
    def delete(name):
        products = load("products.json")
        for product in products:
            if product["name"] == name:
                products.remove(product)
        save("products.json", products)



class Cart:
    pass




def ekranga_chiqar():
    print("-" * 56)
    print(
        f"|{'ID'.center(5)}|{'Nomi'.center(15)}|{'Soni'.center(5)}|{'Narxi'.center(10)}|{'Turi'.center(15)}|")
    print("-" * 56)
    for product in Product.read():
        print(
            f"|{str(product['id']).center(5)}|{product['name'].center(15)}|{str(product['stock']).center(5)}|{str(product['price']).center(10)}|{product['category'].center(15)}|")

    print("-" * 56)

if __name__ == "__main__":
 habar = """
 Mahsulot amallardan birini tanlang:
    1. Ko'rish
    2. Kiritish
    3. O'zgartirish
    4. O'chirish
    5. Chiqish
 """
 while True:
    tanlov = menu(habar, range(1, 6))
    if tanlov == 1:
        ekranga_chiqar()
    elif tanlov == 2:
        name = input("Nomi: ")
        stock = input("Soni: ")
        price = input("Narxi: ")
        cateogry = input("Turi: ")
        Product.create(name, stock, price, cateogry)
    elif tanlov == 3:
        ekranga_chiqar()
        name = input("Mahsulotni nomi: ")
        h = "Nimasini o'zgatirmoqchisiz:\n\t1. Narxi\n\t2.Soni\n\t3.Kategoriyasi"
        atribut = menu(h, range(1, 4))
        match atribut:
            case 1: atribut = "price"
            case 2: atribut = "stock"
            case 3: atribut = "category"
        value = input("Qiymatni kiriting: ")
        Product.update(name,atribut, value)
    elif tanlov == 4:
        ekranga_chiqar()
        name = input("Mahsulotni nomi: ")
        Product.delete(name)
    elif tanlov == 5:
        break
