"""
dragon_curve.py

Draws the Dragon Curve fractal using recursive functions and Python's turtle graphics.
Each recursive step creates a more intricate version of the curve by combining two rules:
A → A + B
B → A - B
"""
import turtle

# Set turtle speed to maximum (0 = no animation delay)
turtle.speed(0)

def draw_dragon_curve_a(step_length, iterations):
    """
    Draws the Dragon Curve variant A.

    Rule:
        A(n) = A(n-1) + turn left 90° + B(n-1)

    Args:
        step_length (float): The length of each segment.
        iterations (int): Number of recursive steps to apply.
    """
    if iterations == 0:
        turtle.forward(step_length)
    else:
        draw_dragon_curve_a(step_length, iterations - 1)
        turtle.left(90)
        draw_dragon_curve_b(step_length, iterations - 1)

def draw_dragon_curve_b(step_length, iterations):
    """
    Draws the Dragon Curve variant B.

    Rule:
        B(n) = A(n-1) - turn right 90° - B(n-1)

    Args:
        step_length (float): The length of each segment.
        iterations (int): Number of recursive steps to apply.
    """
    if iterations == 0:
        turtle.forward(step_length)
    else:
        draw_dragon_curve_a(step_length, iterations - 1)
        turtle.right(90)
        draw_dragon_curve_b(step_length, iterations - 1)

# Start drawing the Dragon Curve with specified segment size and recursion depth
draw_dragon_curve_a(5, 10)

# Keep the turtle window open until closed manually
turtle.done()