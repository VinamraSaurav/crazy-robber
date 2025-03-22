import pygame
import random
from pygame import mixer

from constants import *
from utils import load_image, load_sound, manhattan_distance
from grid import Grid
from robber import Robber
from watchman import Watchman
from coin import Coin
from wall import Wall
from pathfinding import a_star_search
from metrics import calculate_metrics, draw_analysis

class CrazyRobberGame:
    def __init__(self):
        """Initialize the game"""
        self.grid = Grid()
        self.cell_size = GRID_SIZE
        self.obstacles = []
        self.coins = []
        self.watchmen = []
        self.robber = None
        self.exit_pos = None
        self.score = 0
        self.game_over = False
        self.game_won = False
        self.moves_made = 0
        self.start_time = pygame.time.get_ticks()
        self.game_state = PLAYING
        
        
        self.exit_img = load_image("exit")
        
        
        self.caught_sound = load_sound("caught")
        self.win_sound = load_sound("win")
        
        
        self.caught_sound.set_volume(0.3)
        self.win_sound.set_volume(0.3)
        

        self.init_game()
    
    def init_game(self):
        """Initialize or reset the game state"""
        
        self.grid.clear()
        self.obstacles = []
        self.coins = []
        self.watchmen = []
        self.score = 0
        self.game_over = False
        self.game_won = False
        self.moves_made = 0
        self.start_time = pygame.time.get_ticks()
        
        
        num_obstacles = random.randint(15, 30)
        self.obstacles = Wall.generate_walls(self.grid, num_obstacles)
        
        
        self.robber = Robber.generate_robber(self.grid)
        
        
        self.place_exit()
        
       
        num_coins = random.randint(5, 10)
        self.coins = Coin.generate_coins(self.grid, num_coins)
        
        
        num_watchmen = random.randint(2, 4)
        self.watchmen = Watchman.generate_watchmen(
            self.grid, 
            num_watchmen, 
            (self.robber.x, self.robber.y)
        )
    
    def place_exit(self):
        """Place the exit at a random position far from the robber"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            
            if (not self.grid.is_occupied(x, y) and 
                manhattan_distance((self.robber.x, self.robber.y), (x, y)) > GRID_WIDTH // 2):
                self.exit_pos = (x, y)
                self.grid.set_cell(x, y, 3)  
                break
    
    def move_robber(self, dx, dy):
        """Move the robber in the specified direction"""
        if self.game_over or self.game_won:
            return
        
        
        if self.robber.move(dx, dy, self.grid):
            self.moves_made += 1
            
            
            self.check_watchman_collision()
            self.check_coin_collection()
            self.check_exit_reached()
    
    def check_coin_collection(self):
        """Check if robber collected a coin"""
        robber_pos = (self.robber.x, self.robber.y)
        
        for coin in self.coins[:]:  
            if (coin.x, coin.y) == robber_pos:
                self.score += coin.collect()
                self.coins.remove(coin)
    
    def check_exit_reached(self):
        """Check if robber reached the exit"""
        if (self.robber.x, self.robber.y) == self.exit_pos:
            self.game_won = True
            self.win_sound.play()
    
    def move_watchmen(self):
        """Move all watchmen"""
        if self.game_over or self.game_won:
            return
            
        for watchman in self.watchmen:
            watchman.move(self.grid)
                
        
        self.check_watchman_collision()
    
    def check_watchman_collision(self):
        """Check if robber is caught by a watchman"""
        
        for watchman in self.watchmen:
            if (self.robber.x, self.robber.y) == (watchman.x, watchman.y):
                self.game_over = True
                self.caught_sound.play()
                return
                
            
            if watchman.can_see(self.robber.x, self.robber.y):
                self.game_over = True
                self.caught_sound.play()
                return
    
    def draw(self, screen):
        """Draw the game on the screen"""
        
        screen.fill(BLACK)
        
        
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT), 1)
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y), 1)
        
       
        for obstacle in self.obstacles:
            obstacle.draw(screen, GRID_SIZE)
        
        
        screen.blit(self.exit_img, (self.exit_pos[0] * GRID_SIZE, self.exit_pos[1] * GRID_SIZE))
        
        
        for coin in self.coins:
            coin.draw(screen, GRID_SIZE)
        
       
        for watchman in self.watchmen:
            watchman.draw(screen, GRID_SIZE)
        
        
        self.robber.draw(screen, GRID_SIZE)
        
       
        font = pygame.font.SysFont('Arial', 24)
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        
        time_elapsed = (pygame.time.get_ticks() - self.start_time) // 1000
        time_text = font.render(f'Time: {time_elapsed}s', True, WHITE)
        screen.blit(time_text, (WIDTH - 120, 10))
        
        
        if self.game_over:
            self.draw_message(screen, "GAME OVER! Caught by watchman!", RED)
        elif self.game_won:
            self.draw_message(screen, f"YOU WIN! Score: {self.score}", GREEN)
            
        
        if self.game_state == ANALYSIS:
            self.draw_analysis(screen)
    
    def draw_message(self, screen, message, color):
        """Draw a message on the screen"""
        font = pygame.font.SysFont('Arial', 36)
        text = font.render(message, True, color)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        
        
        s = pygame.Surface((WIDTH, 80))
        s.set_alpha(100)
        s.fill(BLACK)
        screen.blit(s, (0, HEIGHT//2 - 40))
        
        
        screen.blit(text, text_rect)
        
        
        font_small = pygame.font.SysFont('Arial', 24)
        if self.game_over or self.game_won:
            restart_text = font_small.render("Press R to restart or A to analyze", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
            screen.blit(restart_text, restart_rect)
    
    def analyze_game(self):
        """Switch to analysis mode"""
        self.game_state = ANALYSIS
        
    def draw_analysis(self, screen):
        """Draw game analysis visualization"""
        
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        
        wall_positions = [(wall.x, wall.y) for wall in self.obstacles]
        
        
        start_pos = self.robber.path[0]
        optimal_path = a_star_search(start_pos, self.exit_pos, self.grid, wall_positions)
        
        
        if optimal_path:
            for i in range(len(optimal_path) - 1):
                start_x, start_y = optimal_path[i]
                end_x, end_y = optimal_path[i + 1]
                pygame.draw.line(screen, GREEN, 
                                (start_x * GRID_SIZE + GRID_SIZE//2, start_y * GRID_SIZE + GRID_SIZE//2),
                                (end_x * GRID_SIZE + GRID_SIZE//2, end_y * GRID_SIZE + GRID_SIZE//2), 3)
        
        
        for i in range(len(self.robber.path) - 1):
            start_x, start_y = self.robber.path[i]
            end_x, end_y = self.robber.path[i + 1]
            pygame.draw.line(screen, BLUE, 
                            (start_x * GRID_SIZE + GRID_SIZE//2, start_y * GRID_SIZE + GRID_SIZE//2),
                            (end_x * GRID_SIZE + GRID_SIZE//2, end_y * GRID_SIZE + GRID_SIZE//2), 3)
        
        
        metrics = calculate_metrics(
            self.robber.path, 
            optimal_path,
            self.score // 10,  
            len(self.coins) + (self.score // 10)  
        )
        
        # Draw metrics
        font = pygame.font.SysFont('Arial', 24)
        draw_analysis(screen, font, metrics, WIDTH, HEIGHT)