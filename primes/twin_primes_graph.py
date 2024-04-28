import argparse
import matplotlib.pyplot as plt
import numpy as np


# global list of twin primes
tps = \
[(3,5), (5,7), (11,13), (17,19), (29,31), (41,43), (59,61), (71,73), (101, 103), (107, 109), 
 (137, 139), (149, 151), (179, 181), (191, 193), (197, 199), (227, 229), (239, 241), (269, 271), (281, 283), (311, 313),
 (347, 349), (419, 421), (431, 433), (461, 463), (521, 523), (569, 571), (599, 601), (617, 619), (641, 643), (659, 661),
 (809, 811), (821, 823), (827, 829), (857, 859), (881, 883), (1019, 1021)]


def produce_image(params):
    size = tuple(params['size'])
    background = params['background']
    cmap_name = params['cmap']
    filename = params['filename']
    show = params['show']
    
    # list of linearly spaced points being applied to function to for a line
    x = np.linspace(-20,20,100)
    y = abs((6*x)+1)
    
    # inital graph setup
    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.axis('off')
    
    # plot the intial function |6x+1|
    plt.plot(x,y, 'r')
    
    # set the new length of the line
    x = np.linspace(-20,200000, 200000)
    
    # set the color of the graph
    cmap = plt.get_cmap(cmap_name)
    colors = cmap(np.linspace(0,1,len(tps)))
    
    # create the equation of each line formed by the twin primes. This is the line
    # formed by where the twin primes intersect the function |6x+1|
    for i, t in enumerate(tps):
        m = (t[0]+1)/6
        y = (x/m)+(6*m)
        plt.plot(x,y, color=colors[i])

    # optionally save and show the plot
    plt.xlim([-5, 200000])
    plt.ylim([0, 3000])
    if filename:
        plt.savefig(filename, bbox_inches='tight', pad_inches=0)

    if show:
        plt.show()
