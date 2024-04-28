import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from pathlib import Path


def collatz(n):
    if n == 1:
        return [n]
    elif n % 2 == 0:
        return collatz(n // 2) + [n]
    elif n % 2 == 1:
        return collatz((3 * n) + 1) + [n]


def color_picker():
    return np.random.choice(['#FF5E02', 'red', 'blue', '#6400FF', '#E10060', '#02D1FF'])


def transforms(x, et=-5, ot=7.5):
    seq = [0]
    val = [0]
    rad = 0

    even = et * (np.pi / 180)
    odd = ot * (np.pi / 180)

    for i in range(1, len(x)):
        if x[i] % 2 == 0:
            seq.append(seq[i - 1] + np.sin(rad + even))
            rad = rad + even
        else:
            seq.append(seq[i - 1] + np.sin(rad + odd))
            rad = rad + odd
        val.append(val[i - 1] + np.cos(rad))
    return val, seq


def collatz_drawn(params):
    n = params['n']
    background = params['background']
    size = tuple(params['size'])
    save = params['save']
    colors = params['colors']
    cmap_name = params['cmap']
    show = params['show']
    thetas = params['thetas']
    gradient = params['gradient']

    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.grid(False)

    runs = n

    if cmap_name:
        cmap = cm.get_cmap(cmap_name, runs)
        cmap_vals = np.linspace(0, 1, runs)

    for i in range(1, runs):
        length = collatz(i)
        x, y = transforms(np.array(length), thetas[0], thetas[1])
        if cmap_name:
            ax.plot(x, y, alpha=0.15, c=cmap(cmap_vals[i]))
        else:
            ax.plot(x, y, alpha=0.15, c=np.random.choice(colors))

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

        ax.imshow([[0, 0], [1, 1]], cmap=cm.get_cmap(gradient), interpolation='bicubic', extent=plotlim)#, aspect='equal')

    ax.axis('off')

    if save:
        path = f"output/collatz/{params['func']}/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f'{gradient if gradient else background}_{colors if colors else cmap_name}_{thetas[0]}_{thetas[1]}.png'
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)
    if show:
        plt.show()


def collatz_escape(params):
    n = params['n']
    size = tuple(params['size'])
    save = params['save']
    cmap_name = params['cmap']
    show = params['show']
    escape = params['escape']
    x = tuple(params['x'])
    y = tuple(params['y'])

    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    ax.grid(False)

    x = np.linspace(x[0], x[1], x[2])
    y = np.linspace(y[0], y[1], y[2])

    z = x + 1.0j * y.reshape(-1, 1)
    image = np.zeros((len(x), len(y)), dtype='int')
    mask = np.full(image.shape, True)
    for i in range(n):
        z[mask] = (2 + 7*abs(z[mask]) - (2 + 5*abs(z[mask]))*np.cos(np.pi*abs(z[mask])))/4;
        mask = abs(z) < escape
        image += mask

    ax.axis('off')
    plt.imshow(image, aspect='equal', cmap=cmap_name, origin='lower',
               extent=(x[0], x[-1], y[0], y[-1]))

    if save:
        path = f"output/collatz/{params['func']}/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f'{cmap_name}_{escape}.png'
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)
    if show:
        plt.show()


def produce_image(params):

    if params['func'] == 'draw':
        collatz_drawn(params)
    elif params['func'] == 'escape':
        collatz_escape(params)



