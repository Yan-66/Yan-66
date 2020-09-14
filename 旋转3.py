import turtle as t
t.bgcolor("black")
n=6
colors=["red","yellow","blue","green","orange","purple"]
for x in range(100):
    t.pencolor(colors[x%n])
    t.forward(x*3/n+x)
    t.left(360/n+2)
    t.width(x*n/100)
