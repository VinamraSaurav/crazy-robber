import random
from utils import load_image, manhattan_distance

class Watchman:
    def __init__(self, x, y):
        """Initialize a watchman at given position"""
        self.x = x
        self.y = y
        self.direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        self.image = load_image("watchman")
        self.light_image = load_image("light", (120, 120))  
        self.light_range = 1  
    
    @staticmethod
    def generate_watchmen(grid, num_watchmen, robber_pos, min_distance=3):
        """Generate random watchmen on the grid"""
        watchmen = []
        for _ in range(num_watchmen):
            x = random.randint(0, grid.grid_width - 1)
            y = random.randint(0, grid.grid_height - 1)
            
            
            if (not grid.is_occupied(x, y) and 
                manhattan_distance((x, y), robber_pos) > min_distance):
                watchman = Watchman(x, y)
                watchmen.append(watchman)
                grid.set_cell(x, y, 5)  
        
        return watchmen
    
    def get_valid_moves(self, grid):
        """Get valid moves for watchman"""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        valid_moves = []
        
        for dx, dy in directions:
            new_x, new_y = self.x + dx, self.y + dy
            
            if not grid.is_valid_position(new_x, new_y):
                continue
                
            if grid.get_cell(new_x, new_y) != 1 and grid.get_cell(new_x, new_y) != 5:
                valid_moves.append((dx, dy))
                
        return valid_moves
    
    def move(self, grid):
        """Move the watchman randomly to a valid position"""
        
        grid.set_cell(self.x, self.y, 0)
        
        
        valid_moves = self.get_valid_moves(grid)
        
        if valid_moves:
            
            dx, dy = random.choice(valid_moves)
            self.x += dx
            self.y += dy
            self.direction = (dx, dy)
            grid.set_cell(self.x, self.y, 5)  
        else:
            
            grid.set_cell(self.x, self.y, 5)
    
    def can_see(self, robber_x, robber_y):
        """Check if the watchman can see the robber"""
        return (abs(self.x - robber_x) <= self.light_range and 
                abs(self.y - robber_y) <= self.light_range)
    
    def draw(self, screen, grid_size):
        """Draw the watchman and its light on screen"""
        
        light_surface = self.light_image.copy()
        light_surface.set_alpha(100)
        screen.blit(light_surface, ((self.x-1) * grid_size, (self.y-1) * grid_size))
        
        
        screen.blit(self.image, (self.x * grid_size, self.y * grid_size))