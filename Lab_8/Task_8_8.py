def F(n, lst):
    if n != 1:
        if n % 2 == 1:
            lst += "X"
            return F(n-1, lst)
        else:
            lst += "S"
            return F(n/2, lst)
    return lst[::-1]

n = int(input())
lst = ""

res = F(n, lst)

print(res)