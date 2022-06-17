import pygame
from settings import screen_width, screen_height
import sys
from layout import Layout

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
layout = Layout(screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    layout.run()

    pygame.display.update()
    clock.tick(60)
