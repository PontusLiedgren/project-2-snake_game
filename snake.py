import pygame

WHITE = (255, 255, 255)


class Snake(pygame.sprite.Sprite):
    speed = 3

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveRight(self):
        self.rect.x = self.rect.x + self.speed

    def moveLeft(self):
        self.rect.x = self.rect.x - self.speed

    def moveUp(self):
        self.rect.y = self.rect.y - self.speed

    def moveDown(self):
        self.rect.y = self.rect.y + self.speed
