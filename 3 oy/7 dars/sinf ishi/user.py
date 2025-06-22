import  json
from load_save_menu import load,save,menu

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
            if user["username"] == username:
                users.remove(user)
        save("user.json", users)

    @staticmethod
    def update(username, atribut, value):
        users = load("user.json")
        for user in users:
            if user["username"] == username:
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

def foydalanuvchi_menu():
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
             username = input("username: ")
             password = input("parol: ")
             role = input("roli: ")
             User.create(username, password, role)

         elif tanlov == 3:
             ekranga_chiqar()
             username = input("usernameni kiriting: ")
             h = "Nimasini o'zgatirmoqchisiz:\n\t1. password\n\t2.role"
             atribut = menu(h, range(1, 4))
             match atribut:
                 case 1:
                     atribut = "password"
                 case 2:
                     atribut = "role"

             value = input("yangi parol/role kiriting: ")
             User.update(username, atribut, value)
         elif tanlov == 4:
             ekranga_chiqar()
             username = input("usernameni kiriting:  ")
             User.delete(username)
         elif tanlov == 5:
             break

foydalanuvchi_menu()