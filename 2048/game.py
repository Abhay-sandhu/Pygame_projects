import pygame
from Block2048 import Block, Grid

class Game():

    WIDTH = 500
    HEIGHT = 500
    FPS = 60
    BG_COLOR = (250, 250, 250, 255)
    def __init__(self):
        
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.width = Game.WIDTH
        self.height = Game.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('2048')
        self.color = Game.BG_COLOR
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 40, bold=True)
        self.score = 0
        self.new_game()
    def new_game(self):
        self.score = 0
        self.grid = Grid(self)
        self.block = Block(self)

    def update(self):
        self.block.update()
        self.grid.update()
        pygame.display.update()
        self.clock.tick(Game.FPS)

    def draw(self):
        self.screen.fill(self.color)

    def event_handler(self,run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return run
        self.block.control()
        return run

    def run(self):
        run = True
        while run:
            run = self.event_handler(run)
            self.draw()
            self.update()
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = Game()
    game.run()