"""
--- Day 16: Reindeer Maze ---
"""

import heapq

# Directions: East, South, West, North (clockwise order)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIR_COST = 1  # Cost of moving one tile
TURN_COST = 1000  # Cost of rotating 90 degrees

def part_one(filename: str, verbose=False):
    grid = []
    start = end = None

    with open(filename) as file:        
        for i, line in enumerate(file):
            line = line.strip()
            grid.append(list(line))
            if 'S' in line:
                start = (i, line.index('S'))
            if 'E' in line:
                end = (i, line.index('E'))
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 0))

    while pq:
        score, x, y, direction = heapq.heappop(pq)

        if (x, y) == end:
            return score

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        dx, dy = DIRECTIONS[direction]
        nx, ny = x + dx, y + dy

        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
            heapq.heappush(pq, (score + DIR_COST, nx, ny, direction))

        heapq.heappush(pq, (score + TURN_COST, x, y, (direction + 1) % 4))
        heapq.heappush(pq, (score + TURN_COST, x, y, (direction - 1) % 4))


print(f"=== [PART 1] TEST ===")
print(f"Test 1: {part_one("day16/test/sample1.txt")}")
print(f"Test 2: {part_one("day16/test/sample2.txt")}")
print(f"=== [PART 1] PUZZLE RESULT ===")
print(f"Puzzle result: {part_one("day16/input/puzzle.txt")}")