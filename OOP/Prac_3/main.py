import re

from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation

def write_file(file_name, read_name):
    reader = read_file(read_name)
    with open(file_name, 'w') as file:
        for line in reader:
            file.write(f"{line}\n")


def read_file(file_name):
    with open(file_name, 'r') as file:
        solves = []
        for line in file:
            num = line.strip().split()
            sol_eq = []
            if len(num) == 2:
                e = Equation(int(num[0]), int(num[1]))
                sol_eq.append(str(f"{num[0]}x + {num[1]} = 0"))
                if e.solve == "None":
                    sol_eq.append("None")
                elif e.solve() == "infinity":
                    sol_eq.append("infinity")
                else:
                    sol_eq.append([e.solve()])

            elif len(num) == 3:
                e = QuadraticEquation(int(num[0]), int(num[1]), int(num[2]))
                if "None" in str(e.solve()):
                    sol_eq.append("None")
                    continue
                else:
                    sol = e.solve()
                    if len(sol) != 1:
                        sl = set(sol)
                        x = []
                        for s in sl:
                            x.append(s)
                        sol_eq.append(str(f"{num[0]}x^2 + {num[1]}x + {num[2]} = 0"))
                        if len(x) == 2:
                            sol_eq.append([x[0], x[1]])
                        elif len(x) == 1:
                            sol_eq.append([x[0]])
                        elif e.solve() == "infinity":
                            sol_eq.append("infinity")
            elif len(num) == 5:
                e = BiQuadraticEquation(int(num[0]), int(num[2]), int(num[4]))
                if "None" in str(e.solve()):
                    sol_eq.append("None")
                    continue
                else:
                    sol = e.solve()
                    if len(sol) != 1:
                        sl = set(sol)
                        x = []
                        for s in sl:
                            x.append(s)
                        sol_eq.append(str(f"{num[0]}x^4 + {num[2]}x^2 + {num[4]} = 0"))
                        if len(x) == 4:
                            sol_eq.append([x[0], x[1], x[2], x[3]])
                        if len(x) == 3:
                            sol_eq.append([x[0], x[1], x[2]])
                        if len(x) == 2:
                            sol_eq.append([x[0], x[1]])
                        elif len(x) == 1:
                            sol_eq.append([x[0]])
                        elif e.solve() == "infinity":
                            sol_eq.append("infinity")
            solves.append(sol_eq)
        return solves

def sol(input_file):
    with open(input_file, "r") as file:
        solves = []
        non = ["None:"]
        inf = ["Inf:"]
        one = ["One:"]
        two = ["Two:"]
        three = ["Three:"]
        four = ["Four:"]
        min_s = 10000000
        max_s = -10000000
        for line in file:
            all_el = re.sub(r"[()\[\]\'\"\s\n]", "", line)
            all_el = all_el.split(",")
            eq = all_el[0]
            sol = all_el[1:]
            if ("''" or '""' ) in str(sol):
                sol = sol[:-1]
            if "None" in sol:
                non.append(eq)
            elif "infinity" in sol:
                inf.append(eq)
            elif len(sol) == 1 and "None" not in sol and "infinity" not in sol:
                one.append(eq)
                for i in sol:
                    if float(i) <= min_s:
                        min_s = float(i)
                    if float(i) >= max_s:
                        max_s = float(i)
            elif len(sol) == 2:
                two.append(eq)
                for i in sol:
                    if float(i) <= min_s:
                        min_s = float(i)
                    if float(i) >= max_s:
                        max_s = float(i)
            elif len(sol) == 3:
                three.append(eq)
                for i in sol:
                    if float(i) <= min_s:
                        min_s = float(i)
                    if float(i) >= max_s:
                        max_s = float(i)
            elif len(sol) == 4:
                four.append(eq)
                for i in sol:
                    if float(i) <= min_s:
                        min_s = float(i)
                    if float(i) >= max_s:
                        max_s = float(i)
        solves.append(non)
        solves.append(inf)
        solves.append(one)
        solves.append(two)
        solves.append(three)
        solves.append(four)
        solves.append(f"min: {min_s}")
        solves.append(f"max: {max_s}")
        return solves

def write_sol(name_file, input_file):
    f = sol(input_file)
    with open(name_file, "w") as file:
        for line in f:
            file.write(f"{line}\n")



write_file("helper01.txt", "input01.txt")
write_file("helper02.txt", "input02.txt")
write_file("helper03.txt", "input03.txt")
write_sol("res01.txt", "helper01.txt")
write_sol("res02.txt", "helper02.txt")
write_sol("res03.txt", "helper03.txt")