"""Turtle code."""

import colorsys
import turtle as t

t.bgcolor("black")
t.tracer(10)
t.pensize(5)
h = 0

for i in range(300):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.005
    t.pencolor(c)
    t.fillcolor("black")
    t.begin_fill()
    for j in range(2):
        t.fd(i * 1.2)
        t.rt(60)
        t.fd(300)
        t.rt(120)
    t.rt(121)
    t.end_fill()
t.done()
