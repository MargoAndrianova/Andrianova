from turtle import *
from random import *
from math import sin, radians


class Triangle:
    def __init__(self, size):
        self.size = size
        self.color = self.random_color()
        self.position = self.move
        self.angles = []
        self.vertex = self.draw()
        self.side = self.sides()

        self.angles.append(randint(30, 120))
        self.angles.append(randint(30, 150 - self.angles[0]))
        self.angles.append(180 - self.angles[0] - self.angles[1])


    @staticmethod
    def random_color():
        r = random()
        g = random()
        b = random()
        return r, g, b

    @staticmethod
    def move():
        up()
        pos_x = randint(-500, 500)
        pos_y = randint(-250, 250)
        goto(pos_x, pos_y)
        down()

    def sides(self):
        ang = self.angles
        a = self.size
        b = self.size * sin(radians(ang[2])) / sin(radians(ang[1]))
        c = self.size * sin(radians(ang[0])) / sin(radians(ang[1]))
        return [a, b, c]

    def draw(self):
        ang = self.angles
        color(self.color)
        a = self.size
        b = self.size*sin(radians(ang[2]))/sin(radians(ang[1]))
        c = self.size*sin(radians(ang[0]))/sin(radians(ang[1]))
        begin_fill()
        x1 = xcor()
        y1 = ycor()
        forward(a)
        left(180 - ang[0])
        x2 = xcor()
        y2 = ycor()
        forward(b)
        left(180 - ang[1])
        x3 = xcor()
        y3 = ycor()
        forward(c)
        left(180 - ang[2])
        end_fill()
        return [(x1, y1), (x2, y2), (x3, y3)]

    def turn(self):
        triangle = Triangle(self.size*2)
        penup()
        speed(0)
        for i in range(120):
            import time
            undo()
            right(3)
            triangle.draw()
            time.sleep(0.2)

    # def coord_bisector(self):
    #     coord = self.vertex
    #     sides = self.side
    #     vertex_2 = coord[1]
    #     vertex_3 = coord[2]
    #     coord_bis = (((sides[1] * vertex_2[0] + sides[3] * vertex_3[0])/(sides[1] + sides[2])),
    #                  ((sides[1] * vertex_2[1] + sides[2] * vertex_3[1])/(sides[1] + sides[2])))
    #     return [coord_bis]
    #
    # def turn_bisector(self):
    #     coord = self.coord_bisector()
    #     vertex_start = self.vertex
    #     up()
    #     goto(coord[0])


if __name__ == '__main__':
    speed(0)
    bgcolor(0.2, 0.2, 0.2)
    turner = randint(0, 100)
    bisector = randint(0, 100)
    for i in range(100):
        triangle = Triangle(randint(30, 70))
        if i == turner:
            triangle.turn()
        elif i == bisector:
            triangle.turn_bisector()
        else:
            triangle.move()
            triangle.draw()
    mainloop()