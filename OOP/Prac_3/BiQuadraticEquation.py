from math import sqrt

from QuadraticEquation import QuadraticEquation

class BiQuadraticEquation(QuadraticEquation):

    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def __str__(self):
        return f'{self.a}x^4 +{self.b}x^2 + {self.c} = 0'

    def solve(self):
        result_sol = set()
        solution_of_quad = super().solve()
        if solution_of_quad == BiQuadraticEquation.Inf:
            return solution_of_quad
        for solution in solution_of_quad:
            if solution < 0:
                continue
            if solution >= 0:
                x1 = sqrt(solution)
                x2 = -x1
                result_sol.add(x1)
                result_sol.add(x2)
        return tuple(result_sol)

if __name__ == '__main__':
    eq1 = BiQuadraticEquation(0, 5, 6)
    eq2 = BiQuadraticEquation(0, 0, 0)
    eq3 = BiQuadraticEquation(0, 0, 5)
    eq4 = BiQuadraticEquation(1, 0, 5)
    eq5 = BiQuadraticEquation(1, -10, 25)
    eq6 = BiQuadraticEquation(1, -7, 12)
    eq7 = BiQuadraticEquation(4, 1, -5)
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
    print(eq7)
    print(eq7.solve())