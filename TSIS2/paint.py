import pygame
import math
from datetime import datetime
from tools import flood_fill

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint TSIS2")

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(BLACK)

palette = [
    (255,0,0),(0,255,0),(0,0,255),
    (255,255,0),(255,165,0),(255,255,255)
]

color = palette[0]
tool = "brush"
brush_size = 5

drawing = False
start_pos = (0,0)
last_pos = None

font = pygame.font.SysFont(None, 22)

typing = False
text_input = ""
text_pos = (0,0)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:

            # TOOL MENU
            if event.key == pygame.K_1: tool = "brush"
            elif event.key == pygame.K_2: tool = "pencil"
            elif event.key == pygame.K_3: tool = "line"
            elif event.key == pygame.K_4: tool = "rect"
            elif event.key == pygame.K_5: tool = "circle"
            elif event.key == pygame.K_6: tool = "square"
            elif event.key == pygame.K_7: tool = "triangle"
            elif event.key == pygame.K_8: tool = "rhombus"
            elif event.key == pygame.K_9: tool = "fill"
            elif event.key == pygame.K_0: tool = "text"

            # SIZE + -
            if event.key == pygame.K_EQUALS or event.key == pygame.K_KP_PLUS:
                brush_size += 1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                brush_size = max(1, brush_size - 1)

            # SAVE
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)

            # TEXT
            if typing:
                if event.key == pygame.K_RETURN:
                    canvas.blit(font.render(text_input, True, color), text_pos)
                    typing = False
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos

            for i,c in enumerate(palette):
                if 10+i*50 <= x <= 50+i*50 and 10 <= y <= 50:
                    color = c

            drawing = True
            start_pos = event.pos
            last_pos = event.pos

            if tool == "fill":
                flood_fill(canvas, x, y, color)

            if tool == "text":
                typing = True
                text_pos = event.pos
                text_input = ""

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if tool == "line":
                pygame.draw.line(canvas,color,start_pos,end_pos,brush_size)

            elif tool == "rect":
                pygame.draw.rect(canvas,color,
                    (min(start_pos[0],end_pos[0]),
                     min(start_pos[1],end_pos[1]),
                     abs(start_pos[0]-end_pos[0]),
                     abs(start_pos[1]-end_pos[1])),brush_size)

            elif tool == "circle":
                r = int(((start_pos[0]-end_pos[0])**2+(start_pos[1]-end_pos[1])**2)**0.5)
                pygame.draw.circle(canvas,color,start_pos,r,brush_size)

            elif tool == "square":
                side = min(abs(start_pos[0]-end_pos[0]),abs(start_pos[1]-end_pos[1]))
                pygame.draw.rect(canvas,color,(start_pos[0],start_pos[1],side,side),brush_size)

            elif tool == "triangle":
                pygame.draw.polygon(canvas,color,[start_pos,end_pos,(start_pos[0],end_pos[1])],brush_size)

            elif tool == "rhombus":
                cx = (start_pos[0]+end_pos[0])//2
                cy = (start_pos[1]+end_pos[1])//2
                pygame.draw.polygon(canvas,color,
                    [(cx,start_pos[1]),(end_pos[0],cy),(cx,end_pos[1]),(start_pos[0],cy)],brush_size)

        if event.type == pygame.MOUSEMOTION and drawing:

            if tool == "brush":
                pygame.draw.circle(canvas,color,event.pos,brush_size)

            elif tool == "pencil":
                pygame.draw.line(canvas,color,last_pos,event.pos,brush_size)
                last_pos = event.pos

    # PREVIEW
    screen.fill(BLACK)

    if drawing and tool in ["line","rect","circle"]:
        temp = canvas.copy()
        mx,my = pygame.mouse.get_pos()

        if tool == "line":
            pygame.draw.line(temp,color,start_pos,(mx,my),brush_size)

        elif tool == "rect":
            pygame.draw.rect(temp,color,
                (min(start_pos[0],mx),
                 min(start_pos[1],my),
                 abs(start_pos[0]-mx),
                 abs(start_pos[1]-my)),brush_size)

        elif tool == "circle":
            r = int(((start_pos[0]-mx)**2+(start_pos[1]-my)**2)**0.5)
            pygame.draw.circle(temp,color,start_pos,r,brush_size)

        screen.blit(temp,(0,0))
    else:
        screen.blit(canvas,(0,0))

    # TEXT PREVIEW
    if typing:
        screen.blit(font.render(text_input, True, color), text_pos)

    # PALETTE
    for i,c in enumerate(palette):
        pygame.draw.rect(screen,c,(10+i*50,10,40,40))

    # MENU
    menu = [
        "1 Brush","2 Pencil","3 Line","4 Rect","5 Circle",
        "6 Square","7 Triangle","8 Rhombus","9 Fill","0 Text",
        "+ / - Size","Ctrl+S Save"
    ]

    for i,line in enumerate(menu):
        screen.blit(font.render(line, True, WHITE), (10, 70+i*20))

    info = font.render(f"Tool: {tool} | Size: {brush_size}", True, WHITE)
    screen.blit(info,(10,50))

    pygame.display.flip()
    clock.tick(60)