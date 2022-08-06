import argparse
import matplotlib.pyplot as plt
import numpy as np


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

def main():
    parser = argparse.ArgumentParser(description='Procude graph depicting the twin primes.')
    parser.add_argument('prime', metavar='p', type=int,
                        help='the max number of primes to calculate up to.')
    parser.add_argument('size', metavar='s', nargs=2, type=int,
                        help='the size of the graph/image')
    parser.add_argument('background', metavar='b', type=str,
                        help='the background color of the graph/image')
    parser.add_argument('cmap', metavar='c', type=str,
                        help='the colormap used for the graph/image')
    parser.add_argument('filename', metavar='f', nargs='?', type=str,
                        help='(optional) the filename of where to save the image')
    args = parser.parse_args()
    
    n = vars(args)['prime']
    size = tuple(vars(args)['size'])
    background = vars(args)['background']
    cmap_name = vars(args)['cmap']
    filename = vars(args)['filename']
    
    primes = primesfrom2to(n)
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    fig.set_size_inches(size)
    fig.patch.set_facecolor(background)
    ax.grid(False)
    ax.scatter(primes, primes, c=primes, cmap=cmap_name)
    ax.axis('off')
    
    if filename:
        plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.show()
    
    
main()