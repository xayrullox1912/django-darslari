import json
user_file = "users.json"
order_file = "orders.json"
product_file = "products.json"

def data_read(file_name):
    try:
        with open(file_name, "r") as file:
            datas = json.load(file)            
    except FileNotFoundError:
        with open(file_name, "w") as file:
            datas = []
            json.dump(datas,file)
    return datas

def data_write(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def register():
    users = data_read(user_file)
            
    login = input("Login: ")
    parol = input("Parol: ")
    id_list = [] # id
    for user in users:
        if user['username'] == login:
            print("Bu login bazada bor")
            return
        id_list.append(user['id']) # id
    
    id = max(id_list, default=0) + 1 # id
        
    users.append({"id":id, "username": login,"password": parol,"role": "user"})
    print("Ro'yxatdan o'tdingiz")
    data_write(users)


def login():
    users = data_read(user_file)
            
    login = input("Login: ")
    parol = input("Parol: ")
    for user in users:
        if user['username'] == login and user['password'] == parol:
            print("Do'konga hush kelibsiz")
            return login, user['role']
            
    print("Bazada bunday login yo'q")
    return None, None
    

def accepted_orders(status):
    orders = data_read(order_file)
    if not orders:
        print("Buyurtmalar yo'q")
    
    for order in orders:
        if order['status'] == status or status is None:
            print(f"id: {order['order_id']}; {order['username']} {order['product_id']} {order['product_name']}")

def new_product():
    products = data_read(product_file)
    name = input("maxsulot nomi: ")
    category = input("turini kiriting")
    price = int("narxini yozing")
    id_list = []
    product = [{"id": 1,"name": name,"category": category,"price": price,"stock": 5}] 
    if products.append(product):
        print("new product append")
        id = max(id_list, default=0) + 1 

def admin_menu():
    while True:
        try:
            menu = int(input("""Admin menyusi
        1. New orders (status: new)
        2. Accepted orders (status: accepted)
        3. Canceled orders (status: canceled)
        4. Add new product
        5. Delete product
        6. Logout\n"""))
        except:
            print("Xato. 1-6 oraliqda son kiriting:")
            continue
        if menu == 1:
            accepted_orders()
        elif menu == 2:
            accepted_orders('accepted')
        elif menu == 3:
            accepted_orders('canceled')
        elif menu == 4:
            new_product()
        

    

def user_menu(username):
    print(f"user {username}")

def main():

    while True:
        try:
            menu = int(input("""Elektron do'kon:
            1. Register
            2. Login
            3. Exit\n"""))
        except:
            print("Xato. 1-3 oraliqda son tanlang")
            continue

        if menu == 1:
            register()
        elif menu == 2:
            username, role = login()
            if role == "admin":
                admin_menu()
            elif role == "user":
                user_menu(username)            
        elif menu == 3:
            break
        else:
            print("Xato. 1-3 oraliqda son tanlang")

main()