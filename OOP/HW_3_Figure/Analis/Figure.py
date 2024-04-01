from math import sqrt, pi

class Figure:
    def dimention(self):
        pass

    def perimetr(self):
        pass

    def square(self):
        pass

    def height(self):
        pass

    def squareSurface(self):
        pass

    def squareBase(self):
        return self.square()

    def volume(self):
        if self.dimention() == 2:
            return self.square()

class Triangle(Figure):
    def __init__(self, a, b = None, c = None):
        self.a = a
        self.b = b
        self.c = c

    def dimention(self):
        return int(2)

    def perimetr(self):
        return sum([self.a, self.b, self.c])

    def square(self):
        p = self.perimetr() / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def height(self):
        return (2 * self.square()) / self.a

    def volume(self):
        return super().volume()

    def check(self):
        if self.a + self.b <= self.c or self.c + self.b <= self.a or self.a + self.c <= self.b:
            return False

class Rectangle(Figure):
    def __init__(self, a, b = None):
        self.a = a
        self.b = b

    def dimention(self):
        return int(2)

    def perimetr(self):
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b

    def volume(self):
        return super().volume()

    def check(self):
        if self.a * self.b == 0:
            return False


class Trapeze(Figure):
    def __init__(self, a, b = None, c = None, d = None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def dimention(self):
        return int(2)

    def perimetr(self):
        return super().perimetr()

    def height(self):
        p = (self.c + self.d + abs(self.a - self.b)) / 2
        return (2 * sqrt(p * (p - abs(self.a - self.b)) * (p - self.d) * (p - self.c))) / abs(self.a - self.b)

    def square(self):
        return (self.a + self.b) * self.height() / 2

    def volume(self):
        return super().volume()

    def check(self):
        if (self.a * self.b * self.c * self.d == 0) or (self.a == self.b) or \
           (self.a + self.b <= self.c + self.d) or \
           (abs(self.a - self.b) + self.d <= self.c or self.c + self.d <= abs(self.a - self.b) or abs(self.a - self.b) + self.c <= self.d):
            return False

class Parallelogram(Figure):
    def __init__(self, a, b = None, h = None):
        self.a = a
        self.b = b
        self.h = h

    def dimention(self):
        return int(2)

    def perimetr(self):
        return (self.a + self.b) * 2

    def height(self):
        return self.h

    def square(self):
        if self.a < self.h:
            return self.b * self.h
        else:
            return self.a * self.h

    def volume(self):
        return super().volume()

    def check(self):
        if self.a * self.b * self.h == 0:
            return False


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return int(2)

    def perimetr(self):
        return 2 * self.r * pi

    def square(self):
        return pi * self.r ** 2

    def volume(self):
        return super().volume()

    def check(self):
        if self.r == 0:
            return False

class Ball(Circle):
    def __init__(self, r):
        super().__init__(r)

    def dimention(self):
        return int(3)

    def height(self):
        return self.r * 2

    def squareSurface(self):
        return pi * 4 * self.r ** 2

    def squareBase(self):
        return super().squareBase()

    def volume(self):
        return pi * 4 / 3 * self.r ** 3

    def check(self):
        super().check()

class TriangularPyramid(Triangle):
    def __init__(self, a, h = None):
        super().__init__(a)
        self.a = a
        self.b = a
        self.c = a
        self.h = h

    def dimention(self):
        return int(3)

    def height(self):
        return self.h

    def squareSurface(self):
        return self.squareBase() + 3 * (0.5 * self.a**2 * sqrt(0.75))

    def squareBase(self):
        return sqrt(3/2 * self.a * (3/2 * self.a - self.a) ** 3)

    def volume(self):
        return 1/3 * self.squareBase() * self.h

    def check(self):
        if self.a * self.h == 0:
            return False
        else:
            super().check()

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b = None, h = None):
        super().__init__(a, b)
        self.h = h

    def dimention(self):
        return int(3)

    def height(self):
        return self.h

    def squareSurface(self):
        return self.squareBase() + 2 * (0.5 * self.a**2 * sqrt(0.75)) + 2 * (0.5 * self.b**2 * sqrt(0.75))

    def squareBase(self):
        return super().square()

    def volume(self):
        return self.squareBase() * self.h / 3

    def check(self):
        if self.a * self.b * self.h == 0:
            return False
        else:
            super().check()

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b = None, h = None):
        super().__init__(a, b)
        self.h = h

    def dimention(self):
        return int(3)

    def height(self, height=None):
        return self.h

    def squareSurface(self):
        return 2 * (self.squareBase() + self.a**2 + self.b**2)

    def squareBase(self):
        return super().square()

    def volume(self):
        return self.squareBase() * self.h

    def check(self):
        if self.a * self.b * self.h == 0:
            return False
        else:
            super().check()

class Cone(Circle):
    def __init__(self, r, h = None):
        super().__init__(r)
        self.h = h

    def dimention(self):
        return int(3)

    def height(self):
        return self.h

    def squareSurface(self):
        return super().perimetr() * self.h + 2 * self.squareBase()

    def squareBase(self):
        return super().square()

    def volume(self):
        return 1/3 * self.squareBase() * self.h

    def check(self):
        if self.r * self.h == 0:
            return False
        else:
            super().check()

class TriangularPrism(Triangle):
    def __init__(self, a, b = None, c = None, h = None):
        super().__init__(a, b, c)
        self.h = h

    def dimention(self):
        return int(3)

    def height(self):
        return self.h

    def squareSurface(self):
        return 2 * self.squareBase() + (self.a + self.b + self.c) * self.h

    def squareBase(self):
        return super().square()

    def volume(self):
        return self.squareBase() * self.h

    def check(self):
        if self.a * self.b * self.c * self.h == 0 or self.a + self.b <= self.c or self.c + self.b <= self.a or self.a + self.c <= self.b:
            return False


if __name__ == '__main__':
    tri = Triangle(3, 4, 5)
    print(f"{tri.square():0.2f}, {tri.perimetr():0.2f}")
    rec = Rectangle(3, 4)
    print(f"{rec.square():0.2f}, {rec.perimetr():0.2f}")
    trap = Trapeze(10, 7, 5, 4)
    print(f"{trap.square():0.2f}, {trap.perimetr():0.2f}")
    par = Parallelogram(3, 4, 5)
    print(f"{par.square():0.2f}, {par.perimetr():0.2f}")
    circ = Circle(5)
    print(f"{circ.square():0.2f}, {circ.perimetr():0.2f}")
