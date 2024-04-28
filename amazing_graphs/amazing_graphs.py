import numpy as np
import matplotlib.pyplot as plt
import os
from utils import compute_primes as cp
from pathlib import Path


def forrest_fire(params):
    background = params['background']
    size = tuple(params['size'])
    save = params['save']
    colors = params['colors']
    cmap_name = params['cmap']
    show = params['show']

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

    # size = (60, 60)

    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.axis('off')

    if colors:
        plt.scatter(nx, ny, c=colors, marker='1')
    else:
        plt.scatter(nx, ny, c=nx, cmap=cmap_name, marker='1')

    if save:
        path = f"output/amazing_graphs/{params['func']}/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f'{background}_{colors if colors else cmap_name}.png'
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)
    if show:
        plt.show()


def hofstadters(params):
    background = params['background']
    size = tuple(params['size'])
    save = params['save']
    colors = params['colors']
    cmap_name = params['cmap']
    show = params['show']

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

    # size = (20, 10)

    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.axis('off')

    if colors:
        # plt.scatter(x, l, c=x, edgecolors=colors)
        plt.scatter(x, l, c=colors)
    else:
        plt.scatter(x, l, c=x, cmap=cmap_name)

    if save:
        path = f"output/amazing_graphs/{params['func']}/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f'{background}_{colors if colors else cmap_name}.png'
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)
    if show:
        plt.show()


def primes(params):
    background = params['background']
    size = tuple(params['size'])
    save = params['save']
    colors = params['colors']
    cmap_name = params['cmap']
    show = params['show']

    prime_vals = cp.primesfrom2to(250000)

    vals = []
    for p in prime_vals:
        b = bin(p)[2:]
        rb = b[::-1]
        irb = int(rb, 2)
        val = p - irb
        vals.append(val)

    x = range(len(vals))
    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.axis('off')

    if colors:
        plt.scatter(x, vals, c=colors)
        # plt.scatter(x, vals, c=x, edgecolors=colors)
    else:
        plt.scatter(x, vals, c=x, cmap=cmap_name)

    if save:
        path = f"output/amazing_graphs/{params['func']}/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f'{background}_{colors if colors else cmap_name}.png'
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)
    if show:
        plt.show()


def remy(params):
    background = params['background']
    size = tuple(params['size'])
    save = params['save']
    colors = params['colors']
    cmap_name = params['cmap']
    show = params['show']

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
    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.axis('off')

    if colors:
        plt.scatter(x, l, c=colors)
    else:
        plt.scatter(x, l, c=x, cmap=cmap_name, marker='.')

    if save:
        path = f"output/amazing_graphs/{params['func']}/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f'{background}_{colors if colors else cmap_name}.png'
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)
    if show:
        plt.show()


def produce_image(params):

    if params['func'] == 'hofstadters':
        hofstadters(params)
    elif params['func'] == 'forrest_fire':
        forrest_fire(params)
    elif params['func'] == 'primes':
        primes(params)
    elif params['func'] == 'remy':
        remy(params)
