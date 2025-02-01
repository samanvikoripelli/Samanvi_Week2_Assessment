from abc import ABC, abstractmethod
import math
class ishape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class rectangle(ishape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
class circle(ishape):
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
if __name__ == "__main__":
    rectangle = rectangle(4,8)
    circle = circle(5)
    print(f"area of rectangle: {rectangle.calculate_area()}")
    print(f"area of circle: {circle.calculate_area():.2f}")