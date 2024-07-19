#imports
from random import choice
from pygame.sprite import Group
from pygame import display, image, transform, draw, sprite, key, Color, K_LEFT, K_RIGHT, K_DOWN, time 

class Block(sprite.Sprite):
    COLORS = iter([1,2,3,4])
    COLOR_BLOCK_DICT = {
            1: image.load('Tetris/assets/1.png'),
            2: image.load('Tetris/assets/2.png'),
            3: image.load('Tetris/assets/3.png'),
            4: image.load('Tetris/assets/4.png')
            }
    def __init__(self, game, row, col,):
        super().__init__()
        self.color = next(Block.COLORS)
        self.image = transform.scale(image.load('Tetris/assets/block.png'), (game.block_size, game.block_size))
        self.rect = self.image.get_rect()
        self.rect.x = col * game.block_size
        self.rect.y = row * game.block_size

# Shape Class
class Shape():
    # All Possible Shapes
    VERSION = {
        'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
        'Z': [[4, 5, 9, 10], [2, 6, 5, 9]],
        'S': [[6, 7, 9, 10], [1, 5, 6, 10]],
        'L': [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J': [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        'O': [[1, 2, 5, 6]]
    }
    SHAPES = ['I', 'Z', 'S', 'L', 'J', 'T', 'O']
    def __init__(self):
        self.type = choice(Shape.SHAPES)
        self.shape = choice(Shape.VERSION[self.type])
        self.images = []
        self.rects = []
    def draw(self):
        pass

# Game Class
class Master():
    def __init__(self):
        self.next = None

    
    def generate_shape(self):
        if self.next is None:
            self.next = Shape()
        self.figure = self.next
        self.next = Shape()
        #color,block,type,shape


