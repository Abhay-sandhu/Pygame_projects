import pygame
from pygame import image, transform, font, mixer, time, display, sprite, event
from Enemy import Enemy
from settings import *

class Game():
    def __init__(self):

        pygame.init()
        mixer.init()
        font.init()

        self.screen = display.set_mode((WIDTH, HEIGHT))
        display.set_caption("Tower of the Defender")

        self.clock = time.Clock()
        self.font = font.SysFont("Comic Sans MS", 40, bold=True)
        self.font_small = font.SysFont("Comic Sans MS", 20)
        self.new_game()

    def new_game(self):
        self.level = transform.scale(image.load(LEVEL_1), (WIDTH, HEIGHT))
        self.enemy_group = sprite.Group()
        self.enemy = Enemy(self)
        self.enemy_group.add(self.enemy)
        print(self.enemy, self.enemy_group)
    def update(self):
        self.enemy_group.update()
        display.update()
        self.clock.tick(FPS)
    
    def draw(self):
        self.screen.blit(self.level, (0,0))
        self.enemy_group.draw(self.screen)

    def event_handler(self):
        for e in event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
    
    def run(self):
        while True:
            self.event_handler()
            self.draw()
            self.update()

if __name__ == "__main__":
    game = Game()
    game.run()