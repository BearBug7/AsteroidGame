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

def main():
  clock.tick(60)
  screen.fill(colour)
  screen.blit(player.image, player.rect)
  pygame.display.flip()

if __name__ == "__main__":
  main()