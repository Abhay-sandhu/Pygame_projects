import pygame

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