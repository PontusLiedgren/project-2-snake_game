# project-2-snake
#
# Author: Pontus Liedgren
# https://github.com/PontusLiedgren/project-2-snake_game


# Snake game

# imports
import pygame   

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()

pygame.draw.rect(screen, (30, 128, 255), pygame.Rect(30, 30, 60, 60))
