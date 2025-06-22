
import json
from load_save_menu import save,load,menu







class Product:
    def __init__(self, name, stock, price, category):
        self.id = None
        self.name = name
        self.stock = stock
        self.price = price
        self.category = category

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

    @staticmethod
    def read():
        return load("products.json")

    @staticmethod
    def update(name, atribut, value):
        products = load("products.json")
        for product in products:
            if product["name"] == name:
                if atribut in product:
                    product[atribut] = value
        save("products.json", products)

    @staticmethod
    def delete(name):
        products = load("products.json")
        for product in products:
            if product["name"] == name:
                products.remove(product)
        save("products.json", products)

def ekranga_chiqar():
    print("-" * 56)
    print(
        f"|{'ID'.center(5)}|{'Nomi'.center(15)}|{'Soni'.center(5)}|{'Narxi'.center(10)}|{'Turi'.center(15)}|")
    print("-" * 56)
    for product in Product.read():
        print(
            f"|{str(product['id']).center(5)}|{product['name'].center(15)}|{str(product['stock']).center(5)}|{str(product['price']).center(10)}|{product['category'].center(15)}|")

    print("-" * 56)


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    @staticmethod
    def read():
        return load("user.json")

    @staticmethod
    def create(username, password, role):
        users = load("user.json")
        lst = []
        for user in users:
            lst.append(user['id'])
        max_id = max(lst)
        users.append(
            {
                "id": max_id + 1,
                "username": username,
                "password": password,
                "role": role})
        save("user.json", users)

    @staticmethod
    def delete(username):
        users = load("user.json")
        for user in users:
            if username["name"] == username:
                users.remove(user)
        save("user.json", users)

    @staticmethod
    def update(name, atribut, value):
        users = load("user.json")
        for user in users:
            if user["name"] == name:
                if atribut in user:
                    user[atribut] = value
        save("user.json", users)

def ekranga_chiqar():
    print("-" * 56)
    print(
        f"|{'ID'.center(5)}|{'Username'.center(15)}|{'Password'.center(5)}|{'Roli'.center(10)}|")
    print("-" * 56)
    for user in User.read():
        print(
            f"|{str(user['id']).center(5)}|{user['username'].center(15)}|{user['password'].center(5)}|{user['role'].center(10)}|")

    print("-" * 56)



def admin_menu():
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




def foydalanuvchi_menu():
     habar = """
     Mahsulot amallardan birini tanlang:
        1. Mahsulotni Ko'rish
        2. Mahsulotni qidirish
        3. Mahsulotni filtrlash
        4. Savatchaga qoshish olish
        5. Savatchani Korish
        6. Savatchadan ochirish
        7. Profil
        0. Chiqish
     """
     while True:
        tanlov = menu(habar, range(1, 6))
        if tanlov == 1:
            ekranga_chiqar()
        elif tanlov == 2:
            username = input("username: ")
            password = input("parol: ")
            role = input("roli: ")
            User.create(username,password,role)

        elif tanlov == 4:
            ekranga_chiqar()
            name = input("Mahsulotni nomi: ")
            User.delete(name)
        elif tanlov == 5:
            break

def login():
    username = input("Username: ")
    password = input("Password: ")

    users = User.read()
    if not users:
        print("Foydalanuvchi mavjud emas. Avval ro'yxatdan o'ting.")
        return

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"\nXush kelibsiz, {username}!")
            if user["role"] == "admin":
                admin_menu()
            else:
                foydalanuvchi_menu()
            return
    print("Xatolik! Username yoki parol noto'g'ri.")


def register():
    users = User.read()
    username = input("Yangi username: ")
    if any(u['username'] == username for u in users):
        print("Bu username allaqachon mavjud.")
        return
    password = input("Parol: ")
    role = "customer"
    User.create(username, password, role)
    print("Muvaffaqiyatli ro'yxatdan o'tdingiz!")

if __name__ == "__main__":
    while True:
        tanlov = menu("""
Bittasini tanlang:
    1. Kirish
    2. Ro'yxatdan o'tish
    3. Chiqish
""", [1, 2, 3])
        if tanlov == 1:
            login()
        elif tanlov == 2:
            register()
        elif tanlov == 3:
            print("Dasturdan chiqildi.")
            break

