"""
A → A - B + A + B - A
B → B B
"""
import turtle

# Set turtle speed to maximum (0 = no animation delay)
turtle.speed(0)

def draw_sierpinski_a(step_length, iterations):
    if iterations == 0:
        turtle.forward(step_length)
    else:
        draw_sierpinski_a(step_length, iterations - 1)
        turtle.left(120)
        draw_sierpinski_b(step_length, iterations - 1)
        turtle.right(120)
        draw_sierpinski_a(step_length, iterations - 1)
        turtle.right(120)
        draw_sierpinski_b(step_length, iterations - 1)
        turtle.left(120)
        draw_sierpinski_a(step_length, iterations - 1)

def draw_sierpinski_b(step_length, iterations):
    if iterations == 0:
        turtle.forward(step_length)
    else:
        draw_sierpinski_b(step_length, iterations - 1)
        draw_sierpinski_b(step_length, iterations - 1)

# Start drawing the Dragon Curve with specified segment size and recursion depth
draw_sierpinski_a(4, 6)

# Keep the turtle window open until closed manually
turtle.done()