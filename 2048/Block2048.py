import pygame

vec2d = pygame.math.Vector2

class Block(pygame.sprite.Sprite):
    BLOCK_COLOR = (235, 235, 235, 255)
    BLOCK_BORDER = (200, 200, 200, 255)
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.width = self.game.width//4
        self.height = self.game.height//4
        self.color = Block.BLOCK_COLOR
        self.border_color = Block.BLOCK_BORDER
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.delay = 100
        self.time = 0
    
    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)
        pygame.draw.rect(self.game.screen, self.border_color, self.rect, width=2)
        font = self.game.font.render('1', 1, (255,255,255,255))
        self.game.screen.blit(font, (self.rect.centerx - font.get_width()/2, self.rect.centery - font.get_height()/2))

    def time_delta(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.delay:
            self.time = time_now
            return True
        return False

    def control(self):
        if self.time_delta():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.rect.move_ip(0, -self.game.block.height)
            if keys[pygame.K_DOWN]:
                self.rect.move_ip(0, self.game.block.height)
            if keys[pygame.K_LEFT]:
                self.rect.move_ip(-self.game.block.width, 0)
            if keys[pygame.K_RIGHT]:
                self.rect.move_ip(self.game.block.width, 0)


    def update(self):
        self.draw()

class Grid():
    GRID_COLOR = (220, 220, 220, 255)
    ROWS = 4
    COLS = 4
    def __init__(self, game):
        self.game = game
        self.color = Grid.GRID_COLOR
        self.rows = Grid.ROWS
        self.cols = Grid.COLS
        self.blocks = []
    
    def draw_grid(self):
        [pygame.draw.line(self.game.screen, self.color, (x * self.game.block.width,0), (x * self.game.block.width,self.game.height), 5) for x in range(self.cols + 1)]
        [pygame.draw.line(self.game.screen, self.color, (0,y * self.game.block.width), (self.game.width,y * self.game.block.width), 5) for y in range(self.rows)]

    def update(self):
        self.draw_grid()