import pygame
from pygame import font, mixer, time, display, sprite, event
from enemy import Enemy
from world import World
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
        self.world = World(self)
        self.enemy_group = sprite.Group()
        self.enemy = Enemy(self)
        self.enemy_group.add(self.enemy)
        print(self.enemy, self.enemy_group)
    def update(self):
        self.enemy_group.update()
        display.update()
        self.clock.tick(FPS)
    
    def draw(self):
        self.world.draw()
        self.enemy_group.draw(self.screen)
        print(pygame.display.Info())

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