import pygame
import sys
from constants import FPS
from game import CrazyRobberGame
from utils import create_assets_folder

def main():
    # Initialize pygame
    pygame.init()
    
    # Create screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Crazy Robber")
    
    # Create clock
    clock = pygame.time.Clock()
    
    # Create assets folder
    create_assets_folder()
    
    # Create game
    game = CrazyRobberGame()
    
    # Main game loop
    running = True
    while running:
        # Handle events
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
            
            # Handle restart or analysis when game is over
            if (game.game_over or game.game_won) and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.init_game()
                    game.game_state = "playing"
                elif event.key == pygame.K_a:
                    game.analyze_game()
            
            # Exit analysis mode
            if game.game_state == "analysis" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.init_game()
                    game.game_state = "playing"
                elif event.key == pygame.K_ESCAPE:
                    game.game_state = "playing"
        
        # Draw game
        game.draw(screen)
        
        # Update display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(FPS)
    
    # Quit game
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()