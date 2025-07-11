"""
levy_c_curve.py

Draws the Lévy C Curve using Python's turtle graphics module.
This fractal curve forms a zigzagging shape by recursively replacing
a straight segment with two at 45° angles.
"""

import turtle

# Set turtle speed to fastest for quicker rendering
turtle.speed(0)

def draw_levy_c_curve(step_length, iterations):
    """
    Recursively draws the Lévy C Curve.

    Each straight line segment is replaced by two smaller segments joined at a 90° angle,
    rotated by 45° left and right, producing a fractal pattern of increasing complexity.

    Args:
        step_length (float): Length of the base segment.
        iterations (int): Number of recursive steps to apply.
    """
    if iterations == 0:
        turtle.forward(step_length)
    else:
        turtle.left(45)
        draw_levy_c_curve(step_length, iterations - 1)
        turtle.right(90)
        draw_levy_c_curve(step_length, iterations - 1)
        turtle.left(45)

# Start drawing with a small step length and 10 recursion levels
draw_levy_c_curve(2, 10)

# Keep the turtle window open after drawing
turtle.done()