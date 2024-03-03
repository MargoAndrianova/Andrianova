def turn(self):
    triangle = Triangle(*self._vertex1, *self._vertex2)
    penup()
    goto(0, 0)
    speed(0)
    v1 = [-self._vertex1[0], -self._vertex1[1]]
    v2 = [self._vertex2[0] - self._vertex1[0], self._vertex2[1] - self._vertex1[1]]
    v3 = [-self._vertex2[0], - self._vertex2[1]]
    len_1 = sqrt(v1[0] ** 2 + v1[1] ** 2)
    len_2 = sqrt(v2[0] ** 2 + v2[1] ** 2)
    a_b = v1[0] * v2[0] + v1[1] * v2[1]
    angle_1 = acos()
    for i in range(120):
        import time
        left(3)
        forward(len_1)
        left(180 -)
        time.sleep(0.2)
        clear()
        left(180)