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
HEALTH = 100
MONEY = 650
LEVEL_REWARD = [150, 300, 450, 600, 1000]
HEART = "Tower_Defense\\assets\images\gui\heart.png"
COIN = "Tower_Defense\\assets\images\gui\coin.png"

# enemy settings
WAY_POINTS = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(4)]
ENEMY_1 = "Tower_Defense\\assets\images\enemies\enemy_1.png"
ENEMY_2 = "Tower_Defense\\assets\images\enemies\enemy_2.png"
ENEMY_3 = "Tower_Defense\\assets\images\enemies\enemy_3.png"
ENEMY_4 = "Tower_Defense\\assets\images\enemies\enemy_4.png"
SPAWN_COOLDOWN = 400
ENEMY_DATA = {
        'weak': {'image': ENEMY_1, 'health': 10, 'speed': 2, 'size': 50, 'bounty': 10, 'damage': 2},
        'strong': {'image': ENEMY_2, 'health': 50, 'speed': 2.5, 'size': 65, 'bounty': 25, 'damage': 4},
        'elite': {'image': ENEMY_3, 'health': 125, 'speed': 3, 'size': 80, 'bounty': 100, 'damage': 16},
        'boss': {'image': ENEMY_4, 'health': 500, 'speed': 3, 'size': 100, 'bounty': 1000, 'damage': 64}
    }
ENEMY_SPAWN_DATA = [
        {'weak': 15, 'strong': 1, 'elite': 0, 'boss': 0},
        {'weak': 25, 'strong': 5, 'elite': 0, 'boss': 0},
        {'weak': 35, 'strong': 10, 'elite': 1, 'boss': 0},
        {'weak': 45, 'strong': 15, 'elite': 3, 'boss': 1},
        {'weak': 60, 'strong': 25, 'elite': 7, 'boss': 3},
    ]


# turret settings
CURSOR_TURRET = "Tower_Defense\\assets\images\\turrets\cursor_turret.png"
ANIMATION_STEPS = 8
ANIMATION_DELAY = 15
MAX_LEVEL = 4
BUY_COST = 100
UPGRADE_COST = 150
SHOT_SOUND = "Tower_Defense\\assets\\audio\shot.wav"
SHOT_VOLUME = 0.05
TURRET_1 = "Tower_Defense\\assets\images\\turrets\\turret_1.png"
TURRET_2 = "Tower_Defense\\assets\images\\turrets\\turret_2.png"
TURRET_3 = "Tower_Defense\\assets\images\\turrets\\turret_3.png"
TURRET_4 = "Tower_Defense\\assets\images\\turrets\\turret_4.png"
TURRET_DATA = [
        {'range': 90, 'cooldown': 1500, 'sprite_sheet': TURRET_1, 'damage': 3,},
        {'range': 110, 'cooldown': 1200, 'sprite_sheet': TURRET_2, 'damage': 9,},
        {'range': 130, 'cooldown': 1000, 'sprite_sheet': TURRET_3, 'damage': 18,},
        {'range': 160, 'cooldown': 700, 'sprite_sheet': TURRET_4, 'damage': 54,}
    ]

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