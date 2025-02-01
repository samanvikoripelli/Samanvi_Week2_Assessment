class shape:
    def area(self):
        pass
class square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side ** 2
class triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
square = square(6)
triangle = triangle(2,4)
print(f"area of square: {square.area()}")
print(f"area of triangle: {triangle.area()}")
