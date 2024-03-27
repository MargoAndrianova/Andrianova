class Real:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def __add__(self, other):
        assert type(other) == Real
        return Real(self.x + other.x)

class Complex(Real):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def __str__(self):
        return f'{self.x} + {self.y}i'

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.x + other.x, self.y + other.y)
        elif isinstance(other, Real):
            return Complex(self.x + other.x, self.y)

if __name__ == "__main__":
    res = Complex(3, 4) + Real(12) + Complex(7, 3)
    print(res)