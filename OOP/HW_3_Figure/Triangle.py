from random import *
from turtle import *

from Figure import Figure

class Triangle(Figure):

    def __init__(self, x1, y1, x2, y2):
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        super().__init__()

    def draw(self):
        color(self.color)
        v0 = self.calc_pos((randint(-650, 650), randint(-250, 250)))
        v1 = self.calc_pos(self._vertex1)
        v2 = self.calc_pos(self._vertex2)
        up()
        setpos(*v0)
        begin_fill()
        goto(*v1)
        goto(*v2)
        goto(*v0)
        end_fill()

if __name__ == '__main__':
    speed(0)
    bgcolor(0.2, 0.2, 0.2)
    r = randint(0, 100)
    for i in range(100):
        x = []
        y = []
        for j in range(2):
            x.append(randint(-200, 200))
            y.append(randint(-50, 50))
        triangle = Triangle(x[0], y[0], x[1], y[1])
        if i == r:
            triangle.turn()
        else:
            triangle.draw()
    mainloop()