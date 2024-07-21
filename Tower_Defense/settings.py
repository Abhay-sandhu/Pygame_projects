import random, pygame
#Window settings
WIDTH = 800
HEIGHT = 650
FPS = 60

# enemy settings
ENEMY_SIZE = 70
WAY_POINTS = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(4)]
ENEMY_1 = "Tower_Defense/assets/enemy_1.png"


# Level settings
LEVEL_1 = "Tower_Defense/levels/level.png"


#Colors
BG_COLOR = (150, 100, 200, 200)
PATH_COLOR = (255,255,255,255)