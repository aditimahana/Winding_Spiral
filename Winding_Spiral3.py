# WindingSpiral3
import turtle
t = turtle.Pen()
t.speed(0)
colors = ["crimson", "navajowhite", "cornflowerblue", "olivedrab"]
for x in range(200):
    t.pencolor(colors[x % 4])
    t.forward(x)
    t.left(91)
