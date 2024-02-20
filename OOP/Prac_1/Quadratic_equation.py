from math import sqrt
class Quadratic_equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def show(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c} = 0")
    def disc(self):
        return self.b ** 2 - 4 * self.c * self.a

    def calculations(self):
        eq = Quadratic_equation(self.a, self.b, self.c)
        res = []
        if eq.a == 0:
            if eq.b == 0:
                if eq.c == 0:
                    res.append("Infinity solution")
                else:
                    res.append("No solution")
            else:
                res.append(f"x = {-eq.c / eq.b}")
        else:
            if eq.disc() == 0:
                res.append(f"x = {-1 * eq.b / (2 * eq.a)}")
            elif eq.disc() > 0:
                res.append(f"x_1 = {(-1 * eq.b + sqrt(eq.disc())) / (2 * eq.a):0.2f}")
                res.append(f"x_2 = {(-1 * eq.b - sqrt(eq.disc())) / (2 * eq.a):0.2f}")
            else:
                res.append("No solution")
        return res


if __name__ == '__main__':
    a, b, c = [float(el) for el in input().split()]
    eq = Quadratic_equation(a, b, c)
    eq.show()
    print(*eq.calculations())