import pygame
import random

W, H = 400, 600

car = pygame.image.load("assets/car.png")
car = pygame.transform.scale(car, (50, 90))

coin = pygame.image.load("assets/coin.png")
coin = pygame.transform.scale(coin, (30, 30))

road = pygame.image.load("assets/road.png")
road = pygame.transform.scale(road, (W, H))

enemy = pygame.image.load("assets/enemy.png")
enemy = pygame.transform.scale(enemy, (50, 80))


class Player:
    def __init__(self):
        self.rect = car.get_rect(center=(W//2, H-100))
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        self.rect.x = max(0, min(W - self.rect.width, self.rect.x))

    def draw(self, s):
        s.blit(car, self.rect)


class Road:
    def __init__(self):
        self.y = 0

    def update(self):
        self.y += 5
        if self.y >= H:
            self.y = 0

    def draw(self, s):
        s.blit(road, (0, self.y))
        s.blit(road, (0, self.y - H))


class Coin:
    def __init__(self):
        self.rect = coin.get_rect()
        self.rect.x = random.randint(100, W-100)
        self.rect.y = -40

    def update(self):
        self.rect.y += 5

    def draw(self, s):
        s.blit(coin, self.rect)


class Enemy:
    def __init__(self):
        self.rect = enemy.get_rect()
        self.rect.x = random.randint(100, W-100)
        self.rect.y = -60

    def update(self):
        self.rect.y += 6

    def draw(self, s):
        s.blit(enemy, self.rect)