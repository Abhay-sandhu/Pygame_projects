import random
from pygame import mixer, sprite,transform, image, font, key, K_w, K_s, K_a, K_d



class Main(sprite.Sprite):
    def init(self, image_file, screen, x, y, speed):
        super().__init__()
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.speed= speed
        self.image = transform.scale(image.load(image_file), (self.screen_width, self.screen_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(Main):
    def __init__(self, image_file, screen, x, y, speed):
        super().__init__(image_file, screen, x, y, speed)
    
    def control(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < self.screen_height - self.rect.height:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < self.screen_width - self.rect.width:
            self.rect.x += self.speed


class Enemy(Main):
    def __init__(self, image_file, screen, x, y, speed):
        super().__init__(image_file, screen, x, y, speed)
    
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed

        if self.rect.x > self.screen_width or self.rect.y > self.screen_height:
            self.speed *= -1
        if self.rect.x < 0 or self.rect.y < 0:
            self.speed *= -1


class Coins(sprite.Sprite):
    def __init__(self, image_file, screen):
        super().__init__()
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.image = transform.scale(image.load(image_file), (50, 50))
        self.rect = self.image.get_rect()

    def draw_coins(self):
        self.rect.x = random.randint(0, self.screen_width - self.rect.width)
        self.rect.y = random.randint(0, self.screen_height - self.rect.height)
        self.screen.blit(self.image, self.rect)


class Walls(sprite.Sprite):
    def __init__(self, image_file, screen):
        super().__init__()
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.image = transform.scale(image.load(image_file), (self.screen_width, self.screen_height))
        self.rect = self.image.get_rect()


