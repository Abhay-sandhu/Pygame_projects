import random, pygame

# Window and World settings
GAME_LOGO = "Tower_Defense\\assets\images\gui\logo.png"
ROWS = 15
COLS = 15
TILE_SIZE = 48
SIDE_PANEL = 250
WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE
FPS = 60

# enemy settings
ENEMY_SIZE = 70
ENEMY_SPEED = 3
WAY_POINTS = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(4)]
ENEMY_1 = "Tower_Defense\\assets\images\enemies\enemy_1.png"

# turret settings
CURSOR_TURRET = "Tower_Defense\\assets\images\\turrets\cursor_turret.png"
ANIMATION_STEPS = 8
TURRET_1 = "Tower_Defense\\assets\images\\turrets\\turret_1.png"


# Button settings

BUY_TURRET_BTN = "Tower_Defense\\assets\images\\buttons\\buy_turret.png"
CANCEL_BTN = "Tower_Defense\\assets\images\\buttons\cancel.png"
UPGRADE_TURRET_BTN = "Tower_Defense/assets/images/buttons/upgrade_turret.png"
FAST_FORWARD_BTN = "Tower_Defense\\assets\images\\buttons\\fast_forward.png"
START_BTN = "Tower_Defense\\assets\images\\buttons\\begin.png"
RESTART_BTN = "Tower_Defense\\assets\images\\buttons\\restart.png"

# Level settings
LEVEL_1 = "Tower_Defense\levels\level.png"
LEVEL_1_JSON = "Tower_Defense\levels\level.tmj"

# Colors
BG_COLOR = (100, 200, 150, 200)
PATH_COLOR = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
HIGHLIGHT_GRID_VALID = (55, 255, 55, 75)
HIGHLIGHT_GRID_INVALID = (255, 55, 55, 75)
HIGHLIGHT_GRID_FILLED = (55, 55, 255, 75)