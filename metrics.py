def calculate_metrics(player_path, optimal_path, coins_collected, total_coins):
    """Calculate game performance metrics"""
    
    optimal_length = len(optimal_path) - 1 if optimal_path else 0
    player_length = len(player_path) - 1
    
    
    if player_length > 0 and optimal_length > 0:
        efficiency = (optimal_length / player_length * 100)
    else:
        efficiency = 0
    
    return {
        "optimal_path_length": optimal_length,
        "player_path_length": player_length,
        "path_efficiency": efficiency,
        "coins_collected": coins_collected,
        "total_coins": total_coins
    }

def draw_analysis(screen, font, metrics, width, height):
    """Draw analysis metrics on screen"""
    import pygame
    from constants import BLACK, WHITE
    
    
    text_bg = pygame.Surface((300, 300))
    text_bg.set_alpha(200)
    text_bg.fill(BLACK)
    screen.blit(text_bg, (width - 350, height - 350))
    
    
    lines = [
        f"Analysis Results:",
        f"Optimal path length: {metrics['optimal_path_length']} steps",
        f"Your path length: {metrics['player_path_length']} steps",
        f"Path efficiency: {metrics['path_efficiency']:.1f}%",
        f"Coins collected: {metrics['coins_collected']} of {metrics['total_coins']}",
        f"",
        f"Green: Optimal path",
        f"Blue: Your path",
        f"",
        f"Press R to restart",
        f"or ESC to exit analysis"
    ]
    
    
    for i, line in enumerate(lines):
        text = font.render(line, True, WHITE)
        screen.blit(text, (width - 340, height - 340 + i * 30))