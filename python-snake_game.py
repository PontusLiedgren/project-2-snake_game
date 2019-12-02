# project-2-snake
#
# Author: Pontus Liedgren
# https://github.com/PontusLiedgren/project-2-snake_game


# Snake game

# imports
import pygame, random

from snake import Snake

pygame.init()

GREEN = (76, 187, 40)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLUE = (80, 0, 255)

SCREENWIDTH = 600
SCREENHEIGHT = 600

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

all_sprites_list = pygame.sprite.Group()

playerSnake = Snake(BLUE, 40, 40)
playerSnake.rect.x = SCREENWIDTH / 2
playerSnake.rect.y = SCREENHEIGHT / 2


all_sprites_list.add(playerSnake)

carryOn = True
clock = pygame.time.Clock()
direction = 0

def steering(player):
    for y in range(height):
            for x in range(width):
                    rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.rect.y += rect
        player.rect.x -= rect
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.rect.y += rect
        player.rect.x += rect
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.rect.x += rect
        player.rect.y -= rect
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.rect.x += rect
        player.rect.y += rect




while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False
        
    keys = pygame.key.get_pressed()
    steering(playerSnake)
    all_sprites_list.update()
    screen.fill(GREEN)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
