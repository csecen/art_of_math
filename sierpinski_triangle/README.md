### Sierpinski Triangle

##### The Sierpinski Triangle is a famous example of a fractal recursizely made of equilateral triangles. More information can be found [here](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle).

##### The goal of this application is to visualize a Sierpinski triangle. Running the code is fairly simple:
1) Import the code using <code>from sierpinski_triangle import Sierpinski_triangle</code>
2) Create an instance sierpinski triangle code <code>st = Sierpinski_triangle(length, depth)</code>. 
    - The length argument is the length of the base of the triangle in pixels.
    - The depth argument is the recursize depth of the triangle.
3) Run the code <code>st.draw_sierpinski(bg, lc, size, starting_point, filename)</code>
    - The bg argument is the background color supplied to the turtle module.
    - The lc argument is the line color supplied to the turtle module.
    - The size argument is the size of the visualization.
    - The starting_point argument is where the visualization will start on the screen.
    - The filename argument is optional. If supplied it saves the file as a JPG with the given filename.

##### The following code will produce the image below:

    from sierpinski_triangle import Sierpinski_triangle
    st = Sierpinski_triangle(850, 7)
    bg = (212, 166, 83)
    lc = 'black'
    size = (1200, 1000)
    starting_point = (-425, -275)
    filename = 'seirpinski_triangle'
    st.draw_sierpinski(bg, lc, size, starting_point, filename)

![Sierpinski triangle example visualization](./images/sierpinski_triangle.jpg)
