import turtle

t = turtle.Turtle()

t.speed(0)

x = 0
y = 0
r = 50

while True:
    t.clear()

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(r)
    t.screen.bgcolor("black")
    t.pencolor("brown")

    angle = t.heading() + 10
    t.setheading(angle)

turtle.done()
