import turtle

t = turtle.Turtle()
turtle.Screen().bgcolor("green")
turtle.Screen().title("Beautiful Spiral")
turtle.speed(0)
size = 5

while True:
    for i in range(4):
        t.fd(size)
        t.rt(90)
        size += 5