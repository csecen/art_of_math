import turtle
import os
from PIL import Image
import sys
sys.path.insert(1, '../utils/')
from setup_background import setup_background


class Sierpinski_triangle:
    '''
    This class is used to draw a normal Sierpinski triangle using the turtle
    module.
    '''
    
    def __init__(self, length: int, depth: int):
        '''
        Initialize the length and the depth of the triangle.
        
        Parameters:
            length --> length of the base of the triangle in pixels
            depth  --> the recursize depth of the sierpinski triangle
        '''
        self.length = length
        self.depth = depth
        
        
    def build_sierpinski(self, depth: int, length: int):
        '''
        Recursively draw the sierpinski triangle. When the depth is 0, draw a
        single triangle. Otherwise, follow the rules of the sierpinski
        triangle to complete the rest.
        
        Parameters:
            depth  --> the recursize depth of the sierpinski triangle
            length --> length of the base of the triangle in pixels
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
        Set the background of the image and draw the triangle according to the
        parameters passed in by the user. Optionally saves the image to a file.
        
        Parameters:
            bg             --> background color of image
            lc             --> line color of image
            size           --> size of the image
            starting_point --> starting point of the image
            filename       --> Optional: filename of the image file. If not
                               provided, image will not be saved.
        '''
        setup_background(size, bg, starting_point)
        turtle.pencolor(lc)

        self.build_sierpinski(self.depth, self.length)

        turtle.update()

        if filename:
            turtle.getscreen().getcanvas().postscript(file= filename+'.eps', colormode='color')
            img = Image.open(filename + '.eps') 
            if not os.path.exists('./images'): os.makedirs('./images')
            img.save(f'images/{filename}.jpg')
            img.close()
            os.remove(f'{filename}.eps')

        turtle.done()
        