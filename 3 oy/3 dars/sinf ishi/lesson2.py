class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __sub__(self, other):
        if self.currency != other.currency:
            raise  Exception(f"{self.currency} valyuta {other.currency} vayuta bilan bir xil emas")
        obj = Money(self.currency, self.amount - other.amount)
        return obj

    def __str__(self):
        return f"{self.currency} {self.amount}"


obj1 = Money("USD", 1000)
obj2 = Money("USD", 500)
obj3 = Money("UZS", 1_000_000)

p = obj1 - obj2
print(p)