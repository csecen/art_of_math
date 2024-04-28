import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from pathlib import Path


def produce_image(params):

    # parse input parameters
    s = params['s']
    size = tuple(params['size'])
    background = params['background']
    cmap_name = params['cmap_name']
    save = params['save']
    show = params['show']
    title_color = params['title_color']
    title_size = params["title_size"]

    fig, ax = plt.subplots()
    fig.set_size_inches(size)
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(background)
    ax.grid(False)
    vls = [-10, -5, 0, 5, 10]
    plt.vlines(x=vls, ymin=-15, ymax=15)

    x = 4
    y = 0

    c = 0

    thetas = np.random.randint(361, size=s)

    if isinstance(cmap_name, list):
        top = cm.get_cmap(cmap_name[0], s // 2)
        bottom = cm.get_cmap(cmap_name[1], s // 2)

        cmap = np.vstack((top(np.linspace(0, 1, s // 2)),
                          bottom(np.linspace(0, 1, s // 2))))

        color_name = '_'.join(cmap_name)
    else:
        cmap = cm.get_cmap(cmap_name, 1000)
        cmap_vals = np.linspace(0, 1, s)
        color_name = cmap_name

    for idx, theta in enumerate(thetas):
        nx = x * np.cos(np.deg2rad(theta)) - y * np.sin(np.deg2rad(theta))
        ny = x * np.sin(np.deg2rad(theta)) + y * np.cos(np.deg2rad(theta))

        xt = np.random.uniform(low=-11, high=11)
        yt = np.random.uniform(low=-11, high=11)

        if isinstance(cmap_name, list):
            plt.plot([xt, nx + xt], [yt, ny + yt], c=cmap[idx])
        else:
            plt.plot([xt, nx + xt], [yt, ny + yt], c=cmap(cmap_vals[idx]))

        for l in vls:
            if min(xt, nx + xt) <= l <= max(xt, nx + xt):
                c += 1

    pi = (2 * 4 * s) / (c * 5)

    ax.axis('off')
    ax.set_title(r'$\pi \approx %s$' %(str(pi)), math_fontfamily='stix', fontsize=title_size, color=title_color)
    
    if save:
        path = f"output/pi_sticks/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f'{background}_{color_name}.png'
        plt.savefig(filename, bbox_inches='tight', pad_inches=1, dpi=400)

    if show:
        plt.show()
