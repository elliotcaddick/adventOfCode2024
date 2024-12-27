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
print(f"Puzzle result: {part_one("day16/input/puzzle.txt")}\n")

import time
from collections import deque

def part_two(filename: str, verbose=False):
    with open(filename) as file:        
        grid = [list(line.strip()) for line in file if line.strip()]
    
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    
    def turn_right(cur_dir):
        return directions[(directions.index(cur_dir) + 1 + len(directions)) % len(directions)]


    def turn_left(cur_dir):
        return directions[(directions.index(cur_dir) - 1 + len(directions)) % len(directions)]
    
    def bfs(_map):
        queue = deque()
        start = (len(_map) - 2, 1, (0, 1), 0)  # x, y, direction, score
        _map[len(_map) - 2][1] = 0
        queue.append(start)

        while queue:
            current = queue.popleft()
            cur_x = current[0]
            cur_y = current[1]
            cur_dir = current[2]
            cur_score = current[3]

            allowed_directions_n_score = [
                (cur_dir, cur_score + 1),
                (turn_left(cur_dir), cur_score + 1001),
                (turn_right(cur_dir), cur_score + 1001)
            ]

            for new_dir, new_score in allowed_directions_n_score:
                new_x, new_y = cur_x + new_dir[0], cur_y + new_dir[1]
                if _map[new_x][new_y] == "#":
                    continue

                if _map[new_x][new_y] in [".", "E"] or (isinstance(_map[new_x][new_y], int) and _map[new_x][new_y] > new_score):
                    _map[new_x][new_y] = new_score
                    queue.append((new_x, new_y, new_dir, new_score))

        return _map[1][len(_map[1]) - 2]


    def backwards_bfs(_map):
        queue = deque()
        res = 1
        start_1 = (1, len(_map[1]) - 2, (1, 0), _map[1][len(_map[1]) - 2])  # x, y, direction, score
        start_2 = (1, len(_map[1]) - 2, (0, -1), _map[1][len(_map[1]) - 2])  # x, y, direction, score
        queue.append(start_1)
        queue.append(start_2)
        visited = set()

        while queue:
            current = queue.popleft()
            cur_x = current[0]
            cur_y = current[1]
            cur_dir = current[2]
            cur_score = current[3]

            allowed_directions_n_score = [
                (cur_dir, cur_score - 1),
                (turn_left(cur_dir), cur_score - 1001),
                (turn_right(cur_dir), cur_score - 1001)
            ]

            for new_dir, new_score in allowed_directions_n_score:
                new_x, new_y = cur_x + new_dir[0], cur_y + new_dir[1]
                if isinstance(_map[new_x][new_y], int) and (_map[new_x][new_y] in [new_score, new_score - 1000]) and (new_x, new_y) not in visited:
                    res += 1
                    queue.append((new_x, new_y, new_dir, new_score))
                    visited.add((new_x, new_y))

        return res
    
    bfs(grid)
    return backwards_bfs(grid)
    
    


print(f"=== [PART 2] TEST ===")
print(f"Test 1: {part_two("day16/test/sample1.txt")}")
print(f"Test 2: {part_two("day16/test/sample2.txt")}")  
print(f"=== [PART 2] PUZZLE RESULT ===")
print(f"Puzzle result: {part_two("day16/input/puzzle.txt")}")