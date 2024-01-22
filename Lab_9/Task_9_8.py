n = int(input())
lst = {int(el) for el in input().split()}

res = {}
for el in lst:
    if abs(el) in res:
        res[abs(el)] += 1
    else:
        res[abs(el)] = 1

print(len(res))