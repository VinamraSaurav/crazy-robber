import pygame
import os
from pygame import mixer
from constants import GRID_SIZE, BLUE, RED, GOLD, GRAY, GREEN, WHITE


mixer.init()

def manhattan_distance(a, b):
    """Calculate Manhattan distance between two points"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def load_image(name, size=(GRID_SIZE, GRID_SIZE)):
    """Load an image from assets folder or create a placeholder"""
    try:
        image = pygame.image.load(f"assets/{name}.png").convert_alpha()
        return pygame.transform.scale(image, size)
    except pygame.error:
        
        surf = pygame.Surface(size)
        if name == "robber":
            surf.fill(BLUE)
        elif name == "watchman":
            surf.fill(RED)
        elif name == "coin":
            surf.fill(GOLD)
        elif name == "wall":
            surf.fill(GRAY)
        elif name == "exit":
            surf.fill(GREEN)
        else:
            surf.fill(WHITE)
        return surf

def load_sound(name):
    """Load a sound file from assets folder or create a dummy sound object"""
    try:
        sound = mixer.Sound(f"assets/{name}.wav")
        return sound
    except:
        return type('obj', (object,), {'play': lambda: None, 'set_volume': lambda x: None})

def create_assets_folder():
    """Create assets folder if it doesn't exist"""
    try:
        if not os.path.exists('assets'):
            os.makedirs('assets')
    except:
        pass