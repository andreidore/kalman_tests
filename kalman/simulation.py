import numpy as np
import pygame
from filterpy.kalman import KalmanFilter
from pygame.time import get_ticks

from kalman.profile import Profile1
from kalman.robot import Robot

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

font = pygame.font.Font('freesansbold.ttf', 14)

profile = Profile1()

kalman_filter = KalmanFilter(dim_x=4, dim_z=2)
kalman_filter.x = np.array([0, 0, 0, 0])
kalman_filter.F = np.array([[1, 0, 1, 0],
                            [0, 1, 0, 1],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])

robot = Robot()
robot.state.v = profile.velocity
last_time = get_ticks()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    img = font.render(profile.name, True, (0, 0, 0))
    rect = img.get_rect()
    pygame.draw.rect(img, (0, 0, 0), rect, 1)

    delta_time = get_ticks() - last_time
    last_time = get_ticks()
    delta_time /= 1000.

    robot.update(delta_time)

    robot.render(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
