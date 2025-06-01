import csv
import os

FILENAME = 'students.csv'

def load_students():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME,newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def save_students(students):
    with open(FILENAME,"w",newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames=['id','name','course','email','phone'])
        writer.writeheader()
        writer.writerows(students)

def show_students():
    students = load_students
    if not students:
        print('hech qanday students yoq')
        return
    for i in students:
        print(f"{i['id']}. {i['name']} - {i['course']} - {i['email']} - {i['phone']}")

def add_students():
    students = load_students
    new_id = str(max([int(i['id']) for i in students], default=0)+1)
    name = input("ism kiriting: ")
    course = input("kurs kiriting: ")
    email = input("email kiriting: ")
    phone = input("phone kiriting: ")
    students.append({'id': new_id , 'name': name, 'course': course, 'email': email, 'phone': phone})
    save_students(students)
    print('talaba qoshildi')



def update_student():
    students = load_students()
    id_ = input("Yangilamoqchi bolgan student ID sini kiriting: ")
    for s in students:
        if s['id'] == id_:
            name = input(f"Ism Familya ({s['name']}): ") or s['name']
            course = input(f"Kurs ({s['course']}): ") or s['course']
            email = input(f"Email ({s['email']}): ") or s['email']
            phone = input(f"Telefon ({s['phone']}): ") or s['phone']
            s.update({'name': name, 'course': course, 'email': email, 'phone': phone})
            save_students(students)
            print("Yangilandi.")
            return
    print("Bunday ID topilmadi.")

def delete_students():
    students = load_students
    id_ = input('ochirmoqchi bolgan student id ni kiriting: ')
    for i in students:
        if i['id'] == id_:
            students.remove(i)
            save_students(students)
            print('student ochirildi')
        else:
            print('bunday id mavjud emas')

def search_student():
    students = load_students()
    keyword = input("Qidiruv (ism yoki kurs): ").lower()
    found = [s for s in students if keyword in s['full_name'].lower() or keyword in s['course'].lower()]
    if found:
        for s in found:
            print(f"{s['id']}. {s['full_name']} - {s['course']}")
    else:
        print("Natija topilmadi.")

def course_statistika():
    students = load_students
    status = []
    for i in students:
        course = i['course']
        status[course] = status.get(course ,0) +1
    for course , count in status.iteams():
        print(f'{course} kursida: {count} student bor')


def menu():
    while True:
        print("""TALABALAR BAZASI BILAN ISHLASH
1. Barcha talabalarni korish
2. Yangi talaba qoshish
3. Talaba malumotini yangilash
4. Talabani ochirish
5. Qidiruv (ism yoki kurs boyicha)
6. Statistika (kurslar boyicha)
0. Chiqish
        """)
        choice = input("Tanlovingizni kiriting: ")

        if choice == "1":
            show_students()
        elif choice == "2":
            add_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_students()
        elif choice == "5":
            search_student()
        elif choice == "6":
            course_statistika()
        elif choice == "0":
            print("Dastur yakunlandi.")
            break
        else:
            print("Notogri tanlov.")
