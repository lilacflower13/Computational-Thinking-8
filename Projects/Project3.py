### setup
import turtle
turtle.Screen().bgcolor("black")
t1 = turtle.Turtle()
t = turtle.Turtle()
###Pink turtle
t.goto(-50,-50)
t.color("pink")
t.speed(10)
for i in range ( 600 ):
    t.forward(100+i)
    t.left(90+1)
###second turtle
t1.speed(10)
t1.penup()
t1.goto(0,0)
t1.pendown()
t1.color("light blue")
for i in range ( 700 ):
    t1.forward(1+i)
    t1.left(120+1)


turtle.exitonclick()