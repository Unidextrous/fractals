import numpy as np
import matplotlib.pyplot as plt

def compute_mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        
        z = (z * z) + c
    
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (np.array([[compute_mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def display(xmin, xmax, ymin, ymax, width, height, max_iter):
    d = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(d, extent = (xmin, xmax, ymin, ymax))
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.show()

width, height = 800, 800
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
max_iter = 256

display(xmin, xmax, ymin, ymax, width, height, max_iter)