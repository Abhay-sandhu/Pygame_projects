import pygame
from pygame import transform, image, key, Color

pygame.init()

WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 50
BALL_RADIUS = 10
BALL_SPEED = 10
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG!")
clock = pygame.time.Clock()
background = transform.scale(image.load("Pong/assets/bricks_background.jpg"), (WIDTH, HEIGHT))
myfont = pygame.font.SysFont("Comic Sans MS", 18)
# draw paddle
def draw_paddle():
    paddle_1 = pygame.draw.rect(screen, Color(255, 255, 255, 255), (10, HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT))
    paddle_1 = pygame.draw.rect(screen, Color(255, 255, 255, 255), (WIDTH - PADDLE_WIDTH - 10, HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT))
# draw ball
def draw_ball():
    ball = pygame.draw.circle(screen, Color(255, 255, 255, 255), (WIDTH/2, HEIGHT/2), BALL_RADIUS)
# update ball
# reset ball

run = True
while run:
    screen.blit(background, (0, 0))
    draw_ball()
    draw_paddle()
    score1 = myfont.render("Score", 1, (0,0,0))
    score2 = myfont.render("Score", 1, (0,0,0))
    screen.blit(score1, (WIDTH / 3, 10))
    screen.blit(score2, ((WIDTH * 2 / 3), 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    # events and conditions

    pygame.display.update()
    clock.tick(FPS)