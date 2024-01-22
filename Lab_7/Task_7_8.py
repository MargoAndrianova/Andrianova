def NSD(a, b):
    if a < b:
        a,b = b,a
    while b > 0:
        a, b = b, a % b

    return a

def NSK(a, b):
    nsk = (a * b)/NSD(a, b)
    return nsk

a, b = [int(el) for el in input().split()]

cnt = 0

for p in range(a, b+1, a):
    q = a * b // p
    if NSD(p, q) == a and NSK(p, q) == b:
       cnt += 1

print(cnt)