import pygame, math
from pygame.math import Vector2
from pygame import image, transform, draw
from settings import *

vec2d = pygame.math.Vector2
point = pygame.math.Vector2


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.speed = ENEMY_SPEED
        self.waypoints = self.game.world.waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.angle = 0
        self.original_image = transform.scale(
            image.load(ENEMY_1), (ENEMY_SIZE, ENEMY_SIZE)
        )
        self.image = transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def move(self):
        try:
            draw.lines(self.game.screen, PATH_COLOR, False, self.waypoints, 2)
            self.target = Vector2(self.waypoints[self.target_waypoint])
            dist = self.target - self.pos
            if dist.length() > 0:
                self.pos = Vector2.move_towards(self.pos, self.target, self.speed)
                # draw.line(self.game.screen, PATH_COLOR, self.pos, self.target)
            else:
                self.target_waypoint += 1
        except IndexError:
            self.kill()

    def rotate(self):
        dist = self.target - self.pos
        self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
        self.image = transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.move()
        self.rotate()
