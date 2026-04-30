import pygame
import math

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Canvas surface
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(BLACK)

# Color palette
palette = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (255, 255, 255)
]

# Default settings
color = (0, 0, 255)
tool = 'brush'
radius = 10

drawing = False
start_pos = (0, 0)

font = pygame.font.SysFont(None, 24)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # 🔥 TOOL SELECTION
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = 'brush'
            elif event.key == pygame.K_2:
                tool = 'rect'
            elif event.key == pygame.K_3:
                tool = 'circle'
            elif event.key == pygame.K_4:
                tool = 'eraser'
            elif event.key == pygame.K_5:
                tool = 'square'
            elif event.key == pygame.K_6:
                tool = 'right_triangle'
            elif event.key == pygame.K_7:
                tool = 'equilateral_triangle'
            elif event.key == pygame.K_8:
                tool = 'rhombus'

            # 🔥 SIZE CONTROL
            if event.type == pygame.KEYDOWN:

                # Increase size (+ or =)
                if event.key == pygame.K_EQUALS:
                    radius += 2

                # Decrease size (-)
                elif event.key == pygame.K_MINUS:
                    radius = max(1, radius - 2)

                # Numpad support
                elif event.key == pygame.K_KP_PLUS:
                    radius += 2

                elif event.key == pygame.K_KP_MINUS:
                    radius = max(1, radius - 2)

        # Mouse press
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Select color
            for i, c in enumerate(palette):
                if 10 + i*50 <= x <= 50 + i*50 and 10 <= y <= 50:
                    color = c

            if event.button == 1:
                drawing = True
                start_pos = event.pos

        # Mouse release → draw shapes
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos

                # Rectangle
                if tool == 'rect':
                    pygame.draw.rect(canvas, color,
                        (min(start_pos[0], end_pos[0]),
                         min(start_pos[1], end_pos[1]),
                         abs(start_pos[0]-end_pos[0]),
                         abs(start_pos[1]-end_pos[1])), 2)

                # Circle
                elif tool == 'circle':
                    r = int(((start_pos[0]-end_pos[0])**2 +
                             (start_pos[1]-end_pos[1])**2)**0.5)
                    pygame.draw.circle(canvas, color, start_pos, r, 2)

                # 🔥 Square
                elif tool == 'square':
                    side = min(abs(start_pos[0]-end_pos[0]),
                               abs(start_pos[1]-end_pos[1]))
                    pygame.draw.rect(canvas, color,
                        (start_pos[0], start_pos[1], side, side), 2)

                # 🔥 Right triangle
                elif tool == 'right_triangle':
                    points = [
                        start_pos,
                        (start_pos[0], end_pos[1]),
                        end_pos
                    ]
                    pygame.draw.polygon(canvas, color, points, 2)

                # 🔥 Equilateral triangle
                elif tool == 'equilateral_triangle':
                    side = abs(start_pos[0] - end_pos[0])
                    height = int((math.sqrt(3)/2)*side)

                    points = [
                        (start_pos[0], start_pos[1]),
                        (start_pos[0] + side, start_pos[1]),
                        (start_pos[0] + side//2, start_pos[1] - height)
                    ]
                    pygame.draw.polygon(canvas, color, points, 2)

                # 🔥 Rhombus
                elif tool == 'rhombus':
                    center_x = (start_pos[0] + end_pos[0]) // 2
                    center_y = (start_pos[1] + end_pos[1]) // 2

                    points = [
                        (center_x, start_pos[1]),
                        (end_pos[0], center_y),
                        (center_x, end_pos[1]),
                        (start_pos[0], center_y)
                    ]
                    pygame.draw.polygon(canvas, color, points, 2)

        # Drawing with brush/eraser
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == 'brush':
                    pygame.draw.circle(canvas, color, event.pos, radius)
                elif tool == 'eraser':
                    pygame.draw.circle(canvas, BLACK, event.pos, radius)

    # Draw screen
    screen.fill(BLACK)
    screen.blit(canvas, (0, 0))

    # Draw palette
    for i, c in enumerate(palette):
        pygame.draw.rect(screen, c, (10 + i*50, 10, 40, 40))

    # Info text
    text1 = font.render(f"Tool: {tool} | Size: {radius}", True, WHITE)
    text2 = font.render("Keys: 1-Brush 2-Rect 3-Circle 4-Eraser 5-Square 6-RightTri 7-EquiTri 8-Rhombus", True, WHITE)

    screen.blit(text1, (10, 60))
    screen.blit(text2, (10, 85))

    pygame.display.flip()
    clock.tick(60)