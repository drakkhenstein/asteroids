import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.rotation = 0
        #self.rotation_speed = 0
        #self.rotation_speed = random.uniform(-ASTEROID_ROTATION_SPEED, ASTEROID_ROTATION_SPEED)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        #self.rotation += self.rotation_speed * dt
        self.position += self.velocity * dt
        #self.position.x %= SCREEN_WIDTH
        #self.position.y %= SCREEN_HEIGHT

        