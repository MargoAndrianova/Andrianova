n = int(input())
lst = input().split()

t = {}

for el in lst:
    if el in t:
        t[el] += 1
    else:
        t[el] = 1

for el in lst:
    if t[el] == 1:
        print(el, end = " ")

# for el in lst:
#     if lst.count(el) == 1:
#         print(el, end = " ")