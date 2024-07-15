import pygame
from pygame import transform, image, key, K_SPACE, KEYUP, KEYDOWN, Rect, draw, Color, font, mixer, sprite
import random


class Main(sprite.Sprite):
    def __init__(self, screen, file, x, y, speed):
        self.screen = screen
        self.image = transform.scale(image.load(file), (100, 80))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


class Bird(Main):
    def __init__(self, screen, file, x, y, speed):
        super().__init__(screen, file, x, y, speed)
        self.angle = 0

    def control(self, flap):
        if flap and self.rect.y > 0:
            self.rect.y -= self.speed
            self.angle = 15
        elif self.rect.y < HEIGHT - bird.rect.height:
            self.rect.y += self.speed
            self.angle = min(-15, self.angle + self.speed)
    def update(self):
        rotated_image = transform.rotate(self.image, self.angle)
        self.screen.blit(rotated_image, (self.rect.x, self.rect.y))
        self.angle += self.speed
        self.angle = min(0, self.angle)


class Pipe(sprite.Sprite):
    def __init__(self, screen, file, x, y, speed):
        self.screen = screen
        self.width = 100
        self.height = random.randint(10, 400)
        self.speed = speed
        self.top_image = transform.scale(image.load(file), (self.width, self.height))
        self.bottom_image = transform.rotate(transform.scale(image.load(file), (self.width, HEIGHT - self.height - 200)), 180)
        
        #self.top_pipe = Rect(x, y, self.width, self.height)
        #self.bottom_pipe = Rect(x, y + self.height + 200, self.width, HEIGHT - self.height - 200)
        
        self.top_pipe = self.top_image.get_rect()
        self.top_pipe.x = x
        self.top_pipe.y = y

        self.bottom_pipe = self.top_image.get_rect()
        self.bottom_pipe.x = x
        self.bottom_pipe.y = y + self.height + 200

    def update(self):
        global score
        self.top_pipe.x -= self.speed
        self.bottom_pipe.x -= self.speed
        if self.top_pipe.x < -self.width:
            score += 1
            score_sound.play()
            self.reset()

    def draw_pipe(self):
        #draw.rect(self.screen, Color(255, 255, 255, 255), self.top_pipe)
        #draw.rect(self.screen, Color(255, 255, 255, 255), self.bottom_pipe)

        self.screen.blit(self.top_image, (self.top_pipe.x, self.top_pipe.y))
        self.screen.blit(self.bottom_image, (self.bottom_pipe.x, self.bottom_pipe.y))

    def reset(self):
        if self.top_pipe.x < -self.width:
            self.top_pipe.x = WIDTH
            self.bottom_pipe.x = WIDTH
            self.height = random.randint(100, 300)


def collision_check( rect, top_pipe_rect, bottom_pipe_rect):
    if rect.colliderect (top_pipe_rect) or bird.rect.colliderect(bottom_pipe_rect):
            collision_sound.play()
            return True
    return False

pygame.init()
mixer.init()
font.init()

WIDTH = 700
HEIGHT = 650
FPS = 60
BIRD_SPEED = 5
PIPE_SPEED = 4
VOLUME = 0.05
score = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

background = transform.scale(
    image.load("Flappy_birds/assets/background.jpg"), (WIDTH, HEIGHT)
)

mixer.music.load('Flappy_birds/assets/A Short Walk With You.mp3')
mixer.music.set_volume(VOLUME * 0.5)
mixer.music.play(-1, 0, 4000)


score_sound = mixer.Sound('Flappy_birds/assets/sfx_point.wav')
collision_sound = mixer.Sound('Flappy_birds/assets/sfx_die.wav')
wing_flap_sound = mixer.Sound('Flappy_birds/assets/sfx_wing_flap.wav')

wing_flap_sound.set_volume(VOLUME * 0.5)
score_sound.set_volume(VOLUME)
collision_sound.set_volume(VOLUME)

bird = Bird(screen, "Flappy_birds/assets/bird2.png", 300, 200, BIRD_SPEED)
pipes = [Pipe(screen, "Flappy_birds/assets/pipe.png", WIDTH + i * 400, 0, PIPE_SPEED) for i in range(2)]

score_font = font.SysFont("Comic Sans MS", 25)

flap = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                flap = True
                wing_flap_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == K_SPACE:
                flap = False

    screen.blit(background, (0, 0))
    bird.control(flap)
    bird.update() 
    for pipe in pipes:
        pipe.draw_pipe()
        pipe.update()
        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (100, 10))
        if collision_check(bird.rect, pipe.top_pipe, pipe.bottom_pipe):
            pygame.time.wait(int(collision_sound.get_length() * 1000))
            print(f"GAME OVER\nSCORE:{score}")
            run = False
    if bird.rect.y >= HEIGHT - bird.rect.height or bird.rect.y <= 0:
        print(f"GAME OVER\nSCORE:{score}")
        collision_sound.play()
        pygame.time.wait(int(collision_sound.get_length() * 1000))
        run = False

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
