from matplotlib.animation import FuncAnimation as animation
import matplotlib.pyplot as plt
import numpy as np

g = 9.81  # constant
a = 55  # start angle (degrees)
m = 2  # mass
P = 35  # power
x0 = 0  # initial coordinate x
y0 = 0  # initial coordinate y
fps = 120  # frames per second
duration = 5  # animation duration
k = 0.8  # air resistance

H = 15
V = 16

fig = plt.figure()

ax = plt.axes(xlim=(0, V), ylim=(0, H))
line, = ax.plot([], [], lw=3)
a = np.deg2rad(a)


def get_values():
    return {'g': g, 'start_angle': a, 'object_mass': m, 'start_power': P, 'start_coords': {'x': x0, 'y': y0},
            'air_resistance': k}


def create_legend():
    ax.text(0.5 * (V / 15), (H / 15) * (H - 1), f'g = {g}')
    ax.text(0.5 * (V / 15), (H / 15) * (H - 1.7), f'α = {np.rad2deg(a)}')
    ax.text(0.5 * (V / 15), (H / 15) * (H - 2.4), f'm = {m}')
    ax.text(0.5 * (V / 15), (H / 15) * (H - 3.1), f'P = {P}')
    ax.text(3 * (V / 15), (H / 15) * (H - 1), f'fps = {fps}')
    ax.text(3 * (V / 15), (H / 15) * (H - 2.4), f's  = ({x0},{y0})')
    ax.text(3.2 * (V / 15), (H / 15) * (H - 2.7), '0', fontsize=8)
    ax.text(3 * (V / 15), (H / 15) * (H - 1.7), f'C  = {k}')
    ax.text(3.3 * (V / 15), (H / 15) * (H - 1.9), 'f', fontsize=8)
    ax.text(3 * (V / 15), (H / 15) * (H - 3.1), f't    = {duration}')
    ax.text(3.2 * (V / 15), (H / 15) * (H - 3.3), 'all', fontsize=8)
    line.set_data([], [])
    return line


@np.vectorize
def calculate_y(t):
    y = y0 + (P * np.sin(a) * t) / m - (g * t ** 2) / 2
    return y


def animate(i):
    t = np.linspace(0, i / fps, 1000)
    x = (x0 + (P * np.cos(a) * t) / m) * k ** t
    y = calculate_y(t)
    line.set_data(x, y)
    return line


def create_gif(filename):
    anim = animation(fig, animate, init_func=create_legend, frames=duration * fps, interval=fps)
    anim.save(f'animations/{filename}/example.gif')
