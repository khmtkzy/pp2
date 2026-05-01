import json
import pygame

# Palette
COLORS = {
    'FRAME': (0, 0, 0),
    'DBLUE': (6, 10, 71),
    'BLUE': (14, 18, 92),
    'PINK': (250, 105, 250),
    'SNAKE': (255, 255, 255),
    'HEADER': (10, 16, 84),
    'FOOD': (0, 255, 0),
    'POISON': (139, 0, 0),
    'BONUS': (255, 215, 0),
    'WALL': (100, 100, 100),
    'SHIELD': (0, 255, 255)
}

# Game Configurations
SIZE_BLOCK = 20
COUNT_BLOCK = 20
HEADER_MARGIN = 70
MARGIN = 1

size = [SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK,
        SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK + HEADER_MARGIN]

class Settings:
    def __init__(self):
        self.snake_color = COLORS['SNAKE']
        self.show_grid = True
        self.sound_enabled = True
        self.load_settings()
    
    def load_settings(self):
        try:
            with open('settings.json', 'r') as f:
                data = json.load(f)
                self.snake_color = tuple(data.get('snake_color', COLORS['SNAKE']))
                self.show_grid = data.get('show_grid', True)
                self.sound_enabled = data.get('sound_enabled', True)
        except FileNotFoundError:
            self.save_settings()
    
    def save_settings(self):
        with open('settings.json', 'w') as f:
            json.dump({
                'snake_color': list(self.snake_color),
                'show_grid': self.show_grid,
                'sound_enabled': self.sound_enabled
            }, f, indent=4)
    
    def update(self, **kwargs):
        if 'snake_color' in kwargs:
            self.snake_color = kwargs['snake_color']
        if 'show_grid' in kwargs:
            self.show_grid = kwargs['show_grid']
        if 'sound_enabled' in kwargs:
            self.sound_enabled = kwargs['sound_enabled']
        self.save_settings()