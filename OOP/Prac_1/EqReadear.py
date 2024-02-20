from Quadratic_equation import Quadratic_equation


class EqReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        equations = []
        with open(self.file_name) as f:
            for line in f:
                a, b, c = [float(el) for el in line.split()]
                eq = Quadratic_equation(a, b, c)
                eqs = eq.calculations()
                equations.append(eqs)
        return equations

if __name__ == '__main__':
    read = EqReader('input.txt')
    print(read.read())
