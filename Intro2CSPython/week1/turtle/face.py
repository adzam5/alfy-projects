import turtle

def goto(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()

def square():
	for i in range(4):
		turtle.forward(100)
		turtle.right(90)

def ears():
	def draw(x,y):
		goto(x,y)
		turtle.circle(15)
		turtle.circle(25)
	draw(0,0)
	draw(100,0)

def eyes(color):
	def draw(x,y):
		goto(x,y)
		turtle.fillcolor(color)
		turtle.circle(10)
		turtle.begin_fill()
		turtle.circle(5)
		turtle.end_fill()
	draw(20,-35)
	draw(80, -35)

def nose(color):
	goto(57,-58)
	turtle.color(color)
	for i in range(3):
		turtle.right(240)
		turtle.forward(15)

def smile(color):
	goto(25,-68)
	turtle.color(color)
	turtle.width(4)
	turtle.right(90)
	turtle.circle(25,extent = 180)

square()
ears()
eyes("blue")
nose("black")
smile("red")

turtle.hideturtle()
turtle.exitonclick()
