import pygame, math
from pygame.math import Vector2
from pygame import image, transform, sprite
from settings import *

class Turret(sprite.Sprite):
    def __init__(self, game, tile):
        super().__init__()
        self.game = game
        self.tile = tile
        self.level = 1
        self.pos = Vector2((tile[0] + 0.5) * TILE_SIZE, (tile[1] + 0.5) * TILE_SIZE)
        self.selected = False
        self.target = None

        self.sprite_sheet = image.load(TURRET_DATA[self.level - 1]['sprite_sheet']).convert_alpha()
        self.animation_frames = self.load_frames()
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        self.angle = 90
        self.original_image = self.animation_frames[self.frame_index]
        self.image = transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
        self.cooldown = TURRET_DATA[self.level - 1]['cooldown']
        self.damage = TURRET_DATA[self.level - 1]['damage']
        self.last_shot = pygame.time.get_ticks()

        self.range = TURRET_DATA[self.level - 1]['range']
        self.range_image = pygame.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0,0,0))
        self.range_image.set_colorkey((0,0,0))
        pygame.draw.circle(self.range_image, ((100,100,100)), (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def load_frames(self):
        frame_size = self.sprite_sheet.get_height()
        animation_list = []
        for i in range(ANIMATION_STEPS):
            animation_list.append(self.sprite_sheet.subsurface(i * frame_size, 0, frame_size, frame_size))
        return animation_list

    def play_animation(self):
        self.original_image = self.animation_frames[self.frame_index]
        current_time = pygame.time.get_ticks()
        if current_time - self.update_time > ANIMATION_DELAY:
            self.update_time = pygame.time.get_ticks()
            self.frame_index = (self.frame_index + 1) % len(self.animation_frames)
        if self.frame_index == 0:
            self.last_shot = pygame.time.get_ticks()
            self.game.shot_sound.play()
            self.target = None

    def upgrade(self):
        self.level += 1
        self.range = TURRET_DATA[self.level - 1]['range']
        self.cooldown = TURRET_DATA[self.level - 1]['cooldown']
        self.damage = TURRET_DATA[self.level - 1]['damage']

        self.sprite_sheet = image.load(TURRET_DATA[self.level - 1]['sprite_sheet']).convert_alpha()
        self.animation_frames = self.load_frames()
        self.original_image = self.animation_frames[self.frame_index]

        self.range = TURRET_DATA[self.level - 1]['range']
        self.range_image = pygame.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0,0,0))
        self.range_image.set_colorkey((0,0,0))
        pygame.draw.circle(self.range_image, ((100,100,100)), (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center


    def update(self, enemy_group):
        if self.target:
            self.play_animation()
        else:
            if pygame.time.get_ticks() - self.last_shot > self.cooldown:
                self.aim(enemy_group)

    def aim(self, enemy_group):
        x_dist = 0
        y_dist = 0
        for enemy in enemy_group:
            if enemy.health > 0:
                x_dist = enemy.rect.x - self.rect.x
                y_dist = enemy.rect.y - self.rect.y
                dist = math.sqrt(x_dist * x_dist + y_dist * y_dist)
                if dist <= self.range:
                    self.target = enemy
                    self.target.health -= self.damage
                    self.angle = math.degrees(math.atan2(-y_dist, x_dist))
                    break
            
    def draw(self, surface):
        self.image = transform.rotate(self.original_image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)