import turtle
n = turtle.Turtle()
n.pensize(3)

for i in range(5):
    n.left(90)
    n.forward(50)
    for i in range(3):
        n.right(90)
        n.forward(100)
    n.right(90)
    n.forward(50)
    n.right(162)

turtle.done()
