import turtle


def disegnaQuadrato(lato):
    for _ in range(4):
        turtle.forward(lato)
        turtle.left(90)


for i in range(4):
    for j in range(4):
        turtle.penup()
        turtle.goto(j * 10, -i * 10)
        turtle.pendown()
        disegnaQuadrato(10)
