def inverse(n):
    k = 0
    for i in range(len(str(n))):
        p = n % 10
        k += p * 10**(len(str(n))-1)
        n //= 10
    return k

def isPrime(n: int):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def lucky(n):
    if n != inverse(n):
        if (isPrime(n) == True and isPrime(inverse(n)) == True):
            return n

n = int(input())

lst = []
k = 13

while len(lst) != n:
    if lucky(k):
        lst.append(k)
        k+=1
    else:
        k += 1

if len(str(lst[n-1])) < 7:
    print(lst[n-1])
else:
    print(-1)