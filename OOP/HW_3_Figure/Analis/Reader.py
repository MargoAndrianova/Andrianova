from Figure import *
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
            ball = []
            trp = []
            qup = []
            recp = []
            cone = []
            trpr = []
            for line in f:
                lines = line.strip().split()
                name = lines[0]
                param = list(map(int, lines[1:]))
                if name == "Triangle":
                    tr = Triangle(*param)
                    if tr.check() == False:
                        continue
                    else:
                        tria.append(round(tr.volume(), 2))
                elif name == "Rectangle":
                    rec = Rectangle(*param)
                    if rec.check() == False:
                        continue
                    else:
                        rect.append(round(rec.volume(), 2))
                elif name == "Trapeze":
                    tra = Trapeze(*param)
                    if tra.check() == False:
                        continue
                    else:
                        trap.append(round(tra.volume(), 2))
                elif name == "Parallelogram":
                    pr = Parallelogram(*param)
                    if pr.check() == False:
                        continue
                    else:
                        para.append(round(pr.volume(), 2))
                elif name == "Circle":
                    cr = Circle(*param)
                    if cr.check() == False:
                        continue
                    else:
                        circ.append(round(cr.volume(), 2))
                elif name == "Ball":
                    b = Ball(*param)
                    if b.check() == False:
                        continue
                    else:
                        ball.append(round(b.volume(), 2))
                elif name == "TriangularPyramid":
                    tp = TriangularPyramid(*param)
                    if tp.check() == False:
                        continue
                    else:
                        trp.append(round(tp.volume(), 2))
                elif name == "QuadrangularPyramid":
                    qp = QuadrangularPyramid(*param)
                    if qp.check() == False:
                        continue
                    else:
                        qup.append(round(qp.volume(), 2))
                elif name == "RectangularParallelepiped":
                    rpr = RectangularParallelepiped(*param)
                    if rpr.check() == False:
                        continue
                    else:
                        recp.append(round(rpr.volume(), 2))
                elif name == "Cone":
                    c = Cone(*param)
                    if c.check() == False:
                        continue
                    else:
                        cone.append(round(c.volume(), 2))
                elif name == "TriangularPrism":
                    tp = TriangularPrism(*param)
                    if tp.check() == False:
                        continue
                    else:
                        trpr.append(round(tp.volume(), 2))
            max_tria = max(tria)
            max_rect = max(rect)
            max_trap = max(trap)
            max_para = max(para)
            max_circ = max(circ)
            max_ball = max(ball)
            max_trp = max(trp)
            max_qup = max(qup)
            max_recp = max(recp)
            max_cone = max(cone)
            max_trpr = max(trpr)
            # print(max(tria))
            # print(max(rect))
            # print(max(trap))
            # print(max(para))
            # print(max(circ))
            # print(max(ball))
            # print(max(trp))
            # print(max(qup))
            # print(max(recp))
            # print(max(cone))
            res = max(max_tria, max_rect, max_circ, max_para, max_trap, max_ball, max_trp, max_qup, max_recp, max_cone, max_trpr)
            return res


if __name__ == '__main__':
    reader = Reader('input01.txt')
    print(reader.read())
