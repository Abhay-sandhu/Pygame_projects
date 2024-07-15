import pygame
from pygame import mixer, sprite,transform, image, font, key, K_w, K_s, K_a, K_d
from sys import exit


class Main(sprite.Sprite):
    def init(self, image_file, screen, x, y, speed):
        super().__init__()
        self.screen = screen
        self.speed= speed
        self.image = transform.scale(image.load(image_file), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(Main):
    def __init__(self, image_file, screen, x, y, speed):
        super().__init__(image_file, screen, x, y, speed)
    
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
    def __init__(self, image_file, screen, x, y, speed):
        super().__init__(image_file, screen, x, y, speed)
    
    def update(self):
        pass
        
class Walls(sprite.Sprite):
    def __init__(self, image_file, screen):
        super().__init__()
        self.screen = screen
        self.image = transform.scale(image.load(image_file), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()











pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        screen.fill((200,150,200))

        #game code


        pygame.display.update()
        clock.tick(60)

pygame.quit()
exit()