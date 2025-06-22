import json

def load(file_name):
    try:
        with open(file_name, "r") as file:
            users = json.load(file)
            return users
    except FileNotFoundError:
        with open(file_name, "w") as file:
            json.dump([], file)
            return []

def save(file_name:str, items:list):
    with open(file_name, "w") as file:
        json.dump(items, file, indent=4)




def menu(habar, choice) -> int:
    while True:
        try:
            tanlov = int(input(habar))
            assert tanlov in choice
            return tanlov
        except:
            print("Xato. Qayta kiriting")