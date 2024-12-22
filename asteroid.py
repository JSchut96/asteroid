import pygame

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.radius, 2)

    def update(self, dt):
        self.x += self.velocity[0] * dt
        self.y += self.velocity[1] * dt