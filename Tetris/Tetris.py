#imports
from random import choice
import pygame
from pygame import display, transform, draw, sprite, key, Color, K_LEFT, K_RIGHT, K_DOWN 

#Constants and variables
WIDTH = 400
HEIGHT = 800
screen = display.set_mode((WIDTH, HEIGHT))

# Shape Class
class Shape(sprite.Sprite):
    
    # All Possible Shapes
    All_Shapes = [1,2,3,4]
    Colors = [1,2,3,4]
    Angles = [0,90,180,270]
    def __init__(self):
        super().__init__()
        self.color = choice(Shape.Colors)
        self.shape = transform.rotate(choice(Shape.All_Shapes), choice(Shape.Angles)) # random rotate shape
    
    # method to draw shape onto the screen grid
    def update(self):
        pass
    
    # shape controller event (left, right, down keys)
    def control(self):
        pass

# Game Class
class Game():
    def __init__(self):
        # Create gameboard
            # Create a grid
            # create bottom panel
                # show upcoming shape
        # generate new shapes
        # save shape to gameboard
        # remove row
        pass

    