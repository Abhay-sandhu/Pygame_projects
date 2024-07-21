from pygame import image, transform
from pygame.math import Vector2
import json
from settings import *


class World:
    def __init__(self, game):
        self.game = game
        self.level = transform.scale(
            image.load(LEVEL_1).convert_alpha(), (WIDTH, HEIGHT)
        )
        self.level_file = LEVEL_1_JSON
        self.load_level_data(self.level_file)
        self.process_level_data()

    def draw(self):
        self.game.screen.blit(self.level, (0, 0))

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
                self.tile_data = layer["data"]
                self.process_tile_data()
                print(self.tile_data)

    def process_waypoints(self):
        temp = []
        for waypoint in self.waypoints:
            temp.append(Vector2(waypoint.get("x"), waypoint.get("y")))
        self.waypoints = temp

    def process_tile_data(self):
        temp = []
        for row in range(ROWS):
            tile_row = []
            for col in range(COLS):
                tile_row.append(self.tile_data[row * 15 + col])
            temp.append(tile_row)
        self.tile_data = temp