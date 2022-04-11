import turtle

tur = turtle.Turtle()
r = 8

tur.speed(10	)

for i in range(100):
    tur.pu()
    # tur.forward(2*r+5)
    # tur.left(35-i/10)
    tur.circle(4*r + i, 35)
    tur.color("red")
    tur.pd()
    tur.begin_fill()
    tur.circle(r)
    tur.end_fill()
