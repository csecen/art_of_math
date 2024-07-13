import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import cm
from utils import compute_primes as cp
from pathlib import Path


def forrest_fire(params):
    if os.path.exists('/home/connor/Projects/art_of_math/amazing_graphs/forest_fire.txt'):
        with open('/home/connor/Projects/art_of_math/amazing_graphs/forest_fire.txt', 'r') as f:
            data = f.readlines()
        y = [int(d) for d in data]
    else:
        y = []
        x = np.arange(100000)

        for n in x:
            i, j, b = 1, 1, set()

            while n - 2 * i >= 0:
                b.add(2 * y[n - i] - y[n - 2 * i])
                i += 1

                while j in b:
                    b.remove(j)
                    j += 1

            y.append(j)

        y = np.array(y)

        with open('forest_fire.txt', 'w') as file:
            file.write('\n'.join(str(v) for v in y))

    y = np.array(y)
    x = np.arange(100000)
    nx = np.random.choice(x, int(len(x) * 1), replace=False)
    ny = y[nx]

    return nx, ny

def hofstadters(params):
    l = []
    x = range(1, 10000001)

    for i, n in enumerate(x):
        if n == 1 or n == 2:
            l.append(1)
        else:
            fIdx = n - 1
            fInner = l[fIdx - 1]
            first = l[fInner - 1]

            sIdx = n - 2
            sInner = l[sIdx - 1]
            tInner = n - sInner - 1
            second = l[tInner - 1]
            val = first + second
            l.append(val)

    return x, l

def primes(params):
    prime_vals = cp.primesfrom2to(250000)

    vals = []
    for p in prime_vals:
        b = bin(p)[2:]
        rb = b[::-1]
        irb = int(rb, 2)
        val = p - irb
        vals.append(val)

    x = range(len(vals))

    return x, vals

def remy(params):
    n = 10000
    l = []
    g = n * [0]
    for i in range(1, n + 1):
        a = 0
        while g[a] & i:
            a += 1
        g[a] += i
        l.append(a)

    x = range(len(l))

    return x, l

def produce_image(params):
    background = params['background']
    size = tuple(params['size'])
    save = params['save']
    color = params['colors']
    cmap_name = params['cmap_name']
    show = params['show']
    marker = params['marker']
    gradient = params['gradient']

    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.axis('off')

    if params['func'] == 'hofstadters':
        x, y = hofstadters(params)
    elif params['func'] == 'forrest_fire':
        x, y = forrest_fire(params)
    elif params['func'] == 'primes':
        x, y = primes(params)
    elif params['func'] == 'remy':
        x, y = remy(params)

    if colors:
        plt.scatter(x, y, c=color, marker=marker)
    else:
        plt.scatter(x, y, c=x, cmap=cmap_name, marker=marker)

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

    if save:
        path = f"output/amazing_graphs/{params['func']}/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f"{gradient if gradient else background.replace('#','')}_{color.replace('#','') if color else cmap_name}.png"
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)
    if show:
        plt.show()
