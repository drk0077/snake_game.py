# clone of snake_xenzia
# @drk0077

# imports
import random
import time
import turtle

# initial scores
score = 0
high_score = 0
delay = 0.1

# set up screen
screen = turtle.Screen()
screen.title("snake_game")
screen.bgcolor("#7fff00")
screen.setup(width=600, height=600)
screen.tracer(0)

# snake_head
head = turtle.Turtle()
head.goto(0, 0)
head.speed(0)
head.shape("square")
head.color("#0000ff")
head.penup()
head.direction = "stop"

# snake_food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
food.speed(0)

# score_board
sc = turtle.Turtle()
sc.penup()
sc.color("black")
sc.hideturtle()
sc.goto(0, 260)
sc.speed(0)
sc.shape("square")
sc.write("Score: 0  High_Score: 0", align="center", font=("ds-digital", 24, "normal"))


# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# keyboard_bindings
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

segments = []

# mainloop
while True:
    screen.update()

    # check collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segment of the body
        for segment in segments:
            segment.goto(1000, 1000)  # out of range
            # clear the segments
        segments.clear()
        # reset the score
        score = 0
        # reset the delay
        delay = 0.1
        # reset the score_board
        sc.clear()
        sc.write(f"Score: {score}  High_Score: {high_score}", align="center", font=("ds-digital", 24, "normal"))

    # check the collision with the food
    if head.distance(food) < 20:
        """move the food to some random space"""
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # add new segments
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("#0000ff")
        new_segment.penup()
        segments.append(new_segment)
        # delay shortening
        delay -= 0.001
        # adding the score
        score += 10
        # rewriting the high_score
        if score > high_score:
            high_score = score
        sc.clear()
        sc.write(f"Score: {score}  High_Score: {high_score}", align="center", font=("ds-digital", 24, "normal"))

    # move the segments in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    # move the segments 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # checks for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide segments
            for segment in segments:
                segment.goto(1000, 100)
            segments.clear()
            score = 0
            delay = 0.1

            # update the score
            sc.clear()
            sc.write(f"Score: {score}  High_Score: {high_score}", align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)

screen.mainloop()
