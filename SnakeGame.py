import turtle

import time

import random

import math

import sys

from threading import Timer

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

sprint("Hello player :>")


turtle.Screen().bgcolor("lightblue")


w = turtle.Turtle()

w.speed(5)

w.color("green")
w.hideturtle()
w.penup()
w.goto(-200, 440)
w.write("Rules!", font=("Pacifico", 14, "normal"))

w.goto(-600, 400)
w.write("In this game, you will be catching apples. Your goal is to level up your fruit catcher to level 50, and get to the final shape, the turtle!", font=("Pacifico", 14, "normal"))

w.goto(-800, 380)
w.write(" Once you hit a certan level, your fruit catcher will increase in sise, and get better! You can also increase your fruit's power! If you go outside of the green box, however, you will lose the game. Be careful and Good luck!", font=("Pacifico", 14, "normal"))

w.color("red")
w.goto(-800, 260)
w.write("Fruit catcher!", font=("Pacifico", 34, "normal"))
w.width(10)
w.goto(-810, 250)
w.pendown()
w.goto(-810, 350)
w.goto(-510, 350)
w.goto(-510, 250)
w.goto(-810, 250)
w.penup()


w.color("blue")
w.goto(-810, 240)
w.pendown()
w.goto(-810, -400)
w.goto(-510, -400)
w.goto(-510, 240)
w.goto(-810, 240)


w.penup()
w.goto(-740, 180)

w.write("Levels", font=("Pacifico", 24, "normal"))
w.goto(-790, 140)

w.write("Level 10 = Fruit catcher upgrade.", font=("Pacifico", 14, "normal"))

w.goto(-790, 100)

w.write("Level 20 = Fruit upgrade.", font=("Pacifico", 14, "normal"))

w.goto(-790, 60)

w.write("Level 30 = Fruit catcher upgrade.", font=("Pacifico", 14, "normal"))
w.goto(-775, 40)
w.write("(Another fruit per catch.)", font=("Pacifico", 14, "normal"))

w.goto(-790, 0)

w.write("Level 40 = Fruit upgrade.", font=("Pacifico", 14, "normal"))

w.goto(-790, -40)

w.write("Level 50 = Victory!", font=("Pacifico", 14, "normal"))

w.goto (-810, -60)
w.pendown()
w.goto(-510, -60)
w.penup()

w.goto(-710, -120)
w.write("Timer", font=("Pacifico", 30, "normal"))

#add stopwatch function here
w.goto(-760, -130)

w.write("The orange circle = the pause button.", font=("Pacifico", 10, "normal"))

w.goto(-760, -150)
w.write("The green circle = the play button. ", font=("Pacifico", 10, "normal"))

w.goto(-770, -180)
w.write("The purple circle play's only the game. ", font=("Pacifico", 10, "normal"))

w.goto (-810, -300)
w.pendown()
w.goto(-510, -300)
w.penup()

l = turtle.Turtle()

l.speed(5)

l.color("green")
l.hideturtle()
l.penup()

l.width(5)

l.goto(-500,-400)
l.pendown()
l.goto(650,-400)
l.goto(650,350)
l.goto(-500,350)
l.goto(-500,-400)

l.color("black")

l.penup()
l.goto(-820, 360)
l.pendown()

l.goto(660, 360)
l.goto(660, -410)
l.goto(-820, -410)
l.goto(-820, 360)


pausegame = 2
# 2 = true
#1 = false

b = turtle.Turtle()

b.speed(5)

def st(x,y):
    global pausegame
    sprint("When this is clicked, stop the timer.")
    pausegame = 1
    

b.penup()
b.hideturtle()

b.goto(-780, -80)
b.shape("circle")
b.color("orange")

b.showturtle()

b.onclick(st)

c = turtle.Turtle()
c.speed(5)

def s(x,y):
    global pausegame
    sprint("When this is clicked, play the timer.")
    pausegame = 2
    

c.penup()
c.hideturtle()

c.goto(-530, -80)
c.shape("circle")
c.color("green")

c.showturtle()

c.onclick(s)

d = turtle.Turtle()
d.speed(5)

timetrue = turtle.Turtle()

timetrue.speed(5)

timetrue.penup()
timetrue.hideturtle()

timetrue.goto(300, 300)


tim = 2
# 2 = true
#1 = false


def ply(x,y):
    global timetrue
    timetrue.clear()
    global pausegame
    sprint("When this is clicked, play only the game.")
    pausegame = 2
    tim = 1
    ti = 1
    

d.penup()
d.hideturtle()

d.goto(-550, -80)
d.shape("circle")
d.color("purple")

d.showturtle()

d.onclick(ply)





u = 1

ti = 0

t = turtle.Screen()

snake = turtle.Turtle()
apple = turtle.Turtle()
apple2 = turtle.Turtle()
apple3 = turtle.Turtle()
s = turtle.Turtle()


snake.speed(5)
apple.speed(5)
apple2.speed(5)
apple3.speed(5)


apple.penup()
apple2.penup()
apple3.penup()

snake.penup()
s.penup()
snake.color("yellow")


apple.shape("circle")
apple.color("red")
apple2.shape("circle")
apple2.color("red")
apple3.shape("circle")
apple3.color("red")

s.color("purple")

apple2.hideturtle()
apple3.hideturtle()

s.hideturtle()

s.goto(-680,-380)
apple.goto(100,100)
apple2.goto(1000,1000)
apple3.goto(1000,1000)
score = 0
s.write("Level: {}".format(score), align="center", font=("Pacifico", 24, "normal"))

s1 = 1

s2 = 1

s3 = 1

s4 = 1

s5 = 1

#Timer
start = time.time()

def temp():
    
            #Timer tests

    
    
    global score
    global s1
    global s2
    global s3
    global s4
    global s5
    
    if (abs(snake.xcor() -apple.xcor())<=20 and abs(snake.ycor() -apple.ycor())<=20 or abs(snake.xcor() -apple2.xcor())<=20 and abs(snake.ycor() -apple2.ycor())<=20 or abs(snake.xcor() -apple3.xcor())<=20 and abs(snake.ycor() -apple3.ycor())<=20):
        
        timetrue.goto(-780, -257)
        timetrue.clear()
        #
        time_elapsed  = time.time() - start     
        #timetrue.write("tst")
        hour = math.floor(time_elapsed / 3600)
        minute = math.floor((time_elapsed % 3600) / 60)
        second = round((time_elapsed % 3600) % 60)
        
        timetrue.write(f'Time elapsed: {hour}:{minute}:{second}', font=("Pacifico", 20, "normal"))
        
        x = random.randrange(-500,650)
        y = random.randrange(-400,350)
        apple.goto(x,y)
        score += 1
        s.clear()
        s.write("Level: {}".format(score), align="center", font=("Pacifico", 24, "normal"))
         
        x2 = random.randrange(-500,650)
        y2 = random.randrange(-400,350)
        apple2.goto(x2,y2)
        
        x3 = random.randrange(-500,650)
        y3 = random.randrange(-400,350)
        apple2.goto(x3,y3)
        
        if score > 29:
            print("bonus fruit added!")
            score += 1
        
        
    if snake.xcor() < -500:
        print("you lose :<")
        quit()
        
    if snake.xcor() > 650:
        print("you lose :<")
        quit()
        
    if snake.ycor() < -400:
        print("you lose :<")
        quit()
        
    if snake.ycor() > 350:
        print("you lose :<")
        quit()
    
    
    if s1 == 1:
        if score == 10:
            print("You've moved on to the next level!")
            snake.shape("triangle")
            s1 = 2
    
    if s2 == 1:
        if score == 20:
            print("You've updated your fruit to a pear!")
            apple.shape("triangle")
            apple.color("green")
            apple2.showturtle()
            
            s2 = 2
    
    if s3 == 1:
        if score == 30:
            print("You've moved on to the next level!")
            snake.shape("square")
            s3 = 2
    
    if s4 == 1:
        if score == 40:
            print("You've updated your fruit to a orange!")
            apple.shape("circle")
            apple.color("orange")
            apple2.shape("triangle")
            apple2.color("green")
            apple3.showturtle()
            s4 = 2
            
    if s5 == 1:
        if score == 50:
            if ti == 0:
                
                l.penup()
                
                l.goto(0,0)
                l.write("You Won!!!", font=("Pacifico", 14, "normal"))
                l.goto(-60,-20)
                l.write("If you want to keep playing, the timer will still be running for you", font=("Pacifico", 14, "normal"))
                snake.shape("turtle")
               
                print("You Won!")
                s5 = 2
            else:
                print("you paused the timer, so this run is not eligible for records")
                quit()


def godown():
    if pausegame == 2:
        snake.setheading(270)
        snake.forward(20)
        temp()
    else:
        print("paused!")
    
def goup():
    if pausegame == 2:
        snake.setheading(90)
        snake.forward(20)
        temp()
    else:
        print("paused!")
    
def goleft():
    if pausegame == 2:
        snake.setheading(180)
        snake.forward(20)
        temp()
    else:
        print("paused!")
        
def goright():
    if pausegame == 2:
        snake.setheading(0)
        snake.forward(20)
        temp()
    else:
        print("paused!")
    
    
    
t.listen()

t.onkeypress(goup, "w")

t.onkeypress(godown, "s")

t.onkeypress(goleft, "a")

t.onkeypress(goright, "d")

t.onkeypress(goup, "Up")

t.onkeypress(godown, "Down")

t.onkeypress(goleft, "Left")

t.onkeypress(goright, "Right")

