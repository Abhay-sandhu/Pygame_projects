import pygame, math
from pygame.math import Vector2
from pygame import image, transform, draw, sprite
from settings import *

class Turret(sprite.Sprite):
    def __init__(self, game, tile):
        super().__init__()
        self.game = game
        self.tile = tile
        self.pos = Vector2((tile[0] + 0.5) * TILE_SIZE, (tile[1] + 0.5) * TILE_SIZE)
        
        self.sprite_sheet = image.load(TURRET_1).convert_alpha()
        self.animation_frames = self.load_frames()
        self.frame_index = 0

        self.image = self.animation_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.cooldown = 0
        self.bullets = pygame.sprite.Group()

    def load_frames(self):
        frame_size = self.sprite_sheet.get_height()
        animation_list = []
        print(self.sprite_sheet.get_width(), frame_size)
        for i in range(ANIMATION_STEPS):
            animation_list.append(self.sprite_sheet.subsurface(i * frame_size, 0, frame_size, frame_size))
        return animation_list

