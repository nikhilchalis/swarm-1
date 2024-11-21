import pymunk
import pygame
from pymunk.pygame_util import DrawOptions

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))  # Create a window
clock = pygame.time.Clock()  # For controlling the frame rate
running = True

# Create the PyMunk space
space = pymunk.Space()
space.gravity = (0, -981)  # Set gravity

# Create a body
body = pymunk.Body()  # Create a Body
body.position = (50, 300)  # Set the position of the body

# Create a box shape and attach to the body
poly = pymunk.Poly.create_box(body, size=(50, 50))  # Box dimensions
poly.mass = 10
poly.elasticity = 0.5  # Optional: make it bouncy
space.add(body, poly)

# Create a static floor
static_body = pymunk.Body(body_type=pymunk.Body.STATIC)  # Static body
floor = pymunk.Segment(static_body, (0, 50), (600, 50), 5)  # Floor line
floor.elasticity = 0.5  # Optional: make it bouncy
space.add(static_body, floor)  # Add the body and shape to the space

# Setup PyMunk debug draw options for Pygame
draw_options = DrawOptions(screen)

# Flip the rendering surface vertically
def flip_coordinates(surface, height):
    flipped_surface = pygame.transform.flip(surface, False, True)
    return flipped_surface

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Exit if the user closes the window
            running = False

    # Clear screen
    screen.fill((255, 255, 255))  # White background

    # Step the simulation
    space.step(1/50.0)  # Advance simulation by one step

    # Draw the simulation
    space.debug_draw(draw_options)

    # Flip the surface vertically before displaying it
    flipped_screen = flip_coordinates(screen, screen.get_height())
    screen.blit(flipped_screen, (0, 0))

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(50)

pygame.quit()
