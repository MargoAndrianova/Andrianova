def more_9_bin(n):
    if n > 9:
        res = chr(64 + n - 9)
    else:
        res = n
    return res

def F(n, res):
    if n != 0:
        transform = n % 13
        transformation = more_9_bin(transform)
        res += (str(transformation))
        return F(n // 13, res)
    return res[::-1]

n = int(input())
res = ''

print(F(n, res))