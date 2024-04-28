import os
import turtle
from PIL import Image
# import sys
# sys.path.insert(1, '../utils/')
from utils import setup_background

class Number:
    def __init__(self, value):
        '''
        Initialize the root node of the tree and build the tree out for the
        numbers specified by the user.
        
        Parameter:
            value --> the number that will be drawn
        '''
        self.number = value

        
    def trace_number(self, length):
        '''
        Converts the number to a string of only the digits specified. The 
        method then draws the number, multiplying the current digit by 60
        degrees for the turns.
        
        Parameters:
            length --> length of the forward movement of the pen
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
        
        Parameters:
            bg             --> background color of image
            lc             --> line color of image
            length         --> length of the forward movement of the pen
            size           --> size of the image
            starting_point --> starting point of the image
            filename       --> Optional: filename of the image file. If not
                               provided, image will not be saved.
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
            if not os.path.exists('./images'): os.makedirs('./images')
            img.save(f'images/{filename}.jpg')
            img.close()
            os.remove(f'{filename}.eps')

        turtle.done()