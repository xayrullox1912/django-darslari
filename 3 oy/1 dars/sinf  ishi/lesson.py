from test_ import Test


obj = Test("iPhone", 1000, 10)

obj.set_price(10)
print(obj.get_price())
obj.set_price(-10)
print(obj.get_price())

obj.set_stock(10)
print(obj.get_stock())
obj.get_stock(-10)
print(obj.set_stock())

