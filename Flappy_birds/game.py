import pygame
from pygame import transform, image, key, K_SPACE
import random



class Main():
    def __init__(self, file, x, y, speed):
        self.image = transform.scale(image.load(file), (120,100))
        self.speed = -1 * speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Bird(Main):
    def __init__(self, file, x, y, speed):
        super().__init__(file, x, y, speed)
        self.angle = 30
    
    def control(self):
        keys = key.get_pressed()
        if keys[K_SPACE]:
            speed = abs(self.speed)

    #def update(self):
    #    pass

pygame.init()
WIDTH = 900
HEIGHT = 650
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
background = transform.scale(image.load("Flappy_birds/assets/background.jpg"), (WIDTH, HEIGHT))
bird = Bird('Flappy_birds/assets/bird.png', 300, 200, 3)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    screen.blit(background, (0,0))
    bird.update(screen)
    bird.control() 

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()