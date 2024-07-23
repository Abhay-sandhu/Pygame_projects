from tkinter import W
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
        self.font = font.SysFont("Consolas", 24, bold=True)
        self.font_large = font.SysFont("Comic Sans MS", 36)

        self.shot_sound = mixer.Sound(SHOT_SOUND)
        self.shot_sound.set_volume(SHOT_VOLUME)

        self.new_game()

    def new_game(self):
        
        self.level_started = False
        self.placing_turrets = False
        self.selected_turret = None
        self.last_enemy_spawned = pygame.time.get_ticks()

        self.world = World(self)
        self.add_buttons()
        self.enemy_group = sprite.Group()
        self.turret_group = sprite.Group()

    def add_buttons(self):
        self.buy_turret_btn = Button(self, BUY_TURRET_BTN, (WIDTH + SIDE_PANEL/2 - 30, 120))
        self.upgrade_turret_btn = Button(self, UPGRADE_TURRET_BTN , (WIDTH + SIDE_PANEL/2, 220))
        #self.cancel_btn = Button(self, CANCEL_BTN, (WIDTH + SIDE_PANEL/2, 300))
        self.fast_forward_btn = Button(self, FAST_FORWARD_BTN, (WIDTH + SIDE_PANEL/2, 400))
        self.restart_btn = Button(self, RESTART_BTN, (WIDTH + SIDE_PANEL/2, 480))
        self.start_btn = Button(self, START_BTN, (WIDTH + SIDE_PANEL/2, 400))

    def draw_text(self, text, font, color, x,y):
        rendered_text = font.render(text, 1, color)
        self.screen.blit(rendered_text, (x, y))

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
                self.world.money -= BUY_COST
                self.placing_turrets = False

    def select_turret(self, mouse_pos):
        mouse_tile = (mouse_pos[0]//TILE_SIZE, mouse_pos[1]//TILE_SIZE)
        for existing_turret in self.turret_group:
                if mouse_tile == existing_turret.tile:
                    return existing_turret

    def clear_selections(self):
        for turret in self.turret_group:
            turret.selected = False


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
        self.turret_group.update(self.enemy_group)
        if self.selected_turret:
            self.selected_turret.selected = True
        self.highlight_grid()
        
        if self.world.check_level_complete():
            self.level_started = False
            self.world.money += LEVEL_REWARD[self.world.level_number - 1]
            self.world.level_number += 1
            self.last_enemy_spawned = pygame.time.get_ticks()
            self.world.reset_level()
            self.world.process_enemies()

        display.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(BG_COLOR)
        pygame.draw.line(self.screen, WHITE, (WIDTH, 0), (WIDTH, HEIGHT), 4)
        self.world.draw()

        self.screen.blit(image.load(HEART).convert_alpha(), (WIDTH + 10, 10))
        self.screen.blit(image.load(COIN).convert_alpha(), (WIDTH + 10, 40))
        self.draw_text(f"HEALTH :{self.world.health}", self.font, (200, 40, 40), WIDTH + 50, 15)
        self.draw_text(f"MONEY :{self.world.money}", self.font, (255, 215, 0), WIDTH + 50, 46)
        
        self.screen.blit(image.load(COIN).convert_alpha(), (WIDTH + 20, 150))
        self.draw_text(f"COST {BUY_COST}", self.font, (255, 215, 0), WIDTH + 55, 157)
        
        
        if self.world.health <= 0:
            self.draw_text(f"GAME_OVER", self.font_large, (0,0,0,255), WIDTH//2 - 18* 8, HEIGHT//2 -18)
            pygame.time.delay(1500)
            self.new_game()

        for turret in self.turret_group:
            turret.draw(self.screen)
        self.enemy_group.draw(self.screen)
        
        if not self.level_started:
            if self.start_btn.draw():
                self.level_started = True
        else:
            if pygame.time.get_ticks() - self.last_enemy_spawned > SPAWN_COOLDOWN:
                if self.world.spawned_enemies < len(self.world.enemies_list):
                    enemy_type = self.world.enemies_list[self.world.spawned_enemies]
                    enemy = Enemy(self, enemy_type)
                    self.enemy_group.add(enemy)
                    self.world.spawned_enemies += 1
                    self.last_enemy_spawned = pygame.time.get_ticks()


        # buttons
        if self.restart_btn.draw():
            pass

        if self.buy_turret_btn.draw():
            self.placing_turrets = True

        if self.selected_turret:
            if self.selected_turret.level < MAX_LEVEL:
                self.screen.blit(image.load(COIN).convert_alpha(), (WIDTH + 20, 250))
                self.draw_text(f"COST {UPGRADE_COST}", self.font, (255, 215, 0), WIDTH + 55, 257)
                if self.upgrade_turret_btn.draw() and self.world.money >= UPGRADE_COST:
                    self.selected_turret.upgrade()
                    self.world.money -= UPGRADE_COST

        if self.world.money >= BUY_COST and self.placing_turrets and pygame.mouse.get_pos()[0] < WIDTH:
            cursor_turret = image.load(CURSOR_TURRET).convert_alpha()
            cursor_rect = cursor_turret.get_rect()
            cursor_rect.center = pygame.mouse.get_pos()
            self.screen.blit(cursor_turret, cursor_rect)
            

    def event_handler(self):
        for event in pygame.event.get():

            # quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # add turret
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
                mouse_pos = pygame.mouse.get_pos()
                if 0 < mouse_pos[0] < WIDTH and 0 < mouse_pos[1] < HEIGHT:
                    self.clear_selections()
                    if self.world.money >= BUY_COST and self.placing_turrets:
                        self.create_turret(mouse_pos)
                    else:
                        self.selected_turret = self.select_turret(mouse_pos)
                        
    def run(self):
        while True:
            self.event_handler()
            self.draw()
            self.update()


if __name__ == "__main__":
    game = Game()
    game.run()
