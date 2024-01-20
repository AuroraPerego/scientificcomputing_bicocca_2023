import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

N = 256
x = np.linspace(-2, 2, N)
y = np.linspace(-2, 2, N)
xv, yv = np.meshgrid(x, y, indexing="ij")

c = xv + 1j * yv

z = np.zeros((N, N), dtype=np.complex128)
m = np.ones((N, N))

fig = plt.figure(dpi=100)
plt.axis('off')
im = plt.imshow(m, animated=True, cmap='winter', vmin=0, vmax=1)  # Set binary colormap

def updatefig(*args):
    global z, m
    z = z**2 + c
    m = np.ones_like(m)
    m[np.abs(z) <= 2] = 0.0
    im.set_array(m)
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=100, frames=100, blit=True)
ani.save("mandelbrot.gif", writer=PillowWriter(fps=1))