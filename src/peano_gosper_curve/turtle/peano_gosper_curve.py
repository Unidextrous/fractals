import turtle

turtle.speed(0)

def draw_peano_gosper_curve_a(step_length, iterations):
    if iterations == 0:
        turtle.forward(step_length)
    else:
        draw_peano_gosper_curve_a(step_length, iterations - 1)
        turtle.left(60)
        draw_peano_gosper_curve_b(step_length, iterations - 1)
        turtle.left(120)
        draw_peano_gosper_curve_b(step_length, iterations - 1)
        turtle.right(60)
        draw_peano_gosper_curve_a(step_length, iterations - 1)
        turtle.right(120)
        draw_peano_gosper_curve_a(step_length, iterations - 1)
        draw_peano_gosper_curve_a(step_length, iterations - 1)
        turtle.right(60)
        draw_peano_gosper_curve_b(step_length, iterations - 1)
        turtle.left(60)

def draw_peano_gosper_curve_b(step_length, iterations):
    if iterations == 0:
        turtle.forward(step_length)
    else:
        turtle.right(60)
        draw_peano_gosper_curve_a(step_length, iterations - 1)
        turtle.left(60)
        draw_peano_gosper_curve_b(step_length, iterations - 1)
        draw_peano_gosper_curve_b(step_length, iterations - 1)
        turtle.left(120)
        draw_peano_gosper_curve_b(step_length, iterations - 1)
        turtle.left(60)
        draw_peano_gosper_curve_a(step_length, iterations - 1)
        turtle.right(120)
        draw_peano_gosper_curve_a(step_length, iterations - 1)
        turtle.right(60)
        draw_peano_gosper_curve_b(step_length, iterations - 1)