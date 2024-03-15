from turtle import*
from random import*

speed(0.0000000000000001)

def move(x,y):
    penup()
    goto(x,y)
    pendown()

global level,step,angle,Theorema

move(200,0)

def draw_fraktal(Theorema,step,angle,level):
    for i in range(len(Theorema)):
        if Theorema[i]=='+':
            right(angle)
        elif Theorema[i]=='-':
            left(angle)
        elif Theorema[i]=='[':
            x_turtle=xcor()
            y_turtle=ycor()
            ang_turtle=heading()
        elif Theorema[i]==']':
            move(x_turtle,y_turtle)
            setheading(ang_turtle)
        elif Theorema[i]=='F':
            if level==0:
                forward(step)
            else:
                draw_fraktal(Theorema,step/3.0,angle,level-1)

level=int(input('level='))
step=500
angle=90
Theorema='F-F+F+F-F'

right(225)
for j in range(4):
    draw_fraktal(Theorema,step/3.0,angle,level-1)
    right(270)
