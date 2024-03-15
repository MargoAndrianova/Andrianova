from Equation import Equation
from math import *

class QuadraticEquation(Equation):

    def __init__(self, a, b, c):
        super().__init__(b, c)
        self.a = a

    def __str__(self):
        return f'{self.a}x^2 +{self.b}x + {self.c} = 0'

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        if self.a == 0:
            return super().solve()
        else:
            d = self.discriminant()
            if d < 0:
                return ()
            elif d == 0:
                x1 = - self.b / (2 * self.a)
                return (x1, )
            else:
                x1 = (-self.b + sqrt(d)) / (2 * self.a)
                x2 = (-self.b - sqrt(d)) / (2 * self.a)
                return x1, x2

if __name__ == '__main__':
    eq1 = QuadraticEquation(0, 5, 6)
    eq2 = QuadraticEquation(0, 0, 0)
    eq3 = QuadraticEquation(0, 0, 5)
    eq4 = QuadraticEquation(1, 0, 5)
    eq5 = QuadraticEquation(1, -10, 25)
    eq6 = QuadraticEquation(1, -7, 12)
    eq7 = QuadraticEquation(4, 1, -5)
    print(eq1)
    print(eq1.solve())
    print(eq2)
    print(eq2.solve())
    print(eq3)
    print(eq3.solve())
    print(eq4)
    print(eq4.solve())
    print(eq5)
    print(eq5.solve())
    print(eq6)
    print(eq6.solve())


