import numpy as np
import matplotlib.pyplot as plt


def produce_image(params):

    background = params['background']
    size = tuple(params['size'])
    filename = params['filename']
    colors = params['colors']
    show = params['show']

    if len(colors) == 3:
        c1 = colors[0]
        c2 = colors[1]
        c3 = colors[2]
    elif len(colors) == 1:
        c1 = colors[0]
        c2 = colors[0]
        c3 = colors[0]

    left, width = 0.1, 0.9
    rect1 = [left, 0.7, width, 0.3]  # left, bottom, width, height
    rect2 = [left, 0.4, width, 0.3]
    rect3 = [left, 0.1, width, 0.3]

    fig = plt.figure(figsize=size)
    fig.set_size_inches(size)
    fig.patch.set_facecolor(background)

    ax1 = fig.add_axes(rect1)
    ax2 = fig.add_axes(rect2, sharex=ax1)
    ax3 = fig.add_axes(rect3, sharex=ax1)

    # TODO: make the functions variable
    x = np.linspace(0, 6.5 * np.pi, 200)
    y1 = np.sin(x)
    y2 = np.sin(2 * x)

    ax1.plot(x, y1, color=c1, lw=2)
    ax2.plot(x, y2, color=c2, lw=2)
    ax3.plot(x, y1 + y2, color=c3, lw=2)

    for ax in [ax1, ax2, ax3]:
        for key in ['right', 'top', 'bottom']:
            ax.spines[key].set_visible(False)

    plt.xlim(0, 6.6 * np.pi)
    ax1.axis('off')
    ax2.axis('off')
    ax3.axis('off')

    if filename:
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)

    if show:
        plt.show()
    