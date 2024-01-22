def different(n):
    lst = []
    for i in range(len(str(n))):
        a = n % 10
        if a not in lst:
            lst.append(a)
        else:
            return False
        n //= 10
    return True

a, b = [int(el) for el in input().split()]

for j in range(a, b+1):
    if different(j):
        print(j, end=" ")
