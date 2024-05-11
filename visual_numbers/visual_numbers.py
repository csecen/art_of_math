from mpmath import mp
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from pathlib import Path


def transforms(x, deg=65):
    seq = [0]
    val = [0]
    rad = 0

    for i in range(1, len(x)):
        even = (deg * x[i]) * (np.pi / 180)
        rad = rad + even
        seq.append(seq[i - 1] + np.sin(rad))
        val.append(val[i - 1] + np.cos(rad))
    return val, seq


def produce_image(params):
    n = params['n']
    background = params['background']
    size = tuple(params['size'])
    save = params['save']
    color = params['color']
    show = params['show']
    theta = params['theta']
    constant = params['constant']
    gradient = params['gradient']
    label = params['label']

    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.grid(False)

    mp.dps = n  # set number of digits

    if constant == 'e':
        number = mp.e
        title = 'E'
    elif constant == 'pi':
        number = mp.pi
        title = 'PI'
    elif constant == 'phi':
        number = mp.phi
        title = 'PHI'
    elif constant == 'euler':
        number = mp.euler
        title = 'EULER'

    num_str = str(number)
    num_str = num_str.replace('.', '')

    int_n = [int(n) for n in num_str]
    x, y = transforms(int_n, theta)
    ax.plot(x, y, c=color, linewidth=1.0)

    if gradient:
        am = np.argmax(np.array([abs(plt.xlim()[0] - plt.xlim()[1]), abs(plt.ylim()[0] - plt.ylim()[1])]))
        if am == 0:
            diff = abs(plt.xlim()[0] - plt.xlim()[1]) - abs(plt.ylim()[0] - plt.ylim()[1])
            hdiff = diff / 2
            plotlim = plt.xlim() + (plt.ylim()[0] - hdiff, plt.ylim()[1] + hdiff)

        else:
            diff = abs(plt.ylim()[0] - plt.ylim()[1]) - abs(plt.xlim()[0] - plt.xlim()[1])
            hdiff = diff / 2
            plotlim = (plt.xlim()[0] - hdiff, plt.xlim()[1] + hdiff) + plt.ylim()

        ax.imshow([[0, 0], [1, 1]], cmap=cm.get_cmap(gradient), interpolation='bicubic', extent=plotlim, aspect='equal')

    ax.axis('off')
    if label:
        ax.set_title(r'$\mathbb{%s}$' %(str(title)), fontsize=70, color="white", y=1.0, pad=-20)
    
    if save:
        path = f"output/visual_numbers/{constant}/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f'{gradient if gradient else background}_{color}_theta{theta}_n{n}{"_label" if label else ""}.png'
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)
    if show:
        plt.show()
