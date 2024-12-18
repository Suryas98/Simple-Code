import colorsys
import turtle
screen = turtle.Screen()
screen.bgcolor('black')
t=turtle.Turtle()
t.speed(100)
t.hideturtle()
num_colors = 36
steps = 460
side_length = 300
angle = 145
hue =0
for i in range(steps):
    color = colorsys.hsv_to_rgb(hue, 1, 0.8)
    hue +=1 / num_colors
    t.color(color)
    t.left(angle)
    for _ in range(5):
        t.forward(side_length)
        t.left(150)
turtle.done()
