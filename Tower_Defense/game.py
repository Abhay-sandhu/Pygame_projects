import pygame
from pygame import font, mixer, time, display, sprite, image, Rect
from enemy import Enemy
from turrets import Turret
from world import World
from settings import *


class Game:
    def __init__(self):

        pygame.init()
        mixer.init()
        font.init()

        self.screen = display.set_mode((WIDTH, HEIGHT))
        display.set_caption("Tower of the Defender")
        display.set_icon(image.load(GAME_LOGO))

        self.clock = time.Clock()
        self.font = font.SysFont("Comic Sans MS", 40, bold=True)
        self.font_small = font.SysFont("Comic Sans MS", 20)
        self.new_game()

    def new_game(self):
        self.world = World(self)
        self.enemy_group = sprite.Group()
        self.turret_group = sprite.Group()
        self.enemy_group.add(Enemy(self))

    def create_turret(self, mouse_pos):
        mouse_tile = (mouse_pos[0]//TILE_SIZE, mouse_pos[1]//TILE_SIZE)
        if self.world.tile_data[mouse_tile[0]][mouse_tile[1]] in [6,7]:
            turret = Turret(self, mouse_tile)
            self.turret_group.add(turret)


    def highlight_grid(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_tile = (mouse_pos[0]//TILE_SIZE, mouse_pos[1]//TILE_SIZE)
        left_top = (mouse_tile[0] * TILE_SIZE, mouse_tile[1] * TILE_SIZE)
        grid = Rect(left_top, (TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(self.screen, HIGHLIGHT_GRID, grid, 2, 5)

    def update(self):
        self.enemy_group.update()
        self.turret_group.update()
        self.highlight_grid()
        display.update()
        self.clock.tick(FPS)

    def draw(self):
        self.world.draw()
        self.turret_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        

    def event_handler(self):
        for event in pygame.event.get():

            # quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # add turret
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                self.create_turret(mouse_pos)

    def run(self):
        while True:
            self.event_handler()
            self.draw()
            self.update()


if __name__ == "__main__":
    game = Game()
    game.run()
