import pygame
from pygame import (
    sprite,
    transform,
    image,
    key,
    K_w,
    K_s,
    K_a,
    K_d,
    Rect,
    Color,
    display,
    Surface
)

WIDTH = 800
HEIGHT = 600
WALL_COLOR = Color(52,82,63)
screen = display.set_mode((WIDTH,HEIGHT))

class Main(sprite.Sprite):
    def __init__(self, image_file, x, y, speed):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(
            image.load(image_file), (50, 50)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def game_end(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(Main):
    def __init__(self, x, y, speed, image_file='Coin_Maze/assets/miner.png'):
        super().__init__(image_file, x, y, speed)
    def control(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.speed


class Enemy(Main):
    def __init__(self, x, y, speed, image_file='Coin_Maze/assets/ghost.png'):
        super().__init__(image_file, x, y, speed)
    def update(self):
        self.rect.x += self.speed

        if self.rect.x > WIDTH - self.rect.width or self.rect.y > HEIGHT:
            self.speed *= -1
        if self.rect.x < 200 or self.rect.y < 0:
            self.speed *= -1

class Coins(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = transform.scale(image.load('Coin_Maze/assets/dollar.png'), (25, 25))
        self.rect = Rect(x,y, 25,25)

    def draw_coin(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Border(sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.wall = Surface((self.width, self.height))
        self.wall.fill(color)
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def build_wall(self):
        screen.blit(self.wall, (self.rect.x, self.rect.y))

def game_init():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

