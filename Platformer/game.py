import pygame
import settings as s
class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.block_size = s.BLOCK_SIZE
        self.width = s.WIDTH
        self.height = s.HEIGHT
        self.rows = s.ROWS
        self.cols = s.COLS
        self.score = 0
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('PLATFORMER!')
        self.clock = pygame.time.Clock()
        

        self.font = pygame.font.Font(None, 40)
        self.font.set_bold(True)
        self.win_label = self.font.render('YOU WIN!', 1, s.GREEN)
        self.lose_label = self.font.render('YOU LOSE!', 1, s.RED)

        self.new_game()

    def new_game(self):
        pass


    def draw_grid(self):
        [pygame.draw.line(self.screen, s.GRID_COLOR, (x * self.block_size, 0), (x * self.block_size, self.height))  for x in range(0, self.cols)]
        [pygame.draw.line(self.screen, s.GRID_COLOR, (0, y * self.block_size), (self.width, y * self.block_size)) for y in range(0, self.rows)]


    def update(self):
        pygame.display.update()
        self.clock.tick(s.FPS)


    def draw(self):
        self.screen.fill(s.BLACK)
        self.draw_grid()
        score_text = self.font.render(f"SCORE: {self.score}", 1, s.WHITE)
        self.screen.blit(score_text, (self.width/2 - score_text.get_width()/2, 10))


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