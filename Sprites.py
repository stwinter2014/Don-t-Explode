import pygame
import random

pygame.init()
size = [900, 530]
black = (0,0,0)
white = [255, 255, 255]
class Pong_green(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong1_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def update(self, x_speed, y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed
    
class Pong_blue(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong2_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def update(self, x_speed, y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed

class Pong_red(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong3_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def update(self, x_speed, y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed

class Pong_yellow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong4_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def update(self, x_speed, y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed

class Claw (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Claw.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()

class Explosion (pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load("explosion5.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
    def update (self, x_pos, y_pos, count):
        if (count >= 3 and count < 6) or (count >= 21 and count < 23):
            self.image = pygame.image.load("explosion4.png").convert()
        if (count >= 6 and count < 9) or (count >= 18 and count < 21):
            self.image = pygame.image.load("explosion3.png").convert()
        if (count >= 9 and count < 12) or (count >= 15 and count < 18):
            self.image = pygame.image.load("explosion2.png").convert()
        if count >= 12 and count < 15:
            self.image = pygame.image.load("explosion1.png").convert()
        if count >= 23 and count < 26:
            self.image = pygame.image.load("explosion5.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class Seed(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("seed.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
