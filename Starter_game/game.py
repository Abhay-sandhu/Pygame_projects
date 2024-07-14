import pygame
from pygame import transform, image, key, K_UP, K_DOWN, K_LEFT, K_RIGHT
# Initialize Pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
SPEED = 10
PLANE_X = 100
PLANE_Y = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FLY PLANE')
background = transform.scale(image.load('assets\sky_background.jpg'), (WIDTH, HEIGHT))
plane = transform.scale(image.load('assets\plane_gear_up.png'), (WIDTH * 0.25, HEIGHT * 0.25))
clock = pygame.time.Clock()

run = True
while run:
    screen.blit(background,(0,0))
    screen.blit(plane, (PLANE_X,PLANE_Y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    
    keys = key.get_pressed()
    if keys[K_UP] and PLANE_Y > 1:
        PLANE_Y -= SPEED
    if keys[K_DOWN] and PLANE_Y < HEIGHT - HEIGHT * 0.25:
        PLANE_Y += SPEED
    if keys[K_LEFT] and PLANE_X > 1:
        PLANE_X -= SPEED
    if keys[K_RIGHT] and PLANE_X < WIDTH - WIDTH * 0.25:
        PLANE_X += SPEED
    
    pygame.display.update()
    clock.tick(FPS)