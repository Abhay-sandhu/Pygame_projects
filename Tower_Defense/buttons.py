import pygame
from pygame import transform, image, sprite
from settings import *

class Button(sprite.Sprite):
    def __init__(self, game, image_file, pos, single_click=True):
        super().__init__()
        self.game = game
        self.image = image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.single_click = single_click
        self.clicked = False

    def update(self):
        self.clicked = False
        if self.rect.collidepoint(pygame.mouse.get_pos()) and self.clicked == False:
            if self.single_click:
                self.clicked = True