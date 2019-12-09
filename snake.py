# project-2-snake
#
# Author: Pontus Liedgren
# https://github.com/PontusLiedgren/project-2-snake_game

# Snake game

# imports
import pygame, random

pygame.init()

GREEN = (76, 187, 40)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLUE = (80, 0, 255)

SCREENWIDTH = 600
SCREENHEIGHT = 600
BLOCK_SIZE = 40

GRID = {
    "width": SCREENWIDTH / BLOCK_SIZE,
    "height": SCREENHEIGHT / BLOCK_SIZE
}

PLAYER = {
    "x": 7,
    "y": 7,
    "direction": "down"
}

TAILS = []
SCORE = 0
FOOD = {
    "x": 7,
    "y": 11
}

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

carryOn = True
clock = pygame.time.Clock()
target_per_second = 4
ticker = 0
font = pygame.font.SysFont("comicsansms", 30)

# functions
def create_food():
    FOOD = {
        "x": random.randrange(1, GRID["width"]),
        "y": random.randrange(1, GRID["height"])
    }
    return FOOD
    
def create_tail(x, y):
    new_tail = {
        "x": x,
        "y": y
    }
    return new_tail

while carryOn:
    # event catcher
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                carryOn = False
            if event.key == pygame.K_w:
                if PLAYER["direction"] != "down":
                    PLAYER["direction"] = "up"
            if event.key == pygame.K_s:
                if PLAYER["direction"] != "up":
                    PLAYER["direction"] = "down"
            if event.key == pygame.K_a:
                if PLAYER["direction"] != "right":
                    PLAYER["direction"] = "left"
            if event.key == pygame.K_d:
                if PLAYER["direction"] != "left":
                    PLAYER["direction"] = "right"
    
    # update
    ticker += 1
    if (ticker == (60 / target_per_second)):
        ticker = 0
        
        # tail update   
        if TAILS:
            TAILS.pop(0)
        if SCORE > 0:
            TAILS.append(create_tail(PLAYER["x"], PLAYER["y"]))

        # movement update
        if PLAYER["direction"] == "up":
            PLAYER["y"] -= 1
        if PLAYER["direction"] == "down":
            PLAYER["y"] += 1
        if PLAYER["direction"] == "left":
            PLAYER["x"] -= 1
        if PLAYER["direction"] == "right":
            PLAYER["x"] += 1

        # out of bounds detection
        if PLAYER["x"] < 0 or PLAYER["x"] > GRID["width"]:
            print("OUT OF BOUNDS!")
            carryOn = False

        if PLAYER["y"] < 0 or PLAYER["y"] > GRID["height"]:
            print("OUT OF BOUNDS!")
            carryOn = False

        # food spawn 
        if PLAYER["x"] == FOOD["x"] and PLAYER["y"] == FOOD["y"]:
            SCORE += 1
            FOOD = create_food()
            TAILS.append(create_tail(PLAYER["x"], PLAYER["y"]))

        # player colission
        
    # draw
    screen.fill(GREEN)
    pygame.draw.rect(screen, BLUE,(PLAYER["x"]*BLOCK_SIZE, PLAYER["y"]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED,(FOOD["x"]*BLOCK_SIZE, FOOD["y"]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    
    for tail in TAILS:
        pygame.draw.rect(screen, PURPLE,(tail["x"]*BLOCK_SIZE, tail["y"]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    score_text = font.render("Score: "+str(SCORE), True, GREY)
    screen.blit(score_text,[20,20])

    # push to screen
    pygame.display.flip()
    clock.tick(60)
pygame.quit()