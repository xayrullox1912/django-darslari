class Shape:

    def __init__(self,symbol, length):
        self.symbol = symbol
        self.length = length

    def show(self):
        pass

class Line(Shape):

    def show(self):
       print(self.symbol * self.length)

class Triangle(Shape):

    def show(self):
        for i in range(1, self.length+1):
            print(self.symbol * i)


class Tortburchak(Shape):

    def show(self):
        for i in range(5):
            print(f"{self.symbol * self.length }")



line = Line('+', 10)
line.show()

tortburchak = Tortburchak(' + ', 5 )
tortburchak.show()

triangle = Triangle(' * ', 10)
triangle.show()
