class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 0
        pass

    def growUp(self):
        self.age += 1

    def bite(self, other):
        print(f"Cat {self.name} bite {other.name}")

    def miu(self):
        print(f"Cat {self.name} says: Miu")

catVasil = Cat('Vasil')
catKuzia = Cat('Kuzia')

print(catVasil.age)
for i in range(5):
    catVasil.growUp()
print(catVasil.age)
catVasil.miu()
catKuzia.miu()
catVasil.bite(catKuzia)
