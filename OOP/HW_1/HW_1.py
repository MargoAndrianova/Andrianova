from math import sqrt, pi


class Triangle:
    def __init__(self, a, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Rectangle:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b


class Trapeze:
    def __init__(self, a=None, b=None, c=None, d=None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        p = self.perimeter() / 2
        if self.a > self.b:
            h = sqrt((self.a + self.c + self.d - self.b)*abs(self.b - self.a + max(self.c, self.d) - min(self.c, self.d))*abs(self.b - self.a + min(self.c, self.d) - max(self.c, self.d))) / 4
        else:
            h = sqrt((self.b + self.c + self.d - self.a)*abs(self.a - self.b + max(self.c, self.d) - min(self.c, self.d))*abs(self.a - self.b + min(self.c, self.d) - max(self.c, self.d))) / 4
        return (self.a + self.b) * h / abs(self.a - self.b)


class Parallelogram:
    def __init__(self, a=None, b=None, h=None):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return (self.a + self.b + self.h) * 4

    def area(self):
        return (self.a * self.b + self.a * self.h + self.b * self.h) * 2


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * self.r * pi

    def area(self):
        return pi * self.r ** 2


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
