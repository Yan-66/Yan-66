from turtle import*
bgcolor("black")
n=6
colors=["red","yellow","blue","green","orange","purple"]
for x in range(150):
    pencolor(colors[x%n])
    forward(x*5/n+x)
    left(360/n+2)
    width(x*n/150)
