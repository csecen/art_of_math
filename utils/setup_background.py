import turtle

def setup_background(size, bg, starting_point):
    '''
    Used to set the background for the different images. Drawing the background
    color in is necessary for the color to appear in the saved images.
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