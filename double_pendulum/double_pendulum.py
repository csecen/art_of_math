# import libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
from functools import partial
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


def tracer(i, pend, line, line2):
#     print(pend)
#     thisx = [0, x1[i], x2[i]]
#     thisy = [1, y1[i]+1, y2[i]+1]
    thisx = [0, pend[0][0][i], pend[0][2][i]]
    thisy = [1, pend[0][1][i]+1, pend[0][3][i]+1]
    line.set_data(thisx, thisy)
    line2.set_data(pend[0][2][:i+1], pend[0][3][:i+1]+1)
#     line2.set_data(x2[i:i+10], y2[i:i+10]+1)
    return line, line2,


def main():
    parser = argparse.ArgumentParser(description='Produce different depictions of a double pendulum')
    parser.add_argument('filename', help='name of config file')
    args = parser.parse_args()
    
    config_file = vars(args)['filename']
    
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    G = config['G']  # acceleration due to gravity, in m/s^2
    
    # create a time array from 0..100 sampled at 0.05 second steps
    dt = config['dt']
    time = config['time']
    t = np.arange(0, time, dt)
    
    pendulums = []
    
    for pend in config['starting_states']:
        L1 = pend['L1']  # length of pendulum 1 in m
        L2 = pend['L2']  # length of pendulum 2 in m
        M1 = pend['M1']  # mass of pendulum 1 in kg
        M2 = pend['M2']  # mass of pendulum 2 in kg
        
        # th1 and th2 are the initial angles (degrees)
        # w10 and w20 are the initial angular velocities (degrees per second)
        th1 = pend['th1']
        w1 = pend['w1']
        th2 = pend['th2']
        w2 = pend['w2']
    
        # initial state
        state = np.radians([th1, w1, th2, w2])

        # integrate your ODE using scipy.integrate.
        y = integrate.odeint(derivs, state, t, args=(G, L1, L2, M1, M2))
        
        
        x1 = L1*sin(y[:, 0])
        y1 = -L1*cos(y[:, 0])

        x2 = L2*sin(y[:, 2]) + x1
        y2 = -L2*cos(y[:, 2]) + y1
        
        pendulums.append((x1,y1,x2,y2))
        
    fig = plt.figure()
    fig.patch.set_facecolor('black')
    ax = fig.add_subplot(111, autoscale_on=True, xlim=(-4, 4), ylim=(-4, 4))
    ax.set_aspect('equal')
    ax.axis('off')
    
    line, = ax.plot([], [], lw=2)
    line2, = ax.plot([], [], color='cyan', lw=2)
    
#     ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
#                                   interval=dt*1000, blit=True)
#     print(pendulums)
#     print('#'*50)
    
    ani = animation.FuncAnimation(fig, partial(tracer, pend=pendulums, line=line, line2=line2), range(1, len(y)),
                                  interval=dt*1000, blit=True)
    
    ani.save(config['filename'], writer='pillow', fps=1 / dt)
    
if __name__ == '__main__':
    main()
