import pygame
from random import randrange

vec2d = pygame.math.Vector2

class Snake():
    SNAKE_COLOR = pygame.Color(0, 255, 0, 255)
    def __init__(self, game):
        self.game = game
        self.size = game.block_size
        self.rect = pygame.rect.Rect(1, 1, self.size-1, self.size-1)
        self.rect.center = self.get_random_position()
        self.direction = vec2d(self.size, 0)
        self.delay = 100
        self.time = 0
        self.length = 1
        self.segments = []
    
    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction.y != self.size:
                self.direction = vec2d(0, -self.size)
            elif event.key == pygame.K_DOWN and self.direction.y != -self.size:
                self.direction = vec2d(0, self.size)
            elif event.key == pygame.K_LEFT and self.direction.x != self.size:
                self.direction = vec2d(-self.size, 0)
            elif event.key == pygame.K_RIGHT and self.direction.x != -self.size:
                self.direction = vec2d(self.size, 0)
    
    def time_delta(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.delay:
            self.time = time_now
            return True
        return False
    
    def get_random_position(self):
        return (randrange(self.size//2, self.game.width - self.size//2, self.size), randrange(self.size//2, self.game.height - self.size//2, self.size))
    
    def check_borders(self):
        if self.rect.left < 0 or self.rect.right > self.game.width or self.rect.top < 0 or self.rect.bottom > self.game.height:
            self.game.game_over_sound.play()
            pygame.time.delay(2000)
            self.game.new_game()

    def check_self_eating(self):
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.game_over_sound.play()
            pygame.time.delay(2000)
            self.game.new_game()

    def check_food(self):
        if self.rect.center == self.game.food.rect.center:
            self.game.score += 1
            self.game.food_sound.play()
            self.length += 1
            self.game.food.rect.center = self.get_random_position()

    def draw(self):
        [pygame.draw.rect(self.game.screen, Snake.SNAKE_COLOR, segment) for segment in self.segments]

    def move(self):
        if self.time_delta():
            self.rect.move_ip(self.direction)
            self.game.move_sound.play()
            self.segments.append(self.rect.copy())
            print(len(self.segments))
            self.segments = self.segments[-self.length:]
    def update(self):
        self.check_borders()
        self.check_self_eating()  
        self.check_food()
        self.move()
        

class Food():
    FOOD_COLOR = pygame.Color(0, 0, 255, 255)
    def __init__(self, game):
        self.game = game
        self.size = game.block_size
        self.rect = pygame.rect.Rect(0, 0, self.size, self.size)
        self.rect.center = self.get_random_position()

    def get_random_position(self):
        return (randrange(self.size//2, self.game.width - self.size//2, self.size), randrange(self.size//2, self.game.height - self.size//2, self.size))    
    def draw(self):
        pygame.draw.rect(self.game.screen, Food.FOOD_COLOR,self.rect)