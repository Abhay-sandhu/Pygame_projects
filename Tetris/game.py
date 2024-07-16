import pygame
from random import randint
import Tetris

pygame.init()
pygame.font.init()
pygame.mixer.init()

RED = (255, 0, 0, 255)     # Fully opaque red
GREEN = (0, 255, 0, 255)   # Fully opaque green
BLUE = (0, 0, 255, 255)    # Fully opaque blue
WHITE = (255, 255, 255, 255) # Fully opaque white
BG_COLOR = (31, 25, 76, 255)
GRID = (31, 25, 132)


SCORE = 0
FPS = 60
VOLUME = 0.03
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TETRIS!!!')
clock = pygame.time.Clock()

font = pygame.font.Font(None, 40)
font.set_bold(True)
win_text = font.render('YOU WIN!', 1, GREEN)
lose_text = font.render('YOU LOSE!', 1, RED)

#pygame.mixer.music.load('Tetris/assets/cave.mp3')
#pygame.mixer.music.set_volume(VOLUME * 0.66)
#pygame.mixer.music.play(-1, 0, 1000)

#coin_sound = pygame.mixer.Sound('Tetris/assets/sfx_point.wav')
#lose_sound = pygame.mixer.Sound('Tetris/assets/lose.wav')
#win_sound = pygame.mixer.Sound('Tetris/assets/win.wav')

#coin_sound.set_volume(VOLUME)
#lose_sound.set_volume(VOLUME)
#win_sound.set_volume(VOLUME)





end = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if end != True:
        screen.fill(BG_COLOR)
    else:
        end = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
exit()