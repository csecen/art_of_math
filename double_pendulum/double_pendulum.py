# import libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
from matplotlib.collections import LineCollection
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


def track(i, pend, line, line2):
    thisx = [0, pend[0][0][i], pend[0][2][i]]
    thisy = [1, pend[0][1][i]+1, pend[0][3][i]+1]
    line.set_data(thisx, thisy)
    line2.set_data(pend[0][2][:i+1], pend[0][3][:i+1]+1)
    return line, line2,


def tracer(i, pend, line, line2):
    thisx = [0, pend[0][0][i], pend[0][2][i]]
    thisy = [1, pend[0][1][i]+1, pend[0][3][i]+1]
    line.set_data(thisx, thisy)
    
    line2.set_data(pend[0][2][i-20:i+1], pend[0][3][i-20:i+1]+1)
    return line, line2,

# def init(lines):
#     for line in lines:
#         line.set_data([],[])
#     return lines

def multi(i, pend, lines):
    
    for idx, l in enumerate(lines):
        thisx = [0, pend[idx][0][i], pend[idx][2][i]]
        thisy = [1, pend[idx][1][i]+1, pend[idx][3][i]+1]
#         line = lines[idx]
        l.set_data(thisx, thisy)
    
    return lines


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

    # th1 and th2 are the initial angles (degrees)
    # w10 and w20 are the initial angular velocities (degrees per second)
    th1 = config['th1']
    w1 = config['w1']
    th2 = config['th2']
    w2 = config['w2']
    
    # create a time array from 0..100 sampled at 0.05 second steps
    dt = config['dt']
    time = config['time']
    t = np.arange(0, time, dt)
    
    pendulums = []
    theta_1s = np.linspace(th1, th1+.01, config['num_pendulums'])
    
    for th in theta_1s:
        # initial state
        state = np.radians([th, w1, th2, w2])

        # integrate your ODE using scipy.integrate.
        y = integrate.odeint(derivs, state, t, args=(G, L1, L2, M1, M2))
        
        x1 = L1*sin(y[:, 0])
        y1 = -L1*cos(y[:, 0])

        x2 = L2*sin(y[:, 2]) + x1
        y2 = -L2*cos(y[:, 2]) + y1
        
        pendulums.append((x1,y1,x2,y2))
        
#     fig = plt.figure()
#     fig.patch.set_facecolor('black')
#     ax = fig.add_subplot(111, autoscale_on=True, xlim=(-4, 4), ylim=(-4, 4))
#     ax.set_aspect('equal')
#     ax.axis('off')

#     fig, ax = plt.subplots()
    fig = plt.figure()
    fig.set_size_inches((config['sizex'], config['sizey']))
    fig.patch.set_visible(True)
    fig.patch.set_facecolor(config['background'])
    ax = fig.add_subplot(111, autoscale_on=True, xlim=(-4, 4), ylim=(-4, 4))
    ax.set_aspect('equal')
    ax.axis('off')

    if config['style'] == 'track':
        line, = ax.plot([], [], color='azure', lw=2)
        line2, = ax.plot([], [], color=config['color'], lw=2)
        
        ani = animation.FuncAnimation(fig, partial(track, pend=pendulums, line=line, line2=line2), range(1, len(y)),
                                      interval=dt*1000, blit=True)
        ani.save(config['filename'], writer='pillow', fps=1 / dt)
    elif config['style'] == 'tracer':
        line, = ax.plot([], [], color='azure', lw=2)
        line2, = ax.plot([], [], color=config['color'], lw=2)
        
        ani = animation.FuncAnimation(fig, partial(tracer, pend=pendulums, line=line, line2=line2), range(1, len(y)),
                                      interval=dt*1000, blit=True)
        ani.save(config['filename'], writer='pillow', fps=1 / dt)
    elif config['style'] == 'multi_ani':
        cmap = plt.get_cmap(config['cmap_name'])
        colors = cmap(np.linspace(0,1,len(pendulums)))
        
        lines = []
        for i in range(len(colors)):
            line = ax.plot([], [], color=colors[i], lw=2)
            lines.append(line[0])
        
        ani = animation.FuncAnimation(fig, partial(multi, pend=pendulums, lines=lines), range(1, len(y)),
                                      interval=dt*1000, blit=True)
        ani.save(config['filename'], writer='pillow', fps=1 / dt)
    
#     elif config['style'] == 'multi_still':
        
    elif config['style'] == 'path':
        if 'color' in config:
            ax.plot(pendulums[0][2], pendulums[0][3]+1, color=config['color'])
        else:
            points = np.array([pendulums[0][2], pendulums[0][3]+1]).T.reshape(-1, 1, 2)
            segments = np.concatenate([points[:-1], points[1:]], axis=1)

            norm = plt.Normalize(pendulums[0][3].min(), pendulums[0][3].max())
            lc = LineCollection(segments, cmap='Spectral', norm=norm)
            lc.set_array(pendulums[0][3])
            ax.add_collection(lc)
        
        plt.savefig(config['filename'], bbox_inches='tight', pad_inches=0, dpi=400)
    
    
    
    
if __name__ == '__main__':
    main()
