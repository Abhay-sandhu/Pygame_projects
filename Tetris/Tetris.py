#imports
from random import choice
from pygame.sprite import Group
from pygame import image, transform, sprite, key, K_LEFT, K_RIGHT, K_DOWN, time 

class Block(sprite.Sprite):
    COLORS = ([1,2,3,4])
    COLOR_BLOCK_DICT = {
            1: image.load('Tetris/assets/1.png'),
            2: image.load('Tetris/assets/2.png'),
            3: image.load('Tetris/assets/3.png'),
            4: image.load('Tetris/assets/4.png')
            }
    def __init__(self, game, row, col):
        super().__init__()
        self.game = game
        self.color = choice(Block.COLORS)
        self.image = transform.scale(Block.COLOR_BLOCK_DICT[self.color], (self.game.block_size, self.game.block_size))
        self.rect = self.image.get_rect()
        self.rect.x = col * game.block_size
        self.rect.y = row * game.block_size
  
    
    def draw(self, rect_x, rect_y):
        self.game.screen.blit(self.image, (rect_x * self.game.block_size, rect_y * self.game.block_size))
    
    def update(self):
        pass

# Shape Class
class Shape():
    # All Possible Shapes
    TETRONIMOS = {
        'I': [[(0,1),(0,0),(0,-1),(0,-2)]],# [(-1,1),(0,1),(1,1),(2,1)]],
        'Z': [[(-1,1),(0,1),(0,0),(1,0)]],# [(0,1),(0,0),(-1,0),(-1,-1)]],
        'S': [[(0,1),(-1,1),(-1,0),(-2,0)]],# [(-1,1),(-1,0),(0,0),(0,-1)]],
       # 'L': [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
       # 'J': [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
       # 'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        'O': [[(-1,1),(0,1),(-1,0),(0,0)]]
    }
    SHAPES = ['I', 'Z', 'S', 'O']
    def __init__(self, game):
        self.game = game
        self.type = choice(Shape.SHAPES)
        self.shape = Shape.TETRONIMOS[self.type]
        self.row = -1
        self.col = self.game.cols//2
        self.blocks = []
        self.block = Block(self.game, self.row, self.col)
        self.delay = 100
        self.time = 0

    def draw(self):
        for i in range(len(self.shape[0])):
            block_rect = self.block.rect.copy()
            block_rect.x = self.col + self.shape[0][i][0]
            block_rect.y = self.row + self.shape[0][i][1]            
            self.block.draw(block_rect.x, block_rect.y)
            self.blocks.append(block_rect)
        self.blocks = self.blocks[-len(self.shape[0]):]

    def move(self):
        bottom = max([block.y for block in self.blocks])
        if self.time_delta() and bottom < self.game.rows -1:
            self.row += 1
    
    def control(self):
        keys = key.get_pressed()           
        if keys[K_DOWN] and self.row < self.game.rows:
            self.row += 1
        elif keys[K_LEFT] and self.col > 0 and self.row < self.game.rows - 2:
            self.col -= 1
        elif keys[K_RIGHT] and self.col < self.game.cols and self.row < self.game.rows -2:
            self.col += 1

    def time_delta(self):
        time_now = time.get_ticks()
        if time_now - self.time > self.delay:
            self.time = time_now
            return True
        return False

    def update(self):
        self.draw()
        self.move()

# Game Class
class Master():
    def __init__(self, game):
        self.next = None
        self.shape = None
        self.generate_shape()    
    def generate_shape(self):
        if self.next is None:
            self.next = self.game.shape
        self.shape = self.next
        self.next = Shape()


