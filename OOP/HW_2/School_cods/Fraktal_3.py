from turtle import*
from random import*

speed(0.0000001)

def move(x,y):
    penup()
    goto(x,y)
    pendown()

global level,step,angle,Theorema

move(-200,-50)

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
step=1000
angle=30
Theorema='F[-F]F[+F]'
draw_fraktal(Theorema,step/3.0,angle,level-1)
