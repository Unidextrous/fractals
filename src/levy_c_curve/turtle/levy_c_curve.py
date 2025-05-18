import turtle

turtle.speed(0)

def draw_levy_c_curve(step_length, iterations):
    if iterations == 0:
        turtle.forward(step_length)
    else:
        turtle.left(45)
        draw_levy_c_curve(step_length, iterations - 1)
        turtle.right(90)
        draw_levy_c_curve(step_length, iterations - 1)
        turtle.left(45)