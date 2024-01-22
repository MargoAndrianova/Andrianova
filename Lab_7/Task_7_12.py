def Bin(n: int):
    lst = []
    while n != 0:
        k = n % 2
        lst.append(str(k))
        n //= 2
    lst = lst[::-1]
    return lst

k, l = [int(el) for el in input().split()]

cnt = 0

for i in range(k, l+1):
    n = Bin(i)
    for j in range(len(n)):
        if int(n[j]) == 1:
            cnt += 1

print(cnt)

