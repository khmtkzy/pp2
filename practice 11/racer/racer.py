import pygame, sys
from pygame.locals import *
import random, time

# Init
pygame.init()
pygame.mixer.init()

# FPS
FPS = 60
clock = pygame.time.Clock()

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Variables
BASE_SPEED = 5
SPEED = BASE_SPEED
SCORE = 0
COIN_SCORE = 0

# Fonts
font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)
game_over = font_big.render("Game Over", True, BLACK)

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Background
background = pygame.image.load("images/street.png").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -100)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        # If enemy leaves screen → respawn
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.respawn()


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()

        # Move left
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        # Move right
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)


# Coin class with WEIGHT
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.weight = random.choice([1, 2, 3])  # 🔥 different values

        self.image = pygame.image.load("images/coin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))

        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(-300, -50)
        )

    def move(self):
        self.rect.move_ip(0, 2)

        # Remove coin if off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# Objects
player = Player()
enemy = Enemy()

# Groups
enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group()

all_sprites = pygame.sprite.Group(player, enemy)

# Timer for coins
COIN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_EVENT, 2000)


# Game loop
while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Spawn coin
        if event.type == COIN_EVENT:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    # Draw background
    screen.blit(background, (0, 0))

    # Draw scores
    screen.blit(font_small.render(f"Score: {SCORE}", True, BLACK), (10, 10))
    screen.blit(font_small.render(f"Coins: {COIN_SCORE}", True, BLACK), (260, 10))

    # Update all objects
    for obj in all_sprites:
        screen.blit(obj.image, obj.rect)
        obj.move()

    # Enemy collision
    if pygame.sprite.spritecollideany(player, enemies):
        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Coin collision
    hits = pygame.sprite.spritecollide(player, coins, True)

    for coin in hits:
        COIN_SCORE += coin.weight  # 🔥 add weight

    # 🔥 SPEED increases smoothly based on coins
    SPEED = BASE_SPEED + COIN_SCORE // 5

    pygame.display.update()
    clock.tick(FPS)