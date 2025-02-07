import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def collision_check(self, circleshape):
        distance = self.position.distance_to(circleshape.position)
        if distance <= self.radius + circleshape.radius:
            return True
        else:
            return False
