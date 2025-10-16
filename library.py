import math

class Shape(ABC):
    def area(self) -> float:
        pass

class Circle(Shape):
    def init(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def init(self, side1: float, side2: float, side3: float):
        sides = sorted([side1, side2, side3])
        a,b,c = sides[0], sides[1], sides[2]
        self.a = a
        self.b = b
        self.c = c
        if a<=0 or b<=0 or c<=0:
            raise ValueError("Triangle must have positive values")
        if a+b<=c:
            return ValueError("Triangle must have positive values")

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def triangle_true(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True


def area(shape: Shape):
    return shape.area()

