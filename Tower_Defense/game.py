import pygame
from pygame import font, mixer, time, display, sprite, image, Rect
from enemy import Enemy
from buttons import Button
from turrets import Turret
from world import World
from settings import *


class Game:
    def __init__(self):

        pygame.init()
        mixer.init()
        font.init()

        self.screen = display.set_mode((WIDTH + SIDE_PANEL, HEIGHT))
        display.set_caption("Tower of the Defender")
        display.set_icon(image.load(GAME_LOGO))

        self.clock = time.Clock()
        self.font = font.SysFont("Comic Sans MS", 40, bold=True)
        self.font_small = font.SysFont("Comic Sans MS", 20)
        self.new_game()

    def new_game(self):
        self.world = World(self)
        self.button_group = sprite.Group()
        self.add_buttons()
        self.enemy_group = sprite.Group()
        self.turret_group = sprite.Group()
        self.enemy_group.add(Enemy(self))

    def add_buttons(self):
    
        self.buy_turret_btn = Button(self, BUY_TURRET_BTN, (WIDTH + SIDE_PANEL/2, 100))
        self.upgrade_turret_btn = Button(self, UPGRADE_TURRET_BTN , (WIDTH + SIDE_PANEL/2, 200))
        self.cancel_btn = Button(self, CANCEL_BTN, (WIDTH + SIDE_PANEL/2, 300))
        self.fast_forward_btn = Button(self, FAST_FORWARD_BTN, (WIDTH + SIDE_PANEL/2, 400))
        self.restart_btn = Button(self, RESTART_BTN, (WIDTH + SIDE_PANEL/2, 500))
        self.start_btn = Button(self, START_BTN, (WIDTH + SIDE_PANEL/2, 600))
        self.button_group.add([self.buy_turret_btn, self.upgrade_turret_btn, self.cancel_btn, self.fast_forward_btn, self.restart_btn, self.start_btn])

    def create_turret(self, mouse_pos):
        mouse_tile = (mouse_pos[0]//TILE_SIZE, mouse_pos[1]//TILE_SIZE)
        mouse_tile_index = (mouse_tile[1] * COLS) + mouse_tile[0]
        if self.world.tile_map[mouse_tile_index] == 7 and mouse_pos[0] < WIDTH:
            space_is_free = True
            for existing_turret in self.turret_group:
                if mouse_tile == existing_turret.tile:
                    space_is_free = False
            if space_is_free:
                turret = Turret(self, mouse_tile)
                self.turret_group.add(turret)


    def highlight_grid(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < WIDTH:
            mouse_tile = (mouse_pos[0]//TILE_SIZE, mouse_pos[1]//TILE_SIZE)
            mouse_tile_index = (mouse_tile[1] * COLS) + mouse_tile[0]
            left_top = (mouse_tile[0] * TILE_SIZE, mouse_tile[1] * TILE_SIZE)
            grid = Rect(left_top, (TILE_SIZE, TILE_SIZE))
            if self.world.tile_map[mouse_tile_index] == 7:
                space_is_free = True
                for existing_turret in self.turret_group:
                    if mouse_tile == existing_turret.tile:
                        space_is_free = False
                if space_is_free:
                    pygame.draw.rect(self.screen, HIGHLIGHT_GRID_VALID, grid, 2, 5)
                else:
                    pygame.draw.rect(self.screen, HIGHLIGHT_GRID_FILLED, grid, 2, 5)
            else:
                pygame.draw.rect(self.screen, HIGHLIGHT_GRID_INVALID, grid, 2, 5)


    def update(self):
        self.enemy_group.update()
        self.highlight_grid()
        display.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(BG_COLOR)
        pygame.draw.line(self.screen, WHITE, (WIDTH, 0), (WIDTH, HEIGHT), 4)
        self.world.draw()
        self.turret_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.button_group.draw(self.screen)
        

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
                self.button_group.update()

    def run(self):
        while True:
            self.event_handler()
            self.draw()
            self.update()


if __name__ == "__main__":
    game = Game()
    game.run()
