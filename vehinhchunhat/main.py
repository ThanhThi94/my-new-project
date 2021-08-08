import turtle
n= turtle.Turtle()

#mau sac
n.fillcolor('blue')
n.pencolor('red')

#kich thuoc rua
n.pensize(3)
n.shapesize(2,3,4)

#ve hinh chu nhat
for i in range(2):
    n.forward(100)
    n.right(90)
    n.forward(50)
    n.right(90)

turtle.done()