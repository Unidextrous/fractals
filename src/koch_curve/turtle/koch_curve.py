import turtle

turtle.speed(0)

def draw_koch_curve(step_length, iterations):
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
    for _ in range(3):
        draw_koch_curve(size, iterations)
        if not inverse:
            turtle.right(120)
        else:
            turtle.left(120)