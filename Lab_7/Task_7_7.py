def NSD(a, b):
    if a < b:
        a,b = b,a
    while b > 0:
        a, b = b, a % b

    return a
def NSK(a):
    for i in range(2, a + 1):
        if a % i == 0:
            continue
        else:
            a *= int(i / NSD(a, i))
    return a

a = int(input())
print(NSK(a))