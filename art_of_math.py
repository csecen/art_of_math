import json
import argparse
from double_pendulum import double_pendulum as dp
import ascii_art
from amazing_graphs import amazing_graphs as ag
from adding_waves import adding_waves as aw
from pythagoreanTheorem import pythagoreanTheorem as pt
from primes import polar_primes as pp
from primes import twin_primes_graph as tp
from primes import ulam_spiral as us
from rotation_plots import rotation_plots as rp
from pi_sticks import pi_sticks as ps
from contours import contours as co
from equation_graphs import equation_graphs as eq
from collatz_conjecture import collatz_conjecture as cc
from visual_numbers import visual_numbers as vn


def main():
    parser = argparse.ArgumentParser(description='Produce different depictions of a double pendulum')
    parser.add_argument('filename', help='name of config file')
    args = parser.parse_args()

    config_file = vars(args)['filename']

    with open(config_file, 'r') as f:
        config = json.load(f)

    for command in config:
        func = command['function']
        params = command['params']

        if func == 'pythagorean_theorem':
            pt.produce_image(params)
        elif func == 'double_pendulum':
            dp.produce_image(params)
        elif func == 'adding_waves':
            aw.produce_image(params)
        elif func == 'amazing_graphs':
            ag.produce_image(params)
        elif func == 'polar_primes':
            pp.produce_image(params)
        elif func == 'twin_primes':
            tp.produce_image(params)
        elif func == 'ulam_spiral':
            us.produce_image(params)
        elif func == 'rotation_plots':
            rp.produce_image(params)
        elif func == 'pi_sticks':
            ps.produce_image(params)
        elif func == 'contours':
            co.produce_image(params)
        elif func == 'equation_graphs':
            eq.produce_image(params)
        elif func == 'collatz':
            cc.produce_image(params)
        elif func == 'visual_numbers':
            vn.produce_image(params)
        # elif func == 'mobius':


if __name__ == '__main__':
    main()
