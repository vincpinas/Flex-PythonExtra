import turtle
from random import randint

window = turtle.Screen() # open een nieuw turtle window
turtle.bgcolor("black")
turtle.color("yellow" , "white")
turtle.speed(0)

def draw_star():
    turns = 5
    turtle.begin_fill()
    while turns > 0:
        turtle.forward(25)
        turtle.left(145)
        turns = turns - 1
    turtle.end_fill()

    
num_stars = 0
while num_stars < 20:
    x = randint(-300, 300)
    y = randint(-300, 300)
    draw_star()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    num_stars = num_stars + 1
