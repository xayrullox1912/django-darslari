from itertools import product


class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} maxsulotidan {self.quantity} ta qolgan va uni narxi {self.price}$"

class Cart:
    def __init__(self):
        self.products:list[Product] = []

    @property
    def total_sum(self):
        total_sum1 = 0
        for i in range(len(self.products)):
            total_sum1 += self.products[i].total_price
        return total_sum1

    def add_product(self, other):
        return self.products.append(other)

    def remove_product(self,other):
        if other in self.products:
            self.products.remove(other)

    def __bool__(self):
        return bool(self.products)

    def __len__(self):
        return len(self.products)

    def __contains__(self, item):
        for product in self.products:
            if product.name == item:
                return True
        return False
    def __getitem__(self, item):
        return self.products[item]

    def __delitem__(self, key):
        del self.products[key]

p1 = Product("Monitor", 300, 1)
p2 = Product("Mouse", 50, 2)
cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
print(len(cart))         # 2
print(cart.total_sum)    # 400
print(cart[0])           # Monitor
print("Mouse" in cart)   # True
