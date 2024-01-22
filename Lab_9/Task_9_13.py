

def dictionary(x):
    res = []
    for j in x:
        while j in "-":
            res.clear()
            break
        if j not in "-":
            word = ""
            for i in j:
                if i not in ",.":
                    word += i
            res.append(word)
    return res

n = int(input())

x = {}

for i in range(n):
    lst = input().split()
    for j in range(1):
        x[lst[j]] = dictionary(lst)

res = {}

for ch, count in x.items():
    for word in count:
        if word in res:
            res[word].append(ch)
        else:
            res[word] = [ch]

fuck = sorted(res.keys())

print(len(res))
for ind in fuck:
    result = ', '.join(map(str, res[ind]))
    print(ind, "-", result)

