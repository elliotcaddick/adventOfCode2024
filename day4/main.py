"""
--- Day 4: Ceres Search ---
"""

WORD1 = "XMAS"

def part_one(filename):    
    with open(filename) as file:
        word_search = [line.strip() for line in file]
    
    rows, cols = len(word_search), len(word_search[0])
    word_len = len(WORD1)
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
            if not is_valid(nx, ny) or word_search[nx][ny] != WORD1[i]:
                return False, []
            positions.append((nx, ny))
        return True, positions
    
    results = []
    for r in range(rows):
        for c in range(cols):
            if word_search[r][c] == WORD1[0]:
                for dx, dy in directions:
                    found, positions = search(r, c, dx, dy)
                    if found:
                        results.append((positions, (dx, dy)))
    
    return len(results)


# print(f"Part 1: {part_one("input/puzzle.txt")}")

WORD2 = "MAS"

def part_two(filename):    
    with open(filename) as file:
        word_search = [line.strip() for line in file]
    
    rows, cols = len(word_search), len(word_search[0])
    
    def is_valid(x, y):
        return 0 < x < rows - 1 and 0 < y < cols - 1
    
    occurence = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if word_search[i][j] == WORD2[1]:
                if is_valid(i, j) and\
                    ((word_search[i-1][j-1] == WORD2[0] and word_search[i+1][j+1] == WORD2[2])\
                        or (word_search[i-1][j-1] == WORD2[2] and word_search[i+1][j+1] == WORD2[0])):
                        if ((word_search[i+1][j-1] == WORD2[0] and word_search[i-1][j+1] == WORD2[2])\
                            or (word_search[i+1][j-1] == WORD2[2] and word_search[i-1][j+1] == WORD2[0])):
                                occurence += 1
    
    return occurence

# print(f"Part 2: {part_two("input/puzzle.txt")}")