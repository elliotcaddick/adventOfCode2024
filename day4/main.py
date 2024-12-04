"""
--- Day 4: Ceres Search ---
"""

WORD = "XMAS"

def part_one(filename):    
    with open(filename) as file:
        word_search = [line.strip() for line in file]
    
    rows, cols = len(word_search), len(word_search[0])
    word_len = len(WORD)
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right diagonal
        (-1, -1), # up-left diagonal
        (1, -1),  # down-left diagonal
        (-1, 1)   # up-right diagonal
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def search(x, y, dx, dy):
        positions = []
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or word_search[nx][ny] != WORD[i]:
                return False, []
            positions.append((nx, ny))
        return True, positions
    
    results = []
    for r in range(rows):
        for c in range(cols):
            if word_search[r][c] == WORD[0]:
                for dx, dy in directions:
                    found, positions = search(r, c, dx, dy)
                    if found:
                        results.append((positions, (dx, dy)))
    
    return len(results)


# print(f"Part 1: {part_one("input/puzzle.txt")}")