import numpy as np
import matplotlib.pyplot as plt
from utils import compute_primes as cp
from functools import reduce
from pathlib import Path


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def produce_image(params):

    n = params['n']
    size = tuple(params['size'])
    background = params['background']
    cmap_name = params['cmap_name']
    colors = params['colors']
    save = params['save']
    show = params['show']
    primes_only = params['primes_only']

    up = False
    down = False
    left = False
    right = True
    hor = temp_hor = 1
    ver = temp_ver = 1

    x = y = 0
    primes = set(cp.primesfrom2to(n))
    data = np.zeros((n, 4))

    for i in range(n):

        data[i][0] = x
        data[i][1] = y

        if (i+1) in primes:
            data[i][2] = 1
            data[i][3] = 5
        else:
            data[i][2] = 0
            data[i][3] = .5*len(factors(i+1))

        if right:
            x += 1
            hor -= 1
            if hor == 0:
                temp_hor += 1
                hor = temp_hor
                up = True
                right = False
        elif up:
            y += 1
            ver -= 1
            if ver == 0:
                temp_ver += 1
                ver = temp_ver
                left = True
                up = False
        elif left:
            x -= 1
            hor -= 1
            if hor == 0:
                temp_hor += 1
                hor = temp_hor
                down = True
                left = False
        elif down:
            y -= 1
            ver -= 1
            if ver == 0:
                temp_ver += 1
                ver = temp_ver
                right = True
                down = False

    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.grid(False)

    if primes_only:
        mask = data[:, 2] == 1
        if colors:
            plt.scatter(data[mask, 0], data[mask, 1], c=colors, s=data[mask, 3])
        else:
            plt.scatter(data[mask, 0], data[mask, 1], c=data[mask, 0], s=data[mask, 3], cmap=cmap_name)
    else:
        if colors:
            mask = data[:, 2] == 0
            plt.scatter(data[mask, 0], data[mask, 1], c=colors[0], s=data[mask, 3])
            plt.scatter(data[~mask, 0], data[~mask, 1], c=colors[1], s=data[~mask, 3])
        else:
            plt.scatter(data[:, 0], data[:, 1], c=data[:, 2], s=data[:, 3], cmap=cmap_name)

    ax.axis('off')

    if save:
        path = f"output/primes/ulam/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f"{background}_{cmap_name if cmap_name else '_'.join(colors)}_{'primes' if primes_only else 'all'}.png"
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)

    if show:
        plt.show()
