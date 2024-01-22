n = int(input())
lst = input().split()

t = {}
lst_1 = []

for el in lst:
    if el in t:
        t[el] += 1
    else:
        t[el] = 1

for i in lst[::-1]:
    if t[i] != 1:
        if i not in lst_1:
            lst_1.append(i)


if len(lst_1) == 0:
    print("NO")
else:
    print(*lst_1[::-1])