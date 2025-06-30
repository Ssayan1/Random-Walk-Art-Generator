import turtle as t
import random


tim = t.Turtle()
tim.shape("turtle")
color = ["blue","cornflower blue","light blue","lawn green","yellow","red","black","violet","pink"]
direction = [0, 90, 180,270]
tim.pensize(10)
tim.speed(0)
for _ in range(1000):
    tim.color(random.choice(color))
    tim.forward(30)
    tim.setheading(random.choice(direction))
