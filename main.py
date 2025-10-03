import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import *
from bullet import Bullet

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  bullets = pygame.sprite.Group()

  Player.containers = (updateable, drawable)
  Asteroid.containers = (asteroids, updateable, drawable)
  AsteroidField.containers = (updateable)
  Bullet.containers = (updateable, drawable, bullets)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroidfield = AsteroidField()

  print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

  while True:
    screen.fill("black")
    updateable.update(dt)
    for a in asteroids:
      if a.check_collision(player):
        print("Game over!")
        sys.exit()
      for b in bullets:
        if a.check_collision(b):
          a.kill()
          b.kill()
    for a in drawable:
      a.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
