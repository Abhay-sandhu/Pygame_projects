from pygame import image, transform
from settings import *

class World():
    def __init__(self, game):
        self.game = game
        self.level = transform.scale(image.load(LEVEL_1), (WIDTH, HEIGHT))
    
    def draw(self):
        self.game.screen.blit(self.level, (0, 0))