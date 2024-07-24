import pygame
import settings as s
import sys

class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
        pygame.display.set_caption("PLATFORMER")
        self.clock = pygame.time.Clock()

    def update(self):
        pygame.display.update()
        self.clock.tick(s.FPS)

    def draw(self):
        self.screen.fill(s.WHITE)
    
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        self.running = True
        while self.running:
            self.event_handler()
            self.draw()
            self.update()

if __name__ == "__main__":
    game = Game()
    game.run