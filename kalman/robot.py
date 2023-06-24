import pygame


class State:
    def __init__(self, x=0, y=0, v=0):
        self.x = x
        self.y = y
        self.v = v


class Robot:
    def __init__(self):
        self.state = State()

    def update(self, dt):
        self.state.x += self.state.v * dt
        self.state.y += self.state.v * dt

    def render(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.state.x, self.state.y), 10)
