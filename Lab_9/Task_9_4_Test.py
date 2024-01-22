n = int(input())
lst = input().split()

t = {}
lst_1 = {}
have_not = 0

for el in lst:
    if el in t:
        t[el] += 1
    else:
        t[el] = 1

for i in lst:
    if t[i] != 1:
        have_not += 1
        if i in lst_1:
            if lst_1[i] == t[i] - 1:
                print(i, end=" ")
            else:
                lst_1[i] += 1
        else:
            lst_1[i] = 1

if have_not == 0:
    print("NO")