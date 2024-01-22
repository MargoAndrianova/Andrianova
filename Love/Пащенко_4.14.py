n = int(input())

# for j in range(2,n ** 0.5):
#     if n % j == 0:
#         break
# else:
#     print(1)

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        k = n // i
        print(k)
        break
else:
    print(1)



# n = int(input())
#
# i = 1
# while i < n // 2:
#     i += 1
#     if n % i == 0:
#         print(n//i)
#         break
#     elif i > n ** 0.5:
#         print(1)

