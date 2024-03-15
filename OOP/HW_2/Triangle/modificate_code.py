from time import sleep
from turtle import *
from random import *
from math import *


class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        self._position = (0, 0)
        self.color = self.random_color()

    def midpoint(self, p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    def b_cross(self):
        mid1 = self.midpoint(self._position, self._vertex1)
        mid2 = self.midpoint(self._vertex1, self._vertex2)
        angle = (atan2(self._vertex1[1] - self._position[1], self._vertex1[0] - self._position[0])
                 + atan2(self._vertex2[1] - self._position[1], self._vertex2[0] - self._position[0]) / 2)
        x = mid1[0] + (mid2[0] - mid1[0]) * cos(angle) - (mid2[1] - mid1[1]) * sin(angle)
        y = mid1[1] + (mid2[0] - mid1[0]) * sin(angle) + (mid2[1] - mid1[1]) * cos(angle)
        return (x, y)

    def median_cross(self):
        M_AB = (self.midpoint(self._position, self._vertex1))
        M_BC = ((self.midpoint(self._vertex1, self._vertex2)))
        M_AC = ((self.midpoint(self._vertex2, self._position)))
        x = (M_AB[0] + M_BC[0] + M_AC[0]) / 3
        y = (M_AB[1] + M_BC[1] + M_AC[1]) / 3
        return (x, y)

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

    def turn(self, vertex, ang):
        center = self.b_cross()
        x = (center[0] + (vertex[0] - center[0]) * cos(radians(ang))
                       - (vertex[1] - center[1]) * sin(radians(ang)))
        y = (center[1] + (vertex[0] - center[0]) * sin(radians(ang))
                       + (vertex[1] - center[1]) * cos(radians(ang)))
        return (x, y)

    def draw_turn(self):
        color(self.color)
        v0 = self.calc_pos((randint(-650, 650), randint(-250, 250)))
        v1 = self.calc_pos(self._vertex1)
        v2 = self.calc_pos(self._vertex2)
        for i in range(12, 361, 12):
            v0 = self.turn(v0, radians(i))
            v1 = self.turn(v1, radians(i))
            v2 = self.turn(v2, radians(i))
            up()
            goto(*v0)
            begin_fill()
            goto(*v1)
            goto(*v2)
            goto(*v0)
            end_fill()
            sleep(0.4)
            undo()

    def scretch(self):
        color(self.color)
        v1 = self.calc_pos(self._vertex1)
        v2 = self.calc_pos(self._vertex2)
        v0 = self.calc_pos(self._position)
        for i in range(1, 50):
            up()
            begin_fill()
            setpos(*v0)
            goto(v1[0]*(1+i/50), v1[1]*(1+i/50))
            goto(v2[0]*(1+i/50), v2[1]*(1+i/50))
            goto(v0[0]*(1+i/50), v0[1]*(1+i/50))
            end_fill()
            speed(0.1)
            undo()
            undo()



if __name__ == '__main__':
    speed(0)
    bgcolor(0.2, 0.2, 0.2)
    r = randint(0, 100)
    s = randint(0, 100)
    for i in range(100):
        x = []
        y = []
        for j in range(2):
            x.append(randint(-200, 200))
            y.append(randint(-50, 50))
        triangle = Triangle(x[0], y[0], x[1], y[1])
        if i == 0:
            bisect = triangle.b_cross()
            up()
            goto(*bisect)
            dot(3, "darkred")
            triangle.draw_turn()
        elif i == 101:
            triangle.scretch()
        else:
            triangle.draw()
    mainloop()