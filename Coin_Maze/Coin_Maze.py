import random, pygame
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
    draw,
    Color,
    display
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

    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(Main):
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
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed

        if self.rect.x > WIDTH or self.rect.y > HEIGHT:
            self.speed *= -1
        if self.rect.x < 0 or self.rect.y < 0:
            self.speed *= -1


class Coins(sprite.Sprite):
    def __init__(self, image_file):
        super().__init__()
        self.image = transform.scale(image.load(image_file), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)

    def draw_coin(self):
        screen.blit(self.image, self.rect)

class Walls(sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.color = color
        self.wall = Rect(x, y, width, height)

    def build_wall(self):
        wall = draw.rect(screen, self.color, self.wall)

def game_init():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()


if __name__ == "__main__":
    pass
