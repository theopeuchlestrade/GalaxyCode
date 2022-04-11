from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    right(30)
    forward(10)
    if abs(pos()) < 1:
        break
end_fill()
done()

#blablabla
