import turtle
from random import *
import math

def main():
    t = turtle.Turtle()
    t.ht()

    amount = 5
    length = 500

    dict_of_points = make_points(amount, length)
    draw_boundaries(t, length)
    for _ in range(500):
        move_points(t, dict_of_points, length)

    turtle.exitonclick()

class Point:
    def __init__(self, x, y, speed_x, speed_y, color):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color

    # def move(self):
    #     speed_x = self.speed * math.cos(self.angle)
    #     speed_y = self.speed * math.sin(self.angle)

    #     self.x += speed_x
    #     self.y += speed_y

def make_points(amount, length):
    colors = ['green', 'red', 'blue', 'purple', 'orange', 'yellow']

    dict_of_points = {}
    for i in range(amount):
        p = Point(randint(-(length // 2 - 10), (length // 2 - 10)), randint(-(length // 2 - 10), (length // 2 - 10)), randint(1, 10), randint(1, 10), colors[randint(0, len(colors) - 1)])

        dict_of_points[f'p{i}'] = {}
        dict_of_points[f'p{i}']['x'] = p.x
        dict_of_points[f'p{i}']['y'] = p.y
        dict_of_points[f'p{i}']['speed_x'] = p.speed_x
        dict_of_points[f'p{i}']['speed_y'] = p.speed_y
        dict_of_points[f'p{i}']['color'] = p.color

    return dict_of_points

def draw_boundaries(t, length):
    turtle.tracer(1, 0)
    t.penup()
    t.goto(-length / 2, length / 2)
    t.pendown()
    draw_square(t, length)

def draw_square(t, side_length):
    for _ in range(4):
        t.fd(side_length)
        t.right(90)

def move_points(t, points, length):
    turtle.tracer(10, 0)

    for point in points:
        p = points[point]

        t.color(p['color'])

        x = p['x']
        y = p['y']
        speed_x = p['speed_x']
        speed_y = p['speed_y']

        t.penup()
        t.goto(x, y)
        t.pendown()
        t.circle(5)

        if (abs(x + speed_x + 5) >= (length / 2)):
            speed_x = -speed_x
        if (abs(y + speed_y + 5) >= (length / 2)):
            speed_y = -speed_y

        x += speed_x
        y += speed_y

        p['x'] = x
        p['y'] = y
        p['speed_x'] = speed_x
        p['speed_y'] = speed_y

main()
