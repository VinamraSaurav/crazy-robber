import random
from utils import load_image
from constants import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT

class Wall:
    def __init__(self, x, y):
        """Initialize a wall at given position"""
        self.x = x
        self.y = y
        self.image = load_image("wall")
    
    @staticmethod
    def generate_walls(grid, num_walls):
        """Generate random walls on the grid"""
        walls = []
        for _ in range(num_walls):
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            
            if not grid.is_occupied(x, y):
                wall = Wall(x, y)
                walls.append(wall)
                grid.set_cell(x, y, 1)  
        
        return walls
    
    def draw(self, screen, grid_size):
        """Draw the wall on screen"""
        screen.blit(self.image, (self.x * grid_size, self.y * grid_size))