"""
mandelbrot_set.py

Generates and displays the Mandelbrot Set using NumPy and Matplotlib.
This fractal is computed by iterating the equation z = z² + c for each
point on the complex plane and checking how quickly it diverges.

Author: Isaac (Unidextrous)
"""

import numpy as np
import matplotlib.pyplot as plt

def compute_mandelbrot(c, max_iter):
    """
    Computes how many iterations a complex point takes to escape the Mandelbrot set.

    Args:
        c (complex): The complex point to test.
        max_iter (int): Maximum number of iterations before declaring it bounded.

    Returns:
        int: Number of iterations before escape, or max_iter if bounded.
    """
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n    # Escaped the set
        
        z = (z * z) + c     # Did not escape — likely in the Mandelbrot set
    
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Computes a 2D grid of Mandelbrot values over a complex region.

    Args:
        xmin, xmax (float): Real-axis range.
        ymin, ymax (float): Imaginary-axis range.
        width, height (int): Dimensions of output image.
        max_iter (int): Maximum number of iterations.

    Returns:
        2D NumPy array of iteration counts.
    """
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)

    # Generate grid and compute Mandelbrot values
    return (np.array([[compute_mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def display(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Displays the Mandelbrot Set using matplotlib.

    Args:
        xmin, xmax, ymin, ymax: Region of the complex plane.
        width, height: Output resolution.
        max_iter: Max iterations for escape test.
    """
    d = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(d, extent = (xmin, xmax, ymin, ymax))
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.show()

# Configuration: Zoom level and resolution
width, height = 800, 800
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
max_iter = 256

# Run and display the fractal
display(xmin, xmax, ymin, ymax, width, height, max_iter)