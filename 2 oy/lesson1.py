import csv

def talaba_qoshish(fayl_nomi, ism, familiya, yosh):
    with open(fayl_nomi, mode='a', newline='', encoding='utf-8') as csvfile:
        ustunlar = ['ism', 'familiya', 'yosh']
        yozuvchi = csv.DictWriter(csvfile, fieldnames=ustunlar)
        if csvfile.tell() == 0:
            yozuvchi.writeheader()

        yozuvchi.writerow({'ism': ism, 'familiya': familiya, 'yosh': yosh})

talaba_qoshish('talabalar.csv', 'xaryullox', 'komiljonov', '21')
