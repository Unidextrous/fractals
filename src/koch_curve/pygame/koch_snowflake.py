import pygame
import math

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Koch Snowflake")
clock = pygame.time.Clock()
running = True
dt = 0

# Screen center
cx = screen.get_width() / 2
cy = screen.get_height() / 2

# Constant: Square root of 3 for equilateral triangle math
SQRT3 = math.sqrt(3)

# Color palette
palette = [
    (59, 30, 112),
    (91, 46, 145),
    (122, 66, 179),
    (106, 100, 199),
    (77, 130, 217),
    (43, 91, 160),
    (59, 30, 112)
]

# Animation state
step = 0                # Current growth step
size = 0                # Current triangle growth size
target_size = 200       # Max size before starting next generation
at_target_size = False  # True when current generation is finished growing
grow_speed = 0          # Current growth speed
accel = True            # Whether triagle growth is still accelerating

current_verts = []      # Stores vertices of current fractal boundary

def draw_triangle(pos, size, orientation, at_target_size=False):
    """
    Draws a triangle split into two colored halves
    
    pos: (x, y) position of triangle center
    size: scaling factor
    orientation: one of 6 directions (up, down, up-right, etc.)
    at_target_size: if True, returns vertices for next step
    """
    
    # Pick points and colors based on orientation
    if orientation == "up":
        color_0 = palette[4]
        color_1 = palette[2]

        point_0 = (pos[0] - size, pos[1])
        point_1 = (pos[0], pos[1] - (size * SQRT3))
        point_2 = (pos[0] + size, pos[1])

    elif orientation == "up-right":
        color_0 = palette[1]
        color_1 = palette[3]

        point_0 = (pos[0] - (size * 0.5), pos[1] - (size * 0.866))
        point_1 = (pos[0] + (size * SQRT3 * 0.866), pos[1] - (size * SQRT3 * 0.5))
        point_2 = (pos[0] + (size * 0.5), pos[1] + (size * 0.866))

    elif orientation == "down-right":
        color_0 = palette[2]
        color_1 = palette[0]

        point_0 = (pos[0] + (size * 0.5), pos[1] - (size * 0.866))
        point_1 = (pos[0] + (size * SQRT3 * 0.866), pos[1] + (size * SQRT3 * 0.5))
        point_2 = (pos[0] - (size * 0.5), pos[1] + (size * 0.866))

    elif orientation == "down":
        color_0 = palette[1]
        color_1 = palette[5]

        point_0 = (pos[0] + size, pos[1])
        point_1 = (pos[0], pos[1] + (size * SQRT3))
        point_2 = (pos[0] - size, pos[1])

    elif orientation == "down-left":
        color_0 = palette[0]
        color_1 = palette[4]

        point_0 = (pos[0] + (size * 0.5), pos[1] + (size * 0.866))
        point_1 = (pos[0] - (size * SQRT3 * 0.866), pos[1] + (size * SQRT3 * 0.5))
        point_2 = (pos[0] - (size * 0.5), pos[1] - (size * 0.866))

    elif orientation == "up-left":
        color_0 = palette[5]
        color_1 = palette[3]

        point_0 = (pos[0] - (size * 0.5), pos[1] + (size * 0.866))
        point_1 = (pos[0] - (size * SQRT3 * 0.866), pos[1] - (size * SQRT3 * 0.5))
        point_2 = (pos[0] + (size * 0.5), pos[1] - (size * 0.866))

    else:
        print("Invalid orientation")

    # Draw two polygons to split the triangle into colored halves
    pygame.draw.polygon(screen, color_0, ((pos[0], pos[1]), point_0, point_1))
    pygame.draw.polygon(screen, color_1, ((pos[0], pos[1]), point_1, point_2))

    # Return vertices to track boundary if this triangle has finished growing
    if at_target_size:
        return (point_0, point_1, point_2)
    else:
        return None

screen.fill("white")

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
            
            # First step: Add vertices of seed crystal
            if step == 0:
                new_verts = [(cx, cy -  size), (cx + (size * 0.866), cy + (size * 0.5)), (cx - (size * 0.866), cy + (size * 0.5))]
                current_verts.extend(new_verts)
                new_verts.clear()
    
    size += grow_speed

    # Drawing
    if step == 0:
        # Draw seed crystal manually
        pygame.draw.polygon(screen, palette[0], (
            (cx + (size * 0.866), cy + (size * 0.5)),
            (cx - (size * 0.866), cy + (size * 0.5)),
            (cx, cy)
        ))

        pygame.draw.polygon(screen, palette[2], (
            (cx + (size * 0.866), cy + (size * 0.5)),
            (cx, cy),
            (cx, cy - size)
        ))

        pygame.draw.polygon(screen, palette[4], (
            (cx, cy),
            (cx - (size * 0.866), cy + (size * 0.5)),
            (cx, cy - size)
        ))
        # Draw all triangles around current crystal boundary
    else:
        for vert_index in range(len(current_verts)):
            vert_0_x = current_verts[vert_index][0]
            vert_0_y = current_verts[vert_index][1]
            vert_1_x = current_verts[(vert_index + 1) % len(current_verts)][0]
            vert_1_y = current_verts[(vert_index + 1) % len(current_verts)][1]

            # Midpoint of edge between vert_0 and vert_1
            midpoint = ((vert_0_x + vert_1_x) / 2, (vert_0_y + vert_1_y) / 2)
            
            # Determine orientation of the edge -> decide triangle growth direction
            
            # Left to right
            if vert_0_x < vert_1_x:
                # Flat
                if vert_0_y - 0.01 <= vert_1_y <= vert_0_y + 0.01:
                    new_tri = draw_triangle(midpoint, size, "up", at_target_size)
                # Downward
                elif vert_0_y < vert_1_y:
                    new_tri = draw_triangle(midpoint, size, "up-right", at_target_size)
                # Upward
                elif vert_0_y > vert_1_y:
                    new_tri = draw_triangle(midpoint, size, "up-left", at_target_size)
            
            # Right to left
            elif vert_0_x > vert_1_x:
                # Flat
                if vert_0_y - 0.01 <= vert_1_y <= vert_0_y + 0.01:
                    new_tri = draw_triangle(midpoint, size, "down", at_target_size)
                # Downward
                elif vert_0_y < vert_1_y:
                    new_tri = draw_triangle(midpoint, size, "down-right", at_target_size)
                # Upward
                elif vert_0_y > vert_1_y:
                    new_tri = draw_triangle(midpoint, size, "down-left", at_target_size)

            # Store new vertices if this generation is finished growing
            if new_tri != None:
                new_verts.extend(new_tri)
        
        # Insert new vertices into boundary list in correct order
        for vert_index in range(len(new_verts)):
            current_verts.insert((vert_index // 3) + 1 + vert_index, new_verts[vert_index])

        new_verts.clear()

    # Transition to next step
    if at_target_size:
        # Reset for next growth cycle
        size = 0
        target_size = target_size / 3
        at_target_size = False
        grow_speed = 0
        accel = True
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
