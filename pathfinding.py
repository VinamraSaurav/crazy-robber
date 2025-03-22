import heapq
from utils import manhattan_distance

def a_star_search(start, goal, grid, obstacles):
    """
    A* search algorithm to find optimal path
    Returns a list of positions forming the path from start to goal
    """
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while frontier:
        _, current = heapq.heappop(frontier)
        
        if current == goal:
            break
            
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_pos = (current[0] + dx, current[1] + dy)
            
            
            if not grid.is_valid_position(next_pos[0], next_pos[1]):
                continue
            
            
            if next_pos in obstacles:
                continue
            
            
            new_cost = cost_so_far[current] + 1
            
            
            if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                cost_so_far[next_pos] = new_cost
                priority = new_cost + manhattan_distance(next_pos, goal)
                heapq.heappush(frontier, (priority, next_pos))
                came_from[next_pos] = current
    
    
    if goal not in came_from:
        return None
        
    path = [goal]
    current = goal
    
    while current != start:
        current = came_from[current]
        path.append(current)
        
    path.reverse()
    return path