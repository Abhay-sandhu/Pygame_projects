import pygame
from pygame import sprite
import Coin_Maze
from Coin_Maze import COINS
Coin_Maze.game_init()

RED = (255, 0, 0, 255)     # Fully opaque red
GREEN = (0, 255, 0, 255)   # Fully opaque green
BLUE = (0, 0, 255, 255)    # Fully opaque blue
WHITE = (255, 255, 255, 255) # Fully opaque white

COINS = 0
FPS = 60
VOLUME = 0.03
WIDTH = 800
HEIGHT = 600
WALL_COLOR = pygame.Color(52, 82, 63, 255)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('COIN MAZE!!!')
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load('Coin_Maze/assets/background.jpg'), (WIDTH,HEIGHT))

font = pygame.font.Font(None, 30)
font.set_bold(True)
win_text = font.render('YOU WIN!', 1, GREEN)
lose_text = font.render('YOU LOSE!', 1, RED)
coin_text = font.render(f'COINS: {COINS}', 1, WHITE)

pygame.mixer.music.load('Coin_Maze/assets/cave.mp3')
pygame.mixer.music.set_volume(VOLUME * 0.66)
pygame.mixer.music.play(-1, 0, 1000)

coin_sound = pygame.mixer.Sound('Coin_Maze/assets/sfx_point.wav')
lose_sound = pygame.mixer.Sound('Coin_Maze/assets/lose.wav')
win_sound = pygame.mixer.Sound('Coin_Maze/assets/win.wav')

coin_sound.set_volume(VOLUME)
lose_sound.set_volume(VOLUME)
win_sound.set_volume(VOLUME)

player = Coin_Maze.Player('Coin_Maze/assets/miner.png', screen, 50, 50, 5)
#ghost = Coin_Maze.Enemy('Coin_Maze/assets/ghost.png', screen, 200, 200, 4)
coins = Coin_Maze.Coins('Coin_Maze/assets/dollar.png', screen)
wall = Coin_Maze.Walls(screen, WALL_COLOR, 400, 400, 20, 200)

end = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if end != True:
        screen.blit(background, (0,0))
        screen.blit(coin_text, (WIDTH - 150, 20))
        coins.draw_coin()
        wall.build_wall()
        #game code


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
exit()