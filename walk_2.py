import turtle as t
import random


tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180,270]
tim.pensize(10)
tim.speed("slow")
for _ in range(300):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))
