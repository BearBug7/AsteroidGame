import pygame
import random
from pygame.locals import *
import sys
from ship import Ship

pygame.init()

screen_info = pygame.display.Info()

screen_size = (width, height) = (int(screen_info.current_w), int (screen_info.current_h))
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

colour = (8, 127, 255)

player = Ship((20, 200))

NumLevels = 4
Level = 1

def main():
  global Level, NumLevels

  while Level < NumLevels:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          player.speed[0] = 10
        if event.key == pygame.K_UP:
          player.speed[1] = -10
        if event.key == pygame.K_LEFT:
          player.speed[0] = -10
        if event.key == pygame.K_DOWN:
          player.speed[1] = 10
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
          player.speed[0] = 0
        if event.key == pygame.K_UP:
          player.speed[1] = 0
        if event.key == pygame.K_LEFT:
          player.speed[0] = 0
        if event.key == pygame.K_DOWN:
          player.speed[1] = 0
    player.update()
    screen.fill(colour)
    screen.blit(player.image, player.rect)
    pygame.display.flip()

if __name__ == "__main__":
  main()