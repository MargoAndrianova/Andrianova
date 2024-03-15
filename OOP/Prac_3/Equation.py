class Equation:

    Inf = "infinity"
    def __init__(self, b, c):
        self.b = b
        self.c = c

    def __str__(self):
        return f'{self.b}x + {self.c} = 0'

    def solve(self):
        if self.b == 0:
            if self.c == 0:
                return Equation.Inf
            else:
                return ()
        else:
            x1 = - self.c / self.b
            return (x1, )




if __name__ == "__main__":
    eq1 = Equation(7, 4)
    eq2 = Equation(0, 0)
    eq3 = Equation(0, 5)
    print(eq1.solve())
    print(eq2.solve())
    print(eq3.solve())
