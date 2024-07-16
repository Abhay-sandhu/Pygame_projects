import pygame
from random import randint
import Coin_Maze

Coin_Maze.game_init()

RED = (255, 0, 0, 255)     # Fully opaque red
GREEN = (0, 255, 0, 255)   # Fully opaque green
BLUE = (0, 0, 255, 255)    # Fully opaque blue
WHITE = (255, 255, 255, 255) # Fully opaque white

COINS = 0
FPS = 60
VOLUME = 0.03
WIDTH = 820
HEIGHT = 600
WALL_COLOR = pygame.Color(52, 82, 63, 255)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('COIN MAZE!!!')
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load('Coin_Maze/assets/background.jpg'), (WIDTH,HEIGHT))

font = pygame.font.Font(None, 40)
font.set_bold(True)
win_text = font.render('YOU WIN!', 1, GREEN)
lose_text = font.render('YOU LOSE!', 1, RED)


pygame.mixer.music.load('Coin_Maze/assets/cave.mp3')
pygame.mixer.music.set_volume(VOLUME * 0.66)
pygame.mixer.music.play(-1, 0, 1000)

coin_sound = pygame.mixer.Sound('Coin_Maze/assets/sfx_point.wav')
lose_sound = pygame.mixer.Sound('Coin_Maze/assets/lose.wav')
win_sound = pygame.mixer.Sound('Coin_Maze/assets/win.wav')

coin_sound.set_volume(VOLUME)
lose_sound.set_volume(VOLUME)
win_sound.set_volume(VOLUME)

player = Coin_Maze.Player(35, 50, 5)
ghost = Coin_Maze.Enemy(WIDTH - 200, 225, 6)
wallet = Coin_Maze.Player(WIDTH - 75, HEIGHT - 75, 0, 'Coin_Maze/assets/bitcoin.png')

def create_walls():
    # Coin_Maze.Border(Color, x, y, width, height)
    w1 = Coin_Maze.Border(WALL_COLOR,0,0,WIDTH,10) # top wall
    w2 = Coin_Maze.Border(WALL_COLOR,0,HEIGHT-10,WIDTH,10) #bottom wall
    w3 = Coin_Maze.Border(WALL_COLOR,0,0,10,HEIGHT) # left wall
    w4 = Coin_Maze.Border(WALL_COLOR,WIDTH-10,0,10,HEIGHT) # right wall
    w5 = Coin_Maze.Border(WALL_COLOR,90,0,10,HEIGHT - 90) # vertical left wall 1
    w6 = Coin_Maze.Border(WALL_COLOR,180,80,10, HEIGHT - 80) # vertical left wall 1
    w7 = Coin_Maze.Border(WALL_COLOR,270,300,10,HEIGHT - 300) # vertical left wall 3 bottom
    w8 = Coin_Maze.Border(WALL_COLOR,270,10,10,200) # vertical left wall 3 top
    w9 = Coin_Maze.Border(WALL_COLOR,360,10,10,200) # vertical left wall 4 top
    w10 = Coin_Maze.Border(WALL_COLOR,450,100,10,110) # vertical left wall 5 top
    w11 = Coin_Maze.Border(WALL_COLOR,540,10,10,200) # vertical left wall 6 top
    w12 = Coin_Maze.Border(WALL_COLOR,630,100,10,110) # vertical left wall 7 top
    w13 = Coin_Maze.Border(WALL_COLOR,720,10,10,200) # vertical left wall 8 top
    w14 = Coin_Maze.Border(WALL_COLOR,720,300,10,HEIGHT - 300) # vertical left wall 9 bottom
    w15 = Coin_Maze.Border(WALL_COLOR,360,300,360,10) # Horizontal wall 1
    w16 = Coin_Maze.Border(WALL_COLOR,270,400,360,10) # Horizontal wall 2
    w17 = Coin_Maze.Border(WALL_COLOR,360,500,360,10) # Horizontal wall 3

    return [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17]

def create_coins():
    c1 = Coin_Maze.Coins(randint(50,WIDTH-20),randint(50,HEIGHT-20))
    c2 = Coin_Maze.Coins(randint(50,WIDTH-20),randint(50,HEIGHT-20))
    c3 = Coin_Maze.Coins(randint(50,WIDTH-20),randint(50,HEIGHT-20))
    c4 = Coin_Maze.Coins(randint(50,WIDTH-20),randint(50,HEIGHT-20))
    c5 = Coin_Maze.Coins(randint(50,WIDTH-20),randint(50,HEIGHT-20))
    c6 = Coin_Maze.Coins(randint(50,WIDTH-20),randint(50,HEIGHT-20))
    c7 = Coin_Maze.Coins(randint(50,WIDTH-20),randint(50,HEIGHT-20))
    c8 = Coin_Maze.Coins(randint(50,WIDTH-20),randint(50,HEIGHT-20))

    return [c1,c2,c3,c4,c5,c6,c7,c8]

coins = create_coins()
walls = create_walls()

end = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if end != True:
        screen.blit(background, (0,0))
        wallet.update()
        player.control()
        ghost.update()
        
        for w in walls:
            w.build_wall()
            if pygame.sprite.collide_rect(player, w):
                end = True
                lose_sound.play()
                screen.blit(lose_text, ((WIDTH - lose_text.get_width()) // 2, ((HEIGHT - lose_text.get_height()) // 2)- 20))


        for c in coins:
            c.draw_coin()
            if c.rect.colliderect(player.rect):
                coins.remove(c)
                coin_sound.play()
                COINS += 1
                c.kill()
        coin_text = font.render(f'COINS: {COINS}', 1, WHITE)
        screen.blit(coin_text, (WIDTH - 150, 20))
        
        if pygame.sprite.collide_rect(player, wallet) and COINS == 8:
            end = True
            win_sound.play()
            screen.blit(win_text, ((WIDTH - win_text.get_width()) // 2, ((HEIGHT - win_text.get_height()) // 2)) - 20)

        if pygame.sprite.collide_rect(player, ghost):
            end = True
            lose_sound.play()
            screen.blit(lose_text, ((WIDTH - lose_text.get_width()) // 2, ((HEIGHT - lose_text.get_height()) // 2)- 20))

        
        player.game_end()
        ghost.game_end()
        wallet.game_end()

    else:
        end = False
        for c in coins:
            c.kill()
        coins = create_coins()
        player = Coin_Maze.Player(35, 50, 5)
        pygame.time.delay(1000)
        COINS = 0
        coin_text = font.render(f'COINS: {COINS}', 1, WHITE)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
exit()