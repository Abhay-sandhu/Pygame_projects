import pygame
from settings import *

vec2d = pygame.math.Vector2
point = pygame.math.Vector2
class Enemy():
    def __init__(self, game):
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load('Tower_Defense/assets/enemy_1.png'), (ENEMY_SIZE, ENEMY_SIZE))
        self.rect = self.image.get_rect()
        self.image_m30 = pygame.transform.rotate(self.image, -35)
        self.image_m30.get_rect().center = self.rect.center
        self.image_m135 = pygame.transform.rotate(self.image, -135)
        self.image_m135.get_rect().center = self.rect.center
        self.vec = vec2d(self.rect.centerx, self.rect.centery)
        print(self.vec)
    def draw(self):
        self.game.screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):
        if self.rect.centery <= 397:
            self.vec = pygame.math.Vector2.move_towards(self.vec, point(400,400), 2)
            self.image = self.image_m30
            pygame.draw.line(self.game.screen, PATH_COLOR, self.vec, point(400,400))
            pygame.draw.line(self.game.screen, PATH_COLOR, point(400,400), point(100,600))
        else:
            self.vec = pygame.math.Vector2.move_towards(self.vec, point(100,600), 2)
            self.image = self.image_m135
            pygame.draw.line(self.game.screen, PATH_COLOR, self.vec, point(100,600))
        self.rect.centerx = self.vec[0]
        self.rect.centery = self.vec[1]
        
    def update(self):
        self.move()
        self.draw()