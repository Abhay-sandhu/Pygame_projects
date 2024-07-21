import random, pygame

# Window and World settings
GAME_LOGO = "Tower_Defense\\assets\images\gui\logo.png"
ROWS = 15
COLS = 15
TILE_SIZE = 48
WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE
FPS = 60

# enemy settings
ENEMY_SIZE = 70
ENEMY_SPEED = 3
WAY_POINTS = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(4)]
ENEMY_1 = "Tower_Defense\\assets\images\enemies\enemy_1.png"

# turret settings
TURRET_1 = "Tower_Defense\\assets\images\\turrets\cursor_turret.png"

# Level settings
LEVEL_1 = "Tower_Defense\levels\level.png"
LEVEL_1_JSON = "Tower_Defense\levels\level.tmj"

# Colors
BG_COLOR = (150, 100, 200, 200)
PATH_COLOR = (255, 255, 255, 255)
HIGHLIGHT_GRID = (55, 255, 55, 75)