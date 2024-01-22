def NSD(a, b):
    # a >= b
    if a < b:
        a,b = b,a
    while b > 0:
        a, b = b, a % b

    return a

def NSK(a, b):
    nsk = (a * b)/ NSD(a, b)
    return nsk

a,b = [int(d) for d in input().split()]
print(NSK(a,b))