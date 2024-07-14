import pygame
from pygame import transform, image, key, Color, K_UP, K_DOWN, K_w, K_s

pygame.init()

WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 8
BALL_RADIUS = 10
BALL_SPEED_X = 10
BALL_SPEED_Y = 10
FPS = 60
WHITE = Color(255, 255, 255, 255)

player1_x, player1_y = 10, HEIGHT/2
player2_x, player2_y = WIDTH - PADDLE_WIDTH - 10, HEIGHT/2
score1,score2 = 0,0
ball_x = WIDTH // 2 - BALL_RADIUS // 2
ball_y = HEIGHT // 2 - BALL_RADIUS // 2


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG!")
clock = pygame.time.Clock()
background = transform.scale(image.load("Pong/assets/bricks_background.jpg"), (WIDTH, HEIGHT))
myfont = pygame.font.SysFont("Comic Sans MS", 36)


# draw paddle
def draw_paddle(x, y):
    return pygame.draw.rect(screen, WHITE, (x, y, PADDLE_WIDTH, PADDLE_HEIGHT))


# draw ball
def draw_ball(x,y):
    return pygame.draw.circle(screen, WHITE, (x,y), BALL_RADIUS)


# update ball
def update_ball():
    global ball_x, ball_y, BALL_SPEED_Y, BALL_SPEED_X, BALL_RADIUS, score1, score2

    # bounce against wall
    if (HEIGHT - BALL_RADIUS) < ball_y or ball_y < (BALL_RADIUS) :
        BALL_SPEED_Y *= -1

    # bounce against paddle
    if ball_x <= player1_x + PADDLE_WIDTH and player1_y <= ball_y <= player1_y + PADDLE_HEIGHT:
        BALL_SPEED_X *= -1
    if ball_x >= player2_x and player2_y <= ball_y <= player2_y + PADDLE_HEIGHT:
        BALL_SPEED_X *= -1

    ball_x += BALL_SPEED_X
    ball_y += BALL_SPEED_Y
    ball = draw_ball(ball_x, ball_y)

    if ball_x > WIDTH:
        score1 += 1
    elif ball_x < 0:
        score2 += 1

    return ball


# reset ball'
def reset_ball():
    global ball_x, ball_y, BALL_SPEED_X, BALL_RADIUS

    if WIDTH < ball_x or ball_x < 0:
        ball_x = WIDTH // 2 - BALL_RADIUS // 2
        ball_y = HEIGHT // 2 - BALL_RADIUS // 2
        BALL_SPEED_X *= -1

# Game Loop


run = True
while run:

    # draw assets
    screen.blit(background, (0, 0))
    paddle1 = draw_paddle(player1_x, player1_y)
    paddle2 = draw_paddle(player2_x, player2_y)
    ball = update_ball()
    reset_ball()
    
    # update score
    screen.blit(myfont.render(f"{score1}", 1, WHITE), (WIDTH / 4, 10))
    screen.blit(myfont.render(f"{score2}", 1, WHITE), ((WIDTH * 3 / 4 - 15), 10))
    #BALL_SPEED_X += 0.05
    #BALL_SPEED_Y += 0.05
    # quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    # events
    keys = key.get_pressed()
    if keys[K_w] and player1_y > 1:
        player1_y -= PADDLE_SPEED
    if keys[K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += PADDLE_SPEED
    
    if keys[K_UP] and player2_y > 1:
        player2_y -= PADDLE_SPEED
    if keys[K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += PADDLE_SPEED

    # Win Condition
    if score1 == 10:
        print("Player 1 wins!")
        run = False
    elif score2 == 10:
        print("Player 2 wins!")
        run = False
    
    pygame.display.update()
    clock.tick(FPS)