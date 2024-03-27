from math import sqrt, pi

class Figure:
    def __init__(self, *args, h=None):
        self.el = args[1:]
        self.dimen = args[0]
        self.h = h
    def dimention(self):
        if self.dimen in ["Cone", "Trapeze", "Triangle", "Rectangle", "Parallelogram", "Circle"]:
            return 2
        elif self.dimen in ["Ball", "TriangularPyramid", "QuadrangularPyramid", "RectangularParallelepiped", "TriangularPrism", "Cone"]:
            return 3

    def perimetr(self):
        return sum(self.el)
    def square(self):
        if self.dimention() == 2:
            return self.el[0] * self.el[1]
        elif self.dimention() == 3:
            return None
    def squareSurface(self):
        if self.dimention() == 3:
            return self.perimetr() * self.h
        elif self.dimention() == 2:
            return None
    def squareBase(self):
        if self.dimention() == 3:
            return self.perimetr() * self.h
        elif self.dimention() == 2:
            return None
    def height(self):
        pass
    def volume(self):
        pass


class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b

    def check(self):
        if self.a**2 + self.b**2 == 0:
            return False


class Trapeze:
    def __init__(self, a, b=None, c=None, d=None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        p = (self.c + self.d + abs(self.a - self.b)) / 2
        h = (2 * sqrt(p * (p - abs(self.a - self.b)) * (p - self.d) * (p - self.c)))/abs(self.a - self.b)
        return (self.a + self.b) * h / 2
    def check(self):
        if (self.a**2 + self.b**2 + self.c**2 + self.d**2 == 0) or (self.a == self.b) or \
           (self.a + self.b <= self.c + self.d) or \
           (abs(self.a - self.b) + self.d <= self.c or self.c + self.d <= abs(self.a - self.b) or abs(self.a - self.b) + self.c <= self.d):
            return False

class Parallelogram:
    def __init__(self, a, b=None, h=None):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        if self.a < self.h:
            return self.b * self.h
        else:
            return self.a * self.h

    def check(self):
        if self.a**2 + self.b**2 + self.h**2 == 0:
            return False


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * self.r * pi

    def area(self):
        return pi * self.r ** 2

    def check(self):
        if self.r == 0:
            return False

if __name__ == '__main__':
    tri = Triangle(3, 4, 5)
    print(f"{tri.area():0.2f}")
    rec = Rectangle(3, 4)
    print(f"{rec.area():0.2f}")
    trap = Trapeze(10, 7, 5, 4)
    print(f"{trap.area():0.2f}")
    par = Parallelogram(3, 4, 5)
    print(f"{par.area():0.2f}")
    circ = Circle(5)
    print(f"{circ.area():0.2f}")
