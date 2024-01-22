def readMatrix(file):
    global n, m, k, p
    A = []
    B = []
    with open(file) as f:
        n, m = [int(el) for el in input().split()]
        for i in range(n):
            row = [int(el) for el in f.readline().split()]
            A.append(row)

        k, p = [int(el) for el in input().split()]
        for i in range(k):
            row = [int(el) for el in f.readline().split()]
            B.append(row)
    return A, B




def printMatrix(M):
    for row in M:
        # print(*row)
        for el in row:
            print(f"{el:7.1f}", end="")
        print()

A, B = readMatrix("../Lab_13/input.txt")
printMatrix(A)
printMatrix(B)