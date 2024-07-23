from pygame import image, transform
from pygame.math import Vector2
import json
from settings import *


class World:
    def __init__(self, game):
        self.game = game
        self.health = HEALTH
        self.money = MONEY
        self.map = transform.scale(
            image.load(LEVEL_1).convert_alpha(), (WIDTH, HEIGHT)
        )
        self.level_file = LEVEL_1_JSON
        self.load_level_data(self.level_file)
        self.process_level_data()
        self.level_number = 1
        self.enemies_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0
        self.process_enemies()

    def draw(self):
        self.game.screen.blit(self.map, (0, 0))

    def load_level_data(self, level_file):
        with open(level_file, "r") as file:
            self.level_data = json.load(file)

    def process_level_data(self):
        for layer in self.level_data["layers"]:
            if layer["name"] == "waypoints":
                for obj in layer["objects"]:
                    self.waypoints = obj["polyline"]
                    self.process_waypoints()
            if layer["name"] == "tilemap":
                self.tile_map = layer["data"]

    def process_waypoints(self):
        temp = []
        for waypoint in self.waypoints:
            temp.append(Vector2(waypoint.get("x"), waypoint.get("y")))
        self.waypoints = temp

    def process_enemies(self):
        enemies = ENEMY_SPAWN_DATA[self.level_number -1]
        for enemy_type in enemies:
            for _ in range(enemies[enemy_type]):
                self.enemies_list.append(enemy_type)
        random.shuffle(self.enemies_list)

    def check_level_complete(self):
        if (self.killed_enemies + self.missed_enemies) == len(self.enemies_list):
            return True
        return False
    
    def reset_level(self):
        self.enemies_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0
        