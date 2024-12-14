"""
--- Day 14: Restroom Redoubt ---
"""

NB_SECONDS = 100
WIDE_TEST = 11

class Robot:
    def __init__(self, p, v):
        self.pos = p
        self.velocity = v

def part_one(filename, wide, tall):
    robots = []
    space = [[0] * wide for _ in range(tall)]
    
    # Init robots and their initial positions
    with open(filename) as file:
        for line in file:
            pos_str, velocity_str = line.strip().split(' ')
            px, py = map(int, pos_str[2:].split(','))
            vx, vy = map(int, velocity_str[2:].split(','))
            robots.append(Robot((px, py), (vx, vy)))
            space[py][px] += 1
    
    # Move robots for 100 seconds
    for _ in range(NB_SECONDS):
        for robot in robots:
            px, py = robot.pos
            vx, vy = robot.velocity
            nx = (px + vx) % wide
            ny = (py + vy) % tall
            space[py][px] -= 1
            space[ny][nx] += 1
            robot.pos = (nx, ny)
    
    # Check top left quadrant
    top_left_count = 0
    for i in range(tall // 2):
        for j in range(wide // 2):
            top_left_count += space[i][j]
    
    # Check top right quadrant
    top_right_count = 0
    for i in range(tall // 2):
        for j in range(wide // 2 + 1, wide):
            top_right_count += space[i][j]
    
    # Check bottom left quadrant
    bottom_left_count = 0
    for i in range(tall // 2 + 1, tall):
        for j in range(wide // 2):
            bottom_left_count += space[i][j]
    
    # Check bottom right quadrant
    bottom_right_count = 0
    for i in range(tall // 2 + 1, tall):
        for j in range(wide // 2 + 1, wide):
            bottom_right_count += space[i][j]
    
    return top_left_count * top_right_count * bottom_left_count * bottom_right_count


# print(f"Part 1: {part_one("input/puzzle.txt", 101, 103)}")


# print(f"Part 2: {part_two("input/puzzle.txt")}")