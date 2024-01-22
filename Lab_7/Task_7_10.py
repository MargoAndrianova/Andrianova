def more_9_bin(n):
    if n > 9:
        res = chr(64 + n - 9)
    else:
        res = n
    return res

def to_numbers(n):
    if ord(n) > 64:
        res = ord(n) - 64 + 9
    else:
        res = n
    return res
def transfer_to_any(m, l):
    res = ''
    while m != 0:
        transform = m % l
        transformation = more_9_bin(transform)
        res += (str(transformation))
        m //= l
    res = res[::-1]
    return res

def transfer_from_any(n, k):
    m = len(n)
    res = 0

    for i in range(m):
        des = int(to_numbers(n[i]))
        res += des * k ** (m - i - 1)
    return res

k, l = [int(el) for el in input().split()]
n = str(input())

m = transfer_from_any(n, k)

print(transfer_to_any(m, l))
