import turtle

turtle.Screen().bgcolor("yellow")
board = turtle.Turtle()
board.speed(3)

#1st triangle of star
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.penup()
board.right(150)
board.forward(50)

#2nd triangle of star
board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

turtle.done()