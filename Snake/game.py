import pygame
from Snake import Snake, Food

class Game():

    RED = pygame.Color(255, 0, 0, 255)     # Fully opaque red
    GREEN = pygame.Color(0, 255, 0, 255)   # Fully opaque green
    BLUE = pygame.Color(0, 0, 255, 255)    # Fully opaque blue
    WHITE = pygame.Color(255, 255, 255, 255) # Fully opaque white
    GRID_COLOR = pygame.Color(55, 55, 55, 255)
    BLACK = pygame.Color(0,0,0,255) # black

    FPS = 60
    VOLUME = 0.5
    WIDTH = 800
    HEIGHT = 600
    BLOCK_SIZE = 25
    ROWS = HEIGHT // BLOCK_SIZE
    COLS = WIDTH // BLOCK_SIZE

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.block_size = Game.BLOCK_SIZE
        self.width = Game.WIDTH
        self.height = Game.HEIGHT
        self.rows = Game.ROWS
        self.cols = Game.COLS
        self.score = 0
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('SNAKE!')
        self.clock = pygame.time.Clock()
        
        self.food_sound = pygame.mixer.Sound('Snake/assets/food.mp3')
        self.move_sound = pygame.mixer.Sound('Snake/assets/move.mp3')
        self.game_over_sound = pygame.mixer.Sound('Snake/assets/gameover.mp3')

        self.game_over_sound.set_volume(Game.VOLUME)
        self.food_sound.set_volume(Game.VOLUME)
        self.move_sound.set_volume(Game.VOLUME)

        self.font = pygame.font.Font(None, 40)
        self.font.set_bold(True)
        self.win_label = self.font.render('YOU WIN!', 1, Game.GREEN)
        self.lose_label = self.font.render('YOU LOSE!', 1, Game.RED)
        self.play_bgm()
        self.new_game()

    def new_game(self):
        self.snake = Snake(self)
        self.food = Food(self)
        self.score = 0
    
    def play_bgm(self):
        pygame.mixer.music.load('Snake/assets/music.mp3')
        pygame.mixer.music.set_volume(Game.VOLUME * 0.3)
        pygame.mixer.music.play()
    def draw_grid(self):
        [pygame.draw.line(self.screen, Game.GRID_COLOR, (x * self.block_size, 0), (x * self.block_size, self.height))  for x in range(0, self.cols)]
        [pygame.draw.line(self.screen, Game.GRID_COLOR, (0, y * self.block_size), (self.width, y * self.block_size)) for y in range(0, self.rows)]
    
    def update(self):
        pygame.display.update()
        self.clock.tick(Game.FPS)
        self.snake.update()

    def draw(self):
        self.screen.fill(Game.BLACK)
        self.draw_grid()
        score_text = self.font.render(f"SCORE: {self.score}", 1, Game.WHITE)
        self.screen.blit(score_text, (self.width/2 - score_text.get_width()/2, 10))
        self.snake.draw()
        self.food.draw()
    
    def event_check(self, run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return run
            self.snake.control(event)
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