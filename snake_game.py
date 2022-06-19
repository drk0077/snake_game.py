import turtle

# initial scores
score = 0
high_score = 0

# set up screen
screen = turtle.Screen()
screen.title("snake_game")
screen.bgcolor("yellow")
screen.setup(width=600, height=600)
screen.tracer(0)

# snake_head
head = turtle.Turtle()
head.goto(0, 0)
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.direction = "stop"

# snake_food
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 0)
food.speed(0)

# score_board
sc = turtle.Turtle()
sc.penup()
sc.color("black")
sc.hideturtle()
sc.goto(0, 260)
sc.speed(0)
sc.shape("square")
sc.write("Sore: 0  High_Score: 0", align="center", font=("ds-digital", 24, "normal"))



screen.exitonclick()
