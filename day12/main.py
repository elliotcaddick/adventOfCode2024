"""
--- Day 12: Garden Groups ---
"""

from collections import deque

def part_one(filename):
    garden = []
    
    with open(filename) as file:
        for line in file:
            garden.append([g for g in line.strip()])
    
    rows, cols = len(garden), len(garden[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    total_cost = 0

    def bfs(start, plant_type):
        queue = deque([start])
        visited[start[0]][start[1]] = True
        area = 0
        perimeter = 0
        
        while queue:
            x, y = queue.popleft()
            area += 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols:
                    if garden[nx][ny] == plant_type and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                    elif garden[nx][ny] != plant_type:
                        perimeter += 1
                else:
                    perimeter += 1
        
        return area, perimeter
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                plant_type = garden[i][j]
                area, perimeter = bfs((i, j), plant_type)
                total_cost += area * perimeter
    
    return total_cost
                
            
# print(f"Part 1: {part_one("input/puzzle.txt")}")