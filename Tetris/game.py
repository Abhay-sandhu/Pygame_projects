from random import randint
import pygame
from Tetris import Shape, Block, Master


class Game():
    RED = pygame.Color(255, 0, 0, 255)     # Fully opaque red
    GREEN = pygame.Color(0, 255, 0, 255)   # Fully opaque green
    BLUE = pygame.Color(0, 0, 255, 255)    # Fully opaque blue
    WHITE = pygame.Color(255, 255, 255, 255) # Fully opaque white
    BG_COLOR = pygame.Color(31, 25, 76, 255)
    GRID_COLOR = pygame.Color(31, 25, 132, 255)
    PANEL_COLOR = pygame.Color(25,25,25,255)
    SCORE = 0
    FPS = 60
    VOLUME = 0.03
    BLOCK_SIZE = 20
    WIDTH = 400
    HEIGHT = 560
    PANEL_SIZE = 160
    ROWS = (HEIGHT - PANEL_SIZE) // BLOCK_SIZE
    COLS = (WIDTH) // BLOCK_SIZE
    
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.block_size = Game.BLOCK_SIZE
        self.width = Game.WIDTH
        self.height = Game.HEIGHT
        self.panel_size = Game.PANEL_SIZE
        self.rows = Game.ROWS
        self.cols = Game.COLS
        self.score = 0
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tetris!')
        self.clock = pygame.time.Clock()
        
        #self.food_sound = pygame.mixer.Sound('Snake/assets/food.mp3')
        #self.move_sound = pygame.mixer.Sound('Snake/assets/move.mp3')
        #self.game_over_sound = pygame.mixer.Sound('Snake/assets/gameover.mp3')

        #self.game_over_sound.set_volume(Game.VOLUME)
        #self.food_sound.set_volume(Game.VOLUME)
        #self.move_sound.set_volume(Game.VOLUME)

        self.font = pygame.font.Font(None, 40)
        self.font.set_bold(True)
        self.win_label = self.font.render('YOU WIN!', 1, Game.GREEN)
        self.lose_label = self.font.render('YOU LOSE!', 1, Game.RED)
        #self.play_bgm()
        self.new_game()

    def new_game(self):
        self.score = 0
    
   # def play_bgm(self):
       # pygame.mixer.music.load('Snake/assets/music.mp3')
       # pygame.mixer.music.set_volume(Game.VOLUME * 0.3)
       # pygame.mixer.music.play()
    def draw_grid(self):
        [pygame.draw.line(self.screen, Game.GRID_COLOR, (x * self.block_size, 0), (x * self.block_size, self.height - self.panel_size)) for x in range(0, self.cols)]
        [pygame.draw.line(self.screen, Game.GRID_COLOR, (0, y * self.block_size), (self.width, y * self.block_size)) for y in range(0, self.rows + 1)]
    
    def draw_panel(self):
        pygame.draw.rect(self.screen, Game.PANEL_COLOR,(0, self.height - self.panel_size, self.width, self.panel_size))

    def update(self):
        pygame.display.update()
        self.clock.tick(Game.FPS)

    def draw(self):
        self.screen.fill(Game.BG_COLOR)
        self.draw_grid()
        self.draw_panel()
        score_text = self.font.render(f"SCORE: {self.score}", 1, Game.WHITE)
        self.screen.blit(score_text, (self.width - score_text.get_width() - 50, self.height - self.panel_size/2))

    
    def event_check(self, run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return run
        return run
    
    def run(self):
        run = True
        while run:
            run = self.event_check(run)
            self.draw()
            self.update()
        pygame.quit()
        exit()

if __name__ == "__main__":
    game = Game()
    game.run()