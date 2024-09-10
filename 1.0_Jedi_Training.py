'''
1.0 Jedi Training (17pts)  Name:________________


1. Define Forking (1pt): Making a copy of a repository from an organization to my account on GitHub

2. Define Cloning (1pt): Taking a repository from GitHub and putting it on my computer to work on

3. Define Branching (1pt): 

4. Define Committing (1pt): 

5. Define Merging (1pt): 

6. Define Pushing (1pt):

7. Define Pull Request (1pt):


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle
tom = turtle.Turtle()
screen = turtle.Screen()
tom.speed(1000000)
tom.pensize(4)
switch = 0
graphic_size = 252
r4 = (11 / 12) * graphic_size
r3 = (10 / 12) * graphic_size
r2 = (9 / 12) * graphic_size
r1 = (4 / 12) * graphic_size
def circle(x):
    tom.fillcolor()
    tom.begin_fill()
    tom.circle(x)
    tom.end_fill()
def bar(y):
    tom.begin_fill()
    for i in range(2):
        tom.forward((4 / 3) * y)
        tom.left(90)
        tom.forward((1 / 9) * y)
        tom.left(90)
    tom.end_fill()
def gap(z):
    tom.begin_fill()
    for i in range(4):
        tom.forward((1 / 6) * z)
        (tom .left(90))
    tom.end_fill()
tom.penup()
for radius in [graphic_size, r4, r3, r2, r1]:
    tom.forward(radius)
    tom.left(90)
    tom.pendown()
    circle(radius)
    tom.penup()
    tom.home()
    if switch == 0:
        tom.color("white")
        switch = 1
        continue
    tom.color("black")
    switch = 0
tom.color("black")
for angle in [0, 45, 90, 135]:
    tom.left(angle)
    tom.backward((2 / 3) * graphic_size)
    tom.right(90)
    tom.forward((1 / 18) * graphic_size)
    tom.left(90)
    tom.pendown()
    bar(graphic_size)
    tom.penup()
    tom.home()
tom.color("white")
for i in range(8):
    tom.right(90)
    tom.forward((1 / 12) * graphic_size)
    tom.left(90)
    tom.forward((178.5 / 252) * graphic_size)
    tom.pendown()
    gap(graphic_size)
    tom.penup()
    tom.home()
    tom.left((1 + i) * 45)
tom.penup()
tom.goto(200,-200)
tom.pendown()
tom.pencolor("black")
tom.write('Calen Heller',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing