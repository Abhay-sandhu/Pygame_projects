import pygame, math
from pygame.math import Vector2
from pygame import image, transform
from settings import *

vec2d = pygame.math.Vector2
point = pygame.math.Vector2


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, enemy_type):
        super().__init__()
        self.game = game
        self.waypoints = self.game.world.waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.angle = 0
        self.type = enemy_type
        self.speed = ENEMY_DATA[self.type]['speed']
        self.health = ENEMY_DATA[self.type]['health']
        self.size = ENEMY_DATA[self.type]['size']
        self.original_image = transform.scale(
            image.load(ENEMY_DATA[self.type]['image']), (self.size, self.size)
        )
        self.image = transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def move(self):
        try:
            self.target = Vector2(self.waypoints[self.target_waypoint])
            dist = self.target - self.pos
            if dist.length() > 0:
                self.pos = Vector2.move_towards(self.pos, self.target, self.speed)
            else:
                self.target_waypoint += 1
        except IndexError:
            self.game.world.health -= ENEMY_DATA[self.type]['damage']
            self.game.world.missed_enemies += 1
            self.kill()

    def rotate(self):
        dist = self.target - self.pos
        self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
        self.image = transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def check_alive(self):
        if self.health <= 0:
            self.game.world.money += ENEMY_DATA[self.type]['bounty']
            self.game.world.killed_enemies += 1
            self.kill()
            

    def update(self):
        self.move()
        self.rotate()
        self.check_alive()
