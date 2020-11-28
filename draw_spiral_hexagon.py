from turtle import *

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
p = Pen()
bgcolor('black')
for x in range(360):
    p.pencolor(colors[x%6])
    p.forward(x)
    p.left(59)
done()
