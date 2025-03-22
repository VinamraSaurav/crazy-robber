import random
from utils import load_image, load_sound

class Robber:
    def __init__(self, x, y):
        """Initialize the robber at given position"""
        self.x = x
        self.y = y
        self.path = [(x, y)]
        self.image = load_image("robber")
        self.move_sound = load_sound("move")
        self.move_sound.set_volume(0.2)
    
    @staticmethod
    def generate_robber(grid):
        """Generate robber at a random position on the grid"""
        while True:
            x = random.randint(0, grid.grid_width - 1)
            y = random.randint(0, grid.grid_height - 1)
            
            if not grid.is_occupied(x, y):
                robber = Robber(x, y)
                grid.set_cell(x, y, 2)  
                return robber
    
    def move(self, dx, dy, grid):
        """Move the robber by the given deltas"""
        new_x = self.x + dx
        new_y = self.y + dy
        
        
        if not grid.is_valid_position(new_x, new_y):
            return False
        
        
        if grid.get_cell(new_x, new_y) == 1:  
            return False
        
        
        grid.set_cell(self.x, self.y, 0)
        
        
        self.x, self.y = new_x, new_y
        grid.set_cell(new_x, new_y, 2)  
        self.path.append((new_x, new_y))
        
       
        self.move_sound.play()
        
        return True
    
    def draw(self, screen, grid_size):
        """Draw the robber on screen"""
        screen.blit(self.image, (self.x * grid_size, self.y * grid_size))