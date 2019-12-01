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
pygame.display.set_caption("Snekgem")

all_sprites_list = pygame.sprite.Group()

playerSnake = Snake(BLUE, 30, 30)
playerSnake.rect.x = SCREENWIDTH / 2
playerSnake.rect.y = SCREENHEIGHT / 2


all_sprites_list.add(playerSnake)

carryOn = True
clock = pygame.time.Clock()


def steering(player):
    if keys[pygame.K_LEFT]:
        player.rect.y += 0
        player.rect.x -= 1
    if keys[pygame.K_RIGHT]:
        player.rect.y += 0
        player.rect.x += 1
    if keys[pygame.K_UP]:
        player.rect.x += 0
        player.rect.y -= 1
    if keys[pygame.K_DOWN]:
        player.rect.x += 0
        player.rect.y += 1


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
