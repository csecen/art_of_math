import matplotlib.pyplot as plt
from utils import compute_primes as cp
from pathlib import Path


def produce_image(params):
    n = params['n']
    size = tuple(params['size'])
    background = params['background']
    cmap_name = params['cmap']
    color = params['color']
    save = params['save']
    show = params['show']
    
    primes = cp.primesfrom2to(n)
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    fig.set_size_inches(size)
    fig.patch.set_facecolor(background)
    ax.grid(False)
    if color:
        plt.scatter(primes, primes, c=color)
    else:
        ax.scatter(primes, primes, c=primes, cmap=cmap_name)

    ax.axis('off')
    
    if save:
        path = f"output/primes/polar/{params['size'][0]}x{params['size'][1]}/"
        Path(path).mkdir(parents=True, exist_ok=True)

        filename = path + f"{background}_{cmap_name if cmap_name else color}.png"
        plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=400)

    if show:
        plt.show()
