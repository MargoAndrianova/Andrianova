from HW_1 import *


class Reader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name) as f:
            tria = []
            rect = []
            trap = []
            para = []
            circ = []
            for line in f:
                lines = line.strip().split()
                name = lines[0]
                param = list(map(int, lines[1:]))
                helper = []
                if name == "Triangle":
                    tr = Triangle(*param)
                    if tr.check() == False:
                        continue
                    else:
                        helper.append(tr.perimeter())
                        helper.append(round(tr.area(), 2))
                        tria.append(helper)
                elif name == "Rectangle":
                    rec = Rectangle(*param)
                    if rec.check() == False:
                        continue
                    else:
                        helper.append(rec.perimeter())
                        helper.append(round(rec.area(), 2))
                        rect.append(helper)
                elif name == "Trapeze":
                    tr = Trapeze(*param)
                    if tr.check() == False:
                        continue
                    else:
                        helper.append(tr.perimeter())
                        helper.append(round(tr.area(), 2))
                        trap.append(helper)
                elif name == "Parallelogram":
                    pr = Parallelogram(*param)
                    if pr.check() == True:
                        continue
                    else:
                        helper.append(pr.perimeter())
                        helper.append(round(pr.area(), 2))
                        para.append(helper)
                elif name == "Circle":
                    cr = Circle(*param)
                    if cr.check() == True:
                        continue
                    else:
                        helper.append(round(cr.perimeter(), 2))
                        helper.append(round(cr.area(), 2))
                        circ.append(helper)
            # print(tria)
            # print(rect)
            # print(trap)
            # print(para)
            # print(circ)
            max_tria = max(tria)
            max_rect = max(rect)
            max_trap = max(trap)
            max_para = max(para)
            max_circ = max(circ)
            res = max(max_tria, max_rect, max_circ, max_para, max_trap)
            return res


if __name__ == '__main__':
    reader = Reader('input03.txt')
    print(reader.read())
