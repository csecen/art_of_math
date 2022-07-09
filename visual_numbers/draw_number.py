import os
import turtle
from PIL import Image
import sys
sys.path.insert(1, '../utils/')
from setup_background import setup_background

class Number:
    def __init__(self, value):
        '''
        Initialize the root node of the tree and build the tree out for the
        numbers specified by the user.
        '''
        self.number = value

        
    def trace_number(self, length):
        '''
        Converts the number to a string of only the digits specified. The 
        method then draws the number, multiplying the current digit by 60
        degrees for the turns.
        '''
        num_str = str(self.number)
        num_str = num_str.replace('.', '')
        
        for n in num_str:
            int_n = int(n)
            turtle.forward(length)
            turtle.right(60*int_n)


    def draw_number(self, bg, lc, length, size, starting_point, filename=None):
        '''
        Set the background of the image and draw the number according to the 
        parameters passed in by the user. Optionally saves the image to a file.
        '''        
        setup_background(size, bg, starting_point)
        turtle.radians()
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