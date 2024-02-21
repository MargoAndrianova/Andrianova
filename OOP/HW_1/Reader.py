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
        rows = Reader(self.file_name)
        row = rows.read()
        tria = []
        rect = []
        trap = []
        para = []
        circ = []
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
            elif "Parallelogram" in row[r]:
                if helper[0] == 0 or helper[1] == 0 or helper[2]:
                    continue
                else:
                    pr = Parallelogram(helper[0], helper[1], helper[2])
                    helper_2.append(pr.perimeter())
                    helper_2.append(round(pr.area(), 2))
                    para.append(helper_2)
            elif "Circle" in row[r]:
                if helper[0] == 0:
                    continue
                else:
                    cr = Circle(helper[0])
                    helper_2.append(round(cr.perimeter(), 2))
                    helper_2.append(round(cr.area(), 2))
                    circ.append(helper_2)
        max_tria = max(tria)
        max_rect = max(rect)
        max_trap = max(trap)
        max_para = max(para)
        max_circ = max(circ)
        res = max(max_tria, max_rect, max_circ, max_para, max_trap)
        return res


if __name__ == '__main__':
    reader = Reader('input03.txt')
    print(reader.sort())
