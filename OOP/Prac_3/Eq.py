from BiQuadraticEquation import *



def read_file(file):
    with open(file, 'r'):
        solves_Eq = []
        solves_QuaEq = []
        solves_BiQuaEq = []
        for line in file:
            num = line.strip().split()
            if len(num) == 2:
                e = BiQuadraticEquation(0, int(num[0]), int(num[1]))
                if e.solve == "()":
                    solves_Eq.append(str(num))
            elif len(num) == 3:
                solve = BiQuadraticEquation(int(num[0]),int(num[1]),int(num[2]))
                solves_QuaEq.append(str)
            # elif len(number) == 5:
            #     solve = str(BiQuadraticEquation(number[0],number[2],number[4]))
            #     solves_biquadratic.append(solve)
        return solves_Eq, solves_QuaEq, solves_BiQuaEq

file = "input01.txt"
print(read_file(file))