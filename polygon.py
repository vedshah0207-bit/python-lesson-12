import turtle

turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle() #Initialises turtle
sides = 6
side_len = 70
angle = 360.0 / sides

for i in range(sides):
    polygon.forward(side_len)
    polygon.right(angle)

turtle.done()