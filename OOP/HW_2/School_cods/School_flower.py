from turtle import *
from random import *

bgcolor('green')
speed(4)


def move(x):
    up()
    forward(x)
    down()


def polygon(size, kol_st, count):
    angle = 360 / kol_st
    if count > 0:
        forward(size)
        right(angle)
        polygon(size, kol_st, count - 1)


def kvitka_polygon(size, kol_st, kol_lep, count1):  # квітка з багатокутників за допомогою рекурсії
    angle1 = 360 / kol_lep
    if count1 > 0:
        polygon(size, kol_st, kol_st)
        right(angle1)
        kvitka_polygon(size, kol_st, kol_lep, count1 - 1)


def flower(count):
    col = choice(['yellow', 'light blue', 'pink'])
    size = randint(10, 50)
    up()
    goto(-300, 300)
    down()
    color(col)
    kvitka_polygon(size, 8, 5, 5)
    for j in range(3):
        for u in range(2):
            col = choice(['yellow', 'blue', 'pink'])
            size = randint(10, 50)
            move(300)
            color(col)
            kvitka_polygon(size, 8, 5, 5)
        right(90)
    for i in range(2):
        col = choice(['yellow', 'blue', 'pink'])
        size = randint(10, 50)
        move(300)
        color(col)
        kvitka_polygon(size, 8, 5, 5)
        right(90)


flower(1)