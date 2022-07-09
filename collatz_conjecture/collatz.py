import turtle
import os
from PIL import Image
import sys
sys.path.insert(1, '../utils/')
from setup_background import setup_background
        
        
class Collatz:
    '''
    This class uses the collatz conjecture to build a tree that will be used to
    visually represent the conjecture.
    '''
    class Node:
        '''
        This class represents a node in the tree that can be formed by following
        the collatz conjecture.
        '''
        def __init__(self, value):
            self.value = value
            self.children = []
    
    
    def __init__(self, value):
        '''
        Initialize the root node of the tree and build the tree out for the
        numbers specified by the user.
        '''
        self.node = self.Node(None)
        nodes = {}
            
        for i in range(1, value):
            _ = self.collatz(self.node, i, nodes)
    
    
    def collatz(self, node, n, nodes):
        '''
        Follow the rules of the collatz conjecture to build out a tree that
        represents the numbers obtained. The collatz conjecture is simple:
        
            if the number is even, divide it by 2
            if the number is odd, multiple by 3 and add 1
            
        The conjecture states that any number chosen will eventually reach
        the terminal loop 4 --> 2 --> 1 --> 4...
        These simple rules lead to a complex tree.
        '''
        # if the node has already bee found return it so as to not
        # traverse the same path twice
        if n in nodes:
            return node, nodes[n]
        
        if n == 1:
            # set value of root node, add node to dictionary keeping track
            # of nodes already found
            node.value = 1
            nodes[1] = node
            return node, node
        else:
            new_node = self.Node(n)
            nodes[n] = new_node
            
            # even
            if n % 2 == 0:
                root, ret_node = self.collatz(node, int(n/2), nodes)
            # odd
            elif n % 2 == 1:
                root, ret_node = self.collatz(node, (3*n)+1, nodes)
                
            ret_node.children.append(new_node)
            return root, new_node
            
            
    def draw_collatz(self, tree, tab):
        '''
        Using the python turtle module, this method draws the collatz 
        conjecture for the numbers that were already calculated.
        '''
        pos = turtle.pos()   # save position in case of branching
        heading = turtle.heading()   # save heading in case of branching
        # if the current value is even turn slightly to the right, otherwise
        # turn slightly to the left
        if tree.value % 2 == 0:
            turtle.right(5)
        else:
            turtle.left(5)
        turtle.forward(5)

        if len(tree.children) == 0:
            return
        else:
            for child in tree.children:
                self.draw_collatz(child, tab)
                # reset the starting position after a branching occured
                turtle.pu()
                turtle.goto(pos)
                turtle.seth(heading)
                turtle.pd()
            return
        
        
    def set_turtle(self, bg, lc, size, starting_point, filename=None):
        '''
        Set the background of the image and draw the collatz conjecture
        according to the parameters passed in by the user. Optionally 
        saves the image to a file.
        '''
        setup_background(size, bg, starting_point)
        turtle.pencolor(lc)
        self.draw_collatz(self.node, '')

        turtle.update()
        
        if filename:
            turtle.getscreen().getcanvas().postscript(file= filename+'.eps', colormode='color')
            img = Image.open(filename + '.eps') 
            img.save(filename + '.jpg')
            img.close()
            os.remove(f'{filename}.eps')
            
        turtle.done()