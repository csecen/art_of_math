import os
import turtle
from PIL import Image

class Number:
    def __init__(self, value):
        '''
        Initialize the root node of the tree and build the tree out for the
        numbers specified by the user.
        '''
        self.number = value

        
    def trace_number(self, length):
        num_str = str(self.number)
        num_str = num_str.replace('.', '')
        
        for n in num_str:
            int_n = int(n)
            turtle.forward(length)
            turtle.right(60*int_n)


    def draw_number(self, bg, lc, length, size, starting_point, filename=None):
        '''
        Set the background of the image and initalize the setup to draw the
        visual representation of the collatz conjecture. Optionally save the
        image.
        '''
        turtle.tracer(False)
        turtle.colormode(255)
        turtle.speed(0)
        width, height = size
        turtle.setup(width=width, height=height)

        width, height = size
        heading = turtle.heading()

        turtle.hideturtle()
        turtle.pensize(1)

        turtle.pu()
        turtle.goto(-width/2-2, -height/2+3)
        turtle.fillcolor(bg)
        turtle.begin_fill()
        turtle.setheading(0)
        turtle.forward(width*2)
        turtle.setheading(90)
        turtle.forward(height*2)
        turtle.setheading(180)
        turtle.forward(width*2)
        turtle.setheading(270)
        turtle.forward(height*2)
        turtle.end_fill()

        turtle.radians()
        turtle.pu()
        turtle.goto(starting_point)
        turtle.setheading(heading)
        turtle.pd()
        turtle.pencolor(lc)
        self.trace_number(length)

        turtle.update()

        width, height = size


        if filename:
            turtle.getscreen().getcanvas().postscript(file= filename+'.eps', colormode='color', width=width, height=height)
            img = Image.open(filename + '.eps') 
            img.save(filename + '.jpg')
            img.close()
            os.remove(f'{filename}.eps')

        turtle.done()