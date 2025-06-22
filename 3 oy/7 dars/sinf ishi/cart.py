from load_save_menu import load, save, menu
from datetime import datetime

class Cart:
    def __init__(self, product, user, date, status="tasdiqlanmagan"):
        self.product = product
        self.user = user
        self.date = date
        self.status = status

    @staticmethod
    def read():
        return load("cart.json")

    @staticmethod
    def create(product, user, date):
        carts = load("cart.json")
        ids = [cart['id'] for cart in carts]
        max_id = max(ids) if ids else 0

        carts.append({
            "id": max_id + 1,
            "product": product,  # ex: [{"name": "Olma", "total": 2, "price": 4000}]
            "user": user,
            "date": date,
            "status": "tasdiqlanmagan"
        })

        save("cart.json", carts)

    @staticmethod
    def delete(id_):
        carts = load("cart.json")
        carts = [cart for cart in carts if cart["id"] != id_]
        save("cart.json", carts)

    @staticmethod
    def update(id_, atribut, value):
        carts = load("cart.json")
        for cart in carts:
            if cart["id"] == id_:
                if atribut in cart:
                    cart[atribut] = value
        save("cart.json", carts)

def ekranga_chiqar():
    print("-" * 80)
    print(f"|{'ID'.center(5)}|{'product'.center(30)}|{'user'.center(10)}|{'date'.center(15)}|{'status'.center(15)}|")
    print("-" * 80)
    for cart in Cart.read():
        try:
            product_summary = ", ".join(
                f"{p['name']}({p['total']}x{p['price']})" for p in cart.get("product", [])
            ) if isinstance(cart.get("product"), list) else str(cart.get("product", ""))

            print(f"|{str(cart.get('id', 'N/A')).center(5)}|{product_summary.center(30)}|{cart.get('user','').center(10)}|{cart.get('date','').center(15)}|{cart.get('status','').center(15)}|")

        except Exception as e:
            print(f"❌ Xatolik: {e} => {cart}")

    print("-" * 80)


def foydalanuvchi_menu():
    habar = """
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
            # Mahsulotlar ro'yxati
            mahsulotlar = []
            while True:
                nomi = input("Mahsulot nomi: ")
                soni = int(input("Soni: "))
                narxi = int(input("Narxi: "))
                mahsulotlar.append({"name": nomi, "total": soni, "price": narxi})
                yana = input("Yana mahsulot qo‘shasizmi? (ha/yo'q): ").lower()
                if yana != "ha":
                    break

            user = input("Foydalanuvchi: ")
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Cart.create(mahsulotlar, user, date)

        elif tanlov == 3:
            ekranga_chiqar()
            id_ = int(input("Qaysi ID ni o‘zgartirmoqchisiz? "))

            h = "Nimasini o'zgartirmoqchisiz:\n\t1. product\n\t2. user\n\t3. date\n\t4. status\n"
            atribut = menu(h, range(1, 5))
            match atribut:
                case 1:
                    atribut = "product"
                case 2:
                    atribut = "user"
                case 3:
                    atribut = "date"
                case 4:
                    atribut = "status"

            value = input(f"Yangi {atribut} kiriting: ")

            # Product bo‘lsa, JSON bo‘lishi kerak
            if atribut == "product":
                value = eval(value)  # Masalan: [{'name':'Olma','total':2,'price':4000}]

            Cart.update(id_, atribut, value)

        elif tanlov == 4:
            ekranga_chiqar()
            id_ = int(input("ID ni kiriting: "))
            Cart.delete(id_)

        elif tanlov == 5:
            break
foydalanuvchi_menu()