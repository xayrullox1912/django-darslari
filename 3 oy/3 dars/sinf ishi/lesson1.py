class User:
    def __init__(self, username,familya):
        self.username = username
        self.familya = familya

    def __eq__(self, other):
        return self.familya == other.familya

u1 = User('ali','komiljonov')
u2 = User('ali','komiljonov')
print(u1 == u2)  # True