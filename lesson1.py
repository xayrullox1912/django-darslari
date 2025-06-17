Mahsulotlar = [
    {"nom": "somsa", "tur": "oziq ovqat"},
    {"nom": "mashina", "tur": "texnika"},
]

def admin_panel():
    while True:
        tanlov = input("""
        1. Mahsulot Qoshish
        2. Foydalanuvchi Qoshish    
        3. Mahsulotlar Royhati
        4. Chiqish/n
        """)
        if tanlov == "1":
            nomi = input("Mahsulot nomi: ")
            turi = input("Mahsulot turi: ")
            Mahsulotlar.append({"nom": nomi, "tur": turi})
        elif tanlov == "2":
            input("Foydalanuvchi ismi: ")
        elif tanlov == "3":
            for mahsulot in Mahsulotlar:
                print(mahsulot["nom"], "-", mahsulot["tur"])
        elif tanlov == "4":
            break

def customer_panel():
    while True:
        tanlov = input("""
        1. Mahsulotlar Royhati
        2. Mahsulotlarni Qidirish
        3. Oziq Ovqat
        4. Texnika
        5. Chiqish
        """)
        if tanlov == "1":
            for mahsulot in Mahsulotlar:
                print(mahsulot["nom"], "-", mahsulot["tur"])
        elif tanlov == "2":
            n = input("Qidirilayotgan nom: ")
            for mahsulot in Mahsulotlar:
                if mahsulot["nom"] == n:
                    print(mahsulot["nom"], "-", mahsulot["tur"])
        elif tanlov == "3":
            for mahsulot in Mahsulotlar:
                if mahsulot["tur"] == "oziq ovqat":
                    print(mahsulot["nom"])
        elif tanlov == "4":
            for mahsulot in Mahsulotlar:
                if mahsulot["tur"] == "texnika":
                    print(mahsulot["nom"])
        elif tanlov == "5":
            break

while True:

    tanlov= input(""""
    1. Admin panel
    2. Cutomer panel
    3. Chiqish
    """)
    if tanlov == "1":
        admin_panel()
    elif tanlov == "2":
        customer_panel()
    elif tanlov == "3":
        break