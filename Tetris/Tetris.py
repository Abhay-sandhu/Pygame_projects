#imports
from random import choice
from pygame.sprite import Group
from pygame import display, image, transform, draw, sprite, key, Color, K_LEFT, K_RIGHT, K_DOWN, time 

#Constants and variables
GREEN = Color(0, 255, 0, 255)
WIDTH = 400
HEIGHT = 560
BLOCK_SIZE = 20
PANEL_SIZE = 160
ROWS = ((HEIGHT- PANEL_SIZE)// 20) 
COLS = (WIDTH)//20
drop_zone_x = (WIDTH - BLOCK_SIZE * 4)//2
drop_zone_y = 0
GRID_COLOR = Color(31, 25, 132)
PANEL_COLOR = Color(25, 20, 122)
screen = display.set_mode((WIDTH, HEIGHT))


class Block(sprite.Sprite):
    COLORS = iter([1,2,3,4])
    COLOR_BLOCK_DICT = {
            1: image.load('Tetris/assets/1.png'),
            2: image.load('Tetris/assets/2.png'),
            3: image.load('Tetris/assets/3.png'),
            4: image.load('Tetris/assets/4.png')
            }
    def __init__(self, row, col,):
        super().__init__()
        self.color = next(Block.COLORS)
        self.image = transform.scale(image.load('Tetris/assets/block.png'), (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = col * BLOCK_SIZE
        self.rect.y = row * BLOCK_SIZE

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
        x = drop_zone_x
        y = drop_zone_y
        for cell in self.shape:
            img = transform.scale(self.block, (BLOCK_SIZE, BLOCK_SIZE))
            img_rect = img.get_rect()
            img_rect.x = x + (cell % 4) * BLOCK_SIZE
            img_rect.y = y + (cell // 4) * BLOCK_SIZE
            self.images.append(img)
            self.rects.append(img_rect)
            screen.blit(img, (img_rect.x, img_rect.y)) 
    def drop(self):
        global drop_zone_y
        x = drop_zone_x
        y = drop_zone_y
        drop_zone_y += BLOCK_SIZE
        for cell in self.shape:
            img = transform.scale(self.block, (BLOCK_SIZE, BLOCK_SIZE))
            img_rect = img.get_rect()
            img_rect.x = x + (cell % 4) * BLOCK_SIZE
            img_rect.y = y + (cell // 4) * BLOCK_SIZE
            self.images.append(img)
            self.rects.append(img_rect)
            screen.blit(img, (img_rect.x, img_rect.y)) 
        time.delay(1000)



# Game Class
class Game():
    def __init__(self):
        # Create gameboard
        self.grid = [[0 for x in range(COLS)] for y in range(ROWS)]
        self.score = 0
        self.next = None
        self.end = False
        
        
    # Create a grid
    def create_grid(self):
        for x in range(COLS):
            draw.line(screen, GRID_COLOR, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, HEIGHT - PANEL_SIZE))
        for y in range(ROWS):
            draw.line(screen, GRID_COLOR, (0, y * BLOCK_SIZE), (WIDTH, y * BLOCK_SIZE))
        
    def create_panel(self):
        draw.rect(screen, PANEL_COLOR,(0, HEIGHT - PANEL_SIZE, WIDTH, PANEL_SIZE))
    def generate_shape(self):
        if self.next is None:
            self.next = Shape()
        self.figure = self.next
        self.next = Shape()
        #color,block,type,shape


    
    # create bottom panel
    # show upcoming shape
    # generate new shapes
    # save shape to gameboard
    # remove row
