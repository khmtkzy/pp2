import pygame

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
    (255, 0, 0),    # red
    (0, 255, 0),    # green
    (0, 0, 255),    # blue
    (255, 255, 0),  # yellow
    (255, 165, 0),  # orange
    (255, 255, 255) # white
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

        # Exit program
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Keyboard controls
        if event.type == pygame.KEYDOWN:

            # Select tool
            if event.key == pygame.K_1:
                tool = 'brush'
            elif event.key == pygame.K_2:
                tool = 'rect'
            elif event.key == pygame.K_3:
                tool = 'circle'
            elif event.key == pygame.K_4:
                tool = 'eraser'

            # Change brush size WITHOUT mouse
            elif event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                radius += 2   # increase size

            elif event.key == pygame.K_MINUS:
                radius = max(1, radius - 2)   # decrease size

            # Numpad support
            elif event.key == pygame.K_KP_PLUS:
                radius += 2
            elif event.key == pygame.K_KP_MINUS:
                radius = max(1, radius - 2)

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Select color from palette
            for i, c in enumerate(palette):
                if 10 + i*50 <= x <= 50 + i*50 and 10 <= y <= 50:
                    color = c

            # Start drawing
            if event.button == 1:
                drawing = True
                start_pos = event.pos

        # Mouse release
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos

                # Draw rectangle
                if tool == 'rect':
                    pygame.draw.rect(canvas, color,
                                     (min(start_pos[0], end_pos[0]),
                                      min(start_pos[1], end_pos[1]),
                                      abs(start_pos[0]-end_pos[0]),
                                      abs(start_pos[1]-end_pos[1])), 2)

                # Draw circle
                elif tool == 'circle':
                    r = int(((start_pos[0]-end_pos[0])**2 +
                             (start_pos[1]-end_pos[1])**2)**0.5)
                    pygame.draw.circle(canvas, color, start_pos, r, 2)

        # Mouse movement (drawing)
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == 'brush':
                    pygame.draw.circle(canvas, color, event.pos, radius)

                elif tool == 'eraser':
                    pygame.draw.circle(canvas, BLACK, event.pos, radius)

    # Draw everything
    screen.fill(BLACK)
    screen.blit(canvas, (0, 0))

    # Draw palette
    for i, c in enumerate(palette):
        pygame.draw.rect(screen, c, (10 + i*50, 10, 40, 40))

    # Info text
    text = font.render(
        f"Tool: {tool} | Size: {radius} | Keys: 1-Brush 2-Rect 3-Circle 4-Eraser | +/- size",
        True, WHITE
    )
    screen.blit(text, (10, 60))

    pygame.display.flip()
    clock.tick(60)