import turtle
import time
import random

#screen
delay = 0.1
score = 0
high_score = 0
wn = turtle.getscreen()
wn = turtle.getscreen()
wn.setup (width = 800, height = 800, startx = -400, starty = -40)
wn.title("Jsil's Snake Game")
wn.bgcolor("green")
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

segment = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,360)
pen.write("SCORE : 0   HIGH SCORE : 0", align = "center", font = ("Courier", 20, "normal"))

#snake food
food = turtle.Turtle()
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)


#functions
def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def left():
    if head.direction != "right":
        head.direction = "left"

def right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#keyboard
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

while True:
    wn.update()
    #check for screen collision
    if head.xcor() > 390 or head.xcor() < -390 or head.ycor() > 390 or head.ycor() < -390:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #push segments off the screen
        for seg in segment:
            seg.goto(2000,2000)

        segment.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("SCORE : {}  HIGH SCORE : {}".format(score, high_score), align = "center", font = ("Courier", 20, "normal"))

    if head.distance(food) < 20:
        #randomize position
        x = random.randint(-390, 390)
        y = random.randint(-390, 390)
        food.penup()
        food.goto(x, y)
        #body segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)

        #shorten delay
        delay -= 0.001

        # increase score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("SCORE : {}  HIGH SCORE : {}".format(score, high_score), align = "center", font = ("Courier", 20, "normal"))

    for index in range(len(segment)-1, 0, -1): #range from 9 to zero decreasing by 1
        x = segment[index-1].xcor()
        y = segment[index-1].ycor()
        segment[index].goto(x,y)

    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)

    move()

    for seg in segment:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            #push segments off the screen
            for seg in segment:
                seg.goto(2000,2000)

            segment.clear()
            score = 0
            #reset delay
            delay = 0
            pen.clear()
            pen.write("SCORE : {}  HIGH SCORE : {}".format(score, high_score), align="center",font=("Courier", 20, "normal"))


    time.sleep(delay)

wn.mainloop()