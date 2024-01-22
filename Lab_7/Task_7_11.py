def more_9_bin(n):
    if n > 9:
        res = chr(64 + n - 9)
    else:
        res = n
    return res
def transfer_to_any(n, l):
    res = ''
    while n != 0:
        transform = n % l
        transformation = more_9_bin(transform)
        res += (str(transformation))
        n //= l
    res = res[::-1]
    return res

def palindrom(lst_1):
    lst = lst_1[::-1]

    if lst_1 == lst:
        return True
    else:
        return False

n = int(input())

cnt = []

for i in range(2, 37):
    if palindrom(transfer_to_any(n, i)):
        cnt.append(i)

if len(cnt) == 0:
    print("none")
elif len(cnt) == 1:
    print("unique")
    print(*cnt)
else:
    print("multiple")
    print(*cnt)
