n = int(input())

for i in range(n):
    m = int(input())
    dictionary = {}
    maximum = 0
    res = []
    for j in range(m):
        el = int(input())
        if el in dictionary:
            dictionary[el] += 1
        else:
            dictionary[el] = 1
    for k in dictionary:
        if maximum <= dictionary[k]:
            maximum = dictionary[k]
    for ch, count in dictionary.items():
        if count == maximum:
            res.append(ch)
    print(min(res))