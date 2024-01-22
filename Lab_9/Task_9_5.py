lst = input()

ascii = []
dictionary = {}

for i in lst:
    ascii.append(ord(i))

for el in ascii:
    if el in dictionary:
        dictionary[el] += 1
    else:
        dictionary[el] = 1

print(chr(max(dictionary)), dictionary[max(dictionary)])

