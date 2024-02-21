from HW_1 import *
class Reader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        rows = []
        with open(self.file_name) as f:
            for line in f:
                rows.append(line.strip().split())
        return rows

    def sort(self):
        row = reader.read()
        tria = []
        for r in range(len(row)):
            helper = [int(el) for el in row[r][1:]]
            helper_2 = []
            if "Triangle" in row[r]:
                if helper[0]+helper[1] <= helper[2] or helper[2]+helper[1] <= helper[0] or helper[0]+helper[2] <= helper[1]:
                    continue
                else:
                    tr = Triangle(helper[0], helper[1], helper[2])
                    helper_2.append(tr.perimeter())
                    helper_2.append(round(tr.area(), 2))
                    tria.append(helper_2)
        print(tria)


if __name__ == '__main__':
    reader = Reader('input01.txt')
    print(reader.read())
    reader.sort()
