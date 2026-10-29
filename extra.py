import turtle
t = turtle.Turtle()
t.speed(0)
turtle.Screen().bgcolor("black")
t.pensize(3)
colors = ["red", "blue", "green", "orange", "purple", "pink"]

for i in range(100):
    t.color(colors[i % 6])
    t.forward(i * 2)
    t.rt(59)

turtle.done()