"""turtle project on Indian Flag
----- @drk0077 -------"""
from turtle import Turtle, Screen

flag = Turtle()
screen = Screen()
flag.speed(15)
flag.pensize(5)


# function for the positioning of turtle
def draw(x, y):
    flag.penup()
    flag.goto(x, y)
    flag.pendown()


# drawing ashoka chakra
flag.color("#000080")
for i in range(24):
    flag.forward(80)
    flag.backward(80)
    flag.left(15)
draw(0, -80)
flag.circle(80, 360)

draw(0, -90)

# drawing green area
flag.color("#138808")
flag.begin_fill()
flag.forward(350)
flag.right(90)
flag.forward(200)
flag.right(90)
flag.forward(700)
flag.right(90)
flag.forward(200)
flag.right(90)
flag.forward(350)
flag.end_fill()

# Drawing saffron rectangle
flag.color("#FF9933")
draw(-350, 90)
flag.begin_fill()

for _ in range(4):
    if _ % 2 == 0:
        flag.forward(700)
        flag.left(90)
    else:
        flag.forward(200)
        flag.left(90)
flag.end_fill()

screen.exitonclick()
