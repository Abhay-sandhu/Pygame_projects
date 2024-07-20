import pygame
from TowerDefense import Enemy
from settings import *

class Game():
    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tower of the Defender")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Comic Sans MS", 40, bold=True)
        self.font_small = pygame.font.SysFont("Comic Sans MS", 20)
        self.new_game()

    def new_game(self):
        self.enemy = Enemy(self)

    def update(self):
        self.enemy.update()
        pygame.display.update()
        self.clock.tick(FPS)
    
    def draw(self):
        self.screen.fill((150, 100, 200, 200))

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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