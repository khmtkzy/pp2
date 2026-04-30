import pygame
import sys
import random

pygame.init()

# COLORS
FRAME_COLOR = (0,0,0)
SIZE_BLOCK = 20
DBLUE = (6,10,71)
BLUE = (14,18,92)
PINK = (250,105,250)
SNAKE_COLOR = (255,255,255)
COUNT_BLOCK = 20
HEADER_COLOR = (10,16,84)
HEADER_MARGIN = 70
MARGIN = 1

# SCREEN SIZE
size = [SIZE_BLOCK*COUNT_BLOCK + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCK,
        SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK + HEADER_MARGIN]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont('courier', 36)

# SNAKE BLOCK CLASS
class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

    # check if inside field
    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCK and 0 <= self.y < COUNT_BLOCK


# generate food with WEIGHT
def get_random_empty_block():
    while True:
        x = random.randint(0, COUNT_BLOCK-1)
        y = random.randint(0, COUNT_BLOCK-1)
        block = SnakeBlock(x,y)

        if block not in snake_blocks:
            block.weight = random.choice([1, 2, 3])  # 🔥 food weight
            return block


# draw block
def draw_block(color,row,column):
    pygame.draw.rect(screen,color,[SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column+1),
                                   HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row+1),
                                   SIZE_BLOCK,
                                   SIZE_BLOCK])

# INITIAL STATE
snake_blocks = [SnakeBlock(9,8),SnakeBlock(9,9),SnakeBlock(9,10)]
food = get_random_empty_block()

# 🔥 TIMER FOR FOOD
food_timer = pygame.time.get_ticks()
FOOD_LIFETIME = 5000  # 5 seconds

d_row = 0
d_col = 1

total = 0
speed = 1

# GAME LOOP
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # control snake
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    # draw background
    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    # draw text
    text_total = font.render(f"Score: {total}", True, PINK)
    text_speed = font.render(f"Level: {speed}", True, PINK)
    screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(text_speed, (SIZE_BLOCK+230, SIZE_BLOCK))

    # draw grid
    for row in range(COUNT_BLOCK):
        for column in range(COUNT_BLOCK):
            color = BLUE if (row+column)%2==0 else DBLUE
            draw_block(color,row,column)

    head = snake_blocks[-1]

    # WALL COLLISION
    if not head.is_inside():
        print("Game Over (Wall)")
        pygame.quit()
        sys.exit()

    # 🔥 FOOD TIMER (disappears)
    if pygame.time.get_ticks() - food_timer > FOOD_LIFETIME:
        food = get_random_empty_block()
        food_timer = pygame.time.get_ticks()

    # draw food
    draw_block(PINK, food.x, food.y)

    # draw snake
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    # EAT FOOD
    if food == head:
        total += food.weight  # 🔥 use weight
        speed = total // 5 + 1
        snake_blocks.append(food)

        food = get_random_empty_block()
        food_timer = pygame.time.get_ticks()

    else:
        snake_blocks.pop(0)

    # NEW HEAD
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)

    # SELF COLLISION
    if new_head in snake_blocks:
        print("Game Over (Self)")
        pygame.quit()
        sys.exit()

    snake_blocks.append(new_head)

    pygame.display.flip()
    clock.tick(3 + speed)