suma = 0
with open("input_14") as f:
    s = f.read().strip()
    for c in s:
        try:
            suma += int(c)
        except ValueError:
            pass
print(suma)