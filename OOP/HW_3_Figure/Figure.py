from random import *
from turtle import *


class Figure:
    def __init__(self):
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
        pass