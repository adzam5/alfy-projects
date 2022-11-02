import turtle

def triangle():
    for x in range(6):
        for x in range(3):
            turtle.forward(100)
            turtle.left(120)
        turtle.left(60)

triangle()

turtle.exitonclick()
