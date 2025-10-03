import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.x = x
    self.y = y

  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    random_angle = random.uniform(20, 50)
    vector_1 = self.velocity.rotate(random_angle)
    vector_2 = self.velocity.rotate(random_angle*-1)
    new_radius = self.radius - ASTEROID_MIN_RADIUS

    Asteroid(self.position[0], self.position[1], new_radius).velocity = vector_1 * 1.2
    Asteroid(self.position[0], self.position[1], new_radius).velocity = vector_2 * 1.2