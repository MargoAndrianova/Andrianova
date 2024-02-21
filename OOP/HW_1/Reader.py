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
        rect = []
        trap = []
        for r in range(len(row)):
            helper = [int(el) for el in row[r][1:]]
            helper_2 = []
            if "Triangle" in row[r]:
                if helper[0] + helper[1] <= helper[2] or helper[2] + helper[1] <= helper[0] or helper[0] + helper[2] <= \
                        helper[1]:
                    continue
                else:
                    tr = Triangle(helper[0], helper[1], helper[2])
                    helper_2.append(tr.perimeter())
                    helper_2.append(round(tr.area(), 2))
                    tria.append(helper_2)
            elif "Rectangle" in row[r]:
                if helper[0] == 0 or helper[1] == 0:
                    continue
                else:
                    re = Rectangle(helper[0], helper[1])
                    helper_2.append(re.perimeter())
                    helper_2.append(round(re.area(), 2))
                    rect.append(helper_2)
            elif "Trapeze" in row[r]:
                if (((helper[0] or helper[1] or helper[2] or helper[3]) <= 0) or
                        (helper[0] == helper[1]) or (helper[1] + helper[0] <= helper[2] + helper[3]) or
                        (max(helper[2], helper[3]) >= (helper[0] or helper[1]) + min(helper[2], helper[3]))):
                    continue
                else:
                    tr = Trapeze(helper[0], helper[1], helper[2], helper[3])
                    helper_2.append(tr.perimeter())
                    helper_2.append(round(tr.area(), 2))
                    trap.append(helper_2)
        print(*tria)
        print(*rect)
        print(*trap)


if __name__ == '__main__':
    reader = Reader('input03.txt')
    print(reader.read())
    reader.sort()
