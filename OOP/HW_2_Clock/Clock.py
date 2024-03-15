from datetime import *
from time import sleep
from turtle import *
class Clock:
    def __init__(self, size):
        self.size = size
        self.time = self.world_time()

    def basis(self):
        fillcolor("#F5F5F5")
        radius = self.size
        up()
        goto(0, -radius)
        down()
        begin_fill()
        circle(radius)
        end_fill()
        left(90)
        up()
        goto(0, (radius - radius/5))
        for i in range(1, 13):
            up()
            goto(0, -20)
            setheading(90)
            right(30*i)
            forward(radius - radius/8)
            down()
            write(str(i), align="center", font=("Times New Roman", 32, "normal"))


    def arrow_sec(self):
        pencolor("#222021")
        pensize(6)
        size = self.size - self.size/3
        up()
        goto(0, 0)
        down()
        forward(size)
        backward(size + self.size/5)
        goto(0, 0)

    def arrow_min(self):
        pensize(4)
        size = self.size - self.size/5
        up()
        goto(0, 0)
        down()
        forward(size)
        backward(size + self.size/5)
        goto(0, 0)

    def arrow_hour(self):
        pensize(8)
        size = self.size - self.size/(2.5)
        up()
        goto(0, 0)
        down()
        forward(size)
        backward(size + self.size/5)
        goto(0, 0)

    def world_time(self):
        time_now = datetime.now(timezone.utc)
        kyiv_time = timezone(timedelta(hours=2))
        local_time = time_now.astimezone(kyiv_time)
        hour = local_time.hour
        minute = local_time.minute
        sec = local_time.second
        return [hour, minute, sec]

    def draw(self):
        sec = self.time[2]
        minute = self.time[1]
        hour = self.time[0]
        self.basis()
        color("darkred")
        up()
        goto(0, 0)
        setheading(90)
        right(6 * (minute))
        down()
        self.arrow_min()
        color("#240d15")
        up()
        goto(0, 0)
        setheading(90)
        right(30 * (hour))
        down()
        self.arrow_hour()
        while True:
            self.arrow_sec()
            sleep(1)
            for i in range(3):
                undo()
            sec += 1
            if sec == 60:
                sec = 1
                minute += 1
                setheading(90)
                right(6 * (minute-1))
                color("#F5F5F5")
                self.arrow_min()
                setheading(90)
                right(6 * minute)
                color("darkred")
                self.arrow_min()
                up()
                goto(0, 0)
                setheading(90)
                right(30 * hour)
                down()
                color("#240d15")
                self.arrow_hour()
                if minute == 60:
                    minute = 0
                    hour += 1
                    setheading(90)
                    right(30 * (hour - 1))
                    color("#F5F5F5")
                    self.arrow_hour()
                    setheading(90)
                    right(30 * hour)
                    color("#240d15")
                    self.arrow_hour()
            setheading(90)
            right(6 * sec)



if __name__ == "__main__":
    speed(0)
    hideturtle()
    bgcolor("#696969")
    clock = Clock(300)
    clock.draw()
    mainloop()