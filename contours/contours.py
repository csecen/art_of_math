import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def a(x, y):
    return np.sin(x)**8 + np.cos(20+y*x) * np.cos(y)

def b(x, y):
    return np.sin(x) + np.cos(y*x) * np.cos(y)

def c(x, y):
    return np.cos(y)**8 + np.cos(20+x*y) * np.tan(x/60)

def d(x, y):
    return np.cos(x)*np.sin(y)

def e(x, y):
    return np.cos(x*np.pi) + np.sin(2*y*x)

def produce_image(params):
    size = tuple(params['size'])
    background = params['background']
    cmap_name = params['cmap_name']
    save = params['save']
    show = params['show']
    fill = params['fill']
    func = params['func']
    num = params['num']

    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.axis('off')

    x = np.linspace(0, num, 500)
    y = np.linspace(0, num, 500)

    X, Y = np.meshgrid(x, y)

    functions = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e}

    Z = functions[func](X, Y)

    if fill:
        plt.contourf(X, Y, Z, cmap=cmap_name)
    else:
        plt.contour(X, Y, Z, cmap=cmap_name)

    if save:
        path = f"output/contours/{params['func']}/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f"{background.replace('#','')}_{cmap_name}.png"
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)

    if show:
        plt.show()
        