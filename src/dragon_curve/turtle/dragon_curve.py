import turtle

turtle.speed(0)

def draw_dragon_curve_a(step_length, iterations):
    if iterations == 0:
        turtle.forward(step_length)
    else:
        draw_dragon_curve_a(step_length, iterations - 1)
        turtle.left(90)
        draw_dragon_curve_b(step_length, iterations - 1)

def draw_dragon_curve_b(step_length, iterations):
    if iterations == 0:
        turtle.forward(step_length)
    else:
        draw_dragon_curve_a(step_length, iterations - 1)
        turtle.right(90)
        draw_dragon_curve_b(step_length, iterations - 1)

draw_dragon_curve_a(5, 10)

turtle.done()