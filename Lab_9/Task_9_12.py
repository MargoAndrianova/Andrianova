def freq(word):
    d = {}
    for e in word:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    return d


word_donor = input()
word_recipient = input()
d_donor = freq(word_donor)
d_recipient = freq(word_recipient)

for ch, count in d_recipient.items():
    if ch in d_donor and d_donor[ch]:
        continue
    else:
        print("No")
        break
else:
    print("Ok")