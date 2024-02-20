from EqReadear import EqReader

reader = EqReader("input.txt")
eqs = reader.read()
for eq in eqs:
    print(eq)