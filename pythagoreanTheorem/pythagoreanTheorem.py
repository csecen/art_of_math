import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def produce_image(params):

    # parse the parameters
    background = params['background']
    orientation = params['orientation']
    size = tuple(params['size'])
    filename = params['filename']
    colors = params['colors']
    show = params['show']

    coors = {
        '6810_upright': {'xy': [(10, 1), (2, 7), (10, 15)], 'width': [6, 8, 10], 'height': [6, 8, 10],
                         'angle': [0, 0, -53]},
        '6810_sideways': {'xy': [(10, 11), (20, 11), (10, 1)], 'width': [6, 8, 10], 'height': [6, 8, 10],
                          'angle': [53, 53, 0]},
        '51213_upsidedown': {'xy': [(14, 19), (2, 7), (19, 19)], 'width': [5, 12, 13], 'height': [5, 12, 13],
                             'angle': [0, 0, -112.55]},
        '51213_backwards': {'xy': [(10, 14), (23, 14), (10, 1)], 'width': [12, 5, 13], 'height': [12, 5, 13],
                            'angle': [22.6, 22.6, 0]},
        '51213_upright': {'xy': [(5, 13), (10, 1), (10, 18)], 'width': [5, 12, 13], 'height': [5, 12, 13],
                          'angle': [0, 0, -22.6]}
    }

    # define Matplotlib figure and axis
    fig, ax = plt.subplots()
    fig.set_size_inches(size)

    # create simple line plot
    ax.plot([1, 1], [2, 2])

    coor = coors[orientation]

    # add rectangle to plot
    ax.add_patch(Rectangle(coor['xy'][0], coor['width'][0], coor['height'][0], color='skyblue',
                           angle=coor['angle'][0]))
    ax.add_patch(Rectangle(coor['xy'][1], coor['width'][1], coor['height'][1], color='midnightblue',
                           angle=coor['angle'][1]))
    ax.add_patch(Rectangle(coor['xy'][2], coor['width'][2], coor['height'][2], color='deepskyblue',
                           angle=coor['angle'][2]))

    # set figure parameters
    plt.gca().set_aspect('equal', adjustable='box')
    fig.patch.set_facecolor(background)
    ax.axis('off')

    # display plot
    if filename:
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)

    if show:
        plt.show()
