import turtle
import os
from PIL import Image


class Sierpinski_triangle:
    def __init__(self, length, depth):
        '''
        Initialize the length and the depth of the triangle.
        '''
        self.length = length
        self.depth = depth
        
        
    def build_sierpinski(self, depth, length):
        '''
        Recursively draw the sierpinski triangle. When the depth is 0, draw a
        single triangle. Otherwise, follow the rules of the sierpinski
        triangle to complete the rest.
        '''
        if depth == 0:
            for _ in range(3):
                turtle.forward(length)
                turtle.left(120)
        else:
            # draw bottom left subtriangle of the triangle at the current depth
            self.build_sierpinski(depth-1, length/2)
            turtle.forward(length/2)
            # draw bottom right subtriangle of the triangle at the current depth
            self.build_sierpinski(depth-1, length/2)
            turtle.left(120)
            turtle.forward(length/2)
            turtle.right(120)
            # draw top subtriangle of the triangle at the current depth
            self.build_sierpinski(depth-1, length/2)
            turtle.right(120)
            turtle.forward(length/2)
            turtle.left(120)


    def draw_sierpinski(self, bg, lc, size, starting_point, filename=None):
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

        turtle.pu()
        turtle.goto(starting_point)
        turtle.setheading(heading)
        turtle.pd()
        turtle.pencolor(lc)

        self.build_sierpinski(self.depth, self.length)

        turtle.update()

        if filename:
            turtle.getscreen().getcanvas().postscript(file= filename+'.eps', colormode='color')
            img = Image.open(filename + '.eps') 
            img.save(filename + '.jpg')
            img.close()
            os.remove(f'{filename}.eps')

        turtle.done()
        