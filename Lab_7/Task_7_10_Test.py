def convert_to_base(n):
    if n > 9:
        return chr(55 + n)
    else:
        return str(n)

def convert_from_base(n):
    if 'A' <= n <= 'F':
        return ord(n) - 55
    else:
        return int(n)

def transfer_to_any(m, l):
    res = ''
    while m != 0:
        transform = m % l
        transformation = convert_to_base(transform)
        res += transformation
        m //= l
    res = res[::-1]
    return res

def transfer_from_any(n, k):
    m = len(n)
    res = 0

    for i in range(m):
        des = convert_from_base(n[i])
        res += des * k ** (m - i - 1)
    return res

k, l = [int(el) for el in input().split()]
n = input()

m = transfer_from_any(n, k)

print(transfer_to_any(m, l))
