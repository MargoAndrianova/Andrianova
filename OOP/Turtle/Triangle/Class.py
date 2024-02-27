from turtle import *
from random import *
from math import sin, radians


class Triangle:
    def __init__(self, size):
        self.size = size
        self.color = self.random_color()
        self.position = self.move
        self.angles = []

        self.angles.append(randint(30, 120))
        self.angles.append(randint(30, 150-self.angles[0]))
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

    def draw(self):
        angle = self.angles
        color(self.color)
        b = self.size*sin(radians(angle[2]))/sin(radians(angle[1]))
        c = self.size*sin(radians(angle[0]))/sin(radians(angle[1]))
        begin_fill()
        forward(self.size)
        left(180 - angle[0])
        forward(b)
        left(180 - angle[1])
        forward(c)
        end_fill()

    def turn(self):
        triangle = Triangle(self.size*2)
        penup()
        goto(0, 0)
        speed(0)
        for i in range(120):
            import time
            left(6)
            triangle.draw()
            time.sleep(0.2)
            undo()
            left(180-self.angles[2])


if __name__ == '__main__':
    speed(0)
    bgcolor(0.2, 0.2, 0.2)
    r = randint(0,100)
    for i in range(100):
        triangle = Triangle(randint(30, 70))
        if i == r:
            triangle.turn()
        else:
            triangle.move()
            triangle.draw()
    mainloop()