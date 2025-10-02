import pygame
from constants import *
from player import Player

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

  while True:
    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
