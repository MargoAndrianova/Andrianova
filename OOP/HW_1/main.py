from Reader import *

reader = Reader("input.txt")
eqs = reader.read()
for eq in eqs:
    print(eq)