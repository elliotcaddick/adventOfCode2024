"""
--- Day 18: RAM Run ---
"""

from collections import deque

def part_one(filename, size, limit):
    grid = [['.' for _ in range(size + 1)] for _ in range(size + 1)]

    with open(filename) as file:
        for i, line in enumerate(file):
            if i >= limit:
                break
            line = line.strip()
            x, y = map(int, line.split(','))
            grid[y][x] = '#'

    def find_path(grid):
        rows = cols = len(grid)
        start, end = (0, 0), (rows - 1, cols - 1)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(start, [])])
        visited = set()
        visited.add(start)

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == end:
                return path + [(x, y)]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    if grid[nx][ny] == '.':
                        queue.append(((nx, ny), path + [(x, y)]))
                        visited.add((nx, ny))

        return None
    
    path = find_path(grid)
    return len(path) - 1

            
    


print(f"=== [PART 1] TEST ===")
print(f"{part_one("day18/test/sample.txt", 6, 12)}")
print(f"=== [PART 1] PUZZLE RESULT ===")
print(f"Part 2: {part_one("day18/input/puzzle.txt", 70, 1024)}")