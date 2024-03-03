from turtle import *
from random import *
from math import *


class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        self._position = (0, 0)
        self.color = self.random_color()

    @staticmethod
    def random_color():
        r = random()
        g = random()
        b = random()
        return r, g, b

    def calc_pos(self, vertex):
        x = self._position[0] + vertex[0]
        y = self._position[1] + vertex[1]
        return x, y

    def draw(self):
        color(self.color)
        v0 = self.calc_pos((randint(-300, 300), randint(-100, 100)))
        v1 = self.calc_pos(self._vertex1)
        v2 = self.calc_pos(self._vertex2)
        up()
        setpos(*v0)
        begin_fill()
        goto(*v1)
        goto(*v2)
        goto(*v0)
        end_fill()

    def turn(self):
        triangle = Triangle(*self._vertex1, *self._vertex2)
        up()
        goto(0, 0)
        speed(0)
        v1 = [self._vertex1[0], self._vertex1[1]]
        v2 = [self._vertex2[0] - self._vertex1[0], self._vertex2[1] - self._vertex1[1]]
        v3 = [-self._vertex2[0], -self._vertex2[1]]
        len_1 = sqrt(v1[0] ** 2 + v1[1] ** 2)
        len_2 = sqrt(v2[0] ** 2 + v2[1] ** 2)
        len_3 = sqrt(v3[0] ** 2 + v3[1] ** 2)
        angle_1 = degrees(acos((v1[0] * v2[0] + v1[1] * v2[1]) / (len_1 * len_2)))
        angle_2 = degrees(acos((v2[0] * v3[0] + v2[1] * v3[1]) / (len_2 * len_3)))
        angle_3 = 180 - angle_1 - angle_2
        a = len_1
        b = a * sin(radians(angle_3))/sin(radians(angle_2))
        c = a * sin(radians(angle_1))/sin(radians(angle_2))
        fillcolor(random(), random(), random())
        for i in range(120):
            import time
            begin_fill()
            right(3)
            forward(a)
            left(180 - angle_1)
            forward(b)
            left(180 - angle_2)
            forward(c)
            left(180 - angle_3)
            end_fill()
            time.sleep(0.2)
            undo()


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