class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other,(Money,int)):
            raise TypeError("hatolik money va int ga aloqasi yoq")
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise  TypeError(f"{self.currency} valyuta {other.currency} vayuta bilan bir xil emas")
            val = other.amount
        else:
            val = other

        obj = Money(self.currency, self.amount + val)
        return obj

    def __sub__(self, other):
        if not isinstance(other,(Money,int)):
            raise TypeError("hatolik money va int ga aloqasi yoq")
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise  TypeError(f"{self.currency} valyuta {other.currency} vayuta bilan bir xil emas")
            val = other.amount
        else:
            val = other

        obj = Money(self.currency, self.amount - val)
        return obj

    def __str__(self):
        return f"{self.currency} {self.amount}"


obj1 = Money("USD", 1000)
obj2 = Money("USD", 500)
obj3 = Money("UZS", 1_000_000)


p = obj1 - obj2
print(type(p), p)
p = obj1 + obj2
print(type(p), p)
p = obj1 + 1000
print(type(p), p)