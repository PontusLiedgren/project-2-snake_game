# project-2-snake
#
# Author: Pontus Liedgren
# https://github.com/PontusLiedgren/project-2-snake_game

# Snake game

# imports
import pygame 
import random

pygame.init()

# colors
GREEN = (76, 187, 40)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (150, 0, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# game board
SCREENWIDTH = 600
SCREENHEIGHT = 600
BLOCK_SIZE = 30

TAILS = []
SCORE = 0
PAUSED = False

# highscore

HS_FILE = "highscore.txt"

def read_txt_file(HIGHSCORE):
    with open(HS_FILE, encoding="utf-8") as text_file:
        HIGHSCORE = text_file.read()
    return HIGHSCORE
HIGHSCORE = int(read_txt_file(0))

GRID = {
    "width": SCREENWIDTH / BLOCK_SIZE,
    "height": SCREENHEIGHT / BLOCK_SIZE
}

PLAYER = {
    "x": 7,
    "y": 7,
    "direction": "down",
    "direction_change_allowed": True
}

FOOD = {
    "x": 7,
    "y": 11
}

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

carryOn = True
clock = pygame.time.Clock()
target_per_second = 10
ticker = 0
font_score = pygame.font.SysFont("Terminal", 40)
font_paused = pygame.font.SysFont("Terminal", 100)

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
                if PAUSED:
                    PAUSED = False
                else:
                    PAUSED = True
            if not PAUSED: 
                if event.key == pygame.K_w and PLAYER["direction_change_allowed"]:
                    if PLAYER["direction"] != "down":
                        PLAYER["direction"] = "up"
                        PLAYER["direction_change_allowed"] = False
                if event.key == pygame.K_s and PLAYER["direction_change_allowed"]:
                    if PLAYER["direction"] != "up":
                        PLAYER["direction"] = "down"
                        PLAYER["direction_change_allowed"] = False
                if event.key == pygame.K_a and PLAYER["direction_change_allowed"]:
                    if PLAYER["direction"] != "right":
                        PLAYER["direction"] = "left"
                        PLAYER["direction_change_allowed"] = False
                if event.key == pygame.K_d and PLAYER["direction_change_allowed"]:
                    if PLAYER["direction"] != "left":
                        PLAYER["direction"] = "right"
                        PLAYER["direction_change_allowed"] = False
        
    # update
    if not PAUSED:
        ticker += 1
    if (ticker == (60 / target_per_second) and not PAUSED):
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
        PLAYER["direction_change_allowed"] = True

        # out of bounds detection
        if PLAYER["x"] < 0 or PLAYER["x"] > GRID["width"]:
            print("OUT OF BOUNDS!")
            carryOn = False

        if PLAYER["y"] < 0 or PLAYER["y"] > GRID["height"]:
            print("OUT OF BOUNDS!")
            carryOn = False

        # tail collision
        for tail_collision in TAILS:
            if PLAYER["x"] == tail_collision["x"] and PLAYER["y"] == tail_collision["y"]:
                carryOn = False
        
        # food spawn 
        if PLAYER["x"] == FOOD["x"] and PLAYER["y"] == FOOD["y"]:
            SCORE += 1
            FOOD = create_food()
            TAILS.append(create_tail(PLAYER["x"], PLAYER["y"]))

    # draw
    # background    
    screen.fill(GREEN)
    
    # tail
    for tail in TAILS:
        pygame.draw.rect(
            screen, 
            BLUE,
            (
                tail["x"]*BLOCK_SIZE,
                tail["y"]*BLOCK_SIZE,
                BLOCK_SIZE, 
                BLOCK_SIZE
            )
        )

    # snake head
    pygame.draw.rect(
        screen,
        PURPLE,
        (
            PLAYER["x"]*BLOCK_SIZE,
            PLAYER["y"]*BLOCK_SIZE,
            BLOCK_SIZE, 
            BLOCK_SIZE
        )
    )

    # food
    pygame.draw.rect(
        screen,
        RED,
        (
            FOOD["x"]*BLOCK_SIZE, 
            FOOD["y"]*BLOCK_SIZE, 
            BLOCK_SIZE, 
            BLOCK_SIZE
        )
    )

    # scoreboard
    score_text = font_score.render("Score: "+str(SCORE), True, WHITE)
    screen.blit(score_text,[10,10])

    # pause & highscore
    paused_text = font_paused.render("Paused!", True, WHITE)
    highscores_text = font_score.render("Highscore: "+ str(HIGHSCORE), True, WHITE)

    if PAUSED:
        screen.blit(highscores_text,[190, 300])
        screen.blit(paused_text,[160,220])

    # push to screen
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

# write highscore
if not carryOn:
    if HIGHSCORE >= SCORE:
        file = open(HS_FILE, "w")
        file.write(str(HIGHSCORE))
        file.close()
    else:
        file = open(HS_FILE, "w")
        file.write(str(SCORE))
        file.close()