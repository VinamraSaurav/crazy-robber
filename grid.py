from constants import GRID_WIDTH, GRID_HEIGHT

class Grid:
    def __init__(self):
        """Initialize the game grid"""
        self.grid_width = GRID_WIDTH
        self.grid_height = GRID_HEIGHT
        self.grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
    
    def clear(self):
        """Clear the grid"""
        self.grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
    
    def set_cell(self, x, y, value):
        """Set a cell value in the grid"""
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            self.grid[x][y] = value
    
    def get_cell(self, x, y):
        """Get a cell value from the grid"""
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            return self.grid[x][y]
        return None
    
    def is_valid_position(self, x, y):
        """Check if position is within grid boundaries"""
        return 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT
    
    def is_occupied(self, x, y, excluded_values=None):
        """Check if a cell is occupied (has a non-zero value)"""
        if not self.is_valid_position(x, y):
            return True
        
        if excluded_values and self.grid[x][y] in excluded_values:
            return False
            
        return self.grid[x][y] != 0