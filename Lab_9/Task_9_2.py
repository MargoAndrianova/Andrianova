n = int(input())
lst = [el for el in input().split()]

lst_1 = set(lst)
res = []

for j in lst_1:
    cnt = 0
    for i in range(n):
        if j == lst[i]:
            cnt += 1
    if cnt > n // 2:
        res.append(j)

if len(res) > 0:
    print(res[0])
else:
    print(-1)

n = int(input())
lst = input().split()

t = {}

for el in lst:
    if el in t:
        t[el] += 1
    else:
        t[el] = 1

for num, cnt in t.items():
    if cnt > n // 2:
        print(num)
        break
