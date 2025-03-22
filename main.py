import pygame
import sys
from constants import FPS
from game import CrazyRobberGame
from utils import create_assets_folder

def main():
    
    pygame.init()
    
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Crazy Robber")
    
    
    clock = pygame.time.Clock()
    
   
    create_assets_folder()
    
    
    game = CrazyRobberGame()
    
    
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            
            if game.game_state == "playing":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        game.move_robber(-1, 0)
                        game.move_watchmen()
                    elif event.key == pygame.K_RIGHT:
                        game.move_robber(1, 0)
                        game.move_watchmen()
                    elif event.key == pygame.K_UP:
                        game.move_robber(0, -1)
                        game.move_watchmen()
                    elif event.key == pygame.K_DOWN:
                        game.move_robber(0, 1)
                        game.move_watchmen()
                    elif event.key == pygame.K_r:
                        game.init_game()
                        game.game_state = "playing"
            
            
            if (game.game_over or game.game_won) and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.init_game()
                    game.game_state = "playing"
                elif event.key == pygame.K_a:
                    game.analyze_game()
            
            
            if game.game_state == "analysis" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.init_game()
                    game.game_state = "playing"
                elif event.key == pygame.K_ESCAPE:
                    game.game_state = "playing"
        
        
        game.draw(screen)
        
        
        pygame.display.flip()
        
        
        clock.tick(FPS)
    
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()