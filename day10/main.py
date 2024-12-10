"""
--- Day 10: Hoof It ---
"""

def part_one(filename):
    topographic_map = []
    
    with open(filename) as file:
        for line in file:
            topographic_map.append([int(l) for l in line.strip()])
    
    def find_trailheads(topographic_map):
        trailheads = []
        for i, row in enumerate(topographic_map):
            for j, height in enumerate(row):
                if height == 0:
                    trailheads.append((i, j))
        return trailheads
    
    def explore_trails(topographic_map, start):
        rows, cols = len(topographic_map), len(topographic_map[0])
        visited = set()
        reachable_nines = set()
        
        def dfs(x, y):
            if (x, y) in visited:
                return
            visited.add((x, y))
            
            if topographic_map[x][y] == 9:
                reachable_nines.add((x, y))
                return
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and topographic_map[nx][ny] == topographic_map[x][y] + 1:
                    dfs(nx, ny)
        
        dfs(*start)
        return reachable_nines
    
    trailheads = find_trailheads(topographic_map)
    total_score = 0
    
    for trailhead in trailheads:
        reachable_nines = explore_trails(topographic_map, trailhead)
        total_score += len(reachable_nines)
    
    return total_score
                
            
# print(f"Part 1: {part_one("input/puzzle.txt")}")

