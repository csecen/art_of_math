import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def f(x):
    if x < 0:
        firstpart = (abs(x) ** (2 / 3))
    else:
        firstpart = x ** (2 / 3)

    xsquared = x ** 2
    inner = 3.3 - xsquared
    outer = 0.9 * np.sqrt(inner)

    sininner = 15 * np.pi * x
    sinval = np.sin(sininner)

    val = firstpart + (outer * sinval)
    return val


def produce_image(params):

    size = tuple(params['size'])
    background = params['background']
    save = params['save']
    show = params['show']
    color = params['color']
    graph = params['graph']
    font_color = params['font_color']

    if graph == 'clover':
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        fig.set_size_inches(size)
        fig.patch.set_visible(True)
        fig.patch.set_facecolor(background)   # wheat
        ax.grid(False)

        theta = np.arange(0, 2 * np.pi, .01)[1:]
        r = np.sin(2 * theta) + (1 / 4) * np.sin(6 * theta)
        r2 = (np.sin(2 * theta) + (1 / 4) * np.sin(6 * theta)) / 2

        # change negative r values to positive, rotating theta by 180º
        theta = np.where(r >= 0, theta, theta + np.pi)
        r = np.abs(r)
        ax.plot(theta, r, c=color)
        plt.fill_between(theta, 0, r, color=color)

        theta = np.where(r2 >= 0, theta, theta + np.pi)
        r2 = np.abs(r2)
        ax.plot(theta, r2, c=color)
        plt.fill_between(theta, 0, r2, color='w', alpha=0.2)

        ax.set_title(r'$r = \sin(2\theta) + \frac{1}{4}\sin(6\theta)$', math_fontfamily='stix', fontsize=70, color=font_color, y=1.0, pad=-1700)
        ax.axis('off')

    else:
        xs = np.linspace(0, 1.81, 10000)
        ys = np.array([f(x) for x in xs])

        nxs = np.linspace(-1.81, 0, 10000)
        nys = np.array([f(x) for x in nxs])

        x = np.concatenate((nxs, xs), axis=None)
        y = np.concatenate((nys, ys), axis=None)

        fig, ax = plt.subplots()
        fig.set_size_inches(size)
        fig.patch.set_facecolor(background)
        ax.grid(False)
        plt.plot(x, y, c=color, linewidth=5)
        ax.axis('off')
        ax.set_xlim(-3, 3)
        ax.set_ylim(-2, 3)
        ax.set_title(r'$x^{\frac{2}{3}} + 0.9(3.3 - x^{2})^{\frac{1}{2}} * \sin(\alpha \pi x)$', math_fontfamily='stix', fontsize=70, color=font_color, y=1.0, pad=-1700)

    if save:
        path = f"output/equation_graphs/{params['graph']}/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f'{background}_{color}.png'
        plt.savefig(filename, bbox_inches='tight', pad_inches=1, dpi=400)

    if show:
        plt.show()
