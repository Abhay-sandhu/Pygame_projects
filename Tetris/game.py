import pygame
from pygame import draw
from random import randint
import Tetris

pygame.init()
pygame.font.init()
pygame.mixer.init()

RED = pygame.Color(255, 0, 0, 255)     # Fully opaque red
GREEN = pygame.Color(0, 255, 0, 255)   # Fully opaque green
BLUE = pygame.Color(0, 0, 255, 255)    # Fully opaque blue
WHITE = pygame.Color(255, 255, 255, 255) # Fully opaque white
BG_COLOR = pygame.Color(31, 25, 76, 255)
GRID_COLOR = Tetris.GRID_COLOR

SCORE = 0
FPS = 60
VOLUME = 0.03
BLOCK_SIZE = Tetris.BLOCK_SIZE
WIDTH = Tetris.WIDTH
HEIGHT = Tetris.HEIGHT

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TETRIS!!!')
clock = pygame.time.Clock()

font = pygame.font.Font(None, 40)
font.set_bold(True)
win_text = font.render('YOU WIN!', 1, GREEN)
lose_text = font.render('YOU LOSE!', 1, RED)

def create_drop_zone(X,Y):
        for x in range(X, X + BLOCK_SIZE * 5, BLOCK_SIZE):
            draw.line(screen, RED, (x, 0), (x, Y + BLOCK_SIZE * 4))
        for y in range(Y, Y + BLOCK_SIZE * 5, BLOCK_SIZE):
            draw.line(screen, RED, (X, y), (X + BLOCK_SIZE * 4, y))


game = Tetris.Game()
shape = Tetris.Shape()
end = game.end
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if end != True:
        screen.fill(BG_COLOR)
        game.create_grid()
        game.create_panel()
        shape.drop()
        create_drop_zone(Tetris.drop_zone_x, Tetris.drop_zone_y)
    else:
        end = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
exit()