import pygame, math
from pygame.math import Vector2
from pygame import image, transform, draw, sprite
from settings import *

class Turret(sprite.Sprite):
    def __init__(self, game, tile):
        super().__init__()
        self.game = game
        self.pos = Vector2((tile[0] + 0.5) * TILE_SIZE, (tile[1] + 0.5) * TILE_SIZE)
        self.image = transform.scale(image.load(TURRET_1).convert_alpha(), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.cooldown = 0
        self.bullets = pygame.sprite.Group()

