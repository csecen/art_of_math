import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def produce_image(params):

    # parse input parameters
    n = params['n']
    size = tuple(params['size'])
    background = params['background']
    cmap_name = params['cmap_name']
    color = params['color']
    save = params['save']
    show = params['show']
    scale_perc = params['scale_perc']
    translate_amt = params['translate_amt']
    theta = params['theta']
    vary_size = params['vary_size']
    graph_type = ''

    # generate random coordinate data
    xs = np.random.uniform(low=-10, high=10, size=n)
    ys = np.random.uniform(low=-10, high=10, size=n)

    if vary_size:
        graph_type += "vary_size"
        s = np.random.uniform(low=5, high=20, size=n)
    else:
        s = 10

    # create plot object
    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.grid(False)

    nxs = np.array(xs, copy=True)
    nys = np.array(ys, copy=True)

    if scale_perc:
        graph_type += "scale"
        nxs = nxs*scale_perc
        nys = nys*scale_perc

    if translate_amt:
        graph_type += "translate"
        nxs = nxs+translate_amt
        nys = nys+translate_amt

    if theta:
        graph_type += "rotate"
        nxs = nxs * np.cos(np.deg2rad(theta)) - nys * np.sin(np.deg2rad(theta))
        nys = nxs * np.sin(np.deg2rad(theta)) + nys * np.cos(np.deg2rad(theta))

    if scale_perc and translate_amt and theta:
        graph_type = "all"

    if color:
        plt.scatter(xs, ys, c=color, s=s)
        plt.scatter(nxs, nys, c=color, s=s)
    else:
        plt.scatter(xs, ys, c=xs, cmap=cmap_name, s=s)
        plt.scatter(nxs, nys, c=ys, cmap=cmap_name, s=s)

    ax.axis('off')

    if save:
        path = f"output/rotation_plots/{graph_type}/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f'{background}_{cmap_name if cmap_name else color}.png'
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)

    if show:
        plt.show()
