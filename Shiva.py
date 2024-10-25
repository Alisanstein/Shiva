import turtle

# Create a screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set background color

# Create a turtle
p = turtle.Turtle()
p.color("black")  # Set pen color
p.pensize(2)    # Set pen size
p.speed(3)
#turtle.tracer(0)

#functions to make the drawing easier
def f(num):
    p.forward(num)

def r(num):
    p.right(num)

def l(num):
    p.left(num)

def g(num1,num2):
    p.penup()
    p.goto(num1,num2)
    p.pendown()


#Start
g(-500,-50)

#S
f(40)
for i in range(180):
    f(1)
    l(1)
for i in range(180):
    f(1)
    r(1)
f(40)
l(180)
f(40)
for i in range(180):
    f(1)
    l(1)
for i in range(180):
    f(1)
    r(1)
l(180)

#Space
g(-350, -50)

#H
l(90)
f(230)
r(180)
f(115)
l(90)
f(100)
l(90)
f(115)
l(180)
f(230)
l(90)

#Space
g(-175,-50)

#I
f(125)
l(180)
f(62.5)
r(90)
f(230)
l(90)
f(62.5)
l(180)
f(125)
l(180)
f(62.5)
l(90)
f(230)
l(90)

#Space
g(0,180)

#V
r(60)
f(265)
l(120)
f(265)

#Space
g(250,-50)

#A
f(265)
r(120)
f(265)
l(180)
f(132.5)
l(60)
f(135)
l(180)
f(135)
r(60)
f(132.5)
l(60)


#Finish
g(0,0)
turtle.update()
turtle.done()