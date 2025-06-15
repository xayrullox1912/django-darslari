class User:
    def __init__(self, name, role):
        self.role = role
        self.name = name

    @classmethod
    def from_dict(cls, dct):
        return cls(dct["name"], dct["role"])

    @classmethod
    def from_dict1(cls,dct):
        return cls(dct["name"], dct["role"])

user = User("Otabek", "admin")

data = {"name": "Javohir", "role": "customer"}
user1 = User.from_dict(data)

print(user1.name, user1.role)

users = [{"name": "Javohir", "role": "customer"},{"name": "Javohir", "role": "customer"}]
