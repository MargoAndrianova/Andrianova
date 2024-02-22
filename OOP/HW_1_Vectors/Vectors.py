from math import sqrt
class Vectors:
    def __init__(self, *args):
        self.arguments = args

    def show(self):
        return f"Vector{self.arguments}"

    def dimension(self):
        return f"Dimension is {len(self.arguments)}"

    def length(self):
        length = (self.arguments[0])**2
        for i in range(1, len(self.arguments)):
            length += (self.arguments[i])**2
        return f"Length is {sqrt(length):0.3}"

    def middle(self):
        mid = (self.arguments[0])
        for i in range(1, len(self.arguments)):
            mid += (self.arguments[i])
        return f"Length is {(mid)/len(self.arguments):0.3}"

    def min(self):
        return f"Min is {min(self.arguments)}"

    def max(self):
        return f"Max is {max(self.arguments)}"

if __name__ == '__main__':
    v1 = Vectors(2, 7)
    print(v1.show())
    print(v1.dimension())
    print(v1.length())
    print(v1.middle())
    print(v1.min())
    print(v1.max())