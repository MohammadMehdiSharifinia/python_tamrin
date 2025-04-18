import turtle, math

s = turtle.Screen()
s.bgcolor("lightblue")
s.setup(800, 600)
s.tracer(0)

g = turtle.Turtle()
g.hideturtle()
g.penup()
g.goto(-300, -200)
g.pendown()
g.pensize(5)

b = turtle.Turtle()
b.shape("circle")
b.color("black")
b.shapesize(0.5)
b.penup()
b.hideturtle()
b.goto(-300, -200)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("red")
t.pensize(3)
t.penup()
t.goto(300, -100)
t.setheading(90)
t.pendown()
t.forward(100)
t.penup()
t.goto(315, 15)
t.pendown()
t.circle(15)
t.penup()
t.goto(300, -15)
t.pendown()
t.setheading(180)
t.forward(40)
t.backward(80)
t.penup()
t.goto(300, -100)
t.pendown()
t.setheading(225)
t.forward(40)
t.backward(40)
t.setheading(315)
t.forward(40)

msg = turtle.Turtle()
msg.hideturtle()
msg.penup()
msg.goto(300, 50)

a = turtle.Turtle()
a.hideturtle()
a.penup()
a.goto(-350, 250)

while True:
    msg.clear()
    angle = s.numinput("زاویه", "لطفا زاویه را وارد کن (بین 10 تا 80):", 45, 10, 80)
    if angle is None:
        break

    g.clear()
    g.penup()
    g.goto(-300, -200)
    g.setheading(angle)
    g.pendown()
    g.forward(50)

    a.clear()
    a.write(f"زاویه: {angle}°", font=("Arial", 16))

    b.showturtle()
    b.goto(-300, -200)

    vx = 15 * math.cos(math.radians(angle))
    vy = 15 * math.sin(math.radians(angle))

    b.state = "fire"

    won = False

    while b.state == "fire":
        x = b.xcor() + vx
        y = b.ycor() + vy - 0.5
        b.goto(x, y)
        vy -= 0.2
        if y < -200 or (280 < x < 320 and -150 < y < 50):
            if 280 < x < 320 and -150 < y < 50:
                msg.clear()
                msg.write("شما برنده شدید", align="center", font=("Arial", 24, "bold"))
                won = True
            b.hideturtle()
            b.state = "ready"
            break
        s.update()

    s.update()

    if won:
        turtle.time.sleep(1)
        msg.clear()
