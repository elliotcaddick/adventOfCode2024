"""
--- Day 6: Guard Gallivant ---
"""

def part_one(filename):
    the_map = []
    
    with open(filename) as file:
        for line in file:
            curr_line = (list(l for l in line.strip()))
            the_map.append(curr_line)
    
    x = None
    y = None
    for i in range(len(the_map)):
        for j in range(len(the_map[0])):
            if the_map[i][j] == "^":
                x = i
                y = j
                break
    
    def valid_coord(x, y):
        return 0 <= x < len(the_map) and 0 <= y < len(the_map[0])
    
    
    directions = {
        "^": (-1, 0, ">"),  # Up: decrease x, next direction is '>'
        ">": (0, 1, "v"),   # Right: increase y, next direction is 'v'
        "v": (1, 0, "<"),   # Down: increase x, next direction is '<'
        "<": (0, -1, "^")   # Left: decrease y, next direction is '^'
    }
    visited_coord = [(x, y)]
    while valid_coord(x, y):
        dx, dy = 0, 0

        if the_map[x][y] in directions:
            dx, dy, next_dir = directions[the_map[x][y]]
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < len(the_map) and 0 <= new_y < len(the_map[0]):  # Check bounds
                if the_map[new_x][new_y] == "#":  # Blocked
                    the_map[x][y] = next_dir
                else:  # Swap positions
                    the_map[x][y], the_map[new_x][new_y] = the_map[new_x][new_y], the_map[x][y]
                    x, y = new_x, new_y
                    if (x, y) not in visited_coord:
                        visited_coord.append((x, y))
            else:  # Out of bounds
                x, y = new_x, new_y
        
    return len(visited_coord)
                
        
# print(f"Part 1: {part_one("input/puzzle.txt")}")
