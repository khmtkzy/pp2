import pygame, sys, random
from racer import *
from persistence import *
import ui

pygame.init()

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

# fonts
title_font = pygame.font.SysFont(None, 50)
btn_font = pygame.font.SysFont(None, 32)
small_font = pygame.font.SysFont(None, 24)
fonts = (title_font, btn_font)

state = "menu"
name_input = ""
username = ""

settings = load_settings()
board = load_board()

def reset_game():
    return Player(), Road(), [], [], 0, 0, 0

player, road, coins, enemies, score, coin_count, distance = reset_game()

while True:
    mx, my = pygame.mouse.get_pos()
    click = False

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            click = True

        if state == "name" and e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                username = name_input if name_input else "Player"
                state = "play"
            elif e.key == pygame.K_BACKSPACE:
                name_input = name_input[:-1]
            else:
                name_input += e.unicode

    # ===== MENU =====
    if state == "menu":
        buttons = ui.draw_main_menu(screen, mx, my, W, H, fonts)

        if click:
            if buttons["play"].collidepoint(mx, my):
                state = "name"
            elif buttons["leaderboard"].collidepoint(mx, my):
                state = "leaderboard"
            elif buttons["settings"].collidepoint(mx, my):
                state = "settings"
            elif buttons["quit"].collidepoint(mx, my):
                pygame.quit()
                sys.exit()

    # ===== NAME =====
    elif state == "name":
        buttons = ui.draw_name_entry(screen, mx, my, W, H, fonts, name_input)

        if click and buttons["start"].collidepoint(mx, my):
            username = name_input if name_input else "Player"
            state = "play"

    # ===== GAME =====
    elif state == "play":
        keys = pygame.key.get_pressed()
        player.move(keys)
        road.update()
        distance += 1

        if random.randint(1, 40) == 1:
            coins.append(Coin())

        if random.randint(1, 50) == 1:
            enemies.append(Enemy())

        for c in coins[:]:
            c.update()
            if player.rect.colliderect(c.rect):
                coins.remove(c)
                score += 10
                coin_count += 1

        for en in enemies[:]:
            en.update()
            if player.rect.colliderect(en.rect):
                save_score(username, score, coin_count)
                board = load_board()
                state = "gameover"

        road.draw(screen)

        for c in coins:
            c.draw(screen)

        for en in enemies:
            en.draw(screen)

        player.draw(screen)

        # HUD
        screen.blit(btn_font.render(f"Score: {score}", True, (255,255,255)), (10,10))
        screen.blit(btn_font.render(f"Coins: {coin_count}", True, (255,255,255)), (10,40))
        screen.blit(btn_font.render(f"Dist: {distance}", True, (255,255,255)), (10,70))

    # ===== GAME OVER =====
    elif state == "gameover":
        buttons = ui.draw_game_over(screen, mx, my, W, H, fonts, score, distance, coin_count)

        if click:
            if buttons["retry"].collidepoint(mx, my):
                player, road, coins, enemies, score, coin_count, distance = reset_game()
                state = "play"

            elif buttons["menu"].collidepoint(mx, my):
                player, road, coins, enemies, score, coin_count, distance = reset_game()
                state = "menu"

    # ===== LEADERBOARD =====
    elif state == "leaderboard":
        buttons = ui.draw_leaderboard(screen, mx, my, W, H, fonts, board)

        if click and buttons["back"].collidepoint(mx, my):
            state = "menu"

    # ===== SETTINGS =====
    elif state == "settings":
        buttons = ui.draw_settings(screen, mx, my, W, H, fonts, settings)

        if click:
            if buttons["sound"].collidepoint(mx, my):
                settings["sound"] = not settings["sound"]
                save_settings(settings)

            elif "color_red" in buttons and buttons["color_red"].collidepoint(mx, my):
                settings["car_color"] = "red"

            elif "color_blue" in buttons and buttons["color_blue"].collidepoint(mx, my):
                settings["car_color"] = "blue"

            elif "color_green" in buttons and buttons["color_green"].collidepoint(mx, my):
                settings["car_color"] = "green"

            elif "color_yellow" in buttons and buttons["color_yellow"].collidepoint(mx, my):
                settings["car_color"] = "yellow"

            elif "color_white" in buttons and buttons["color_white"].collidepoint(mx, my):
                settings["car_color"] = "white"

            elif "diff_easy" in buttons and buttons["diff_easy"].collidepoint(mx, my):
                settings["difficulty"] = "easy"

            elif "diff_normal" in buttons and buttons["diff_normal"].collidepoint(mx, my):
                settings["difficulty"] = "normal"

            elif "diff_hard" in buttons and buttons["diff_hard"].collidepoint(mx, my):
                settings["difficulty"] = "hard"

            elif buttons["back"].collidepoint(mx, my):
                save_settings(settings)
                state = "menu"

    pygame.display.flip()
    clock.tick(60)