import pygame
import math

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Sierpinski Triangle")
clock = pygame.time.Clock()
running = True
dt = 0

# Screen center
cx = screen.get_width() / 2
cy = screen.get_height() / 2

# Store triangle centers for recursive generations
current_centers = []
new_centers = []

# Animation state
step = 0                # Current growth step
size = 0                # Current triangle growth size
target_size = 200       # Max size before starting next generation
at_target_size = False  # True when current generation is finished growing
grow_speed = 0          # Current growth speed
accel = True            # Whether triagle growth is still accelerating

screen.fill("black")

# Main loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Growth physics
    if accel:
        # Accelerate growth
        grow_speed += 0.01
        if size >= target_size / 2:
            accel = False
    else:
        # Decelerate growth
        grow_speed -= 0.01

        # Cap at target size
        if size >= target_size:
            size = target_size
            at_target_size = True

    size += grow_speed

    # Drawing
    if step == 0:
        # Draw initial large upright white triangle
        pygame.draw.polygon(screen, "white", (
            (cx + (size * 0.866), cy + (size * 0.5)),
            (cx - (size * 0.866), cy + (size * 0.5)),
            (cx, cy - size)
        ))
    else:
        for center in current_centers:
            pygame.draw.polygon(screen, "black", (
                (center[0] - (size * 0.866), center[1] - (size * 0.5)),
                (center[0] + (size * 0.866), center[1] - (size * 0.5)),
                (center[0], center[1] + size)
            ))

    # Transition to next step
    if at_target_size:
        # Reset for next growth cycle
        size = 0
        target_size = target_size / 2
        at_target_size = False
        grow_speed = 0
        accel = True
        
        if step == 0:
            # First subdivision: place one black triangle in the center
            current_centers = [(cx, cy)]
        else:
            # For each cutout triangle in this generation, generate three new centers for the next generation
            for center in current_centers:
                new_centers.append((center[0], center[1] - (target_size * 2)))
                new_centers.append((center[0] + (target_size * 1.732), center[1] + target_size))
                new_centers.append((center[0] - (target_size * 1.732), center[1] + target_size))

            # Replace current centers with new ones
            current_centers.clear()
            current_centers.extend(new_centers)
            new_centers.clear()

        step += 1

        # Stop after 8 iterations
        if step == 8:
            break


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
