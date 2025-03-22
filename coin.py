import random
from utils import load_image, load_sound

class Coin:
    def __init__(self, x, y):
        """Initialize a coin at given position"""
        self.x = x
        self.y = y
        self.value = 10
        self.image = load_image("coin")
        self.collect_sound = load_sound("coin_collect")
        self.collect_sound.set_volume(0.3)
    
    def collect(self):
        """Handle coin collection logic"""
        self.collect_sound.play()
        return self.value
    
    @staticmethod
    def generate_coins(grid, num_coins):
        """Generate random coins on the grid"""
        coins = []
        for _ in range(num_coins):
            x = random.randint(0, grid.grid_width - 1)
            y = random.randint(0, grid.grid_height - 1)
            
            if not grid.is_occupied(x, y):
                coin = Coin(x, y)
                coins.append(coin)
                grid.set_cell(x, y, 4)  
        
        return coins
    
    def draw(self, screen, grid_size):
        """Draw the coin on screen"""
        screen.blit(self.image, (self.x * grid_size, self.y * grid_size))