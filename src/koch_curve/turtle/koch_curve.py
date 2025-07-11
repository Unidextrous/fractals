"""
koch_curve.py

Draws the Koch Curve and the Koch Snowflake using Python's turtle graphics module.
The Koch fractal is a classic example of recursive geometry — each line segment is
divided into four parts, adding a peak in the middle to form a snowflake-like pattern.
"""
import turtle

# Set turtle speed to maximum for fast rendering
turtle.speed(0)

def draw_koch_curve(step_length, iterations):
    """
    Recursively draws a single Koch curve segment.

    Args:
        step_length (float): Length of the base segment to draw.
        iterations (int): Number of recursion steps to apply.
    """
    if iterations == 0:
        turtle.forward(step_length)
    else:
        draw_koch_curve(step_length, iterations - 1)
        turtle.left(60)
        draw_koch_curve(step_length, iterations - 1)
        turtle.right(120)
        draw_koch_curve(step_length, iterations - 1)
        turtle.left(60)
        draw_koch_curve(step_length, iterations - 1)

def draw_koch_snowflake(size, iterations, inverse=False):
    """
    Draws a complete Koch snowflake by connecting three Koch curves in a triangle.

    Args:
        size (float): Length of each side of the initial triangle.
        iterations (int): Number of recursive steps to apply.
        inverse (bool): If True, reverses the direction of the turns (inward spike).
    """
    for _ in range(3):
        draw_koch_curve(size, iterations)
        if not inverse:
            turtle.right(120)
        else:
            turtle.left(120)

# Start drawing the snowflake with small segments and 4 recursion levels
draw_koch_snowflake(2, 4)

# Keep the window open until closed manually
turtle.done()