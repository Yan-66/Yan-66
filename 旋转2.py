import turtle
turtle.bgcolor("black")
n=6
colors=["red","yellow","blue","green","orange","purple"]
for i in range(100):
    turtle.pencolor(colors[i%n])
    turtle.forward(i*3/n+i)
    turtle.left(360/n+2)
    turtle.width(i*n/100)
    
