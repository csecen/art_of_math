# import libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
import argparse
import json
    

def derivs(state, t, G, L1, L2, M1, M2):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx


def main():
    parser = argparse.ArgumentParser(description='Produce different depictions of a double pendulum')
    parser.add_argument('filename', help='name of config file')
    args = parser.parse_args()
    
    config_file = vars(args)['filename']
    
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    G = config['G']  # acceleration due to gravity, in m/s^2
    L1 = config['L1']  # length of pendulum 1 in m
    L2 = config['L2']  # length of pendulum 2 in m
    M1 = config['M1']  # mass of pendulum 1 in kg
    M2 = config['M2']  # mass of pendulum 2 in kg
    
    # create a time array from 0..100 sampled at 0.05 second steps
    dt = config['dt']
    time = config['time']
    t = np.arange(0, time, dt)
    
    # th1 and th2 are the initial angles (degrees)
    # w10 and w20 are the initial angular velocities (degrees per second)
    th1 = config['th1']
    w1 = config['w1']
    th2 = config['th2']
    w2 = config['w2']
    
    # initial state
    state = np.radians([th1, w1, th2, w2])
    
    
if __name__ == '__main__':
    main()
